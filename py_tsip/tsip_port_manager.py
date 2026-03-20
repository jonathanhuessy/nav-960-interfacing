#
# WARNING: THIS FILE will be removed from py_tsip very soon
# py_tsip needs to be taken over by origin_tsip and this doesn't really fit with
# origin_tsip. Either tsip_port_manager will become its own module or put into
# testatuomation
#

#===========================================================================
# @file tsip_port_manager.cpp
#
# Implements class tsip_port_manager::TsipPortManager.
#
# Copyright (c) 2017, 2025 PTx
#===========================================================================


from enum import Enum
import abc
import shutil
import time
import serial
import serial.tools.list_ports
import logging
import os
import re
from struct import *
import _thread
import threading
from .tsip_packet_publisher import TsipPacketPublisherGroup
from .tsip_packets import *
from .data_buffer import BinaryBuffer
from .tsip_schema import TsipUtils
from .tsip_deviceinfo import ProductId
from .tsip_encoders import TsipMessageEncoder
from .data_buffer import InBuffer, OutBuffer

# Module-level logger
logger = logging.getLogger("py_tsip")
logger.setLevel(logging.WARNING)

# Note: basicConfig configures the root logger - consider removing this
# and letting applications configure logging themselves
logging.basicConfig(
    format='%(asctime)s %(levelname)-7s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


DLE = 0x10  # TSIP packet start/end header   */
ETX = 0x03  # TSIP data packet tail          */
MBEG = 0x3E  # > - TAIP start of message      */
MEND = 0x3C  # < - TAIP end of message        */
NBEG = 0x24  # $ - NMEA start of message      */
NECR = 0x0D  # <cr> - NMEA end of message     */
NELF = 0x0A  # <lf> - NMEA end of message     */
STX = 0x02  # DCOL start of packet           */
CR = 0x0D
LF = 0x0A

def getCurrentTimeMSec():
    return int(round(time.time() * 1000))

def send_break(port, BreakMS):
    # If windows (including WSL, even though it's kinda Linux) need to use break_condition else use send_break for Mac and Linux (non-WSL)
    if os.name == "nt" or shutil.which("wsl.exe") is not None:
        # Using break_condition for windows and WSL
        port.break_condition = True
        break_start_time = time.time()

        while time.time() - break_start_time < BreakMS / 1000:
            time.sleep(0.05) # spin for a bit

        port.break_condition = False
    else:
        logger.debug(f'[py-tsip] send_break, currently {port.baudrate}, {port.parity}')
        # Using send_break for all others (i.e. Mac, Linux)
        port.reset_input_buffer()
        port.reset_output_buffer()
        port.send_break(BreakMS)


class EConnectionStatus(Enum):
    ConnectionStatus_NotConnected = 0
    ConnectionStatus_ConfiguringPort = 1
    ConnectionStatus_Connected = 2

"""
#=============================================================================
# TsipPortManager
#=============================================================================
"""
class TsipPortManager():
    PICUSMUXINDEX = 0
    DEMETERMUXINDEX = 1

    ReadBufferSize = (5 * 1024)  # 5KB

    def __init__(self, portName, muxIndex=0, logAgLevel=0):
        """ Initialize the TsipPortManager

        PortName is the name of the port
            On windows, this will look like "COM1"
            On mac, this will look like "/dev/cu.usbserial-AH55HWMI"
            On linux, this will look like "/dev/ttyUSB0"

        muxIndex specifies which application on the embedded device py_tsip
        should connect to. This should be set to 0 for the majority of devices
            To connect to picus on a NAV-900 or NAV-500, and for all other devices, set muxIndex to PICUSMUXINDEX (0)
            To connect to demeter on a NAV-900 or NAV-500, set muxIndex to DEMETERMUXINDEX (1)

        logAgLevel -- Integer value corresponding to the levels of the 0x3f 0x22 0x00 Diagnostics command
            This level setting is not supported on picus and earlier devices, so any value other than 0
            will default to outputting debug messages.
        """
        logger.debug("[py-tsip] Starting Port Manager v3")
        self._Initialized = False

        # Create TSIP client and server encoders.
        self._ClientEncoder = ClientPacketEncoder()
        self._ServerEncoder = ServerPacketEncoder()

        self.portMuxIndex = muxIndex
        self.logAgLevel = logAgLevel

        logger.debug("[py-tsip] LogAgLevel is %d", self.logAgLevel)

        self._port = serial.Serial()
        self._port.port = portName
        # The first thing PortStateAutoConfigure does is send a break at 9600 baud.
        self._port.baudrate = 9600
        self._port.parity = serial.PARITY_NONE
        self._port.bytesize = serial.EIGHTBITS
        self._port.stopbits = serial.STOPBITS_ONE
        self._port.xonxoff = False
        self._port.rtscts = False
        self._port.timeout = 2
        self._portLock = threading.Lock()

        self._lastTime = getCurrentTimeMSec()
        self._timeoutActive = False
        self._timeoutMsec = 0
        self._readBuffer = BinaryBuffer()
        self._setStateInProgress = False
        self._enabled = True

        self.product = ProductId.Unknown
        self.is_monitor_mode = False

        # Create packet publisher group.
        self._publisherGroup = TsipPacketPublisherGroup(self)

        # Create possible states for this port manager.
        self._stateNotConnected = PortStateNotConnected(self)
        self._stateAutoConfigure = PortStateAutoConfigure(self)
        self._stateConnected = PortStateConnected(self)
        self._stateMonTsip = PortStateMonTsip(self, True)

        # Starting in stateNotConnected will go through the break sequence so we can select the baud rate
        # on the target device (i.e. the receiver or nav controller).
        self._currState = self._stateNotConnected

        self._manageConnection = True
        self._connectedEvent = threading.Event()
        self._monTsipDoneEvent = threading.Event()

        logger.debug(self._port)

        logger.debug("Opening Serial Port")
        try:
            # Don't need to lock here - ProcessLoop thread isn't running yet.
            self._port.open()
        except Exception as ex:
            logger.error("[py-tsip] Failed to open port %s: %s", portName, ex)
            return


        try:
            # ProcessLoop returns if not _Initialized. That's a race condition so we have to set _Initialized = True FIRST.
            self._Initialized = True
            _thread.start_new_thread(self.ProcessLoop, ())
            logger.debug("[py-tsip] Port Manager Initialized")
        except:
            logger.error("[py-tsip] Unable to start Port Manager")
            exit()

    #-----------------------------------------------------------------------------
    # def IsInitialized(...)
    #-----------------------------------------------------------------------------
    def IsInitialized(self):
        return self._Initialized

    #-----------------------------------------------------------------------------
    # def ManageConnection(...)
    #-----------------------------------------------------------------------------
    def ManageConnection(self):
        return self._manageConnection

    def WaitForConnection(self, timeout_s):
        return self._connectedEvent.wait(timeout_s)

    #-----------------------------------------------------------------------------
    # def EnableMonTsip(...)
    #-----------------------------------------------------------------------------
    def EnableMonTsip(self, blocking=True):
        logger.debug("[py-tsip] Enabling MonTsip Connection")
        if self._currState != self._stateConnected:
            logger.debug("not connected, cannot enter montsip state")
            return False
        if self._stateConnected._isMonTsipEnabled:
            return True

        self._stateMonTsip = PortStateMonTsip(self, True)
        self.SetState(self._stateMonTsip)
        if not blocking:
            return True
        # wait for montsip state to finish request
        self._monTsipDoneEvent.wait()
        return self._stateConnected._isMonTsipEnabled

    #-----------------------------------------------------------------------------
    # def DisableMonTsip(...)
    #-----------------------------------------------------------------------------
    def DisableMonTsip(self):
        logger.debug("Disabling MonTsip Connection")
        if self._currState != self._stateConnected or not self._stateConnected._isMonTsipEnabled:
            logger.debug("not in montsip mode, cannot exit that state")
            return False
        if self.product == ProductId.Ceres:
            logger.warning("Ceres is stuck in fsMonitor mode")
            return False

        self._stateMonTsip = PortStateMonTsip(self, False)
        self.SetState(self._stateMonTsip)
        # wait for montsip state to finish request
        self._monTsipDoneEvent.wait()
            
        if not self._stateConnected._isMonTsipEnabled:
            logger.info("MonTsip Disabled Successfully")
            self._publisherGroup.DisableMonTsip()
            return True
        return False

    #-----------------------------------------------------------------------------
    # def Shutdown(...)
    #-----------------------------------------------------------------------------
    def Shutdown(self):
        self._enabled = False
        time.sleep(.5)

    #-----------------------------------------------------------------------------
    # def GetConnectionStatus(...)
    #-----------------------------------------------------------------------------
    def GetConnectionStatus(self):
        if self._currState == self._stateAutoConfigure or self._currState == self._stateMonTsip:
            return EConnectionStatus.ConnectionStatus_ConfiguringPort
        elif self._currState == self._stateNotConnected:
            return EConnectionStatus.ConnectionStatus_NotConnected
        elif self._currState == self._stateConnected:
            return EConnectionStatus.ConnectionStatus_Connected

    def IsUsingDemeter(self):
        return self.product.isDemeterProduct() or \
            (self.product.isFusionProduct() and self.portMuxIndex == TsipPortManager.DEMETERMUXINDEX)

    #-----------------------------------------------------------------------------
    # def SetState(...)
    #-----------------------------------------------------------------------------
    def SetState(self, nextState):
        if self._setStateInProgress:
            logger.warning("Recursive state change from Enter/ExitState")
        self._setStateInProgress = True
        self._currState.ExitState()
        self._currState = nextState
        nextState.EnterState()
        self._setStateInProgress = False

    #-----------------------------------------------------------------------------
    # def SetTimeoutMsec(...)
    #-----------------------------------------------------------------------------
    def SetTimeoutMsec(self, timeoutMsec):
        self._timeoutActive = True
        self._timeoutMsec = timeoutMsec
        self._lastTime = getCurrentTimeMSec()

    #-----------------------------------------------------------------------------
    # def ClearTimeout(...)
    #-----------------------------------------------------------------------------
    def ClearTimeout(self):
        self._timeoutActive = False
        self._timeoutMsec = 0
        self._lastTime = getCurrentTimeMSec()

    #-----------------------------------------------------------------------------
    # def CheckTimeout(...)
    #-----------------------------------------------------------------------------
    def CheckTimeout(self):
        return (self._timeoutActive and self._timeoutMsec == 0)

    #-----------------------------------------------------------------------------
    # def PeriodicHandler(...)
    #-----------------------------------------------------------------------------
    def PeriodicHandler(self):
        # Update the timeout value during each call to periodic handler,
        # before delegating to current state.
        delta = getCurrentTimeMSec() - self._lastTime
        if self._timeoutMsec > delta:
            self._timeoutMsec -= delta
        else:
            self._timeoutMsec = 0

        if not self._setStateInProgress:
            self._currState.PeriodicHandler()

        self._lastTime = getCurrentTimeMSec()

    #-----------------------------------------------------------------------------
    # def PeriodicTimerCallback(...)
    #-----------------------------------------------------------------------------
    def ProcessLoop(self):
        if not self._Initialized:
            return
        sleepCount = 0
        mySleepInt = 0.1
        periodicInterval = int(1 / mySleepInt)
        if periodicInterval < 1:
            periodicInterval = 1
        self.SetState(self.GetStateAutoConfigure())
        port = self._port
        data = None
        count = 0

        while self._enabled:
            # Don't reconfigure the port in the middle of reading data
            with self._portLock:
                count = port.in_waiting
                if count > 0:
                    data = port.read(count)
                    logger.log(9, f"[py-tsip] Read {count} bytes: {data.hex()}")

            # Don't keep the port locked while we call the packet handlers
            if count > 0 and data and not self._setStateInProgress:
                self._currState.HandleStreamRead(data, count)
            time.sleep(mySleepInt)
            sleepCount += 1
            if sleepCount % periodicInterval == 0:
                self.PeriodicHandler()
        port.close()

    #-----------------------------------------------------------------------------
    #   def ConfigPort(...)
    #-----------------------------------------------------------------------------
    def ConfigPort(self, baudRateStr, parity=None):
        """Configure port to enter connected mode, based on product string"""
        baudRate = int(baudRateStr)
        logger.debug("ConfigPort: Setting baud rate to %d, parity to %s", baudRate, parity)
        # Lock the port so we don't reconfigure it in the middle of trying to use it.
        with self._portLock:
            port = self.GetPort()
            # Property setters on the Serial port class automatically reconfigure the port.
            port.baudrate = baudRate
            port.bytesize = serial.EIGHTBITS

            if self.product.isBuffaloProduct() or self.product.isPicusProduct():
                port.parity = parity or serial.PARITY_ODD

            else: # demeter and fusion devices default to PARITY_NONE
                port.parity = parity or serial.PARITY_NONE

            port.stopbits = serial.STOPBITS_ONE

            port.reset_input_buffer()
            port.reset_output_buffer()
            time.sleep(0.1)

    def PortIsOpen(self):
        return self._port.is_open

    #-----------------------------------------------------------------------------
    # This persists across multiple connections as long as port manager is alive.
    # To clear the custom command, set break_command = "" or None.
    #-----------------------------------------------------------------------------
    def SetCustomBreakCommand(self, break_command, break_response, baudrate_str, parity):
        self.GetStateAutoConfigure().SetCustomBreakCommand(break_command, break_response, baudrate_str, parity)
        self.SetState(self.GetStateAutoConfigure())

    def ClearCustomBreakCommand(self):
        self.GetStateAutoConfigure().ClearCustomBreakCommand()

    #-----------------------------------------------------------------------------
    # def PacketWrite(...)
    #-----------------------------------------------------------------------------
    def PacketWrite(self, packet):
        if len(packet) == 0:
            # Not an error - just NOP
            return True

        bytesWritten = 0
        baud = 0
        parity = "-"
        with self._portLock:
            if not self._port.is_open:
                logger.error("The serial port is not open")
                return False
            # Cache baud and parity for logging later
            baud = self._port.baudrate
            parity = self._port.parity
            bytesWritten = self._port.write(packet)

        if bytesWritten != len(packet):
            logger.error("[py-tsip] Serial port write failed")
            return False
        logger.log(9, "[py-tsip] Sent %d bytes at %d baud: %s" % (len(packet), baud, packet.hex()))
        TsipUtils().PacketDump(packet)
        return True

    #-----------------------------------------------------------------------------
    # def TsipSendClientPacket(...)
    #-----------------------------------------------------------------------------
    def TsipSendClientPacket(self, type, packet):
        status = False
        if packet != None:
            data = TsipMessageEncoder().EncodeMessage(type, packet)
            if data == None:
                return False
        else:
            data = None
        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        tmpout = bytearray(tmplist)
        outbuf = OutBuffer(tmpout, TSIPSCHEMA_MAX_PACKET_SIZE)
        self._ClientEncoder.SetCurrentSchema(type.value)
        if data != None:
            tmpin = bytearray(data)
            inbuf = InBuffer(tmpin, len(data))
        else:
            inbuf = InBuffer(None, 0)
        if self._ClientEncoder.Encode(inbuf, outbuf):
            return self.PacketWrite(outbuf.used())

    #-----------------------------------------------------------------------------
    # def TsipSendServerPacket(...)
    #-----------------------------------------------------------------------------
    def TsipSendServerPacket(self, type, packet):
        status = False
        if packet != None:
            data = TsipMessageEncoder().EncodeMessage(type, packet)
            if data == None:
                return False
        else:
            data = None
        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        tmpdata = bytearray(tmplist)
        outbuf = OutBuffer(tmpdata, TSIPSCHEMA_MAX_PACKET_SIZE)
        self._ServerEncoder.SetCurrentSchema(type.value)
        if data != None:
            tmpin = bytearray(data)
            inbuf = InBuffer(tmpin, len(data))
        else:
            inbuf = InBuffer(None, 0)
        if self._ServerEncoder.Encode(data, outbuf):
            return self.PacketWrite(outbuf.used())
    #-----------------------------------------------------------------------------
    # def TsipSendPacket(...)
    #-----------------------------------------------------------------------------

    def TsipSendPacket(self, type, packet):
        if isinstance(type, EServerPackets):
            return self.TsipSendServerPacket(type, packet)
        if isinstance(type, EClientPackets):
            return self.TsipSendClientPacket(type, packet)

        return False

    #-----------------------------------------------------------------------------
    # Get / Set Stuff
    #-----------------------------------------------------------------------------
    def GetPort(self):
        return self._port

    def GetReadBuffer(self):
        return self._readBuffer

    def GetPublisherGroup(self):
        return self._publisherGroup

    def GetStateNotConnected(self):
        return self._stateNotConnected

    def GetStateAutoConfigure(self):
        return self._stateAutoConfigure

    def GetStateConnected(self):
        return self._stateConnected

    #----------------------------------------------------------------------------------------------
    @staticmethod
    def get_port_info_list():
        """ Gets a filtered list of serial ports from pyserial
        Returns:
            list of available ports, filtered for various local devices, and things sounding like
            'usb' moved to the top. If TSIP_PORT environment variable is set, returns only that port.

            Hints:
            # PowerShell
            $env:TSIP_PORT="COM3"

            # Linux/WSL
            export TSIP_PORT="/dev/ttyUSB2"
        """
        # Check if TSIP_PORT environment variable is set
        tsip_port = os.environ.get('TSIP_PORT')
        if tsip_port:
            logger.info("Using TSIP_PORT environment variable: %s", tsip_port)
            # Create a mock port info object for the specified port
            from types import SimpleNamespace
            port_info = SimpleNamespace()
            port_info.device = tsip_port
            port_info.description = f"User-specified port via TSIP_PORT: {tsip_port}"
            port_info.hwid = "ENV_VAR"
            return [port_info]
        
        port_info_list = serial.tools.list_ports.comports()

        for indx, thing in enumerate(port_info_list):
            # Move devices that look like the usb serial to front of list to expedite things
            if 'usb' in thing.device.lower() or 'usb' in thing.description.lower():
                port_info_list.insert(0, port_info_list.pop(indx))

        return port_info_list

    @staticmethod
    def get_preferred_port():
        """ Gets the preferred port name to use.
        Returns:
            Port name from TSIP_PORT environment variable if set, otherwise None
        """
        return os.environ.get('TSIP_PORT')

"""
#=============================================================================
# PortState
#=============================================================================
"""
class PortState(abc.ABC):
    #=========================================================================================

    #-----------------------------------------------------------------------------
    # PortState Constructor
    #-----------------------------------------------------------------------------
    def __init__(self, portmgr):
        self._mgr = portmgr

    #-----------------------------------------------------------------------------
    #   def EnterState(...)
    #-----------------------------------------------------------------------------
    @abc.abstractmethod
    def EnterState(self):
        pass
    #-----------------------------------------------------------------------------
    #   def ExitState(...)
    #-----------------------------------------------------------------------------
    @abc.abstractmethod
    def ExitState(self):
        pass

    #-----------------------------------------------------------------------------
    #   def PeriodicHandler(...)
    #-----------------------------------------------------------------------------
    @abc.abstractmethod
    def PeriodicHandler(self):
        pass

    #-----------------------------------------------------------------------------
    #   def HandleStreamRead(...)
    #-----------------------------------------------------------------------------
    @abc.abstractmethod
    def HandleStreamRead(self, data, length):
        pass


"""
#=============================================================================
# PortStateAutoConfigure
#=============================================================================
"""
class PortStateAutoConfigure(PortState):
    RespWaitTimeoutMsec = 2000  # milliseconds
    BreakRespHeader = "PRODUCT,"
    ProductInfoRegex = rb"PRODUCT,([^,]*);PORT,(.),([0-9]*),([0-9]*),(.),(.),(.),|PRODUCT,([^,]*),"
    BreakMS = 1000

    #-----------------------------------------------------------------------------
    # class ProductInfo
    #-----------------------------------------------------------------------------
    class ProductInfo:
        """ Holds the contents of the productInfo message received from the
        embedded device
        """
        #-----------------------------------------------------------------------------
        # ProductInfo Constructor
        #-----------------------------------------------------------------------------
        def __init__(self):
            self.productId = ProductId.Unknown
            self.baudRateStr = ""
            self.parity = serial.PARITY_NONE
            self.isShortResponse = False
            self.isMonitorMode = False

    #-----------------------------------------------------------------------------
    # PortStateAutoConfigure Constructor
    #-----------------------------------------------------------------------------
    def __init__(self, portMgr):
        super().__init__(portMgr)
        self.retryCount = 0
        self._breakSent = False
        self.ClearCustomBreakCommand()

    def SetCustomBreakCommand(self, break_command, break_response, baudrate_str, parity):
        self._customBreakCommand = bytes(break_command, 'utf-8')
        self._customBreakResponse = bytes(break_response, 'utf-8')
        self._customBreakBaudrateStr = baudrate_str
        self._customBreakParity = parity

    def ClearCustomBreakCommand(self):
        self.SetCustomBreakCommand("", "", "", None)

    #-----------------------------------------------------------------------------
    #   def EnterState(...)
    #-----------------------------------------------------------------------------
    def EnterState(self):
        # Clear local read buffer in preparation for receiving product info in
        # response to break
        logger.debug("StateAutoConfig: Enter")

        port = self._mgr.GetPort()
        self._mgr.GetReadBuffer().Clear()
        logger.debug("Setting RTS high")
        port.rts = True
        time.sleep(0.003)
        logger.debug("Entering serial break mode")
        # Any response to break will arrive at 9600 8N1, so temporarily
        # reconfigure.
        port.baudrate = 9600
        port.parity = serial.PARITY_NONE
        port.bytesize = serial.EIGHTBITS
        port.stopbits = serial.STOPBITS_ONE
        time.sleep(0.1)

        self._mgr.SetTimeoutMsec(PortStateAutoConfigure.RespWaitTimeoutMsec)

        self._mgr.GetReadBuffer().Clear()
        send_break(port, PortStateAutoConfigure.BreakMS)
        self._breakSent = True
        # HandleStreamRead should receive a break response with product data.


    #-----------------------------------------------------------------------------
    #   def ExitState(...)
    #-----------------------------------------------------------------------------
    def ExitState(self):
        logger.debug("StateAutoConfig: Exit")
        self.retryCount = 0
        self._mgr.ClearTimeout()

    #-----------------------------------------------------------------------------
    #   def PeriodicHandler(...)
    #-----------------------------------------------------------------------------
    def PeriodicHandler(self):
        if self._mgr.CheckTimeout():
            max_tries = 20
            # No response was received before timeout interval elapsed.
            self.retryCount += 1
            if self.retryCount >= max_tries:
                self._mgr.SetState(self._mgr.GetStateNotConnected())
                # DON'T CALL Shutdown HERE - we're running in the background thread
                # so the thread won't finish until we return to ProcessLoop. Just set
                # the flag and let it finish naturally.
                self._mgr._enabled = False
                logger.error(f"Failed to connect to unit after {max_tries} tries")
            else:
                # Ideally every break would work first time, but in practice we
                # sometimes have to try a few times before we get a response.
                logger.info("retrying serial break: %d" % self.retryCount)
                self._mgr.SetTimeoutMsec(PortStateAutoConfigure.RespWaitTimeoutMsec)
                self._mgr.GetReadBuffer().Clear()
                port = self._mgr.GetPort()
                port.baudrate = 9600
                time.sleep(0.1)
                # Ceres wants 2 breaks, 900ms apart. We don't know what type of product we're
                # trying to talk to yet, so if we've failed twice, try something different.
                if self._mgr.product == ProductId.Unknown and self.retryCount == 2:
                    send_break(self._mgr.GetPort(), PortStateAutoConfigure.BreakMS)
                    time.sleep(0.9)

                send_break(self._mgr.GetPort(), PortStateAutoConfigure.BreakMS)
                self._breakSent = True

    #-----------------------------------------------------------------------------
    #   def HandleStreamRead(...)
    #-----------------------------------------------------------------------------
    def HandleStreamRead(self, data, length):
        logger.debug("State.AutoConfig:HandleStreamRead: %s", data)
        readBuffer = self._mgr.GetReadBuffer()
        readBuffer.Append(data)

        if self.containsProductInfo(readBuffer):
            self.OnProductInfoReceived(readBuffer)
            readBuffer.Clear()

        elif self.containsCustomBreakResponse(readBuffer):
            # The response comes before FW reconfigures the port so now we're safe to change baud rate
            self._mgr.ConfigPort(self._customBreakBaudrateStr, self._customBreakParity)
            # If we received the Break response from Picus - we need to wait a few sec for Picus to be
            # ready (see p_stream->break_counter in tp_break.c)
            if not self._mgr.IsUsingDemeter():
                self._mgr.ClearTimeout()
                time.sleep(3)
            # We potentially got 3 seconds of garbage so clear it (and the custom break response) before moving on.
            readBuffer.Clear()
            # We're connected
            self.GoToNextState()

        elif self.containsPortSelectPicusResponse(readBuffer):
            readBuffer.Clear()
            self.OnPortSelectPicusResponseReceived()

        elif self.containsBaudSelectedPicusResponse(readBuffer):
            logger.debug("HandleStreamRead: Picus BAUD response received")
            # The response comes before FW reconfigures the port so now we're safe to change baud rate
            baudRate = self.ParsePicusBaudRate(readBuffer)
            self._mgr.ConfigPort(baudRate, serial.PARITY_ODD)
            # Received a Break response from Picus - we need to wait a few sec for Picus to be
            # ready (see p_stream->break_counter in tp_break.c)
            self._mgr.ClearTimeout()
            time.sleep(3)
            readBuffer.Clear()
            # We're connected
            self.GoToNextState()

        elif self.containsPortSelectDemeterResponse(readBuffer):
            self.OnPortSelectDemeterResponseReceived()
            readBuffer.Clear()

        elif self.contains230400BaudSelectedDemeterResponse(readBuffer):
            logger.debug("HandleStreamRead: Demeter 230400 BAUD response received")
            # The response comes before FW reconfigures the port so now we're safe to change baud rate
            self._mgr.ConfigPort('230400', serial.PARITY_NONE)
            self._mgr.ClearTimeout()
            readBuffer.Clear()
            # We're connected
            self.GoToNextState()

        elif self.contains115200BaudSelectedDemeterResponse(readBuffer):
            logger.debug("HandleStreamRead: Demeter 115200 BAUD response received")
            # The response comes before FW reconfigures the port so now we're safe to change baud rate
            self._mgr.ConfigPort('115200', serial.PARITY_NONE)
            self._mgr.ClearTimeout()
            readBuffer.Clear()
            # We're connected
            self.GoToNextState()

        else:
            # Didn't find what we're looking for yet. Make sure that we don't
            # accumulate a huge number of bytes in the buffer, in case we
            # are connected to something that ignores the break and generates
            # a lot of output.
            readBuffer.Truncate(500)


    #-----------------------------------------------------------------------------
    #   def containsProductInfo(...)
    #-----------------------------------------------------------------------------
    def containsProductInfo(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        prog = re.compile(PortStateAutoConfigure.ProductInfoRegex)
        return prog.search(data)

    def containsAutopilotApiSelected(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        match = re.search(b"AUTOPILOT API ENABLED", data)
        return (match is not None)

    #-----------------------------------------------------------------------------
    #   def OnProductInfoReceived(...)
    #-----------------------------------------------------------------------------
    def OnProductInfoReceived(self, readBuffer):
        """ Called when the embedded device sends py_tsip its product info,
        generally in response to a serial break
        """
        self.productInfo = self.ParseProductInfo(readBuffer)

        if self.productInfo is not None:
            self._mgr.product = self.productInfo.productId
            self._mgr.is_monitor_mode = self.productInfo.isMonitorMode

            # Reset the timeout
            self._mgr.SetTimeoutMsec(PortStateAutoConfigure.RespWaitTimeoutMsec)

            if self.productInfo.isMonitorMode:
                logger.info("** Receiver is in monitor mode **")
                self._mgr.ConfigPort(self.productInfo.baudRateStr, self.productInfo.parity)
                self.GoToNextState()

            elif self._customBreakCommand:
                logger.debug("OnProductInfoReceived fusion, sending custom break command")
                self._mgr.PacketWrite(self._customBreakCommand)

            elif self.productInfo.productId.isFusionProduct():
                if self.productInfo.isShortResponse:
                    # In Fusion (shifter/nickel), a short PRODUCT response means Demeter controls the port
                    if self._mgr.portMuxIndex == TsipPortManager.DEMETERMUXINDEX:
                        logger.debug("OnProductInfoReceived fusion, demeter, setting baud")
                        self._mgr.PacketWrite(b"ENTER 230400 BAUD MODE\r\n")
                        # Demeter will respond with ENTERING 230400 BAUD MODE, HandleStreamRead will
                        # set local serial port to 230400 and go to Connected state.
                    else:
                        # The port is connected to fusion demeter, but the py_tsip
                        # client requested to connect to picus
                        logger.debug("OnProductInfoReceived fusion, demeter, selecting Picus")
                        self._mgr.PacketWrite(b"CURRENT PORT SELECT PICUS\r\n")
                        # Demeter will respond with PICUS PORT SELECTED, HandleStreamRead will
                        # then ask Picus to set baud rate to 115200 (HIGH SPEED TSIP BACKDOOR)

                else:
                    # In Fusion, a long PRODUCT response means Picus controls the port.
                    if self._mgr.portMuxIndex == TsipPortManager.DEMETERMUXINDEX:
                        # py_tsip received the product info string from picus
                        # Tell the port we want to talk to demeter
                        logger.debug("OnProductInfoReceived fusion, Picus, selecting Demeter")
                        self._mgr.PacketWrite(b"CURRENT PORT SELECT DEMETER\r\n")
                        # Picus will respond with CURRENT PORT DEMETER MODE SELECTED, HandleStreamRead will
                        # then ask Demeter to set baud rate to 230400 (ENTER 230400 BAUD MODE)

                    else:
                        # Connected to Picus, ask for high speed baud rate.
                        logger.debug("OnProductInfoReceived fusion, Picus, setting baud")
                        self._mgr.PacketWrite(b"HIGH SPEED TSIP BACKDOOR\r\n")
                        # Picus will respond with HIGH SPEED TSIP IS 115200, HandleStreamRead will
                        # set local serial port to 115200 and go to Connected state.

            elif self.productInfo.productId.isDemeterProduct():
                # Ceres/Sito doesn't have portMuxIndex
                logger.debug("OnProductInfoReceived demeter (Ceres)")
                # TODO: 230400 was being very flaky for me - needing up to 10 retries for get_tap and _get_sn. 115200 is stable.
                # This doesn't go into monitor mode - it just sets the baud rate to 115200.
                self._mgr.PacketWrite(b"ENTER HS MONTSIP MODE\r\n")
                # Demeter will response with ENTERING HS MONTSIP MODE, HandleStreamRead will
                # set local serial port to 115200 and go to Connected state.

            else:
                # Buffalo, Picus
                self._mgr.ConfigPort(self.productInfo.baudRateStr, self.productInfo.parity)
                self.GoToNextState() # Connected (TODO: does this work? Shouldn't we select a baud mode?)

        else:
            logger.error("Product info received, parsing error (productInfo is None)")


    def contains230400BaudSelectedDemeterResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        return b"ENTERING 230400 BAUD MODE" in data

    def contains115200BaudSelectedDemeterResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        return b"ENTERING HS MONTSIP MODE" in data

    def containsBaudSelectedPicusResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        match = re.search(rb"HIGH SPEED TSIP IS ([0-9]+)\r\n", data)
        return (match is not None)

    def containsCustomBreakResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        return bool(self._customBreakResponse) and self._customBreakResponse in data


    def ParsePicusBaudRate(self, readBuffer):
        """ Parses baud rate from the Picus port config response
        """
        data = bytearray()
        data[:] = readBuffer.Get()
        match = re.search(rb"HIGH SPEED TSIP IS ([0-9]+)\r\n", data)

        if match:
            return match.group(1).decode('utf-8')
        return "115200"

    #-----------------------------------------------------------------------------
    #   def containsPortSelectResponse(...)
    #-----------------------------------------------------------------------------
    def containsPortSelectDemeterResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        return b"CURRENT PORT DEMETER MODE SELECTED" in data

    def containsPortSelectPicusResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        return b"PICUS PORT SELECTED" in data

    #-----------------------------------------------------------------------------
    #   def OnPortSelectResponseReceived(...)
    #-----------------------------------------------------------------------------

    def OnPortSelectPicusResponseReceived(self):
        logger.info("Port Mux Select Picus Response Received")
        # Reset the timeout
        self._mgr.SetTimeoutMsec(PortStateAutoConfigure.RespWaitTimeoutMsec)
        # Ask Picus to go into high-speed TSIP mode (115200 baud)
        self._mgr.PacketWrite(b"HIGH SPEED TSIP BACKDOOR\r\n")

    def OnPortSelectDemeterResponseReceived(self):
        logger.info("Port Mux Select Demeter Response Received")
        # Reset the timeout
        self._mgr.SetTimeoutMsec(PortStateAutoConfigure.RespWaitTimeoutMsec)

        # Ask Demeter to use 230400 baud
        self._mgr.PacketWrite(b"ENTER 230400 BAUD MODE\r\n")

    #-----------------------------------------------------------------------------
    #   def GoToNextState(...)
    #-----------------------------------------------------------------------------

    def GoToNextState(self):
        self._mgr.SetState(self._mgr.GetStateConnected())

    #-----------------------------------------------------------------------------
    #   def ParseProductInfo(...)
    #-----------------------------------------------------------------------------
    def ParseProductInfo(self, readBuffer):
        """ Parses the product info from the serial break response
        """
        logger.debug("Serial break response found: ")
        data = bytearray()
        data[:] = readBuffer.Get()
        logger.debug("Serial break data: " + str(data))

        productInfo = self.ProductInfo()
        
        if 'MONPRODUCT' in str(data):
            prog = re.compile(rb"MONPRODUCT,([^,]*);")
            # Product info in monitor mode
            productInfo.isMonitorMode = True
            match = prog.search(data)
            if match:
                product = match.group(1).decode('utf-8')
                productInfo.productId = ProductId.getProductId(product)
                productInfo.baudRateStr = "115200"
                productInfo.parity = None
                return productInfo
            return None
            
        prog = re.compile(PortStateAutoConfigure.ProductInfoRegex)
        match = prog.search(data)
        if match:
            product = match.group(1)
            if product is None:
                # Demeter in Fusion reports the short product info
                productInfo.isShortResponse = True
                product = match.group(8).decode("utf-8", errors="ignore").rstrip()
                productInfo.productId = ProductId.getProductId(product)
                productInfo.baudRateStr = "115200"
                # Auto-detect based on product type (in ConfigPort)
                productInfo.parity = None
            else:
                # Long product info response...
                productInfo.isShortResponse = False
                productInfo.productId = ProductId.getProductId(product.decode("utf-8", errors="ignore").rstrip())
                # This is Picus or another product that reports full product info
                productInfo.baudRateStr = match.group(3)
                parityStr = match.group(7)

                if parityStr == b"N":
                    productInfo.parity = serial.PARITY_NONE
                elif parityStr == b"O":
                    productInfo.parity = serial.PARITY_ODD
                # else parity = PARITY_NONE from the ProductInfo initializer

            return productInfo
        else:
            return None

"""
#=============================================================================
# PortStateNotConnected
#=============================================================================
"""
class PortStateNotConnected(PortState):
    NotConnectedTimeoutMsec = 10000  # 10 sec
    
    #-----------------------------------------------------------------------------
    # PortStateNotConnected Constructor
    #-----------------------------------------------------------------------------
    def __init__(self, portMgr):
        super().__init__(portMgr)
    
    #-----------------------------------------------------------------------------
    #   def EnterState(...)
    #-----------------------------------------------------------------------------
    def EnterState(self):
        logger.info("Disconnected from Remote Device")
        self._mgr.SetTimeoutMsec(PortStateNotConnected.NotConnectedTimeoutMsec)

    #-----------------------------------------------------------------------------
    #   def ExitState(...)
    #-----------------------------------------------------------------------------
    def ExitState(self):
        self._mgr.ClearTimeout()

    #-----------------------------------------------------------------------------
    #   def HandleStreamRead(...)
    #-----------------------------------------------------------------------------
    def HandleStreamRead(self, data, length):
        pass

    #-----------------------------------------------------------------------------
    #   def PeriodicHandler(...)
    #-----------------------------------------------------------------------------
    def PeriodicHandler(self):
        if self._mgr.CheckTimeout():
            # 10 sec timer elapsed - try again
            self._mgr.SetState(self._mgr.GetStateAutoConfigure())



"""
#=============================================================================
# PortStateConnected
#=============================================================================
"""
class PortStateConnected(PortState):
    ConnectionTimeoutMsec = 10000  # 10 sec


    #-----------------------------------------------------------------------------
    # PortStateConnected Constructor
    #-----------------------------------------------------------------------------
    def __init__(self, portMgr):
        super().__init__(portMgr)
        self._isMonTsipEnabled = False

    def HandlePacket(self, packetId, packetData):
        # Setting the Diag logAgLevel was the last step in connecting so if this
        # is the response, we can set _connectedEvent.
        if packetId == EServerPackets.e5f01rsp:
            logger.info("M %s", packetData.DiagData)
            self._mgr._connectedEvent.set()
        elif packetId == EServerPackets.e5f2201rsp:
            from datetime import datetime, timezone
            try:
                logger.info("M (%x|%s) %s",
                         int.from_bytes(packetData.Type, sys.byteorder),
                         datetime.fromtimestamp(packetData.Time, timezone.utc),
                         packetData.Msg.decode('ascii'))
            except UnicodeDecodeError as error:
                logger.error(f"Error while decoding: {error}")
            self._mgr._connectedEvent.set()

    #-----------------------------------------------------------------------------
    #   def EnterState(...)
    #-----------------------------------------------------------------------------
    def EnterState(self):
        logger.debug("Starting Connected State")
        logger.info("Connected to Remote Device")

        # Clear packet count and setup timeout
        self._mgr.GetPublisherGroup().ResetPacketCount()
        self._mgr.SetTimeoutMsec(PortStateConnected.ConnectionTimeoutMsec)
        self._mgr.GetReadBuffer().Clear()

        self._syncPacketsSent = 0

        # Demeter doesn't support 3f2200 or 3f02 Diag command
        if self._mgr.logAgLevel is not None and not self._mgr.IsUsingDemeter():
            # Build the mask from the level
            if self._mgr.logAgLevel == 0:
                level = 0 # Off
            elif self._mgr.logAgLevel == 1:
                level = 1 << 0 # Error log
            elif self._mgr.logAgLevel == 2:
                level = 1 << 0 | 1 << 1 # Error log + Run-time log
            elif self._mgr.logAgLevel >= 3:
                level = 1 << 0 | 1 << 1 | 1 << 2 # Error log + Run-time log + Debug diagnostics

            if self._mgr.product.isFusionProduct():
                diag_response_packet = EServerPackets.e5f2201rsp
                diag_enable_cmd = EClientPackets.e3f2200cmd
                diag_enable_data = ClientTupleList[EClientPackets.e3f2200cmd.value](level)
            else:
                diag_enable_cmd = EClientPackets.e3f02cmd
                diag_enable_data = ClientTupleList[EClientPackets.e3f02cmd.value](1 if level > 0 else 0)
                diag_response_packet = EServerPackets.e5f01rsp

            # If the level is set to above off, register an observer to get the result.
            if self._mgr.logAgLevel > 0:
                self._mgr.GetPublisherGroup().RegisterObserver([diag_response_packet], self)

            if not self._mgr.TsipSendPacket(diag_enable_cmd, diag_enable_data):
                logger.error("Failed to enable diagnostic logging at the level requested")
                self._mgr.GetPublisherGroup().UnregisterObserver(self)

            # If diag level is off, we didn't register a response observer, so sleep a little
            # for the receiver to configure and then signal the connected event.
            if 0 == self._mgr.logAgLevel:
                time.sleep(0.1)
                
        #  signal the connected event
        self._mgr._connectedEvent.set()


    #-----------------------------------------------------------------------------
    #   def ExitState(...)
    #-----------------------------------------------------------------------------
    def ExitState(self):
        logger.debug("Leaving Connected State")
        self._mgr.ClearTimeout()
        self._mgr.GetPublisherGroup().UnregisterObserver(self)
        self._mgr._connectedEvent.clear()

    #-----------------------------------------------------------------------------
    #   def PeriodicHandler(...)
    #-----------------------------------------------------------------------------
    def PeriodicHandler(self):
        if self._mgr.GetPublisherGroup().GetPacketCount() > 0:
            # At least one packet was received during last periodic interval.
            self._mgr.GetPublisherGroup().ResetPacketCount()
            self._mgr.SetTimeoutMsec(PortStateConnected.ConnectionTimeoutMsec)
        elif self._mgr.ManageConnection():
            if self._mgr.CheckTimeout():
                # We have not received any TSIP packets during the timeout interval,
                # so it is likely that the connection has been lost.
                self._mgr.SetState(self._mgr.GetStateNotConnected())

    #-----------------------------------------------------------------------------
    #   def HandleStreamRead(...)
    #-----------------------------------------------------------------------------
    def HandleStreamRead(self, data, length):
        readBuffer = self._mgr.GetReadBuffer()
        readBuffer.Append(data)
        self._mgr.GetPublisherGroup().ProcessInput(readBuffer)


"""
#=============================================================================
# PortStateMonTsip
#=============================================================================
"""
class PortStateMonTsip(PortState):
    """This state is used to send and receive messages for enabling/disabling MonTsip
    
    It sends a serial break and then the break command per-device to enable montsip
    WARNING: Ceres devices cannot exit FSMon...for some reason.
    """
    RespWaitTimeoutMsec = 2000  # 2 sec

    HighSpeedTsipRequest = "HIGH SPEED TSIP BACKDOOR\r\n"
    HighSpeedTsipResponse = "HIGH SPEED TSIP IS "

    HighSpeedMonTsipEnterRequest = "ENTER HS MONTSIP MODE\r\n"
    HighSpeedMonTsipEnterResponse = "ENTERING HS MONTSIP MODE\r\n"
    
    HighSpeedMonTsipExitRequest = "STANDARD TSIP BACKDOOR\r\n"
    HighSpeedMonTsipExitResponse = "STANDARD TSIP ENABLED\r\n"

    #----------------------------------------------------------------------------
    # PortStateMonTsip Constructor
    #-----------------------------------------------------------------------------
    def __init__(self, portMgr, enter):
        super().__init__(portMgr)
        self._isEntering = enter
        self._retryCount = 0
        self._breakSent = False

    def GetRequestString(self):
        if self._mgr.product.isDemeterProduct():
            if self._isEntering:
                return PortStateMonTsip.HighSpeedMonTsipEnterRequest
            elif not self._isEntering:
                return PortStateMonTsip.HighSpeedMonTsipExitRequest
        else:
            if self._isEntering:
                return PortStateMonTsip.HighSpeedTsipRequest
            else:
                return PortStateMonTsip.HighSpeedMonTsipExitRequest

    def GetResponseString(self):
        if self._mgr.product.isDemeterProduct():
            if self._isEntering:
                return PortStateMonTsip.HighSpeedMonTsipEnterResponse
            elif not self._isEntering:
                return PortStateMonTsip.HighSpeedMonTsipExitResponse
        else:
            if self._isEntering:
                return PortStateMonTsip.HighSpeedTsipResponse
            else:
                return PortStateMonTsip.HighSpeedMonTsipExitResponse

    #-----------------------------------------------------------------------------
    #   def ConfigPortForRequest(...)
    #-----------------------------------------------------------------------------
    def ConfigPortForRequest(self, port):
        """Configure port to send a break command, send serial break if necessary"""
        port.baudrate = 9600
        port.parity = serial.PARITY_NONE
        time.sleep(0.1)
        port.reset_input_buffer()
        port.reset_output_buffer()
        if not self._breakSent:
            self._mgr.GetReadBuffer().Clear()
            send_break(port, PortStateAutoConfigure.BreakMS)

    #-----------------------------------------------------------------------------
    #   def EnterState(...)
    #-----------------------------------------------------------------------------
    def EnterState(self):
        self._mgr._monTsipDoneEvent.clear()
        # Clear local read buffer in preparation for receiving response to
        # high speed TSIP request.
        self._mgr.GetReadBuffer().Clear()
        
        # Clear UART write buffer and write high speed TSIP request
        port = self._mgr.GetPort()
        self.ConfigPortForRequest(port)

        # TODO: This relies on sleeping 100ms so we receive the product type string. Needs to be done in HandleStreamRead instead.
        if self._mgr.product == ProductId.Unknown:
            logger.warning("Cannot detect product type, disconnecting")
            # TODO: EnterState can't call SetState! It's reentrant and bad.
            self._mgr.SetState(self._mgr.GetStateNotConnected())
            return

        outString = self.GetRequestString()

        logger.debug(outString)

        outData = outString.encode('ascii')
        port.write(outData)

        # Setup timeout
        self._mgr.SetTimeoutMsec(PortStateMonTsip.RespWaitTimeoutMsec)

    #-----------------------------------------------------------------------------
    #   def ExitState(...)
    #-----------------------------------------------------------------------------
    def ExitState(self):
        self._mgr.ClearTimeout()
        self._mgr._monTsipDoneEvent.set()

    #-----------------------------------------------------------------------------
    #   def PeriodicHandler(...)
    #-----------------------------------------------------------------------------
    def PeriodicHandler(self):
        if self._retryCount < 3:
            self._retryCount += 1
            self.EnterState()
        if self._mgr.CheckTimeout():
            # No response was received before timeout interval elapsed.
            logger.error("Unable to configure MonTsip")
            self._mgr.SetState(self._mgr.GetStateConnected())

   
    #-----------------------------------------------------------------------------
    #   def HandleStreamRead(...)
    #-----------------------------------------------------------------------------
    def HandleStreamRead(self, data, length):
        readBuffer = self._mgr.GetReadBuffer()
        readBuffer.Append(data)
        baudRateStr, parity = self.FindResponse(readBuffer)
        if len(baudRateStr) > 0:
            # if we are exiting monTsip on buffalo radio, set baudrate and parity
            # here, as this is the default
            if not self._isEntering and not self._mgr.product.isDemeterProduct():
                baudRateStr = "9600"
                parity = serial.PARITY_ODD

            self._mgr.ConfigPort(baudRateStr, parity)
            # We are now auto-configured to talk TSIP with device connected to port.
            connectedStateInstance = self._mgr.GetStateConnected()
            connectedStateInstance._isMonTsipEnabled = self._isEntering
            logger.info("MonTsip Enabled Successfully")

            if self._isEntering:
                self._mgr._publisherGroup.EnableMonTsip()
            else:
                self._mgr._publisherGroup.DisableMonTsip()

            self._mgr.SetState(connectedStateInstance)
        else:
            # Didn't find what we're looking for yet. Make sure that we don't
            # accumulate a huge number of bytes in the buffer, in case we
            # are connected to something that ignores the break and generates
            # a lot of output.
            readBuffer.Truncate(200)


    #-----------------------------------------------------------------------------
    #   def buffaloParser(...)
    #-----------------------------------------------------------------------------

    def buffaloParser(self, readBuffer):
        ParseMode_FindText = 0
        ParseMode_FindNewline = 1
        ParseMode_ScanBaudRate = 2
        ParseMode_Abort = 3
        ParseMode_Done = 4

        i = 0
        parseMode = ParseMode_FindText
        respHdr = self.GetResponseString()
        respLen = len(respHdr)
        possibleMatch = False
        baudRateStr = ""
        data = readBuffer.Get()
        logger.debug("Auto Connect Data: " + str(data))
        hasCRLF = False
        for byte in data:
            if byte == CR or byte == LF:
                hasCRLF = True
                break
        if not hasCRLF:
            return "", None
        while parseMode < ParseMode_Done:
            if readBuffer.Length() > 0:
                byte = readBuffer.Pop1()
            else:
                parseMode = ParseMode_Done
            if parseMode == ParseMode_FindText:
                if possibleMatch:
                    if i == respLen:
                        parseMode = ParseMode_FindNewline
                    elif byte == ord(respHdr[i]):
                        i += 1
                    else:
                        possibleMatch = False
                        i = 0
                elif byte == ord(respHdr[i]):
                    possibleMatch = True
                    i += 1
            if parseMode == ParseMode_FindNewline:
                if byte == CR or byte == LF:
                    parseMode = ParseMode_Done
                else:
                    baudRateStr = baudRateStr + (chr(byte))
            if parseMode == ParseMode_Abort:
                parseMode = ParseMode_Done
        return baudRateStr, serial.PARITY_ODD if self._isEntering else serial.PARITY_NONE
    
    #-----------------------------------------------------------------------------
    #   def demeterParser(...)
    #-----------------------------------------------------------------------------
    def demeterParser(self, readBuffer):
        respHdr = self.GetResponseString()
        baudRateStr = ""
        data = readBuffer.Get()
        parity = None
        logger.debug("Auto Connect Data: " + str(data))
        if respHdr in data.decode('utf-8'):
            if self._isEntering:
                baudRateStr = "115200"
            else:
                baudRateStr = "9600"
                parity = serial.PARITY_ODD
        return baudRateStr, parity

    #-----------------------------------------------------------------------------
    #   def FindResponse(...)
    #-----------------------------------------------------------------------------
    def FindResponse(self, readBuffer):
        data = bytearray()
        data[:] = readBuffer.Get()
        
        #  Check from response if in monitor mode to set baud and parity
        if 'MONPRODUCT' in str(data):
            baudRateStr = "115200"
            parity = None
            return baudRateStr, parity

        if self._mgr.product.isDemeterProduct():
            return self.demeterParser(readBuffer)
        else:
            return self.buffaloParser(readBuffer)
