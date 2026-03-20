#===========================================================================
# @file tsip_packet_publisher.cpp
#
# Implements class tsip_port_manager.PacketPublisherGroup.

# Copyright (c) 2017 Trimble Navigation Limited
#===========================================================================

from enum import Enum
import copy
import time
import logging
from .data_buffer import BinaryBuffer

# from .data_schema import
from .tsip_schema import *

# Module-level logger
logger = logging.getLogger("py_tsip")
logger.setLevel(logging.WARNING)
from .tsip_packets import ClientPacketEncoder, ServerPacketEncoder, \
    ClientPacketDecoder, ServerPacketDecoder, \
    EClientPackets, EServerPackets
from .tsip_decoders import ClientMessageDecoder, ServerMessageDecoder
from .tsip_encoders import TsipMessageEncoder
from .observer import ObserverManager, BlockingObserver


class PortMode(Enum):
    RemoteClient = 0
    RemoteServer = 1
            

"""
#=============================================================================
# TsipPacketPublisher
#=============================================================================
"""


class TsipPacketPublisher(ObserverManager):
    def __init__(self, portManager, packetDecoder, MessageDecoder):
        super().__init__()
        self._portManager         = portManager
        self._packetDecoder       = packetDecoder
        self._messageDecoder      = MessageDecoder
        
        self._Data = bytearray()
        self._enableMonTsip       = False
        self._packetCount         = 0

    def ResetPacketCount(self):
        self._packetCount = 0
                
    def SetMonTsipEnable(self, flag):
        self._enableMonTsip = flag

    def ProcessPacket(self, readBuffer):
        #trap MonTsip packets and just pass through if enabled
        if self._enableMonTsip and readBuffer[0] == 0x8f and readBuffer[1] == 0xa1:
            self.NotifyObservers(EServerPackets.e8fa1rsp, readBuffer.Get())
            return True
        
        status = self._packetDecoder.Decode(readBuffer)
        if status == TSIP_DECODER_PACKET_AVAILABLE:
            self._packetCount += 1
            packetId = self._packetDecoder.GetSchema().GetEntryType()
            logger.info("[py-tsip] RECV %s: %s", packetId.name if hasattr(packetId, 'name') else str(packetId), self._packetDecoder.get_data().hex())
            message = self._messageDecoder.DecodeMessage(packetId, self._packetDecoder.get_data())
            self.NotifyObservers(packetId, message)
            return True
        else:
            return False

    

"""
#-----------------------------------------------------------------------------
# Publisher Group Class
#-----------------------------------------------------------------------------
"""


class TsipPacketPublisherGroup():
    def __init__(self, portMgr):
        self._portMgr = portMgr
        self._clientPublisher = TsipPacketPublisher(portMgr, ClientPacketDecoder(), ClientMessageDecoder())
        self._serverPublisher = TsipPacketPublisher(portMgr, ServerPacketDecoder(), ServerMessageDecoder())
        self._clientEncoder = ClientPacketEncoder()
        self._serverEncoder = ServerPacketEncoder()
        self._tsipDeframer = TSIPDeframer()
        self._deframeBuffer = BinaryBuffer()
        self._tsipFramer = TSIPFramer()
        self._packetCount = 0

    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.GetPacketCount(...)
    #-----------------------------------------------------------------------------
    def GetPacketCount(self):
        return self._packetCount

    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.ResetPacketCount(...)
    #-----------------------------------------------------------------------------
    def ResetPacketCount(self):
        self._clientPublisher.ResetPacketCount()
        self._serverPublisher.ResetPacketCount()

    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.RegisterObserver(Client...)
    #-----------------------------------------------------------------------------
    def RegisterObserver(self, pktIdSet, observer):
        self._clientPublisher.RegisterObserver(pktIdSet, observer)
        self._serverPublisher.RegisterObserver(pktIdSet, observer)

    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.UnregisterObserver(Client...)
    #-----------------------------------------------------------------------------
    def UnregisterObserver(self, observer):
        self._clientPublisher.UnregisterObserver(observer)
        self._serverPublisher.UnregisterObserver(observer)

    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.EnableMonTsip(Client...)
    #-----------------------------------------------------------------------------
    def EnableMonTsip(self):
        self._clientPublisher.SetMonTsipEnable(True)
        self._serverPublisher.SetMonTsipEnable(True)
        
    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.DisableMonTsip(Client...)
    #-----------------------------------------------------------------------------
    def DisableMonTsip(self):
        self._clientPublisher.SetMonTsipEnable(False)
        self._serverPublisher.SetMonTsipEnable(False)
        
    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.ProcessInput(...)
    #-----------------------------------------------------------------------------
    def ProcessInput(self, readBuffer):
        logger.log(9, "[py-tsip] Received %d new bytes" % (readBuffer.Length()))
        packetData = self._deframeBuffer
        while readBuffer.NotEmpty():
            response = self._tsipDeframer.deframe(readBuffer, packetData)
            if response == TSIP_DECODER_PACKET_AVAILABLE:
                self.PublishPacket(packetData)

    #-----------------------------------------------------------------------------
    # PacketPublisherGroup.PublishPacket(...)
    #-----------------------------------------------------------------------------
    def PublishPacket(self, packetData):
        self._packetCount += 1
        data = packetData.Get()
        # Uncomment me to log packets received from the Nav:
        # logger.info(f"[py-tsip] {data.hex()}")
        status = self._serverPublisher.ProcessPacket(packetData)
        if status == False:
            status = self._clientPublisher.ProcessPacket(packetData)
        if status == False:
            logger.warning(
                "[py-tsip] Packet decode failed for packet %s", data.hex())

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.TsipSendClientPacket(...)
    #-----------------------------------------------------------------------------
    def TsipSendClientPacket(self, type, packet):
        if packet != None:
            data = TsipMessageEncoder().EncodeMessage(type, packet)
            if data == None:
                return False
        else:
            data = None
        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        tmpout = bytearray(tmplist)
        outbuf = OutBuffer(tmpout, TSIPSCHEMA_MAX_PACKET_SIZE)
        self._clientEncoder.SetCurrentSchema(type.value)
        if data != None:
            tmpin = bytearray(data)
            inbuf = InBuffer(tmpin, len(tmpin))
        else:
            inbuf = InBuffer(None, 0)
        if self._clientEncoder.Encode(inbuf, outbuf):
            # Single consolidated log message for TSIP send
            logger.info(f"[py-tsip] SEND {type.name}: {outbuf.used().hex()}")
            return self._portMgr.PacketWrite(outbuf.used())

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.TsipSendServerPacket(...)
    #-----------------------------------------------------------------------------
    def TsipSendServerPacket(self, type, packet):
        if packet != None:
            data = TsipMessageEncoder().EncodeMessage(type, packet)
            if data == None:
                return False
        else:
            data = None
        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        tmpdata = bytearray(tmplist)
        outbuf = OutBuffer(tmpdata, TSIPSCHEMA_MAX_PACKET_SIZE)
        self._serverEncoder.SetCurrentSchema(type.value)
        if data != None:
            tmpin = bytearray(data)
            inbuf = InBuffer(tmpin, len(data))
        else:
            inbuf = InBuffer(None, 0)
        if self._serverEncoder.Encode(inbuf, outbuf):
            # Uncomment me to log TSIP commands sent to the Nav:
            # logger.info(f"[py-tsip] {outbuf.used().hex()}")
            return self._portMgr.PacketWrite(outbuf.used())

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.TsipSendPacket(...)
    #-----------------------------------------------------------------------------
    def TsipSendPacket(self, type, packet):
        if isinstance(type, EClientPackets):
            return self.TsipSendClientPacket(type, packet)
        elif isinstance(type, EServerPackets):
            return self.TsipSendServerPacket(type, packet)
        else:
            return False

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.TsipSendRawPacket(...)
    #-----------------------------------------------------------------------------
    def TsipSendRawPacket(self, data, includeChecksum):
        if (includeChecksum):
            checksum = self.CalcChecksum(data)
            csbytes = pack('>H', checksum)
            data += csbytes

        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        tmpdata = bytearray(tmplist)
        outbuf = OutBuffer(tmpdata, TSIPSCHEMA_MAX_PACKET_SIZE)
        inbuf = InBuffer(data, len(data))
        self._tsipFramer.frame(inbuf, outbuf)
        return self._portMgr.PacketWrite(outbuf.used())

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.CalcChecksum(...)
    #-----------------------------------------------------------------------------
    def CalcChecksum(self, data):
        cs = 0
        # always skip the first byte (ID is not included in checksum)
        for i in range(1, len(data)):
            cs += data[i]
        return cs

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.TsipSendRawData(...)
    #-----------------------------------------------------------------------------
    def TsipSendRawData(self, data):
        return self._portMgr.PacketWrite(data)

    #-----------------------------------------------------------------------------
    # def PacketPublisherGroup.waitForTsipResponse(...)
    #-----------------------------------------------------------------------------
    def waitForTsipResponse(self, id, timeout):
        if isinstance(id, EClientPackets):
            return self._clientPublisher.waitForResponse(id, timeout)
        elif isinstance(id, EServerPackets):
            return self._serverPublisher.waitForResponse(id, timeout)
        else:
            return None

