
#========================================================================
#  Definitions for tsip packet data structures
#  NOTE: this file was auto-generated from tsippackets.xml

# pylint: disable=line-too-long,invalid-name

#------------------------------------------------------------------------
# @name TSIP Packet Conditional Definitions

from enum import Enum
from collections import namedtuple
from .data_buffer import *
from .data_schema import *
from .tsip_schema import *

# Value that defines whether specific functionality is enabled
TSIPENABLED = 4321

# TSIP Client Packet encoding and Server Packet decoding is enabled
TSIP_CLIENT = TSIPENABLED

# TSIP Server Packet encoding and Client Packet decoding is enabled
TSIP_SERVER = TSIPENABLED

  #----------------------------------------------------------------------
  #
  #----------------------------------------------------------------------
  # @name TSIP Packet Structure Definitions

# This is used so we can get to the raw data
S00cmd_tup = namedtuple('S00cmd_tup', ', PacketDataLength, PacketData')
S00cmd_bin = '=B*'
# Wraps RTCM data for output in a TSIP stream.
S1a00cmd_tup = namedtuple('S1a00cmd_tup', ', RTCMDataLength, RTCMData')
S1a00cmd_bin = '=B*'
# Controls forwarding of DCOL packets to connected port
S1a0200cmd_tup = namedtuple('S1a0200cmd_tup', ' NumTypes DCOLTypes')
S1a0200cmd_bin = '=B?B'
# TSIP wrapped DCOL message command to device.
S1a0201cmd_tup = namedtuple('S1a0201cmd_tup', ' NumBytes DCOLMessage')
S1a0201cmd_bin = '=B?B'
# Wraps DCOL messages for processing in a TSIP stream.
S1a0202cmd_tup = namedtuple('S1a0202cmd_tup', ' NumBytes DCOLMessage')
S1a0202cmd_bin = '=B?B'
# Controls forwarding of CAN messages from connected
S1a0300cmd_tup = namedtuple('S1a0300cmd_tup', ' CanPort NumIDs CanIds')
S1a0300cmd_bin = '=BB?L'
# TSIP wrapped CAN message to forward to CAN device
S1a0301cmd_tup = namedtuple('S1a0301cmd_tup', ' CanPort CanId CanMsgLength CanMsg')
S1a0301cmd_bin = '=BLB?B'
# Clears all battery-backed data and performs a software reset to initiate a cold start of the receiver.
S1e4bcmd_tup = namedtuple('S1e4bcmd_tup', '')
S1e4bcmd_bin = '='
# Requests the firmware information from the receiver. Responds with the 0x45 packet.
S1freq_tup = namedtuple('S1freq_tup', '')
S1freq_bin = '='
# Requests the firmware information from the receiver. Responds with the 0x45 packet.
S1freqv1_tup = namedtuple('S1freqv1_tup', ' MachineId RequestType')
S1freqv1_bin = '=BB'
# Requests almanac data for one satellite from the receiver
S20req_tup = namedtuple('S20req_tup', ' SatNumber')
S20req_bin = '=B'
# Requests current GPS time from the receiver. Report packet 0x41 is sent in response.
S21req_tup = namedtuple('S21req_tup', '')
S21req_bin = '='
# Configures the receiver to operate in a specific position fix mode and stores the new mode setting in battery-backed memory.
S22cmd_tup = namedtuple('S22cmd_tup', ' PositionFixMode')
S22cmd_bin = '=B'
# Initiates a software reset for the receiver, causing the receiver to perform the equivalent of powering off and then on. The receiver performs a self-test during the reset routine. Command Packet 0x25 contains no data bytes.
S25cmd_tup = namedtuple('S25cmd_tup', '')
S25cmd_bin = '='
# Requests health and status information from the receiver. Report packets 0x46 and 0x4B are sent in response.
S26req_tup = namedtuple('S26req_tup', '')
S26req_bin = '='
# Requests signal levels for all satellites currently being tracked. Report packet 0x47 is sent in response.
S27req_tup = namedtuple('S27req_tup', '')
S27req_bin = '='
# Controls output of Engineering Diagnostics
S3f02cmd_tup = namedtuple('S3f02cmd_tup', ' DebugEnabled')
S3f02cmd_bin = '=B'
# Request the current operating parameter values of the receiver, which responds with Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory.
S2creq_tup = namedtuple('S2creq_tup', '')
S2creq_bin = '='
# Sets the operating parameter values of a receiver or requests the current parameter values, and the receiver responds by sending the parameter values in Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory.
S2ccmd_tup = namedtuple('S2ccmd_tup', ' DynamicsCode ElevationMask SignalLevelMask PDOPMask PDOPSwitch')
S2ccmd_bin = '=Bffff'
# Requests analog to digital readings from receiver
S33req_tup = namedtuple('S33req_tup', '')
S33req_bin = '='
# Requests the current I/O option flags. The receiver responds by sending Report Packet 0x55.
S35req_tup = namedtuple('S35req_tup', '')
S35req_bin = '='
# Sets the current I/O option flags. The receiver records the I/O option flags settings in battery-backed memory and sends Report Packet 0x55 in response.
S35cmd_tup = namedtuple('S35cmd_tup', ' PosFlags VelocityFlags TimingFlags AuxFlags')
S35cmd_bin = '=BBBB'
# Command Packet 0x38 downloads satellite data from one receiver, and uploads the data to another receiver. The receiver acknowledges a download operation by sending the requested data in Report Packet 0x58. The process of downloading satellite data from one receiver and uploading it to another decreases the amount of time required for the receiver to initialize from a cold start (battery-backed memory cleared). Note that the receiver can initialize itself without uploading data, it merely takes longer. To download data from one receiver, use only bytes 0&#8211;2. To upload the data to another receiver, use all bytes.
S38cmd_tup = namedtuple('S38cmd_tup', ' Operation DataType SVPRN')
S38cmd_bin = '=BBB'
# Command Packet 0x3B requests the current status of satellite ephemeris data. The receiver acknowledges with Report Packet 0x5B when data is available.
S3breq_tup = namedtuple('S3breq_tup', ' SatNumber')
S3breq_bin = '=B'
# Requests the current satellite tracking status. The receiver acknowledges with Report Packet 0x5C when data is available.
S3creq_tup = namedtuple('S3creq_tup', ' SatNumber')
S3creq_bin = '=B'
# Requests the differential GPS position fix mode. Report packet 0x82 is sent in response
S62req_tup = namedtuple('S62req_tup', '')
S62req_bin = '='
# Sets the differential GPS position fix mode. Report packet 0x82 is sent in response
S62cmd_tup = namedtuple('S62cmd_tup', ' FixMode')
S62cmd_bin = '=B'
# Requests DGPS corrections for given SVID
S65req_tup = namedtuple('S65req_tup', ' SVID')
S65req_bin = '=B'
# Requests one of several RTK stats reports. A variant of report packet 0x89 0x33 is sent in response, with the second report packet byte indicating the type of stats.
S6932req_tup = namedtuple('S6932req_tup', ' StatsType Control')
S6932req_bin = '=BB'
# Requests the RTK configuration
S6940req_tup = namedtuple('S6940req_tup', '')
S6940req_bin = '='
# Sets the RTK configuration
S6940cmd_tup = namedtuple('S6940cmd_tup', ' PropagationMode VelocityType')
S6940cmd_bin = '=BB'
# Requests RTK solution info. Report packet 0x89 0x41 is sent in response.
S6941req_tup = namedtuple('S6941req_tup', '')
S6941req_bin = '='
# Requests the RTK auxilliary settings. Report packet 0x89 0x50 is sent in response.
S6950req_tup = namedtuple('S6950req_tup', '')
S6950req_bin = '='
# Updates RTK auxilliary settings. Report packet 0x89 0x50 is sent in response.
S6950cmd_tup = namedtuple('S6950cmd_tup', ' ScintillationMode BackupSource RTKBaseDatum XFillSatFrequency XFillSatBitRate RTKBaseID SatConfigSource')
S6950cmd_bin = '=BBBdfHB'
# Requests the RTK auxilliary status. Report packet 0x89 0x51 is sent in response.
S6951req_tup = namedtuple('S6951req_tup', '')
S6951req_bin = '='
# Requests RTK base info. Report packet 0x89 0x60 is sent in response.
S6960req_tup = namedtuple('S6960req_tup', '')
S6960req_bin = '='
# Requests CMR info. Report packet 0x89 0x61 is sent in response.
S6961req_tup = namedtuple('S6961req_tup', '')
S6961req_bin = '='
# Requests Ionospheric disturbance info. Report packet 0x89 0x62 is sent in response.
S6962req_tup = namedtuple('S6962req_tup', '')
S6962req_bin = '='
# Requests RTK radio status. Report packet 0x89 0x70 0x00 is sent in response.
S697000req_tup = namedtuple('S697000req_tup', '')
S697000req_bin = '='
# Requests RTK radio identity. Report packet 0x89 0x70 0x01 is sent in response.
S697001req_tup = namedtuple('S697001req_tup', '')
S697001req_bin = '='
# Requests RTK radio capabilities. Report packet 0x89 0x70 0x02 is sent in response.
S697002req_tup = namedtuple('S697002req_tup', '')
S697002req_bin = '='
# Requests RTK radio country info. Report packet 0x89 0x70 0x03 is sent in response.
S697003req_tup = namedtuple('S697003req_tup', '')
S697003req_bin = '='
# Requests config specific to 900MHz RTK radio. Report packet 0x89 0x70 0x04 is sent in response.
S697004req_tup = namedtuple('S697004req_tup', '')
S697004req_bin = '='
# Requests config specific to 450MHz RTK radio. Report packet 0x89 0x70 0x05 is sent in response.
S697005req_tup = namedtuple('S697005req_tup', '')
S697005req_bin = '='
# Sets RTK radio country code. Ack packet 0x89 0x70 0x06 is sent in response.
S697006cmd_tup = namedtuple('S697006cmd_tup', ' CountryCode')
S697006cmd_bin = '=B'
# Sets 900MHz RTK radio network ID. Ack packet 0x89 0x70 0x07 is sent in response.
S697007cmd_tup = namedtuple('S697007cmd_tup', ' NetworkId')
S697007cmd_bin = '=B'
# Sets 450MHz RTK radio channel ID. Ack packet 0x89 0x70 0x08 is sent in response.
S697008cmd_tup = namedtuple('S697008cmd_tup', ' ChannelId')
S697008cmd_bin = '=B'
# Sets 450MHz RTK radio channel frequency. Ack packet 0x89 0x70 0x09 is sent in response.
S697009cmd_tup = namedtuple('S697009cmd_tup', ' ChannelId Freq')
S697009cmd_bin = '=BL'
# Sets 450MHz RTK radio mode. Ack packet 0x89 0x70 0x0a is sent in response.
S69700acmd_tup = namedtuple('S69700acmd_tup', ' Mode')
S69700acmd_bin = '=B'
# Restart connected RTK radio and re-establish communication. Ack packet 0x89 0x70 0x0b is sent in response.
S69700bcmd_tup = namedtuple('S69700bcmd_tup', '')
S69700bcmd_bin = '='
# Requests Fallback RTX: X, Y, and Z offsets for the designated source. Response packet is 0x89 0x71 0x00. No longer supported, do not use.
S697100req_tup = namedtuple('S697100req_tup', ' RTXOffsetSource')
S697100req_bin = '=B'
# Set the X, Y, and Z user offsets. ACK packet is 0x89 0x71 0x01. No longer supported, do not use.
S697100cmd_tup = namedtuple('S697100cmd_tup', ' XOffsetValue YOffsetValue ZOffsetValue')
S697100cmd_bin = '=ddd'
# Requests the Fallback RTX configuration mode and the offset source. Response packet is 0x89 0x71 0x01. No longer supported, do not use.
S697101req_tup = namedtuple('S697101req_tup', '')
S697101req_bin = '='
# Sets Fallback RTX mode and offset source. ACK packet is 0x89 0x71 0x03. No longer supported, do not use.
S697101cmd_tup = namedtuple('S697101cmd_tup', ' FallbackMode RTXOffsetSource')
S697101cmd_bin = '=BB'
# Requests xFill Premium configuration. Response packet is 0x89 0x71 0x03.
S697103req_tup = namedtuple('S697103req_tup', '')
S697103req_bin = '='
# Sets xFill Premium Configuration. ACK packet is 0x89 0x71 0x03.
S697103cmd_tup = namedtuple('S697103cmd_tup', ' ScintillationSwitchRule ActivateXFillPremium ActivateHour ActivateMinute DeactivateHour DeactivateMinute RecalXFill')
S697103cmd_bin = '=BBBBBBB'
# Requests current differential corrections output control settings.
S6a01req_tup = namedtuple('S6a01req_tup', '')
S6a01req_bin = '='
# Controls whether or not the receiver will output differential correction information.
S6a01cmd_tup = namedtuple('S6a01cmd_tup', ' CorrectionsUsedInFix CorrectionInfo')
S6a01cmd_bin = '=BB'
# Enables or disables the P/V Filter, Static Filter, and/or Altitude Filter.
S70cmd_tup = namedtuple('S70cmd_tup', ' DynamicFilter StaticFilter AltitudeFilter FilterLevel')
S70cmd_bin = '=BBBB'
# Requests the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode. The receiver acknowledges with Report Packet 0x78.
S77req_tup = namedtuple('S77req_tup', '')
S77req_bin = '='
# Sets the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode.
S77cmd_tup = namedtuple('S77cmd_tup', ' MaxPRCAge')
S77cmd_bin = '=H'
# Requests the data reporting options for the NMEA output on the specified port. The receiver responds with Report Packet 0x7B 0x07.
S7a07req_tup = namedtuple('S7a07req_tup', ' Port')
S7a07req_bin = '=B'
# Sets the data reporting options for the NMEA output on the specified port.
S7a07cmd_tup = namedtuple('S7a07cmd_tup', ' Port Options1')
S7a07cmd_bin = '=BB'
# Requests the data reporting options for NMEA on the specified receiver port. The receiver responds with Report Packet 0x7B 0x08.
S7a08req_tup = namedtuple('S7a08req_tup', ' Port')
S7a08req_bin = '=B'
# Each Ag Receivers supports a varying number of serial ports that can transmit NMEA messages. This command configures various parameters of the NMEA for the specified serial port (if supported) on the receiver. This command supersedes other NMEA configuration commands and is designed to be used stand-alone (and not in conjunction with other NMEA Configuration command packets). The receiver acknowledges with 0x7B 0x08.
S7a08cmd_tup = namedtuple('S7a08cmd_tup', ' Port MessageProtocol MessageInterval OutputMask GGAOptions Precision')
S7a08cmd_bin = '=BBBLBB'
# Requests the NMEA message transmission interval or a combination of the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response.
S7a80req_tup = namedtuple('S7a80req_tup', '')
S7a80req_bin = '='
# Sets the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response.
S7a80cmd_tup = namedtuple('S7a80cmd_tup', ' Interval OutputMask')
S7a80cmd_bin = '=BL'
# Requests the data reporting options for the NMEA GGA, GGL, VTG, and RMC message sentences for the current port. Report Packet 0x7B 0x86 is sent in response.
S7a86req_tup = namedtuple('S7a86req_tup', ' MsgType')
S7a86req_bin = '=B'
# Sets the GGA options and precision for the current port.
S7a8600cmd_tup = namedtuple('S7a8600cmd_tup', ' Options Precision')
S7a8600cmd_bin = '=BB'
# Sets the RMC options and precision for the current port.
S7a8604cmd_tup = namedtuple('S7a8604cmd_tup', ' Options PosPrecision SpeedPrecision')
S7a8604cmd_bin = '=BBB'
# Sets the VTG options for the current port.
S7a8602cmd_tup = namedtuple('S7a8602cmd_tup', ' Options')
S7a8602cmd_bin = '=B'
# Sets the VTG speed precision for the current port.
S7a8603cmd_tup = namedtuple('S7a8603cmd_tup', ' SpeedPrecision')
S7a8603cmd_bin = '=B'
# Sets the VTG Heading Precision for the current port.
S7a8605cmd_tup = namedtuple('S7a8605cmd_tup', ' HeadingPrecision')
S7a8605cmd_bin = '=B'
# Requests the rate for computing position fixes. Report Packet 0x7D 0x00 is sent in response.
S7c00req_tup = namedtuple('S7c00req_tup', '')
S7c00req_bin = '='
# Sets the rate for computing position fixes.
S7c00cmd_tup = namedtuple('S7c00cmd_tup', ' ASAPRate')
S7c00cmd_bin = '=B'
# Requests the position fix rate I/O option bytes. Report Packet 0x7D 0x01 is sent in response.
S7c01req_tup = namedtuple('S7c01req_tup', '')
S7c01req_bin = '='
# Sets the position fix rate I/O options bytes.
S7c01cmd_tup = namedtuple('S7c01cmd_tup', ' OptionFlags1 OptionFlags2')
S7c01cmd_bin = '=BB'
# Requests the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. Report Packet 0x7D 0x02 is sent in response.
S7c02req_tup = namedtuple('S7c02req_tup', '')
S7c02req_bin = '='
# Sets the position fix output interval and offset that are used to deterimne output rate in relation to fix rate.
S7c02cmd_tup = namedtuple('S7c02cmd_tup', ' Interval Offset')
S7c02cmd_bin = '=HH'
# Requests the message interval for the specified port and protocol.
S7c09req_tup = namedtuple('S7c09req_tup', ' Port MessageProtocol')
S7c09req_bin = '=BB'
# Sets the message interval for the specifed port and protocol.
S7c09cmd_tup = namedtuple('S7c09cmd_tup', ' Port MessageProtocol MessageInterval')
S7c09cmd_bin = '=BBB'
# Requests a report containing the current receiver configuration parameter settings and software version number. Report Packet 0x8F 0x7B is sent in response.
S8e7breq_tup = namedtuple('S8e7breq_tup', '')
S8e7breq_bin = '='
# 
S8e7ccmdBoilerPlate_tup = namedtuple('S8e7ccmdBoilerPlate_tup', ', SerialNumber, PartNumber, OverrideName, BriefOverrideName ManufactureDay ManufactureMonth ManufactureYear SuperPacketPP')
S8e7ccmdBoilerPlate_bin = '=22s10s17s6sBBHH'
# 
S8e7ccmdRxDef_tup = namedtuple('S8e7ccmdRxDef_tup', ' ProductId CarrierPhaseOption BeaconOption RefStationOption EverestOption ModemControlOption DESubscriptionWeek LBandProviders HardwareType VRSProcessingOption FirmwareNotInstalled DisabledStreamsOption TiltSensorOption GPSDisabledOption WAASOption MaxPosRateOption CMRInputOption PointLineAreaLoggingOption CANSelfAddressingOption CANDisabledOption AgLeaderVariant TNLSubscriptionWeek AntennaGain RTKOption BrandingDisabledOption PrototypeHardware DefDGPSSource')
S8e7ccmdRxDef_bin = '=BBBBBBHBBBBBBBBBBBBBBHfBBBB'
# 
S8e7ccmdFixedDef_tup = namedtuple('S8e7ccmdFixedDef_tup', ' BoilerPlate RxDef')
S8e7ccmdFixedDef_bin = '=?B?B'
# 
S8e7ccmdPortConfig_tup = namedtuple('S8e7ccmdPortConfig_tup', ' InProtocol OutProtocol InBaudRate OutBaudRate Parity DataBits StopBits FlowControl')
S8e7ccmdPortConfig_bin = '=BBBBBBBB'
# 
S8e7ccmdUserDef_tup = namedtuple('S8e7ccmdUserDef_tup', ', PortConfig PVFilterFlags ExtRTCMTimeout Guidance Language DistanceDisplayUnits DisplayContrast SNRDisplayUnits')
S8e7ccmdUserDef_bin = '=3?S8e7ccmdPortConfigBBBBBBB'
# 
S8e7ccmdConfigBlockV3_tup = namedtuple('S8e7ccmdConfigBlockV3_tup', ' Head CfgBlkVersion StartupCount FixedDef UserDef Tail RxCfgChecksum')
S8e7ccmdConfigBlockV3_bin = '=BBB?B?BHH'
# Used to set the receiver configuration parameters stored in battery-backed RAM (Random Access Memory). Report Packet 0x8F 0x7C is sent in response.
S8e7ccmd_tup = namedtuple('S8e7ccmd_tup', ' PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3')
S8e7ccmd_bin = '=B20sBBBBB?B'
# Request DGPS Receiver ROM Configuration Block Report
S8e7freq_tup = namedtuple('S8e7freq_tup', '')
S8e7freq_bin = '='
# requests the current status of the DGPS service provider. Report packet 0x8f 0x80 is sent in response.
S8e80req_tup = namedtuple('S8e80req_tup', ' Provider Reserved')
S8e80req_bin = '=BH'
# Get spot station info
S8e81req_tup = namedtuple('S8e81req_tup', '')
S8e81req_bin = '='
# Starts or stops the satellite FFT (Fast Fourier Transform) diagnostics and sets the FFT diagnostic options. Acknowledged with Report Packet 0x8F 0x84.
S8e84cmd_tup = namedtuple('S8e84cmd_tup', ' Mode OscillatorOffset FFTPlotType InputSquared CenterFreq NumIntegrations')
S8e84cmd_bin = '=BBBBdB'
# requests the tracking status for the source of DGPS corrections (either beacon or satellite). Report packet 0x8f 0x85 is sent in response.
S8e85req_tup = namedtuple('S8e85req_tup', '')
S8e85req_bin = '='
# Requests current 
S8e88req_tup = namedtuple('S8e88req_tup', ' StreamId')
S8e88req_bin = '=B'
# Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response.
S8e88cmd_tup = namedtuple('S8e88cmd_tup', ' StreamId OptionsFlags')
S8e88cmd_bin = '=BB'
# Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response.
S8e89req_tup = namedtuple('S8e89req_tup', '')
S8e89req_bin = '='
# Controls DGPS source and related settings. Acknowledgement packet 0x8F 0x89 is sent in response.
S8e89cmd_tup = namedtuple('S8e89cmd_tup', ' DGPSSrcMode BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout CorrectionOptions SatConfigSource')
S8e89cmd_bin = '=BBHHHdfHHBB'
# Requests service provider activation information. Report Packet 0x8F 0x8B is sent in response.
S8e8breq_tup = namedtuple('S8e8breq_tup', ' ServiceProvider InfoType')
S8e8breq_bin = '=BB'
# The key press command packet simulates sending a key press to the display. Whenever the end user application wants to move around the remote display (i.e. in response to a key press on its own terminal, touch screen, etc.), this packet is sent to the receiver to indicate that the receiver should process the specified key press action. The receiver will acknowledge the key press command by sending Report Packet 0x8F 0x8C.
S8e8c00cmd_tup = namedtuple('S8e8c00cmd_tup', ' KeyPress')
S8e8c00cmd_bin = '=B'
# Requests the remote display screen contents once. The receiver will respond by sending Report Packet 0x8F 0x8C 0x01. If automatic reporting of the screen contents is configured, this packet must be sent once per minute to maintain that configuration (version 1.40 and later). This provides a timeout mechanism if the receiver is disconnected from the user terminal so the automatic reporting does not continue indefinitely if not needed.
S8e8c01req_tup = namedtuple('S8e8c01req_tup', '')
S8e8c01req_bin = '='
# Requests the remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x03
S8e8c03req_tup = namedtuple('S8e8c03req_tup', '')
S8e8c03req_bin = '='
# Sets the remote display configuration
S8e8c03cmd_tup = namedtuple('S8e8c03cmd_tup', ' DataLocation')
S8e8c03cmd_bin = '=B'
# Requests the extended remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x04
S8e8c04req_tup = namedtuple('S8e8c04req_tup', '')
S8e8c04req_bin = '='
# Sets the extended remote display configuration
S8e8c04cmd_tup = namedtuple('S8e8c04cmd_tup', ' DataLocation')
S8e8c04cmd_bin = '=B'
# Indicates that one of the event lines into the remote display has changed state.
S8e8c05cmd_tup = namedtuple('S8e8c05cmd_tup', ' EventPort LineState')
S8e8c05cmd_bin = '=BB'
# Requests a report containing the receiver's Machine ID and Product ID used to uniquely identify the receiver architecture. Report Packet 0x8F 0x8F is sent in response.
S8e8freq_tup = namedtuple('S8e8freq_tup', '')
S8e8freq_bin = '='
# Request the Guidance Configuration Information
S8e91req_tup = namedtuple('S8e91req_tup', '')
S8e91req_bin = '='
# Set the guidance configuration information
S8e91cmd_tup = namedtuple('S8e91cmd_tup', ' Units DisplayMode Headland Pattern LookAhead SwathDirection SwathWidth AntennaOffset OutputRate SwathsToSkip')
S8e91cmd_bin = '=BBBBhBffLH'
# Requests a list of files found in the specified directory. A File Transfer Listing Reponse packet is sent for each file in the directory (empty directory will produce no response).
S8e931500req_tup = namedtuple('S8e931500req_tup', ', PathLength, Path')
S8e931500req_bin = '=B*'
# Requests that file be opened for reading. File Transfer Get - Open Response is sent with info needed for the transfer.
S8e93150101req_tup = namedtuple('S8e93150101req_tup', ', FilenameLength, Filename')
S8e93150101req_bin = '=B*'
# Requests to read block of data from open file. If successful File Transfer Get - Data Block Response is sent with the data, otherwise File Transfer Get - Close Response or File Transfer Get - Error Response is sent.
S8e93150102req_tup = namedtuple('S8e93150102req_tup', ' FileId Offset Size')
S8e93150102req_bin = '=LLB'
# Requests to close previously opened file. If successful File Transfer Get - Close Response is sent, otherwise File Transfer Get - Error Response is sent.
S8e93150103req_tup = namedtuple('S8e93150103req_tup', ' FileId')
S8e93150103req_bin = '=L'
# Requests an Hash of the specified file in the fusion file system. The receiver will respond with an Hash response packet (8f930104...)
S8e93150104req_tup = namedtuple('S8e93150104req_tup', ' Algorithm, FilenameLength, Filename')
S8e93150104req_bin = '=BB*'
# Requests that file be opened for writing. File Transfer Put - Open Response is sent with info needed for the transfer.
S8e93150201req_tup = namedtuple('S8e93150201req_tup', ', FilenameLength, Filename')
S8e93150201req_bin = '=B*'
# Requests to write block of data to open file. If successful File Transfer Put - Data Block Response is sent with the data, otherwise File Transfer Put - Close Response or File Transfer Put - Error Response is sent.
S8e93150202req_tup = namedtuple('S8e93150202req_tup', ' FileId Offset Size, DataBlockLength, DataBlock')
S8e93150202req_bin = '=LLBB*'
# Requests to close previously opened file. If successful File Transfer Put - Close Response is sent, otherwise File Transfer Put - Error Response is sent.
S8e93150203req_tup = namedtuple('S8e93150203req_tup', ' FileId')
S8e93150203req_bin = '=L'
# Requests delete of specified file. File Transfer Delete Response is sent to indicate status.
S8e931503req_tup = namedtuple('S8e931503req_tup', ', FilenameLength, Filename')
S8e931503req_bin = '=B*'
# Requests a report containing differential correction information. Report Packet 0x8F 0x9A is sent in response.
S8e9areq_tup = namedtuple('S8e9areq_tup', '')
S8e9areq_bin = '='
# Requests a report containing DGPS source priorities. Report Packet 0x8F 0x9E is sent in response.
S8e9ereq_tup = namedtuple('S8e9ereq_tup', '')
S8e9ereq_bin = '='
# Sets the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be set. The resulting receiver configuration is returned in the response packet 0x8F 0x9E.
S8e9ecmd_tup = namedtuple('S8e9ecmd_tup', ' NumSources SourceInfoArray')
S8e9ecmd_bin = '=B?'
# Request an option upgrade via a supplied password. The receiver respond by sending Response Packet 0x8F 0xA0.
S8ea0cmd_tup = namedtuple('S8ea0cmd_tup', ', Password')
S8ea0cmd_bin = '=22s'
# Requests a Position Solution Status 0x8F 0xA2 report.
S8ea2req_tup = namedtuple('S8ea2req_tup', '')
S8ea2req_bin = '='
# Requests specific information about the Omnistar XP/HP process
S8ea3req_tup = namedtuple('S8ea3req_tup', ' Type')
S8ea3req_bin = '=B'
# Sets Auto-Seed information held by the receiver. If the Auto-Seed functionality is turned on in the receiver, these values will be used at startup when the receiver is rebooted.
S8ea304cmd_tup = namedtuple('S8ea304cmd_tup', ' Confidence Latitude Longitude Height LatitudeVariance LongitudeVariance HeightVariance')
S8ea304cmd_bin = '=fdddfff'
# Sets various control parameters of the Omnistar XP/HP processor
S8ea305cmd_tup = namedtuple('S8ea305cmd_tup', ' ValidFields SeedOnStartup ConfidenceThreshold VelocityThreshold ConvergenceThreshold StaticConvergence SourceSelector')
S8ea305cmd_bin = '=HBfffBB'
# Sets up the debugging output of the XP/HP processor
S8ea306cmd_tup = namedtuple('S8ea306cmd_tup', ' Enabled Port')
S8ea306cmd_bin = '=BB'
# Resets the XP/HP engine
S8ea307cmd_tup = namedtuple('S8ea307cmd_tup', '')
S8ea307cmd_bin = '='
# Requests Filter configuration. Report Packet 0x8F 0xA4 is sent in response.
S8ea4req_tup = namedtuple('S8ea4req_tup', ' Type')
S8ea4req_bin = '=B'
# Sets Quadratic Bias Filter configuration. Report Packet 0x8F 0xA4 0x05 is sent in response.
S8ea405cmd_tup = namedtuple('S8ea405cmd_tup', ' Time Depth MaxPropagationTime State')
S8ea405cmd_bin = '=fffB'
# Sets Kalman Filter configuration. Report Packet 0x8F 0xA4 0x06 is sent in response.
S8ea406cmd_tup = namedtuple('S8ea406cmd_tup', ' MaxPropagationTime SpeedSetting State')
S8ea406cmd_bin = '=fBB'
# Command to enable or disable Field Level Smoothing. Response (ACK) Packet is 0x8f 0xa4 0x07
S8ea407cmd_tup = namedtuple('S8ea407cmd_tup', ' SmoothingEnable')
S8ea407cmd_bin = '=B'
# Requests and sets the current SBAS settings. The command and report packets can each contain a variable number of SBAS SV entries.
S8ea500req_tup = namedtuple('S8ea500req_tup', '')
S8ea500req_bin = '='
# Information for a particular SBAS satellite
S8ea500cmdSBASInfo_tup = namedtuple('S8ea500cmdSBASInfo_tup', ' PRN Flags')
S8ea500cmdSBASInfo_bin = '=BB'
# Sets the current SBAS settings. This packet can contain a variable number of SBAS SV entries. SV entries not listed in the command packet will not be updated.
S8ea500cmd_tup = namedtuple('S8ea500cmd_tup', ' NumSvs SBASInfoArray')
S8ea500cmd_bin = '=B?S8ea500cmdSBASInfo'
# Requests the current 'Use SBAS+' settings. Response packet is 0x8F 0xA5 0x01
S8ea501req_tup = namedtuple('S8ea501req_tup', '')
S8ea501req_bin = '='
# Sets the 'Use SBAS+' configuration settings. SBAS+ mode uses as much SBAS correction information as possible and as many satellites as possible to improve yield and accuracy when positioning in SBAS mode. Response packet is 0x8F 0xA5 0x01
S8ea501cmd_tup = namedtuple('S8ea501cmd_tup', ' UseSBASPlus')
S8ea501cmd_bin = '=B'
# Resets the receiver's SBAS constellation tracking scheme to the defaults.
S8ea502cmd_tup = namedtuple('S8ea502cmd_tup', ' ResetSBASTrackingDefaults')
S8ea502cmd_bin = '=B'
# Sets the state of a Output pin.
S8ea601cmd_tup = namedtuple('S8ea601cmd_tup', ' ProductId OutputPin0 OutputPin1 OutputPin2 OutputPin3')
S8ea601cmd_bin = '=BBBBB'
# Request the state of an external input pin.
S8ea602req_tup = namedtuple('S8ea602req_tup', ' ProductId')
S8ea602req_bin = '=B'
# Requests the manufacturing information of the unit.
S8ea608req_tup = namedtuple('S8ea608req_tup', '')
S8ea608req_bin = '='
# Requests Omnistar Id from the unit.
S8ea617req_tup = namedtuple('S8ea617req_tup', '')
S8ea617req_bin = '='
# Requests MAC addresses from the unit.
S8ea622req_tup = namedtuple('S8ea622req_tup', '')
S8ea622req_bin = '='
# Requests the alternate unique ID from the unit.
S8ea623req_tup = namedtuple('S8ea623req_tup', '')
S8ea623req_bin = '='
# Requests unit's extended manufacturing information.
S8ea624req_tup = namedtuple('S8ea624req_tup', '')
S8ea624req_bin = '='
# Sets unit's extended manufacturing information.
S8ea625cmd_tup = namedtuple('S8ea625cmd_tup', ', ModuleSN, FactoryID')
S8ea625cmd_bin = '=16s20s'
# Requests unit's product information.
S8ea626req_tup = namedtuple('S8ea626req_tup', '')
S8ea626req_bin = '='
# Sets unit's product information.
S8ea627cmd_tup = namedtuple('S8ea627cmd_tup', ', PartNumber, Name, AbbrevName')
S8ea627cmd_bin = '=20s18s6s'
# Put the receiver into manufacturing test mode.
S8ea628cmd_tup = namedtuple('S8ea628cmd_tup', ', key')
S8ea628cmd_bin = '=32s'
# Request the firmware signature at the given offset.
S8ea629req_tup = namedtuple('S8ea629req_tup', ' Offset')
S8ea629req_bin = '=L'
# Requests the peak FFT frequency from the RF spectrum analyzer for GNSS bands. Intended for factory test use only.
S8ea630req_tup = namedtuple('S8ea630req_tup', ' ProductId RFBand')
S8ea630req_bin = '=BB'
# Requests metadata about the MSS tracking, including the peak value of the FFT, min/max signal level and gain in db/% 
S8ea631req_tup = namedtuple('S8ea631req_tup', ' ProductId')
S8ea631req_bin = '=B'
# Requests a register read operation to a specific polaris device
S8ea632req_tup = namedtuple('S8ea632req_tup', ' ProductId AntennaId PolarisI2CAddr PolarisRegAddr')
S8ea632req_bin = '=BBBB'
# Writes a value to a specific polaris device's register
S8ea632cmd_tup = namedtuple('S8ea632cmd_tup', ' ProductId AntennaId PolarisI2CAddr PolarisRegAddr WriteData')
S8ea632cmd_bin = '=BBBBB'
# Requests a ADC read of the RSSI on a specific polaris device
S8ea633req_tup = namedtuple('S8ea633req_tup', ' ProductId AntennaId RFBand')
S8ea633req_bin = '=BBB'
# Requests the receiver to perform the Polaris full AGC test. The receiver will acknowledge the request, and then send the 0x8f 0xa6 0x34 response when the test completes.
S8ea634req_tup = namedtuple('S8ea634req_tup', ' ProductId')
S8ea634req_bin = '=B'
# Enables the PLT (Production Line Test) Mode for WiFi testing.
S8ea640cmd_tup = namedtuple('S8ea640cmd_tup', ' ProductId')
S8ea640cmd_bin = '=B'
# Disables the PLT (Production Line Test) Mode for WiFi testing.
S8ea641cmd_tup = namedtuple('S8ea641cmd_tup', ' ProductId')
S8ea641cmd_bin = '=B'
# Configures the device to operate in a specific WiFi band and channel.
S8ea642cmd_tup = namedtuple('S8ea642cmd_tup', ' ProductId Channel Band Bandwidth')
S8ea642cmd_bin = '=BHBB'
# Sets the transmission power of the WL18xx device.
S8ea643cmd_tup = namedtuple('S8ea643cmd_tup', ' ProductId OutputPower Level Band Channel Bandwidth Antenna NonServingChannel ChannelLimitation GainCalculationMode AnalogGainControl')
S8ea643cmd_bin = '=BhBBHbBBBBB'
# Enables TX test using the start_tx command.
S8ea644cmd_tup = namedtuple('S8ea644cmd_tup', ' ProductId Delay Rate Size Mode GuardInterval Options1 Options2, SourceMAC, DestMAC ChannelWidth')
S8ea644cmd_bin = '=BLBHLBBB6?B6?BB'
# Disables TX test using the stop_tx command.
S8ea645cmd_tup = namedtuple('S8ea645cmd_tup', ' ProductId')
S8ea645cmd_bin = '=B'
# Starts calculations of RX statistics.
S8ea646cmd_tup = namedtuple('S8ea646cmd_tup', ' ProductId, SourceMAC, DestMAC')
S8ea646cmd_bin = '=B6?B6?B'
# Requests the RX statistics.
S8ea647req_tup = namedtuple('S8ea647req_tup', ' ProductId')
S8ea647req_bin = '=B'
# Stops calculations of the RX statistics.
S8ea648cmd_tup = namedtuple('S8ea648cmd_tup', ' ProductId')
S8ea648cmd_bin = '=B'
# 
S6e03cmd_tup = namedtuple('S6e03cmd_tup', ' Enable OutputInterval')
S6e03cmd_bin = '=BB'
# Requests current state of automatic position sigma reporting
S6b00req_tup = namedtuple('S6b00req_tup', '')
S6b00req_bin = '='
# Controls automatic reporting of position sigma
S6b00cmd_tup = namedtuple('S6b00cmd_tup', ' EnableOutputs')
S6b00cmd_bin = '=B'
# Requests a single position sigma (error) information report, automatic reporting can be set up with command 0x6B 0x00
S6b02req_tup = namedtuple('S6b02req_tup', '')
S6b02req_bin = '='
# Requests primary receiver configuration block.
Sbb00req_tup = namedtuple('Sbb00req_tup', '')
Sbb00req_bin = '='
# Sets primary receiver configuration block.
Sbb00cmd_tup = namedtuple('Sbb00cmd_tup', ' OperatingDimension DGPSMode DynamicsCode SolutionMode ElevetionMask AMUMask PDOP PDOPSwitch DGPSAgeLimit FoliageMode LowPowerMode ClockHoldMode MeasurementRate PosFixRate')
Sbb00cmd_bin = '=BBBBffffBBBBBB'
# Requests the configuration of a particular serial port
Sbcreq_tup = namedtuple('Sbcreq_tup', ' Port')
Sbcreq_bin = '=B'
# Sets the configuration of a particular serial port. This includes the port settings and input and output protocols.
Sbccmd_tup = namedtuple('Sbccmd_tup', ' Port InputBaudRate OutputBaudRate DataBits Parity StopBits FlowControl InputProtocol OutputProtocol ProtocolOperation')
Sbccmd_bin = '=BBBBBBBBBB'
# Gets the mask controlling diagnostic types output
S3f2200req_tup = namedtuple('S3f2200req_tup', '')
S3f2200req_bin = '='
# Sets the mask controlling diagnostic types output
S3f2200cmd_tup = namedtuple('S3f2200cmd_tup', ' Mask')
S3f2200cmd_bin = '=L'
# Configuration packet command to the Autopilot Navigation Controller
Sbe40cmd_tup = namedtuple('Sbe40cmd_tup', ', PacketDataLength, PacketData')
Sbe40cmd_bin = '=B*'
# Requests the App Version Config version from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe400003cmd_base = namedtuple('Sbe400003cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe400003cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe400003cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe400003cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe400003cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe400003cmd_tup._make = lambda seq: Sbe400003cmd_tup(*seq)
Sbe400003cmd_bin = '=?'
# Requests Options(?) config version from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe400103cmd_base = namedtuple('Sbe400103cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe400103cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe400103cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe400103cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe400103cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe400103cmd_tup._make = lambda seq: Sbe400103cmd_tup(*seq)
Sbe400103cmd_bin = '=?'
# Requests App Version(?) configuration from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe400000cmd_base = namedtuple('Sbe400000cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe400000cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe400000cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe400000cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe400000cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe400000cmd_tup._make = lambda seq: Sbe400000cmd_tup(*seq)
Sbe400000cmd_bin = '=?'
# Requests options configuration from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe400100cmd_base = namedtuple('Sbe400100cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe400100cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe400100cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe400100cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe400100cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe400100cmd_tup._make = lambda seq: Sbe400100cmd_tup(*seq)
Sbe400100cmd_bin = '=?'
# Configuration packet command to get TAP parameter on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe401400cmd_base = namedtuple('Sbe401400cmd_base', ', TAPStringLength, TAPString, Length')

# Factory function for backward compatibility
def Sbe401400cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe401400cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe401400cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe401400cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe401400cmd_tup._make = lambda seq: Sbe401400cmd_tup(*seq)
Sbe401400cmd_bin = '=B*?'
# Configuration packet command to set TAP parameter on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe401401cmd_base = namedtuple('Sbe401401cmd_base', ', TAPStringLength, TAPString, Length')

# Factory function for backward compatibility
def Sbe401401cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe401401cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe401401cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe401401cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe401401cmd_tup._make = lambda seq: Sbe401401cmd_tup(*seq)
Sbe401401cmd_bin = '=B*?'
# File Transfer packet command to the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe41cmd_base = namedtuple('Sbe41cmd_base', ' FileId CmdId PacketNumber, PacketDataLength, PacketData, Length')

# Factory function for backward compatibility
def Sbe41cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe41cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe41cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe41cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe41cmd_tup._make = lambda seq: Sbe41cmd_tup(*seq)
Sbe41cmd_bin = '=BBHB*?'
# Remote Monitor Engineering Data packet command to the Autopilot Navigation Controller
Sbe42cmd_tup = namedtuple('Sbe42cmd_tup', ', PacketDataLength, PacketData')
Sbe42cmd_bin = '=B*'
# Gets status information for navigation
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4201cmd_base = namedtuple('Sbe4201cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4201cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4201cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4201cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4201cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4201cmd_tup._make = lambda seq: Sbe4201cmd_tup(*seq)
Sbe4201cmd_bin = '=?'
# Gets status information for navigation
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4200cmd_base = namedtuple('Sbe4200cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4200cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4200cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4200cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4200cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4200cmd_tup._make = lambda seq: Sbe4200cmd_tup(*seq)
Sbe4200cmd_bin = '=?'
# Gets status information for GNSS
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4202cmd_base = namedtuple('Sbe4202cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4202cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4202cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4202cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4202cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4202cmd_tup._make = lambda seq: Sbe4202cmd_tup(*seq)
Sbe4202cmd_bin = '=?'
# Increases the Simulation Speed (increment is defined in receiver firmware)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe43060100cmd_base = namedtuple('Sbe43060100cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe43060100cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe43060100cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe43060100cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe43060100cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe43060100cmd_tup._make = lambda seq: Sbe43060100cmd_tup(*seq)
Sbe43060100cmd_bin = '=?'
# Decreases the Simulation Speed (increment is defined in receiver firmware)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe43060101cmd_base = namedtuple('Sbe43060101cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe43060101cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe43060101cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe43060101cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe43060101cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe43060101cmd_tup._make = lambda seq: Sbe43060101cmd_tup(*seq)
Sbe43060101cmd_bin = '=?'
# Sets the Simulation Speed to a specific value
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe43060102cmd_base = namedtuple('Sbe43060102cmd_base', ' SpeedMetersPerSecond, Length')

# Factory function for backward compatibility
def Sbe43060102cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe43060102cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe43060102cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe43060102cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe43060102cmd_tup._make = lambda seq: Sbe43060102cmd_tup(*seq)
Sbe43060102cmd_bin = '=f?'
# Steers left in the simulation (angle is defined in receiver firmware)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe43060000cmd_base = namedtuple('Sbe43060000cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe43060000cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe43060000cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe43060000cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe43060000cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe43060000cmd_tup._make = lambda seq: Sbe43060000cmd_tup(*seq)
Sbe43060000cmd_bin = '=?'
# Steers right in the simulation (angle is defined in receiver firmware)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe43060001cmd_base = namedtuple('Sbe43060001cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe43060001cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe43060001cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe43060001cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe43060001cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe43060001cmd_tup._make = lambda seq: Sbe43060001cmd_tup(*seq)
Sbe43060001cmd_bin = '=?'
# Sets the Simulation Steer Angle to a specific value
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe43060002cmd_base = namedtuple('Sbe43060002cmd_base', ' SteerAngleDegrees, Length')

# Factory function for backward compatibility
def Sbe43060002cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe43060002cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe43060002cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe43060002cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe43060002cmd_tup._make = lambda seq: Sbe43060002cmd_tup(*seq)
Sbe43060002cmd_bin = '=f?'
# Enables/disables simulating a GPS outage in the simulation.
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe430dcmd_base = namedtuple('Sbe430dcmd_base', ', Length')

# Factory function for backward compatibility
def Sbe430dcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe430dcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe430dcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe430dcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe430dcmd_tup._make = lambda seq: Sbe430dcmd_tup(*seq)
Sbe430dcmd_bin = '=?'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe430bcmd_base = namedtuple('Sbe430bcmd_base', ', Length')

# Factory function for backward compatibility
def Sbe430bcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe430bcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe430bcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe430bcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe430bcmd_tup._make = lambda seq: Sbe430bcmd_tup(*seq)
Sbe430bcmd_bin = '=?'
# Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets autosteering to enabled/disabled
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4301cmd_base = namedtuple('Sbe4301cmd_base', ' EngageCommand, Length')

# Factory function for backward compatibility
def Sbe4301cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4301cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4301cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4301cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4301cmd_tup._make = lambda seq: Sbe4301cmd_tup(*seq)
Sbe4301cmd_bin = '=L?'
# Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets logging to enabled/disabled
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4303cmd_base = namedtuple('Sbe4303cmd_base', ' PaddingForBackwardsCompatibility1 PaddingForBackwardsCompatibility2 LoggingCommand, Length')

# Factory function for backward compatibility
def Sbe4303cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4303cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4303cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4303cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4303cmd_tup._make = lambda seq: Sbe4303cmd_tup(*seq)
Sbe4303cmd_bin = '=BHB?'
# Remote Monitor Control packet command to the Autopilot Navigation Controller to control Steering/Speed
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4306cmd_base = namedtuple('Sbe4306cmd_base', ' CommandID Command Value, Length')

# Factory function for backward compatibility
def Sbe4306cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4306cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4306cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4306cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4306cmd_tup._make = lambda seq: Sbe4306cmd_tup(*seq)
Sbe4306cmd_bin = '=BBf?'
# Remote Monitor General Data packet command to the Autopilot Navigation Controller
Sbe44cmd_tup = namedtuple('Sbe44cmd_tup', ', PacketDataLength, PacketData')
Sbe44cmd_bin = '=B*'
# Remote Monitor Waypoint Data packet command to the Autopilot Navigation Controller
Sbe45cmd_tup = namedtuple('Sbe45cmd_tup', ', PacketDataLength, PacketData')
Sbe45cmd_bin = '=B*'
# Boot Monitor packet command to the Autopilot Navigation Controller
Sbe46cmd_tup = namedtuple('Sbe46cmd_tup', ', PacketDataLength, PacketData')
Sbe46cmd_bin = '=B*'
# Used to reset the steering controller on the receiver. The AGL currently first sends the SwitchToApp command, followed by ReturnMode after a delay.
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4600cmd_base = namedtuple('Sbe4600cmd_base', ' Command, Length')

# Factory function for backward compatibility
def Sbe4600cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4600cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4600cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4600cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4600cmd_tup._make = lambda seq: Sbe4600cmd_tup(*seq)
Sbe4600cmd_bin = '=B?'
# Debug packet command to the Autopilot Navigation Controller
Sbe47cmd_tup = namedtuple('Sbe47cmd_tup', ', PacketDataLength, PacketData')
Sbe47cmd_bin = '=B*'
# Gets the current diagnostic error type from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470500cmd_base = namedtuple('Sbe470500cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe470500cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470500cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470500cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470500cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470500cmd_tup._make = lambda seq: Sbe470500cmd_tup(*seq)
Sbe470500cmd_bin = '=?'
# Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470501cmd_base = namedtuple('Sbe470501cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe470501cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470501cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470501cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470501cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470501cmd_tup._make = lambda seq: Sbe470501cmd_tup(*seq)
Sbe470501cmd_bin = '=?'
# Gets a diagnostic record item from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470502cmd_base = namedtuple('Sbe470502cmd_base', ' DiagItemId, Length')

# Factory function for backward compatibility
def Sbe470502cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470502cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470502cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470502cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470502cmd_tup._make = lambda seq: Sbe470502cmd_tup(*seq)
Sbe470502cmd_bin = '=H?'
# Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470503cmd_base = namedtuple('Sbe470503cmd_base', ' DiagItemId, Length')

# Factory function for backward compatibility
def Sbe470503cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470503cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470503cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470503cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470503cmd_tup._make = lambda seq: Sbe470503cmd_tup(*seq)
Sbe470503cmd_bin = '=H?'
# Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470504cmd_base = namedtuple('Sbe470504cmd_base', ' ErrorComponentId, Length')

# Factory function for backward compatibility
def Sbe470504cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470504cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470504cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470504cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470504cmd_tup._make = lambda seq: Sbe470504cmd_tup(*seq)
Sbe470504cmd_bin = '=H?'
# Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470505cmd_base = namedtuple('Sbe470505cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe470505cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470505cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470505cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470505cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470505cmd_tup._make = lambda seq: Sbe470505cmd_tup(*seq)
Sbe470505cmd_bin = '=?'
# Gets the description of a diagnostic record item from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470506cmd_base = namedtuple('Sbe470506cmd_base', ' DiagItemId, Length')

# Factory function for backward compatibility
def Sbe470506cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470506cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470506cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470506cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470506cmd_tup._make = lambda seq: Sbe470506cmd_tup(*seq)
Sbe470506cmd_bin = '=H?'
# Acknowledge the current warning on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470507cmd_base = namedtuple('Sbe470507cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe470507cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470507cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470507cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470507cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470507cmd_tup._make = lambda seq: Sbe470507cmd_tup(*seq)
Sbe470507cmd_bin = '=?'
# Gets the maximum number of warnings from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470508cmd_base = namedtuple('Sbe470508cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe470508cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470508cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470508cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470508cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470508cmd_tup._make = lambda seq: Sbe470508cmd_tup(*seq)
Sbe470508cmd_bin = '=?'
# Gets the description of a warning from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470509cmd_base = namedtuple('Sbe470509cmd_base', ' WarningId, Length')

# Factory function for backward compatibility
def Sbe470509cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470509cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470509cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470509cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470509cmd_tup._make = lambda seq: Sbe470509cmd_tup(*seq)
Sbe470509cmd_bin = '=H?'
# Gets the maximum number of messages from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe47050acmd_base = namedtuple('Sbe47050acmd_base', ', Length')

# Factory function for backward compatibility
def Sbe47050acmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe47050acmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe47050acmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe47050acmd_base(*args)

# Add _make method for compatibility with existing code
Sbe47050acmd_tup._make = lambda seq: Sbe47050acmd_tup(*seq)
Sbe47050acmd_bin = '=?'
# Gets a message description from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe47050bcmd_base = namedtuple('Sbe47050bcmd_base', ' MessageId, Length')

# Factory function for backward compatibility
def Sbe47050bcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe47050bcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe47050bcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe47050bcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe47050bcmd_tup._make = lambda seq: Sbe47050bcmd_tup(*seq)
Sbe47050bcmd_bin = '=H?'
# Gets ADC data from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4707cmd_base = namedtuple('Sbe4707cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4707cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4707cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4707cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4707cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4707cmd_tup._make = lambda seq: Sbe4707cmd_tup(*seq)
Sbe4707cmd_bin = '=?'
# Debug packet command to the Autopilot Navigation Controller. Gets current port function
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470e08cmd_base = namedtuple('Sbe470e08cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe470e08cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470e08cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470e08cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470e08cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470e08cmd_tup._make = lambda seq: Sbe470e08cmd_tup(*seq)
Sbe470e08cmd_bin = '=?'
# Debug packet command to the Autopilot Navigation Controller. Sets current port function
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe470e09cmd_base = namedtuple('Sbe470e09cmd_base', ' PortFunctionId, Length')

# Factory function for backward compatibility
def Sbe470e09cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe470e09cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe470e09cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe470e09cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe470e09cmd_tup._make = lambda seq: Sbe470e09cmd_tup(*seq)
Sbe470e09cmd_bin = '=L?'
# Gets number of internal vdb's from the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe471400cmd_base = namedtuple('Sbe471400cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe471400cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe471400cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe471400cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe471400cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe471400cmd_tup._make = lambda seq: Sbe471400cmd_tup(*seq)
Sbe471400cmd_bin = '=?'
# Gets a vdb record from the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe471401cmd_base = namedtuple('Sbe471401cmd_base', ' VDBIndex, Length')

# Factory function for backward compatibility
def Sbe471401cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe471401cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe471401cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe471401cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe471401cmd_tup._make = lambda seq: Sbe471401cmd_tup(*seq)
Sbe471401cmd_bin = '=H?'
# Sets the vdb record on the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe471402cmd_base = namedtuple('Sbe471402cmd_base', ' VDBIndex, Length')

# Factory function for backward compatibility
def Sbe471402cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe471402cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe471402cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe471402cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe471402cmd_tup._make = lambda seq: Sbe471402cmd_tup(*seq)
Sbe471402cmd_bin = '=H?'
# Gets current IMU data from the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe471ecmd_base = namedtuple('Sbe471ecmd_base', ', Length')

# Factory function for backward compatibility
def Sbe471ecmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe471ecmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe471ecmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe471ecmd_base(*args)

# Add _make method for compatibility with existing code
Sbe471ecmd_tup._make = lambda seq: Sbe471ecmd_tup(*seq)
Sbe471ecmd_bin = '=?'
# Calibration packet command to the Autopilot Navigation Controller
Sbe4acmd_tup = namedtuple('Sbe4acmd_tup', ', PacketDataLength, PacketData')
Sbe4acmd_bin = '=B*'
# Steering (P-gain) Calibration Information request
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4a0c00cmd_base = namedtuple('Sbe4a0c00cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4a0c00cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4a0c00cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4a0c00cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4a0c00cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4a0c00cmd_tup._make = lambda seq: Sbe4a0c00cmd_tup(*seq)
Sbe4a0c00cmd_bin = '=?'
# Steering (P-gain) Calibration Information request (part2)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4a0c08cmd_base = namedtuple('Sbe4a0c08cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4a0c08cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4a0c08cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4a0c08cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4a0c08cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4a0c08cmd_tup._make = lambda seq: Sbe4a0c08cmd_tup(*seq)
Sbe4a0c08cmd_bin = '=?'
# Steering angle sensor calibration information request
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4a0b00cmd_base = namedtuple('Sbe4a0b00cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4a0b00cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4a0b00cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4a0b00cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4a0b00cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4a0b00cmd_tup._make = lambda seq: Sbe4a0b00cmd_tup(*seq)
Sbe4a0b00cmd_bin = '=?'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4a0b01cmd_base = namedtuple('Sbe4a0b01cmd_base', ' Command, Length')

# Factory function for backward compatibility
def Sbe4a0b01cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4a0b01cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4a0b01cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4a0b01cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4a0b01cmd_tup._make = lambda seq: Sbe4a0b01cmd_tup(*seq)
Sbe4a0b01cmd_bin = '=B?'
# PGain Commands which do not take any additional request data
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4a0ccmd_base = namedtuple('Sbe4a0ccmd_base', ' Command, Length')

# Factory function for backward compatibility
def Sbe4a0ccmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4a0ccmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4a0ccmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4a0ccmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4a0ccmd_tup._make = lambda seq: Sbe4a0ccmd_tup(*seq)
Sbe4a0ccmd_bin = '=B?'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4a0c09cmd_base = namedtuple('Sbe4a0c09cmd_base', ' PGain, Length')

# Factory function for backward compatibility
def Sbe4a0c09cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4a0c09cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4a0c09cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4a0c09cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4a0c09cmd_tup._make = lambda seq: Sbe4a0c09cmd_tup(*seq)
Sbe4a0c09cmd_bin = '=f?'
# Autotester command to the Autopilot Navigation Controller.
Sbe4bcmd_tup = namedtuple('Sbe4bcmd_tup', ', PacketDataLength, PacketData')
Sbe4bcmd_bin = '=B*'
# External Device packet command to read the manual override info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c00000004cmd_base = namedtuple('Sbe4c00000004cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c00000004cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c00000004cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c00000004cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c00000004cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c00000004cmd_tup._make = lambda seq: Sbe4c00000004cmd_tup(*seq)
Sbe4c00000004cmd_bin = '=?'
# External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c00000104cmd_base = namedtuple('Sbe4c00000104cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c00000104cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c00000104cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c00000104cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c00000104cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c00000104cmd_tup._make = lambda seq: Sbe4c00000104cmd_tup(*seq)
Sbe4c00000104cmd_bin = '=?'
# External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c00000204cmd_base = namedtuple('Sbe4c00000204cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c00000204cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c00000204cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c00000204cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c00000204cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c00000204cmd_tup._make = lambda seq: Sbe4c00000204cmd_tup(*seq)
Sbe4c00000204cmd_bin = '=?'
# External Device packet command to read the Gear lever info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c00000704cmd_base = namedtuple('Sbe4c00000704cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c00000704cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c00000704cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c00000704cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c00000704cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c00000704cmd_tup._make = lambda seq: Sbe4c00000704cmd_tup(*seq)
Sbe4c00000704cmd_bin = '=?'
# Autopilot Field Computer Heartbeat packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0100cmd_base = namedtuple('Sbe4c0100cmd_base', ' FieldComputerVersion FieldComputerFieldState, Length')

# Factory function for backward compatibility
def Sbe4c0100cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0100cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0100cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0100cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0100cmd_tup._make = lambda seq: Sbe4c0100cmd_tup(*seq)
Sbe4c0100cmd_bin = '=BB?'
# External Device packet command to turn logging on on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0106cmd_base = namedtuple('Sbe4c0106cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c0106cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0106cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0106cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0106cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0106cmd_tup._make = lambda seq: Sbe4c0106cmd_tup(*seq)
Sbe4c0106cmd_bin = '=?'
# External Device packet command to turn logging off on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0107cmd_base = namedtuple('Sbe4c0107cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c0107cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0107cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0107cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0107cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0107cmd_tup._make = lambda seq: Sbe4c0107cmd_tup(*seq)
Sbe4c0107cmd_bin = '=?'
# External Device request to get implement width
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0108req_base = namedtuple('Sbe4c0108req_base', ', Length')

# Factory function for backward compatibility
def Sbe4c0108req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0108req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0108req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0108req_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0108req_tup._make = lambda seq: Sbe4c0108req_tup(*seq)
Sbe4c0108req_bin = '=?'
# External Device packet command to set Implement Width
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0108cmd_base = namedtuple('Sbe4c0108cmd_base', ', ImplementWidthLength, ImplementWidth, Length')

# Factory function for backward compatibility
def Sbe4c0108cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0108cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0108cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0108cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0108cmd_tup._make = lambda seq: Sbe4c0108cmd_tup(*seq)
Sbe4c0108cmd_bin = '=B*?'
# External Device packet command to set close any open field
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010acmd_base = namedtuple('Sbe4c010acmd_base', ', Length')

# Factory function for backward compatibility
def Sbe4c010acmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010acmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010acmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010acmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010acmd_tup._make = lambda seq: Sbe4c010acmd_tup(*seq)
Sbe4c010acmd_bin = '=?'
# External Device packet request to get Control State
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010breq_base = namedtuple('Sbe4c010breq_base', ', Length')

# Factory function for backward compatibility
def Sbe4c010breq_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010breq_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010breq_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010breq_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010breq_tup._make = lambda seq: Sbe4c010breq_tup(*seq)
Sbe4c010breq_bin = '=?'
# External Device packet Control State
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010bcmd_base = namedtuple('Sbe4c010bcmd_base', ' ControlState, MiscDataLength, MiscData, Length')

# Factory function for backward compatibility
def Sbe4c010bcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010bcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010bcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010bcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010bcmd_tup._make = lambda seq: Sbe4c010bcmd_tup(*seq)
Sbe4c010bcmd_bin = '=BB*?'
# External Device packet request to get Aggressiveness
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010dreq_base = namedtuple('Sbe4c010dreq_base', ', Length')

# Factory function for backward compatibility
def Sbe4c010dreq_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010dreq_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010dreq_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010dreq_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010dreq_tup._make = lambda seq: Sbe4c010dreq_tup(*seq)
Sbe4c010dreq_bin = '=?'
# External Device packet command to set Aggressiveness
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010dcmd_base = namedtuple('Sbe4c010dcmd_base', ' Aggressiveness, Length')

# Factory function for backward compatibility
def Sbe4c010dcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010dcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010dcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010dcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010dcmd_tup._make = lambda seq: Sbe4c010dcmd_tup(*seq)
Sbe4c010dcmd_bin = '=B?'
# External Device packet request to get Task Delay
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010ereq_base = namedtuple('Sbe4c010ereq_base', ', Length')

# Factory function for backward compatibility
def Sbe4c010ereq_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010ereq_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010ereq_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010ereq_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010ereq_tup._make = lambda seq: Sbe4c010ereq_tup(*seq)
Sbe4c010ereq_bin = '=?'
# External Device packet command to set Task Delay
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010ecmd_base = namedtuple('Sbe4c010ecmd_base', ' TaskDelay, Length')

# Factory function for backward compatibility
def Sbe4c010ecmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010ecmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010ecmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010ecmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010ecmd_tup._make = lambda seq: Sbe4c010ecmd_tup(*seq)
Sbe4c010ecmd_bin = '=H?'
# External Device packet request to get Fix Quality
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010freq_base = namedtuple('Sbe4c010freq_base', ', Length')

# Factory function for backward compatibility
def Sbe4c010freq_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010freq_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010freq_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010freq_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010freq_tup._make = lambda seq: Sbe4c010freq_tup(*seq)
Sbe4c010freq_bin = '=?'
# External Device packet command to set Fix Quality
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c010fcmd_base = namedtuple('Sbe4c010fcmd_base', ' FixQuality, Length')

# Factory function for backward compatibility
def Sbe4c010fcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c010fcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c010fcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c010fcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c010fcmd_tup._make = lambda seq: Sbe4c010fcmd_tup(*seq)
Sbe4c010fcmd_bin = '=B?'
# External Device packet command to Get the Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011000req_base = namedtuple('Sbe4c011000req_base', ', Length')

# Factory function for backward compatibility
def Sbe4c011000req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011000req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011000req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011000req_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011000req_tup._make = lambda seq: Sbe4c011000req_tup(*seq)
Sbe4c011000req_bin = '=?'
# External Device packet command to set the Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011001cmd_base = namedtuple('Sbe4c011001cmd_base', ' Nudge, Length')

# Factory function for backward compatibility
def Sbe4c011001cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011001cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011001cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011001cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011001cmd_tup._make = lambda seq: Sbe4c011001cmd_tup(*seq)
Sbe4c011001cmd_bin = '=f?'
# External Device packet command Apply Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011002cmd_base = namedtuple('Sbe4c011002cmd_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbe4c011002cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011002cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011002cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011002cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011002cmd_tup._make = lambda seq: Sbe4c011002cmd_tup(*seq)
Sbe4c011002cmd_bin = '=B?'
# External Device packet request Get Nudge Total
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011003req_base = namedtuple('Sbe4c011003req_base', ', Length')

# Factory function for backward compatibility
def Sbe4c011003req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011003req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011003req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011003req_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011003req_tup._make = lambda seq: Sbe4c011003req_tup(*seq)
Sbe4c011003req_bin = '=?'
# External Device packet response to Set Total Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011004cmd_base = namedtuple('Sbe4c011004cmd_base', ' Total, Length')

# Factory function for backward compatibility
def Sbe4c011004cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011004cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011004cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011004cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011004cmd_tup._make = lambda seq: Sbe4c011004cmd_tup(*seq)
Sbe4c011004cmd_bin = '=f?'
# External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0111cmd_base = namedtuple('Sbe4c0111cmd_base', ' Mask Rate, Length')

# Factory function for backward compatibility
def Sbe4c0111cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0111cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0111cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0111cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0111cmd_tup._make = lambda seq: Sbe4c0111cmd_tup(*seq)
Sbe4c0111cmd_bin = '=LL?'
# External Device packet command to set the GGA Adjust
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0114cmd_base = namedtuple('Sbe4c0114cmd_base', ' GgaAdjust, Length')

# Factory function for backward compatibility
def Sbe4c0114cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0114cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0114cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0114cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0114cmd_tup._make = lambda seq: Sbe4c0114cmd_tup(*seq)
Sbe4c0114cmd_bin = '=B?'
# Point A geodetic position
Sbe4c011706cmdPointA_tup = namedtuple('Sbe4c011706cmdPointA_tup', ' Latitude Longitude Altitude')
Sbe4c011706cmdPointA_bin = '=ddd'
# Point B geodetic position
Sbe4c011706cmdPointB_tup = namedtuple('Sbe4c011706cmdPointB_tup', ' Latitude Longitude Altitude')
Sbe4c011706cmdPointB_bin = '=ddd'
# Point Center geodetic position
Sbe4c011706cmdCenterPoint_tup = namedtuple('Sbe4c011706cmdCenterPoint_tup', ' Latitude Longitude Altitude')
Sbe4c011706cmdCenterPoint_bin = '=ddd'
# Field computer pattern definition for pivot ACB patterns
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011706cmd_base = namedtuple('Sbe4c011706cmd_base', ' Curvature PointA PointB CenterPoint Radius, Length')

# Factory function for backward compatibility
def Sbe4c011706cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011706cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011706cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011706cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011706cmd_tup._make = lambda seq: Sbe4c011706cmd_tup(*seq)
Sbe4c011706cmd_bin = '=B?B?B?Bd?'
# Point A geodetic position
Sbe4c011710cmdPointA_tup = namedtuple('Sbe4c011710cmdPointA_tup', ' Latitude Longitude Altitude')
Sbe4c011710cmdPointA_bin = '=ddd'
# Point B geodetic position
Sbe4c011710cmdPointB_tup = namedtuple('Sbe4c011710cmdPointB_tup', ' Latitude Longitude Altitude')
Sbe4c011710cmdPointB_bin = '=ddd'
# Swath by swath pattern definition command (PTRN_SWATH_BY_SWATH)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011710cmd_base = namedtuple('Sbe4c011710cmd_base', ' SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB, Length')

# Factory function for backward compatibility
def Sbe4c011710cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011710cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011710cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011710cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011710cmd_tup._make = lambda seq: Sbe4c011710cmd_tup(*seq)
Sbe4c011710cmd_bin = '=hBLB?B?B?'
# 
Sbe4c011711cmdPoint_tup = namedtuple('Sbe4c011711cmdPoint_tup', ' Latitude Longitude Altitude')
Sbe4c011711cmdPoint_bin = '=ddd'
# Swath section pattern definition command (PTRN_SWATH_SECTION)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011711cmd_base = namedtuple('Sbe4c011711cmd_base', ' SwathNumber SwathNumPoints SectionNumPoints SectionIndex Points, Length')

# Factory function for backward compatibility
def Sbe4c011711cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011711cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011711cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011711cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011711cmd_tup._make = lambda seq: Sbe4c011711cmd_tup(*seq)
Sbe4c011711cmd_bin = '=hHHH?Sbe4c011711cmdPoint?'
# Point A geodetic position
Sbe4c011713cmdPointA_tup = namedtuple('Sbe4c011713cmdPointA_tup', ' Latitude Longitude Altitude')
Sbe4c011713cmdPointA_bin = '=ddd'
# Point B geodetic position
Sbe4c011713cmdPointB_tup = namedtuple('Sbe4c011713cmdPointB_tup', ' Latitude Longitude Altitude')
Sbe4c011713cmdPointB_bin = '=ddd'
# Swath by swath fragment pattern definition command (PTRN_SWATH_BY_SWATH_FRAGMENT)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011713cmd_base = namedtuple('Sbe4c011713cmd_base', ' SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB, Length')

# Factory function for backward compatibility
def Sbe4c011713cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011713cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011713cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011713cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011713cmd_tup._make = lambda seq: Sbe4c011713cmd_tup(*seq)
Sbe4c011713cmd_bin = '=hBLB?B?B?'
# Point A geodetic position
Sbe4c011720cmdPointA_tup = namedtuple('Sbe4c011720cmdPointA_tup', ' Latitude Longitude Altitude')
Sbe4c011720cmdPointA_bin = '=ddd'
# Point B geodetic position
Sbe4c011720cmdPointB_tup = namedtuple('Sbe4c011720cmdPointB_tup', ' Latitude Longitude Altitude')
Sbe4c011720cmdPointB_bin = '=ddd'
# Swath by swath FFA pattern definition command (PTRN_SWATH_BY_SWATH_FFA)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011720cmd_base = namedtuple('Sbe4c011720cmd_base', ' SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB, Length')

# Factory function for backward compatibility
def Sbe4c011720cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011720cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011720cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011720cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011720cmd_tup._make = lambda seq: Sbe4c011720cmd_tup(*seq)
Sbe4c011720cmd_bin = '=hBLB?B?B?'
# Geodetic position
Sbe4c011721cmdPoint_tup = namedtuple('Sbe4c011721cmdPoint_tup', ' Latitude Longitude Altitude')
Sbe4c011721cmdPoint_bin = '=ddd'
# Swath section FFA pattern definition command (PTRN_SWATH_SECTION_FFA)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011721cmd_base = namedtuple('Sbe4c011721cmd_base', ' SwathNumber SwathNumPoints SectionNumPoints SectionIndex Points, Length')

# Factory function for backward compatibility
def Sbe4c011721cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011721cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011721cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011721cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011721cmd_tup._make = lambda seq: Sbe4c011721cmd_tup(*seq)
Sbe4c011721cmd_bin = '=hHHH?Sbe4c011721cmdPoint?'
#  This packet should be sent from the Field Computer to the Controller when communication is established. It allows the controller to identify what hardware it is connected to and allows the Field Computer (from the Controller's response) to know what sort of Controller the Field Computer is connected to
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c0119cmd_base = namedtuple('Sbe4c0119cmd_base', ' ManufacturerId DisplayId ProductId FirmwareVersion, Length')

# Factory function for backward compatibility
def Sbe4c0119cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c0119cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c0119cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c0119cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c0119cmd_tup._make = lambda seq: Sbe4c0119cmd_tup(*seq)
Sbe4c0119cmd_bin = '=BBBf?'
# External Device packet to request the enable state of the guidance status message
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c2000req_base = namedtuple('Sbe4c2000req_base', ', Length')

# Factory function for backward compatibility
def Sbe4c2000req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c2000req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c2000req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c2000req_base(*args)

# Add _make method for compatibility with existing code
Sbe4c2000req_tup._make = lambda seq: Sbe4c2000req_tup(*seq)
Sbe4c2000req_bin = '=?'
# External Device packet command to set the automatic update of the guidance status message
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c2000cmd_base = namedtuple('Sbe4c2000cmd_base', ' Enabled, Length')

# Factory function for backward compatibility
def Sbe4c2000cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c2000cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c2000cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c2000cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c2000cmd_tup._make = lambda seq: Sbe4c2000cmd_tup(*seq)
Sbe4c2000cmd_bin = '=B?'
# External Device packet to request the guidance status message
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c2001req_base = namedtuple('Sbe4c2001req_base', ', Length')

# Factory function for backward compatibility
def Sbe4c2001req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c2001req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c2001req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c2001req_base(*args)

# Add _make method for compatibility with existing code
Sbe4c2001req_tup._make = lambda seq: Sbe4c2001req_tup(*seq)
Sbe4c2001req_bin = '=?'
# Informs the NAV that a Nextswath related button was pressed on the display
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c8000cmd_base = namedtuple('Sbe4c8000cmd_base', ' Reserved FfaButton, Length')

# Factory function for backward compatibility
def Sbe4c8000cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c8000cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c8000cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c8000cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c8000cmd_tup._make = lambda seq: Sbe4c8000cmd_tup(*seq)
Sbe4c8000cmd_bin = '=BB?'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c8001cmd_base = namedtuple('Sbe4c8001cmd_base', ' InnerHeadlandExists OuterHeadlandExists BoundaryCount NumberOfExclusionZones, Length')

# Factory function for backward compatibility
def Sbe4c8001cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c8001cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c8001cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c8001cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c8001cmd_tup._make = lambda seq: Sbe4c8001cmd_tup(*seq)
Sbe4c8001cmd_bin = '=BBBB?'
# GPS simulation command to the Autopilot Navigation Controller. Used for NAV to NAV communication.
Sbe4dcmd_tup = namedtuple('Sbe4dcmd_tup', ', PacketDataLength, PacketData')
Sbe4dcmd_bin = '=B*'
# Piped message command to the Autopilot Navigation Controller.
Sbe4ecmd_tup = namedtuple('Sbe4ecmd_tup', ', PacketDataLength, PacketData')
Sbe4ecmd_bin = '=B*'
# This is an alias to 0x8e 0xa1.
Sbe4fcmd_tup = namedtuple('Sbe4fcmd_tup', ', PacketDataLength, PacketData')
Sbe4fcmd_bin = '=B*'
# This is an alias to 0x8e 0xa1.
S8ea1cmd_tup = namedtuple('S8ea1cmd_tup', ', PacketDataLength, PacketData')
S8ea1cmd_bin = '=B*'
# Configuration packet command to the Autosteer Controller
Sbe50cmd_tup = namedtuple('Sbe50cmd_tup', ', PacketDataLength, PacketData')
Sbe50cmd_bin = '=B*'
# TAP packet command to the Autosteer Controller
Sbe5014cmd_tup = namedtuple('Sbe5014cmd_tup', ' CommandID, PacketDataLength, PacketData')
Sbe5014cmd_bin = '=BB*'
# File Transfer packet command to the Autosteer Controller
Sbe51cmd_tup = namedtuple('Sbe51cmd_tup', ', PacketDataLength, PacketData')
Sbe51cmd_bin = '=B*'
# Remote Monitor Engineering Data packet command to the Autosteer Controller
Sbe52cmd_tup = namedtuple('Sbe52cmd_tup', ', PacketDataLength, PacketData')
Sbe52cmd_bin = '=B*'
# Remote Monitor Control packet command to the Autosteer Controller
Sbe53cmd_tup = namedtuple('Sbe53cmd_tup', ', PacketDataLength, PacketData')
Sbe53cmd_bin = '=B*'
# Remote Monitor Control Steering packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe530600cmd_base = namedtuple('Sbe530600cmd_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbe530600cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe530600cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe530600cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe530600cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe530600cmd_tup._make = lambda seq: Sbe530600cmd_tup(*seq)
Sbe530600cmd_bin = '=B?'
# Remote Monitor Control Speed packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe530601cmd_base = namedtuple('Sbe530601cmd_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbe530601cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe530601cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe530601cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe530601cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe530601cmd_tup._make = lambda seq: Sbe530601cmd_tup(*seq)
Sbe530601cmd_bin = '=B?'
# Remote Monitor General Data packet command to the Autosteer Controller
Sbe54cmd_tup = namedtuple('Sbe54cmd_tup', ', PacketDataLength, PacketData')
Sbe54cmd_bin = '=B*'
# Remote Monitor Waypoint Data packet command to the Autosteer Controller
Sbe55cmd_tup = namedtuple('Sbe55cmd_tup', ', PacketDataLength, PacketData')
Sbe55cmd_bin = '=B*'
# Boot Monitor packet command to the Autosteer Controller
Sbe56cmd_tup = namedtuple('Sbe56cmd_tup', ', PacketDataLength, PacketData')
Sbe56cmd_bin = '=B*'
# Debug packet command to the Autosteer Controller
Sbe57cmd_tup = namedtuple('Sbe57cmd_tup', ', PacketDataLength, PacketData')
Sbe57cmd_bin = '=B*'
# Field Computer Ack Current Warning packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe570507cmd_base = namedtuple('Sbe570507cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe570507cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe570507cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe570507cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe570507cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe570507cmd_tup._make = lambda seq: Sbe570507cmd_tup(*seq)
Sbe570507cmd_bin = '=?'
# Calibration packet command to the Autosteer Controller
Sbe5acmd_tup = namedtuple('Sbe5acmd_tup', ', PacketDataLength, PacketData')
Sbe5acmd_bin = '=B*'
# External Device packet command to the Autosteer Controller
Sbe5ccmd_tup = namedtuple('Sbe5ccmd_tup', ', PacketDataLength, PacketData')
Sbe5ccmd_bin = '=B*'
# Extended Field Computer Heartbeat packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c011acmd_base = namedtuple('Sbe4c011acmd_base', ' FieldComputerFieldState AutosteerAllowed SequenceNumber, Length')

# Factory function for backward compatibility
def Sbe4c011acmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c011acmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c011acmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c011acmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c011acmd_tup._make = lambda seq: Sbe4c011acmd_tup(*seq)
Sbe4c011acmd_bin = '=BBB?'
# Field Computer Heartbeat packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c0100cmd_base = namedtuple('Sbe5c0100cmd_base', ' FieldComputerVersion FieldComputerFieldState, Length')

# Factory function for backward compatibility
def Sbe5c0100cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c0100cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c0100cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c0100cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c0100cmd_tup._make = lambda seq: Sbe5c0100cmd_tup(*seq)
Sbe5c0100cmd_bin = '=BB?'
# Field Computer Logging On packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c0106cmd_base = namedtuple('Sbe5c0106cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe5c0106cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c0106cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c0106cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c0106cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c0106cmd_tup._make = lambda seq: Sbe5c0106cmd_tup(*seq)
Sbe5c0106cmd_bin = '=?'
# Field Computer Logging Off packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c0107cmd_base = namedtuple('Sbe5c0107cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe5c0107cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c0107cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c0107cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c0107cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c0107cmd_tup._make = lambda seq: Sbe5c0107cmd_tup(*seq)
Sbe5c0107cmd_bin = '=?'
# Field Computer Get Nudge packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011000cmd_base = namedtuple('Sbe5c011000cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe5c011000cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011000cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011000cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011000cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011000cmd_tup._make = lambda seq: Sbe5c011000cmd_tup(*seq)
Sbe5c011000cmd_bin = '=?'
# Field Computer Set Nudge packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011001cmd_base = namedtuple('Sbe5c011001cmd_base', ' NudgeIncrement, Length')

# Factory function for backward compatibility
def Sbe5c011001cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011001cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011001cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011001cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011001cmd_tup._make = lambda seq: Sbe5c011001cmd_tup(*seq)
Sbe5c011001cmd_bin = '=f?'
# Field Computer Apply Nudge packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011002cmd_base = namedtuple('Sbe5c011002cmd_base', ' NudgeDirection, Length')

# Factory function for backward compatibility
def Sbe5c011002cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011002cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011002cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011002cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011002cmd_tup._make = lambda seq: Sbe5c011002cmd_tup(*seq)
Sbe5c011002cmd_bin = '=B?'
# Field Computer Get Total Nudge packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011003cmd_base = namedtuple('Sbe5c011003cmd_base', ', Length')

# Factory function for backward compatibility
def Sbe5c011003cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011003cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011003cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011003cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011003cmd_tup._make = lambda seq: Sbe5c011003cmd_tup(*seq)
Sbe5c011003cmd_bin = '=?'
# Field Computer Set Total Nudge packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011004cmd_base = namedtuple('Sbe5c011004cmd_base', ' TotalNudge, Length')

# Factory function for backward compatibility
def Sbe5c011004cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011004cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011004cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011004cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011004cmd_tup._make = lambda seq: Sbe5c011004cmd_tup(*seq)
Sbe5c011004cmd_bin = '=f?'
# Field Computer Close Field packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c010acmd_base = namedtuple('Sbe5c010acmd_base', ', Length')

# Factory function for backward compatibility
def Sbe5c010acmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c010acmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c010acmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c010acmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c010acmd_tup._make = lambda seq: Sbe5c010acmd_tup(*seq)
Sbe5c010acmd_bin = '=?'
# Field Computer Control State packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c010bcmd_base = namedtuple('Sbe5c010bcmd_base', ' GuidanceType, Length')

# Factory function for backward compatibility
def Sbe5c010bcmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c010bcmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c010bcmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c010bcmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c010bcmd_tup._make = lambda seq: Sbe5c010bcmd_tup(*seq)
Sbe5c010bcmd_bin = '=B?'
# Field Computer NMEA configuration packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c0111cmd_base = namedtuple('Sbe5c0111cmd_base', ' NMEAMask OutputInterval, Length')

# Factory function for backward compatibility
def Sbe5c0111cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c0111cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c0111cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c0111cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c0111cmd_tup._make = lambda seq: Sbe5c0111cmd_tup(*seq)
Sbe5c0111cmd_bin = '=LL?'
# Field Computer Adjust GGA position command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c0114cmd_base = namedtuple('Sbe5c0114cmd_base', ' AdjustPosition, Length')

# Factory function for backward compatibility
def Sbe5c0114cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c0114cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c0114cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c0114cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c0114cmd_tup._make = lambda seq: Sbe5c0114cmd_tup(*seq)
Sbe5c0114cmd_bin = '=B?'
# Field Computer Pattern Definition Parallel A/B packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011700cmd_base = namedtuple('Sbe5c011700cmd_base', ' SwathNumber Direction NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude, Length')

# Factory function for backward compatibility
def Sbe5c011700cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011700cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011700cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011700cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011700cmd_tup._make = lambda seq: Sbe5c011700cmd_tup(*seq)
Sbe5c011700cmd_bin = '=HBLBBBBBBBBdddddd?'
# Field Computer Pattern Definition Pivot packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011706cmd_base = namedtuple('Sbe5c011706cmd_base', ' SwathNumber PivotDirection NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude CenterPointLatitude CenterPointLongitude CenterPointAltitude PivotRadius Unused1 Unused2, Length')

# Factory function for backward compatibility
def Sbe5c011706cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011706cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011706cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011706cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011706cmd_tup._make = lambda seq: Sbe5c011706cmd_tup(*seq)
Sbe5c011706cmd_bin = '=HBLBBBBBBBBdddddddddddd?'
# Field Computer Pattern Definition Swath By Swath packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011710cmd_base = namedtuple('Sbe5c011710cmd_base', ' SwathNumber SwathType NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude, Length')

# Factory function for backward compatibility
def Sbe5c011710cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011710cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011710cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011710cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011710cmd_tup._make = lambda seq: Sbe5c011710cmd_tup(*seq)
Sbe5c011710cmd_bin = '=hBLBBBBBBBBdddddd?'
# Field Computer Pattern Definition Swath By Swath Fragment packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c011713cmd_base = namedtuple('Sbe5c011713cmd_base', ' SwathNumber SwathType NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude, Length')

# Factory function for backward compatibility
def Sbe5c011713cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c011713cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c011713cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c011713cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c011713cmd_tup._make = lambda seq: Sbe5c011713cmd_tup(*seq)
Sbe5c011713cmd_bin = '=hBLBBBBBBBBdddddd?'
# Field Computer Pattern Definition Swath Section packet command to the Autosteer Controller
Sbe5c011711cmd_tup = namedtuple('Sbe5c011711cmd_tup', ' SwathNumber NumSwathPoints NumSectionPoints SectionIndex Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7, PacketDataLength, PacketData')
Sbe5c011711cmd_bin = '=hHHHBBBBBBBB*'
# Field Computer Information packet command to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe5c0119cmd_base = namedtuple('Sbe5c0119cmd_base', ' ManufacturerID ProductID1 ProductID2 ProductVersion Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8, Length')

# Factory function for backward compatibility
def Sbe5c0119cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe5c0119cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe5c0119cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe5c0119cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe5c0119cmd_tup._make = lambda seq: Sbe5c0119cmd_tup(*seq)
Sbe5c0119cmd_bin = '=BBBfBBBBBBBB?'
# Sets up default automatic reports for a selected antenna. This will output the position used internally by the receiver.
S8ea70000cmd_tup = namedtuple('S8ea70000cmd_tup', ' Enable AntennaId')
S8ea70000cmd_bin = '=BB'
# Sets up automatic reports for a selected antenna based on the position engine used to generate the solution. Only positions of from the specified engines will be output
S8ea70001cmd_tup = namedtuple('S8ea70001cmd_tup', ' Enable AntennaId NumEngs PositionEngArray')
S8ea70001cmd_bin = '=BBB?B'
# Sets up automatic reports for a selected antenna based on the position type produced. Only positions of those types will be output.
S8ea70002cmd_tup = namedtuple('S8ea70002cmd_tup', ' Enable AntennaId NumTypes PositionTypeArray')
S8ea70002cmd_bin = '=BBB?B'
# Sets up automatic reports for a selected antenna based on the position flags assigned. Only positions with the given flags will be output.
S8ea70003cmd_tup = namedtuple('S8ea70003cmd_tup', ' Enable AntennaId SetFlags ClearedFlags')
S8ea70003cmd_bin = '=BBLL'
# Requests the last position from for a specified antenna. If the last position wasn't valid, a no position is output instead
S8ea70100req_tup = namedtuple('S8ea70100req_tup', ' AntennaId')
S8ea70100req_bin = '=B'
# Requests the last position from the given engine on the specified antenna. If the last position wasn't valid, a no position is output instead
S8ea70101req_tup = namedtuple('S8ea70101req_tup', ' AntennaId PositionEng')
S8ea70101req_bin = '=BB'
# Requests the last position of the given type from the specified antenna. If the last position wasn't valid, a no position is output instead
S8ea70102req_tup = namedtuple('S8ea70102req_tup', ' AntennaId PositionType')
S8ea70102req_bin = '=BB'
# Requests the last position matching the provided flags from the specified antenna. If the last position wasn't valid, a no position is output instead
S8ea70103req_tup = namedtuple('S8ea70103req_tup', ' AntennaId SetFlags ClearedFlags')
S8ea70103req_bin = '=BLL'
# Request the VRS Radio Status
S8ea800req_tup = namedtuple('S8ea800req_tup', '')
S8ea800req_bin = '='
# Set the NTRIP parameters for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
S8ea801cmd_tup = namedtuple('S8ea801cmd_tup', ' IPPort IPAddrLength IPAddress MountPointLength MountPoint UserNameLength UserName PasswordLength Password UseForRTX')
S8ea801cmd_bin = '=HB?cB?cB?cB?cB'
# Request the NTRIP parameters for the VRS Radio
S8ea801req_tup = namedtuple('S8ea801req_tup', '')
S8ea801req_bin = '='
# Set the GPRS Username for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
S8ea802cmd_tup = namedtuple('S8ea802cmd_tup', ' StringLength UserName')
S8ea802cmd_bin = '=B?c'
# Request the GPRS Username for the VRS Radio
S8ea802req_tup = namedtuple('S8ea802req_tup', '')
S8ea802req_bin = '='
# Set the GPRS Password for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
S8ea803cmd_tup = namedtuple('S8ea803cmd_tup', ' StringLength Password')
S8ea803cmd_bin = '=B?c'
# Request the GPRS Password for the VRS Radio
S8ea803req_tup = namedtuple('S8ea803req_tup', '')
S8ea803req_bin = '='
# Set the GPRS InitString for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
S8ea804cmd_tup = namedtuple('S8ea804cmd_tup', ' StringLength InitString')
S8ea804cmd_bin = '=B?c'
# Request the GPRS InitString for the VRS Radio
S8ea804req_tup = namedtuple('S8ea804req_tup', '')
S8ea804req_bin = '='
# Set the GPRS CPIN for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
S8ea805cmd_tup = namedtuple('S8ea805cmd_tup', ' StringLength CPIN')
S8ea805cmd_bin = '=B?c'
# Configure the VRS Radio
S8ea806cmd_tup = namedtuple('S8ea806cmd_tup', ' EnableVRS EnableAutoReport StreamType')
S8ea806cmd_bin = '=BBB'
# Request the VRS Radio Config
S8ea806req_tup = namedtuple('S8ea806req_tup', '')
S8ea806req_bin = '='
# Requests the various firmware and hardware version information
S8ea900req_tup = namedtuple('S8ea900req_tup', '')
S8ea900req_bin = '='
# Requests that the receiver begin upgrading with the provided file. The upgrading performed by the receiver will depend on the hardware, but it is expected to begin upgrading if possible. The receiver will respond with information regarding whether the request was carried out.
S8ea90100cmd_tup = namedtuple('S8ea90100cmd_tup', ' ImageType FilenameLen Filename')
S8ea90100cmd_bin = '=BB?c'
# Allows the user to start and stop logging, and provide the location to log to.
S8ea90101cmd_tup = namedtuple('S8ea90101cmd_tup', ' Action prefixLen prefix')
S8ea90101cmd_bin = '=BB?c'
# Requests the current status of the logging control
S8ea90101req_tup = namedtuple('S8ea90101req_tup', '')
S8ea90101req_bin = '='
# Requests a particular log be dumped to specified path.
S8ea90102cmd_tup = namedtuple('S8ea90102cmd_tup', ' LogType FilenameLen Filename')
S8ea90102cmd_bin = '=BB?c'
# Sends a variable length data packet (ping), that will be returned by the receiver (pong). This allows a type of serial communication test to occur.
S8ea90103cmd_tup = namedtuple('S8ea90103cmd_tup', ' PingSize Data')
S8ea90103cmd_bin = '=B?B'
# Request the IP Address and port number for the VRS Daemon
S8ea90104req_tup = namedtuple('S8ea90104req_tup', '')
S8ea90104req_bin = '='
# Set the IP Address and port number for the VRS Daemon
S8ea90104cmd_tup = namedtuple('S8ea90104cmd_tup', ', IP Port')
S8ea90104cmd_bin = '=20sH'
# Requests that the receiver install licenses with a given file
S8ea90105cmd_tup = namedtuple('S8ea90105cmd_tup', ' FilenameLen Filename')
S8ea90105cmd_bin = '=B?c'
# Request the current state of the receiver automatic reboot capability
S8ea90106req_tup = namedtuple('S8ea90106req_tup', '')
S8ea90106req_bin = '='
# Control the frequency at which the receiver will automatically reboot
S8ea90106cmd_tup = namedtuple('S8ea90106cmd_tup', ' Frequency')
S8ea90106cmd_bin = '=B'
# Request the IP Address and port number for the CLAAS RTK NET modem
S8ea90107req_tup = namedtuple('S8ea90107req_tup', '')
S8ea90107req_bin = '='
# Set the IP Address and port number for the CLAAS RTK NET modem
S8ea90107cmd_tup = namedtuple('S8ea90107cmd_tup', ', IP Port')
S8ea90107cmd_bin = '=20sH'
# Request the TNFS Host Address
S8ea90108req_tup = namedtuple('S8ea90108req_tup', '')
S8ea90108req_bin = '='
# Set the IP Address for the TNFS Host Address
S8ea90108cmd_tup = namedtuple('S8ea90108cmd_tup', ', IP')
S8ea90108cmd_bin = '=20s'
# Requests the upgrade/downgrade version floor of the receiver
S8ea90130req_tup = namedtuple('S8ea90130req_tup', '')
S8ea90130req_bin = '='
# Checks if an upgrade/downgrade to the given version is allowed
S8ea90131req_tup = namedtuple('S8ea90131req_tup', ' MajorVersion MinorVersion BuildNum BuildType FeatureSpecific')
S8ea90131req_bin = '=BBHBB'
# Request the mux settings of the digital output of a particular port.
S8ea90200req_tup = namedtuple('S8ea90200req_tup', ' PortId')
S8ea90200req_bin = '=B'
# Sets the mux behaviour of the digital output for a particular port.
S8ea90200cmd_tup = namedtuple('S8ea90200cmd_tup', ' PortId MuxType OutputValue')
S8ea90200cmd_bin = '=BBB'
# Request the settings of the digital input of a particular port.
S8ea90201req_tup = namedtuple('S8ea90201req_tup', ' PortId')
S8ea90201req_bin = '=B'
# Sets the behaviour of the digital input for a particular port.
S8ea90201cmd_tup = namedtuple('S8ea90201cmd_tup', ' PortId Threshold Pull')
S8ea90201cmd_bin = '=BBB'
# Request the settings of the Pollux FPGA GPO.
S8ea90202req_tup = namedtuple('S8ea90202req_tup', '')
S8ea90202req_bin = '='
# Sets the behaviour of the GPO for the Pollux FPGA.
S8ea90202cmd_tup = namedtuple('S8ea90202cmd_tup', ' GPOSetting')
S8ea90202cmd_bin = '=B'
# Requests information about connected Antennas.
S8ea90300req_tup = namedtuple('S8ea90300req_tup', '')
S8ea90300req_bin = '='
# Commands the power state of an antenna. The command is acknowledged with the Antenna info packet.
S8ea90301cmd_tup = namedtuple('S8ea90301cmd_tup', ' AntennaId PowerOn')
S8ea90301cmd_bin = '=BB'
# Requests information on the Radar setup
S8ea90400req_tup = namedtuple('S8ea90400req_tup', '')
S8ea90400req_bin = '='
# Configures the Radar setup
S8ea90400cmd_tup = namedtuple('S8ea90400cmd_tup', ' Enable FreqSpeedRate')
S8ea90400cmd_bin = '=Bf'
# Place a string command into the receiver program log. Responds with a simple ack.
S8ea905cmd_tup = namedtuple('S8ea905cmd_tup', ' TimeStamp EventType Length LogMessage')
S8ea905cmd_bin = '=LBB?c'
# Requests the settings of the Module-A Digital Pin Muxing.
S8ea90700req_tup = namedtuple('S8ea90700req_tup', ' DigitalPin')
S8ea90700req_bin = '=B'
# Sets the Module-A Digital Pin Muxing.
S8ea90700cmd_tup = namedtuple('S8ea90700cmd_tup', ' DigitalPin MuxType Output')
S8ea90700cmd_bin = '=BBB'
# Requests the settings of the pwmon control point.
S8ea90701req_tup = namedtuple('S8ea90701req_tup', ' CtrlPoint')
S8ea90701req_bin = '=B'
# Sets the Module-A power monitor options.
S8ea90701cmd_tup = namedtuple('S8ea90701cmd_tup', ' CtrlPoint CtrlCmd')
S8ea90701cmd_bin = '=BB'
# Requests the settings Video Input Mux.
S8ea90703req_tup = namedtuple('S8ea90703req_tup', ' VideoInput')
S8ea90703req_bin = '=B'
# Sets the Module-A Video Mux options.
S8ea90703cmd_tup = namedtuple('S8ea90703cmd_tup', ' VideoInput MuxInputValue Output')
S8ea90703cmd_bin = '=BBB'
# Requests Module-A auto shutdown timer settings.
S8ea90704req_tup = namedtuple('S8ea90704req_tup', '')
S8ea90704req_bin = '='
# Sets Module-A auto shutdown timer delay.
S8ea90704cmd_tup = namedtuple('S8ea90704cmd_tup', ' Delay')
S8ea90704cmd_bin = '=B'
# Gets the network interface configuration info.
S8ea90705req_tup = namedtuple('S8ea90705req_tup', ' NetIfaceSettingLife')
S8ea90705req_bin = '=B'
# Sets the Module A's network interface to a specific setting.
S8ea90705cmd_tup = namedtuple('S8ea90705cmd_tup', ' NetIfaceSettingLife NetIfaceMode IP NetMask Gateway Broadcast')
S8ea90705cmd_bin = '=BBLLLL'
# Retrieves the current counters statistics for a port on the switch
S8ea90708req_tup = namedtuple('S8ea90708req_tup', ' Port')
S8ea90708req_bin = '=B'
# The current counters statistics for a port on the switch
S8fa90708req_tup = namedtuple('S8fa90708req_tup', ' Port rxLoPriorityByte rxHiPriorityByte rxUndersizePkt rxFragments rxOversize rxJabbers rxSymbolError rxCRCError rxAlignmentError rxControl8808Pkts rxPausePkts rxBroadcast rxMulticast rxUnicast rx64Octets rx65To127Octets rx128To255Octets rx256To511Octets rx512To1023Octets rx1024To1522Octets txLoPriorityByte txHiPriorityByte txLateCollision txPausePkts txBroadcastPkts txMulticastPackets txUnicastPackets txDeferred txTotalCollision txExcessiveCollision txSingleCollision txMultipleCollision txDroppedPackets rxDroppedPackets')
S8fa90708req_bin = '=BLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLHH'
# Requests the reading of the given ADC Channel
S8ea90600req_tup = namedtuple('S8ea90600req_tup', ' Normalized Channel')
S8ea90600req_bin = '=BB'
# Requests Module-A hardware configuration
S8ea90706req_tup = namedtuple('S8ea90706req_tup', '')
S8ea90706req_bin = '='
# Requests the socket uart device details configured for Port-D on the Module-A
S8ea90707req_tup = namedtuple('S8ea90707req_tup', '')
S8ea90707req_bin = '='
# Sets the socket uart device to be used for Port-D on the Module-A.  The device must be a TBIP device that supports the socket-uart protocol.
S8ea90707cmd_tup = namedtuple('S8ea90707cmd_tup', ' TBIPDeviceType, SerialNumber UartId')
S8ea90707cmd_bin = '=L32sB'
# Requests the current state of RTK correction rebroadcasting
S8ea90800req_tup = namedtuple('S8ea90800req_tup', '')
S8ea90800req_bin = '='
# Sets the state of RTK correction rebroadcasting
S8ea90800cmd_tup = namedtuple('S8ea90800cmd_tup', ' Operation')
S8ea90800cmd_bin = '=B'
# Requests all the enabled features in the Feature Manager
S8ea90a00req_tup = namedtuple('S8ea90a00req_tup', '')
S8ea90a00req_bin = '='
# Requests the license status from the Feature Manager
S8ea90a01req_tup = namedtuple('S8ea90a01req_tup', '')
S8ea90a01req_bin = '='
# Request the status of the Receiver LEDs (if supported). This request invokes a response TSIP packet: 0x8F 0xA9 0x08 0x00.
S8ea909req_tup = namedtuple('S8ea909req_tup', ' RcvrId LEDId')
S8ea909req_bin = '=BB'
# Sets the behaviour of Receiver LEDs. This command is acknowledged with TSIP Packet 0x8F 0xA9 0xA8 0x00.
S8ea909cmd_tup = namedtuple('S8ea909cmd_tup', ' RcvrId EnableTSIPControl LEDId LEDState')
S8ea909cmd_bin = '=BBBB'
# Requests the status of receiver unlocks
S8ea910req_tup = namedtuple('S8ea910req_tup', '')
S8ea910req_bin = '='
# Product Information Request
S8ea911req_tup = namedtuple('S8ea911req_tup', '')
S8ea911req_bin = '='
# Boot Count Information Request
S8ea912req_tup = namedtuple('S8ea912req_tup', '')
S8ea912req_bin = '='
# Geoidal Separation Information Request
S8ea913req_tup = namedtuple('S8ea913req_tup', '')
S8ea913req_bin = '='
# Initiates transfer operation (get or put) for the given file type.
S8ea91500cmd_tup = namedtuple('S8ea91500cmd_tup', ' xferType fileType fileSize clientFileIdSize clientFileId')
S8ea91500cmd_bin = '=BBLB?B'
# Request to get a block from a system file
S8ea91501cmd_tup = namedtuple('S8ea91501cmd_tup', ' fileId offset')
S8ea91501cmd_bin = '=LL'
# Request to put block to a system file
S8ea91502cmd_tup = namedtuple('S8ea91502cmd_tup', ' fileId offset blockSize blockData')
S8ea91502cmd_bin = '=LLB?B'
# Closes the open stream identified by fileId
S8ea91503cmd_tup = namedtuple('S8ea91503cmd_tup', ' fileId')
S8ea91503cmd_bin = '=L'
# Requests deletion of the specified system file
S8ea91504cmd_tup = namedtuple('S8ea91504cmd_tup', ' fileType')
S8ea91504cmd_bin = '=B'
# Get the mode of the GP uart mux
S8ea9160000req_tup = namedtuple('S8ea9160000req_tup', '')
S8ea9160000req_bin = '='
# Change internal routing of the General Purpose UART port in Fusion
S8ea9160000cmd_tup = namedtuple('S8ea9160000cmd_tup', ' mode')
S8ea9160000cmd_bin = '=B'
# Get the mux mode of the TX UART port in Fusion
S8ea9160001req_tup = namedtuple('S8ea9160001req_tup', '')
S8ea9160001req_bin = '='
# Change internal routing of the TX UART port in Fusion
S8ea9160001cmd_tup = namedtuple('S8ea9160001cmd_tup', ' mode')
S8ea9160001cmd_bin = '=B'
# Request the mux mode of the Radio port uart in Fusion
S8ea9160002req_tup = namedtuple('S8ea9160002req_tup', '')
S8ea9160002req_bin = '='
# Change internal routing of the Radio port uart in Fusion
S8ea9160002cmd_tup = namedtuple('S8ea9160002cmd_tup', ' mode')
S8ea9160002cmd_bin = '=B'
# Request the mode of the internal AP virtual uart in Fusion
S8ea9160100req_tup = namedtuple('S8ea9160100req_tup', '')
S8ea9160100req_bin = '='
# Sets the mode of the internal AP virtual uart in Fusion
S8ea9160100cmd_tup = namedtuple('S8ea9160100cmd_tup', ' mode')
S8ea9160100cmd_bin = '=B'
# Request Bluetooth state (enabled or disabled)
S8ea91602req_tup = namedtuple('S8ea91602req_tup', '')
S8ea91602req_bin = '='
# Enable/disable Bluetooth
S8ea91602cmd_tup = namedtuple('S8ea91602cmd_tup', ' enable')
S8ea91602cmd_bin = '=B'
# Clear All Licenses installed via user entry and factory installation
S8ea91603cmd_tup = namedtuple('S8ea91603cmd_tup', '')
S8ea91603cmd_bin = '='
# Remove / Restore Manufacturing Licenses
S8ea91604cmd_tup = namedtuple('S8ea91604cmd_tup', ' ClearType')
S8ea91604cmd_bin = '=B'
# Remove Licenses By Fragment command
S8ea91605cmd_tup = namedtuple('S8ea91605cmd_tup', ' FragmentLen Fragment')
S8ea91605cmd_bin = '=B?c'
# Requests UDS diagnostic status
S8ea91606req_tup = namedtuple('S8ea91606req_tup', '')
S8ea91606req_bin = '='
# Request the IMU settings. Expects response of 0x8f 0xa9 0x17 0x00.
S8ea91700req_tup = namedtuple('S8ea91700req_tup', '')
S8ea91700req_bin = '='
# Send IMU settings to configure pitch and roll corrected positions. Expects response of 0x8f 0xa9 0x17 0x00.
S8ea91700cmd_tup = namedtuple('S8ea91700cmd_tup', ' AntLevX AntLevY AntLevZ ImuAngleRoll ImuAnglePitch ImuAngleYaw ImuLevX ImuLevY ImuLevZ ImuRollOffset ImuPitchOffset')
S8ea91700cmd_bin = '=fffffffffff'
# Enable Fusion position correction based on IMU values.
S8ea91701cmd_tup = namedtuple('S8ea91701cmd_tup', ' EnableIMUCorrection EnableIMUDetailStream')
S8ea91701cmd_bin = '=BB'
# Query if IMU-Corrected positions and streaming are enabled.
S8ea91701req_tup = namedtuple('S8ea91701req_tup', '')
S8ea91701req_bin = '='
# Get the position details in case streaming is off; IMU-corrected if enabled.
S8ea91702req_tup = namedtuple('S8ea91702req_tup', '')
S8ea91702req_bin = '='
# Request the IMU settings Block 2. Expects response of 0x8f 0xa9 0x17 0x03.
S8ea91703req_tup = namedtuple('S8ea91703req_tup', '')
S8ea91703req_bin = '='
# Send IMU settings to configure extra settings related to the Fusion IMU supported features. Expects response of 0x8f 0xa9 0x17 0x03.
S8ea91703cmd_tup = namedtuple('S8ea91703cmd_tup', ' ProPointEngineMode StaticBenchModeEnable StaticBenchHeading VehicleType')
S8ea91703cmd_bin = '=BBfB'
# Requests the cryptochip configuration CRC value
S8ea918req_tup = namedtuple('S8ea918req_tup', '')
S8ea918req_bin = '='
# Request information on the CAN bus configuration
S8e9f00req_tup = namedtuple('S8e9f00req_tup', '')
S8e9f00req_bin = '='
# CAN Channel Config
S8e9f00cmdCANChannelCfg_tup = namedtuple('S8e9f00cmdCANChannelCfg_tup', ' Channel BusSpeed J1939Address J1939ECUInstance J1939FunctionInstance Flags')
S8e9f00cmdCANChannelCfg_bin = '=BBBBBB'
# Sets the CAN bus configuration for specified channels
S8e9f00cmd_tup = namedtuple('S8e9f00cmd_tup', ' NumChannels ChannelCfg')
S8e9f00cmd_bin = '=B?S8e9f00cmdCANChannelCfg'
# Request information on the CAN bus status
S8e9f01req_tup = namedtuple('S8e9f01req_tup', '')
S8e9f01req_bin = '='
# Request current J1939 message configuration for channel
S8e9f02req_tup = namedtuple('S8e9f02req_tup', ' Channel')
S8e9f02req_bin = '=B'
# J1939 message configuration
S8e9f02cmdMsgCfg_tup = namedtuple('S8e9f02cmdMsgCfg_tup', ' MsgType MsgInterval')
S8e9f02cmdMsgCfg_bin = '=BH'
# Configures one or more J1939 messages for channel
S8e9f02cmd_tup = namedtuple('S8e9f02cmd_tup', ' Channel NumMessages MsgCfgArray')
S8e9f02cmd_bin = '=BB?S8e9f02cmdMsgCfg'
# Request current NMEA2K message configuration for channel
S8e9f03req_tup = namedtuple('S8e9f03req_tup', ' Channel')
S8e9f03req_bin = '=B'
# NMEA2K message configuration
S8e9f03cmdMsgCfg_tup = namedtuple('S8e9f03cmdMsgCfg_tup', ' MsgType MsgInterval')
S8e9f03cmdMsgCfg_bin = '=BH'
# Configures one or more NMEA2K messages for channel
S8e9f03cmd_tup = namedtuple('S8e9f03cmd_tup', ' Channel NumMessages MsgCfgArray')
S8e9f03cmd_bin = '=BB?S8e9f03cmdMsgCfg'
# Request current ISO message configuration for channel
S8e9f04req_tup = namedtuple('S8e9f04req_tup', ' Channel')
S8e9f04req_bin = '=B'
# ISO message configuration
S8e9f04cmdMsgCfg_tup = namedtuple('S8e9f04cmdMsgCfg_tup', ' MsgType MsgInterval')
S8e9f04cmdMsgCfg_bin = '=BH'
# Configures one or more ISO messages for channel
S8e9f04cmd_tup = namedtuple('S8e9f04cmd_tup', ' Channel NumMessages MsgCfgArray')
S8e9f04cmd_bin = '=BB?S8e9f04cmdMsgCfg'
# Requests the PPS configuration settings. The response is sent in 0xB0 0x80.
Sb000req_tup = namedtuple('Sb000req_tup', ' PPSNumber')
Sb000req_bin = '=B'
# Sets the PPS configuration settings. The command is acknowleged with a 0xB0 0x80 response.
Sb000cmd_tup = namedtuple('Sb000cmd_tup', ' PPSNumber EnableFlag PPSTimebase PPSPolarity AutoReport Frequency Offset MaxUncThreshold')
Sb000cmd_bin = '=BBBBBddf'
# Enables or disables the specified PPS signal. The command is acknowledged with a 0xB0 0x81 response.
Sb001cmd_tup = namedtuple('Sb001cmd_tup', ' PPSNumber EnableFlag')
Sb001cmd_bin = '=BB'
# Configuration packet command to the INS feature
Sbe60cmd_tup = namedtuple('Sbe60cmd_tup', ', PacketDataLength, PacketData')
Sbe60cmd_bin = '=B*'
# TAP packet command to the Inertial Nav feature
Sbe6014cmd_tup = namedtuple('Sbe6014cmd_tup', ' CommandID, PacketDataLength, PacketData')
Sbe6014cmd_bin = '=BB*'
# Remote Monitor Control Steering packet command to the Inertial Nav feature
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe630600cmd_base = namedtuple('Sbe630600cmd_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbe630600cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe630600cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe630600cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe630600cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe630600cmd_tup._make = lambda seq: Sbe630600cmd_tup(*seq)
Sbe630600cmd_bin = '=B?'
# Remote Monitor Control Speed packet command to the Inertial Nav feature
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe630601cmd_base = namedtuple('Sbe630601cmd_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbe630601cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe630601cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe630601cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe630601cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe630601cmd_tup._make = lambda seq: Sbe630601cmd_tup(*seq)
Sbe630601cmd_bin = '=B?'
# Publish Parameter Block Hardware Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710000req_base = namedtuple('Sbe710000req_base', ', Length')

# Factory function for backward compatibility
def Sbe710000req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710000req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710000req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710000req_base(*args)

# Add _make method for compatibility with existing code
Sbe710000req_tup._make = lambda seq: Sbe710000req_tup(*seq)
Sbe710000req_bin = '=?'
# Publish Parameter Block Software Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710100req_base = namedtuple('Sbe710100req_base', ', Length')

# Factory function for backward compatibility
def Sbe710100req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710100req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710100req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710100req_base(*args)

# Add _make method for compatibility with existing code
Sbe710100req_tup._make = lambda seq: Sbe710100req_tup(*seq)
Sbe710100req_bin = '=?'
# Publish Parameter Block OPS Config Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710200req_base = namedtuple('Sbe710200req_base', ', Length')

# Factory function for backward compatibility
def Sbe710200req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710200req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710200req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710200req_base(*args)

# Add _make method for compatibility with existing code
Sbe710200req_tup._make = lambda seq: Sbe710200req_tup(*seq)
Sbe710200req_bin = '=?'
# Publish Parameter Block OPS Config Information packet SET from the Display    to Autopilot Nudge and Draft
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710201req_base = namedtuple('Sbe710201req_base', ' LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset, Length')

# Factory function for backward compatibility
def Sbe710201req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710201req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710201req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710201req_base(*args)

# Add _make method for compatibility with existing code
Sbe710201req_tup._make = lambda seq: Sbe710201req_tup(*seq)
Sbe710201req_bin = '=fBffff?'
# Publish Parameter Block Platform Config Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710300req_base = namedtuple('Sbe710300req_base', ', Length')

# Factory function for backward compatibility
def Sbe710300req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710300req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710300req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710300req_base(*args)

# Add _make method for compatibility with existing code
Sbe710300req_tup._make = lambda seq: Sbe710300req_tup(*seq)
Sbe710300req_bin = '=?'
# Publish Parameter Block Safety Config Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710400req_base = namedtuple('Sbe710400req_base', ', Length')

# Factory function for backward compatibility
def Sbe710400req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710400req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710400req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710400req_base(*args)

# Add _make method for compatibility with existing code
Sbe710400req_tup._make = lambda seq: Sbe710400req_tup(*seq)
Sbe710400req_bin = '=?'
# Publish Parameter Block Version Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710500req_base = namedtuple('Sbe710500req_base', ', Length')

# Factory function for backward compatibility
def Sbe710500req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710500req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710500req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710500req_base(*args)

# Add _make method for compatibility with existing code
Sbe710500req_tup._make = lambda seq: Sbe710500req_tup(*seq)
Sbe710500req_bin = '=?'
# Publish Parameter Block Sensor Hyd Status Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710600req_base = namedtuple('Sbe710600req_base', ', Length')

# Factory function for backward compatibility
def Sbe710600req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710600req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710600req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710600req_base(*args)

# Add _make method for compatibility with existing code
Sbe710600req_tup._make = lambda seq: Sbe710600req_tup(*seq)
Sbe710600req_bin = '=?'
# Publish Parameter Block Raw Sensor Status Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710700req_base = namedtuple('Sbe710700req_base', ', Length')

# Factory function for backward compatibility
def Sbe710700req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710700req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710700req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710700req_base(*args)

# Add _make method for compatibility with existing code
Sbe710700req_tup._make = lambda seq: Sbe710700req_tup(*seq)
Sbe710700req_bin = '=?'
# Publish Parameter Block Selected IMU Status Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710800req_base = namedtuple('Sbe710800req_base', ', Length')

# Factory function for backward compatibility
def Sbe710800req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710800req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710800req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710800req_base(*args)

# Add _make method for compatibility with existing code
Sbe710800req_tup._make = lambda seq: Sbe710800req_tup(*seq)
Sbe710800req_bin = '=?'
# Publish Parameter Block CS Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710900req_base = namedtuple('Sbe710900req_base', ', Length')

# Factory function for backward compatibility
def Sbe710900req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710900req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710900req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710900req_base(*args)

# Add _make method for compatibility with existing code
Sbe710900req_tup._make = lambda seq: Sbe710900req_tup(*seq)
Sbe710900req_bin = '=?'
# Publish Parameter Block Group1 Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710a00req_base = namedtuple('Sbe710a00req_base', ', Length')

# Factory function for backward compatibility
def Sbe710a00req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710a00req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710a00req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710a00req_base(*args)

# Add _make method for compatibility with existing code
Sbe710a00req_tup._make = lambda seq: Sbe710a00req_tup(*seq)
Sbe710a00req_bin = '=?'
# Publish Parameter Block Group2 Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710b00req_base = namedtuple('Sbe710b00req_base', ', Length')

# Factory function for backward compatibility
def Sbe710b00req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710b00req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710b00req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710b00req_base(*args)

# Add _make method for compatibility with existing code
Sbe710b00req_tup._make = lambda seq: Sbe710b00req_tup(*seq)
Sbe710b00req_bin = '=?'
# Publish Parameter Block Group3 Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710c00req_base = namedtuple('Sbe710c00req_base', ', Length')

# Factory function for backward compatibility
def Sbe710c00req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710c00req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710c00req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710c00req_base(*args)

# Add _make method for compatibility with existing code
Sbe710c00req_tup._make = lambda seq: Sbe710c00req_tup(*seq)
Sbe710c00req_bin = '=?'
# Publish Parameter Block GPS Guidance Status Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710d00req_base = namedtuple('Sbe710d00req_base', ', Length')

# Factory function for backward compatibility
def Sbe710d00req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710d00req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710d00req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710d00req_base(*args)

# Add _make method for compatibility with existing code
Sbe710d00req_tup._make = lambda seq: Sbe710d00req_tup(*seq)
Sbe710d00req_bin = '=?'
# Publish Parameter Block GPS Guidance Diag Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710e00req_base = namedtuple('Sbe710e00req_base', ', Length')

# Factory function for backward compatibility
def Sbe710e00req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710e00req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710e00req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710e00req_base(*args)

# Add _make method for compatibility with existing code
Sbe710e00req_tup._make = lambda seq: Sbe710e00req_tup(*seq)
Sbe710e00req_bin = '=?'
# Publish Parameter Block Group4 Information packet request from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe710f00req_base = namedtuple('Sbe710f00req_base', ', Length')

# Factory function for backward compatibility
def Sbe710f00req_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe710f00req_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe710f00req_base(*args, 0)
    # Otherwise use args as provided
    return Sbe710f00req_base(*args)

# Add _make method for compatibility with existing code
Sbe710f00req_tup._make = lambda seq: Sbe710f00req_tup(*seq)
Sbe710f00req_bin = '=?'
# FFA command to Autopilot Navigation Controller.
Sbe8000cmd_tup = namedtuple('Sbe8000cmd_tup', ' Version Button')
Sbe8000cmd_bin = '=BB'
# Requests the status of SecureRTK and the 5 rover keys.
S690000req_tup = namedtuple('S690000req_tup', ' Version')
S690000req_bin = '=B'
# Rover Key Data
S690001req_tup = namedtuple('S690001req_tup', ' Version KeySlot')
S690001req_bin = '=BB'
# Set Rover Key Data
S690002cmd_tup = namedtuple('S690002cmd_tup', ' Version KeySlot, KeyString, DescriptionString')
S690002cmd_bin = '=BB17s16s'
# Delete Rover Key Data
S690003cmd_tup = namedtuple('S690003cmd_tup', ' Version KeySlot')
S690003cmd_bin = '=BB'
# New 27 character passcode upgrade request packet
S8ea9a5req_tup = namedtuple('S8ea9a5req_tup', ', PasscodeString')
S8ea9a5req_bin = '=65s'
# Requests type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response.
S8eaa00req_tup = namedtuple('S8eaa00req_tup', ' AntennaId')
S8eaa00req_bin = '=B'
# Command to set type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response.
S8eaa00cmd_tup = namedtuple('S8eaa00cmd_tup', ' AntennaId AntennaType')
S8eaa00cmd_bin = '=BH'
# Checks the RTX subscription on the receiver and shows which connections are available
S8eab00req_tup = namedtuple('S8eab00req_tup', '')
S8eab00req_bin = '='
# Requests the Centerpoint RTX fast Network Info from the receiver. Packet 0x8f 0xab 0x01 is sent in response.
S8eab01req_tup = namedtuple('S8eab01req_tup', '')
S8eab01req_bin = '='
# Cancels RTX std FastRestart. The command is acknowledged with packet 0x8f 0xab 0x02.
S8eab02cmd_tup = namedtuple('S8eab02cmd_tup', '')
S8eab02cmd_bin = '='
# Requests CenterPoint RTX status. The command is acknowledged with packet 0x8f 0xab 0x03.
S8eab03req_tup = namedtuple('S8eab03req_tup', '')
S8eab03req_bin = '='
# Allows TSIP to confirm whether vehicle has moved post reboot on FastRestart enabled Ag receivers. The command is acknowledged with packet 0x8f 0xab 0x04.
S8eab04cmd_tup = namedtuple('S8eab04cmd_tup', ' HasVehicleMoved')
S8eab04cmd_bin = '=B'
# Custom RTX offset
S8eab05cmdRTXOffset_tup = namedtuple('S8eab05cmdRTXOffset_tup', ' enabled east north up')
S8eab05cmdRTXOffset_bin = '=Bfff'
# Allows the RTX output settings to be selected using TSIP. The command is acknowledged with packet 0x8f 0xab 0x05.
S8eab05cmd_tup = namedtuple('S8eab05cmd_tup', ' RTXOutputDatum RTXOffset')
S8eab05cmd_bin = '=B?B'
# Requests the current RTX output settings using TSIP. The request is acknowledged with packet 0x8f 0xab 0x05.
S8eab05req_tup = namedtuple('S8eab05req_tup', '')
S8eab05req_bin = '='
# If RTK is unlocked, function automatically determines what Centerpoint RTX (FAST/STD) to be used based on what Centerpoint license is available. If RTK and/or RTX unlock(s) are not found, convergence is autoamtically set to SBAS. The request is acknowledged with packet 0x8f 0xab 0x06.
S8eab06cmd_tup = namedtuple('S8eab06cmd_tup', '')
S8eab06cmd_bin = '='
# Request the current configuration and mode of the MSS Mode Switch
S8eab07req_tup = namedtuple('S8eab07req_tup', '')
S8eab07req_bin = '='
# Control the MSS Mode Switch
S8eab07cmd_tup = namedtuple('S8eab07cmd_tup', ' MSSControlMode')
S8eab07cmd_bin = '=B'
# Requests the realtime RTK/RTX Custom Offsets using TSIP. The request is acknowledged with packet 0x8f 0xab 0x08.
S8eab08req_tup = namedtuple('S8eab08req_tup', ' RtkRtxCustomOffsetRequest')
S8eab08req_bin = '=B'
# Sets the configuration for genral parameters of the boom height system
S8eac0000cmd_tup = namedtuple('S8eac0000cmd_tup', ' APIversion enabled targetHeight sprayerSuspensionType sensingMode groundSensitivity canopySensitivity groundFilter canopyFilter chevronThresh maximumHeight minimumHeight minSafeHeightBelowTarget heightStep aggressiveness downSlewLim downGainStabilizer wingPhasingHeightThreshold useKato autoDisableTimeout')
S8eac0000cmd_bin = '=BBdbbBBBBdddddhHHdBL'
# 
S8eac0001cmdsensors_tup = namedtuple('S8eac0001cmdsensors_tup', ', serialNumber enabled location sideOffset nozzleOffset')
S8eac0001cmdsensors_bin = '=11sBbdd'
# Sets the configuration for sensor parameters of the boom height system
S8eac0001cmd_tup = namedtuple('S8eac0001cmd_tup', ' APIversion numberOfSensors sensorsArray')
S8eac0001cmd_bin = '=BB?S8eac0001cmdsensors'
# 
S8eac0002cmdactuators_tup = namedtuple('S8eac0002cmdactuators_tup', ', serialNumber enabled slopeCalibrated deadbandCalibrated zone operation positiveSlope positiveDeadband negativeSlope negativeDeadband calSensorArmLength aggressiveness isInverted fineControlZone')
S8eac0002cmdactuators_bin = '=11sBBBBbdddddhBd'
# Sets the configuration for actuator parameters of the boom height system
S8eac0002cmd_tup = namedtuple('S8eac0002cmd_tup', ' APIversion numberOfActuators actuatorsArray')
S8eac0002cmd_bin = '=BB?S8eac0002cmdactuators'
# Requests the configuration for genral parameters
S8eac0100req_tup = namedtuple('S8eac0100req_tup', ' APIversion')
S8eac0100req_bin = '=B'
# Requests the configuration for sensor parameters
S8eac0101req_tup = namedtuple('S8eac0101req_tup', ' APIversion')
S8eac0101req_bin = '=B'
# Requests the configuration for actuator parameters
S8eac0102req_tup = namedtuple('S8eac0102req_tup', ' APIversion')
S8eac0102req_bin = '=B'
# Commands to initiate actuator calibration modes
S8eac02cmd_tup = namedtuple('S8eac02cmd_tup', ' APIversion CalType ChangeStateAction ZoneLocation')
S8eac02cmd_bin = '=BBBB'
# Request for actuator status
S8eac03req_tup = namedtuple('S8eac03req_tup', ' APIversion')
S8eac03req_bin = '=B'
# 
S8eac04cmdZoneMan_tup = namedtuple('S8eac04cmdZoneMan_tup', ' ZoneLocation Rate')
S8eac04cmdZoneMan_bin = '=Bf'
# Sets the Boom Height control state system including various parameters. This is typically sent periodically at 5Hz
S8eac04cmd_tup = namedtuple('S8eac04cmd_tup', ' APIversion TargetHeight SystemAggr SensorMode SensorSensitivity NumManZones ManualZoneArray')
S8eac04cmd_bin = '=BfhBBB?S8eac04cmdZoneMan'
# Commands to commit system actions
S8eac05cmd_tup = namedtuple('S8eac05cmd_tup', ' APIversion StateAction ZoneLocation')
S8eac05cmd_bin = '=BBB'
# Requests alert statuses
S8eac06req_tup = namedtuple('S8eac06req_tup', ' APIversion')
S8eac06req_bin = '=B'
# Request list of attached devices
S8eac07req_tup = namedtuple('S8eac07req_tup', ' APIversion')
S8eac07req_bin = '=B'
# Retrieve Centerpoint or Rangepoint RTX Passcodes on the receiver if a subscription is available. Response Packet: 0x8f 0xad 0x00
S8ead00req_tup = namedtuple('S8ead00req_tup', '')
S8ead00req_bin = '='
# Command to erase/clear Centerpoint/Rangepoint RTX Passcodes installed in the receiver. ACK Packet is 0x8f 0xad 0x01
S8ead01cmd_tup = namedtuple('S8ead01cmd_tup', ' PasscodeType')
S8ead01cmd_bin = '=B'
# Retrieve RTX Position Allowed Status on the receiver. Response Packet: 0x8f 0xad 0x02
S8ead02req_tup = namedtuple('S8ead02req_tup', '')
S8ead02req_bin = '='
# Command to set or clear the RTX position allowed flag status. Response Packet: 0x8f 0xad 0x02
S8ead03cmd_tup = namedtuple('S8ead03cmd_tup', ' RTXPositionAllowed')
S8ead03cmd_bin = '=B'
# Requests satellite constellation report from receiver. One or more 0xd5 0x00 packets are sent in response.
Sc500req_tup = namedtuple('Sc500req_tup', ' AntennaId')
Sc500req_bin = '=B'
# Set which satellite systems are enabled/disabled
Sc501cmd_tup = namedtuple('Sc501cmd_tup', ' SatelliteSystemControlFlag')
Sc501cmd_bin = '=H'
# Request report which satellite system is enabled/disabled
Sc502req_tup = namedtuple('Sc502req_tup', '')
Sc502req_bin = '='
# TBIP authenticated command to set the allowed GeoFencing Regions.
Sc60000cmd_tup = namedtuple('Sc60000cmd_tup', ' KeyIndex DeviceType, SerialNumber, ChallengeResponse RegionProtectMask, Digest')
Sc60000cmd_bin = '=HH32s16?BL16?B'
# Authorized base array entry
Sc60100cmdAuthorizedBaseEntry_tup = namedtuple('Sc60100cmdAuthorizedBaseEntry_tup', ' IsValid AccessControlId ExpiryGPSDay')
Sc60100cmdAuthorizedBaseEntry_bin = '=BLH'
# TBIP authenticated command to set list of authorized SecureRTK bases.
Sc60100cmd_tup = namedtuple('Sc60100cmd_tup', ' KeyIndex DeviceType, SerialNumber, ChallengeResponse, AuthorizedBaseArray, Digest')
Sc60100cmd_bin = '=HH32s16?B5?Sc60100cmdAuthorizedBaseEntry16?B'
# TBIP authenticated command to authorize the output of GPS fix engines (per antenna) by accuracy level.
Sc60200cmd_tup = namedtuple('Sc60200cmd_tup', ' KeyIndex DeviceType, SerialNumber, ChallengeResponse, AuthorizedFixEngineArray, Digest')
Sc60200cmd_bin = '=HH32s16?B4?B16?B'
# TBIP authenticated command to allow RTX datum selection.
Sc60400cmd_tup = namedtuple('Sc60400cmd_tup', ' KeyIndex DeviceType, SerialNumber, ChallengeResponse AuthorizedRTXAdvDatum, Digest')
Sc60400cmd_bin = '=HH32s16?BB16?B'
# Lock or Unlock all stinger channels. The action is persistent unless a command forces the existing state to change. This packet is for diagnostic purposes only and may change without notice. Acknowledge Packet: 0xD7 0x00
Sc700cmd_tup = namedtuple('Sc700cmd_tup', ' ChannelInformation LockChannel')
Sc700cmd_bin = '=HB'
# Request setting of Band and Filter switches for a signal.
Sc701req_tup = namedtuple('Sc701req_tup', ' Band_Select')
Sc701req_bin = '=B'
# Set Band and Filter switches for a signal.  0xd7 0x01 is the acknowledge packet.
Sc701cmd_tup = namedtuple('Sc701cmd_tup', ' Band_Select Filter_Select')
Sc701cmd_bin = '=BB'
# Requests the Bluetooth pairing information from the receiver
S8eae00req_tup = namedtuple('S8eae00req_tup', '')
S8eae00req_bin = '='
# Commands the power state of the Bluetooth module
S8eae01cmd_tup = namedtuple('S8eae01cmd_tup', ' Parameter')
S8eae01cmd_bin = '=B'
# Commands the Bluetooth pairing state of the receiver
S8eae02cmd_tup = namedtuple('S8eae02cmd_tup', ' Parameter')
S8eae02cmd_bin = '=B'
# Commands the receiver to unpair all Bluetooth devices
S8eae03cmd_tup = namedtuple('S8eae03cmd_tup', '')
S8eae03cmd_bin = '='
# Request the NAV to report pairing state changes
S8eae04req_tup = namedtuple('S8eae04req_tup', '')
S8eae04req_bin = '='
# Request notifications for Bluetooth device pairing and connection events
S8eae05req_tup = namedtuple('S8eae05req_tup', ' DeviceEventType')
S8eae05req_bin = '=L'
# New Path command starts a new guidance path. Set points to be interpreted as Polyline or Clothoid points
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c2300cmd_base = namedtuple('Sbe4c2300cmd_base', ' type, Length')

# Factory function for backward compatibility
def Sbe4c2300cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c2300cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c2300cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c2300cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c2300cmd_tup._make = lambda seq: Sbe4c2300cmd_tup(*seq)
Sbe4c2300cmd_bin = '=B?'
# Extend the guidance path by 1 point. Each point has a position XYZ and optional parameters for Clothoids
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c2301cmd_base = namedtuple('Sbe4c2301cmd_base', ' Sequence_Number X Y Z Heading Speed, Length')

# Factory function for backward compatibility
def Sbe4c2301cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c2301cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c2301cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c2301cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c2301cmd_tup._make = lambda seq: Sbe4c2301cmd_tup(*seq)
Sbe4c2301cmd_bin = '=Ldddff?'
# Query the usage of the clothoid guidance path for steering the vehicle.
Sbe4c2302req_tup = namedtuple('Sbe4c2302req_tup', '')
Sbe4c2302req_bin = '='
# Send to configure usage of the clothoid guidance path for steering the vehicle.
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbe4c2302cmd_base = namedtuple('Sbe4c2302cmd_base', ' Activate, Length')

# Factory function for backward compatibility
def Sbe4c2302cmd_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbe4c2302cmd_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbe4c2302cmd_base(*args, 0)
    # Otherwise use args as provided
    return Sbe4c2302cmd_base(*args)

# Add _make method for compatibility with existing code
Sbe4c2302cmd_tup._make = lambda seq: Sbe4c2302cmd_tup(*seq)
Sbe4c2302cmd_bin = '=B?'
# This is used so we can get to the raw data
S00rsp_tup = namedtuple('S00rsp_tup', ', PacketDataLength, PacketData')
S00rsp_bin = '=B*'
# Packet 0x13 is sent to notify the calling software when the receiver cannot parse the data sent in a command packet. The contents of the problem packet are included in the report.
S13rsp_tup = namedtuple('S13rsp_tup', ' PacketId, PacketDataLength, PacketData')
S13rsp_bin = '=BB*'
# Wraps NMEA messages for output in a TSIP stream. Command Packet 0x7A 0x07 configures the output of the NMEA wrapped data on a particular port.
S1a01rsp_tup = namedtuple('S1a01rsp_tup', ' NumBytes NMEAData')
S1a01rsp_bin = '=B?c'
# Indicates current settings for forwarding DCOL packets to connected port
S1a0200rsp_tup = namedtuple('S1a0200rsp_tup', ' NumTypes DCOLTypes')
S1a0200rsp_bin = '=B?B'
# TSIP wrapped DCOL message response from device.
S1a0201rsp_tup = namedtuple('S1a0201rsp_tup', ' NumBytes DCOLMessage')
S1a0201rsp_bin = '=B?B'
# TSIP wrapped CAN message
S1a0300rsp_tup = namedtuple('S1a0300rsp_tup', ' CanPort NumIDs CanIds')
S1a0300rsp_bin = '=BB?L'
# TSIP wrapped CAN message forwarded from device
S1a0301rsp_tup = namedtuple('S1a0301rsp_tup', ' CanId CanMsgLength CanMsg')
S1a0301rsp_bin = '=LB?B'
# reports the almanac data for a single satellite
S40rsp_tup = namedtuple('S40rsp_tup', ' SatNumber T_zc Week Eccentricity T_oa i_o Omega_dot sqrt_A Omega_o Omega m_o')
S40rsp_bin = '=Bfhffffffff'
# Reports receiver's machine ID and additional status info in response to packet 0x26.
S4brsp_tup = namedtuple('S4brsp_tup', ' MachineId StatusFlags1 StatusFlags2')
S4brsp_bin = '=BBB'
# Signal level info
S47rspSignalLevelInfo_tup = namedtuple('S47rspSignalLevelInfo_tup', ' PRN SignalLevel')
S47rspSignalLevelInfo_bin = '=Bf'
# Reports signal levels for all satellites currently being tracked in response to packet 0x27.
S47rsp_tup = namedtuple('S47rsp_tup', ' NumSats SignalLevelsInfoArray')
S47rsp_bin = '=B?S47rspSignalLevelInfo'
# GPS system message
S48rsp_tup = namedtuple('S48rsp_tup', ', LineContents')
S48rsp_bin = '=22s'
# Analog to digital readings from receiver
S53rsp_tup = namedtuple('S53rsp_tup', ' Temp Unused1 Unused2 AgcVoltage BatteryVotage Unused3 Unused4 Unused5')
S53rsp_bin = '=ffffffff'
# Provides the single precision lls fix values stored in the receiver
S4arsp_tup = namedtuple('S4arsp_tup', ' Altitude InverseVariance Flags')
S4arsp_bin = '=ffB'
# Provides the single precision lls fix values stored in the receiver
S4arspv1_tup = namedtuple('S4arspv1_tup', ' LLH_0 LLH_1 LLH_2 ClockBias Time')
S4arspv1_bin = '=fffff'
# Provides the single precision lls fix values stored in the receiver
S4arspv2_tup = namedtuple('S4arspv2_tup', ' LLH_0 LLH_1 LLH_2 ClockBias Time')
S4arspv2_bin = '=ffffd'
# Provides the operating parameter values of a receiver or requests the current parameter values stored in the receiver
S4crsp_tup = namedtuple('S4crsp_tup', ' DynamicsCode ElevationMask SignalLevelMask PDOPMask PDOPSwitch')
S4crsp_bin = '=Bffff'
# Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F.
S45rsp_tup = namedtuple('S45rsp_tup', ' NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear')
S45rsp_bin = '=BBBBBBBBBB'
# Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F.
S45rspv1_tup = namedtuple('S45rspv1_tup', ' NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear, BCDSerialNumber BCDChecksum Revision ConfigLength NumChannels RTCMInput RTCMOutput FixRate SynchMeas Miscellaneous NMEAOutput PPSOutput ProductId')
S45rspv1_bin = '=BBBBBBBBBB4?BBHBBBBBBBBBB'
# Reports current I/O options in response to Command Packet 0x35.
S55rsp_tup = namedtuple('S55rsp_tup', ' PosFlags VelocityFlags TimingFlags AuxFlags')
S55rsp_bin = '=BBBB'
# Report Packet 0x58 provides GPS data (almanac, ephemeris, etc.). The receiver sends this packet on request or in response to Command Packet 0x38 (acknowledging the loading of data). To get ionosphere or ephemeris, this report packet must be used
S58rsp_tup = namedtuple('S58rsp_tup', ' Operation DataType PRN NumBytes SVData')
S58rsp_bin = '=BBBB?B'
# Report data specific to the almanc response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
S5822rsp_tup = namedtuple('S5822rsp_tup', ' PRN NumBytes t_oa_raw SV_HEALTH e t_oa i_io omega_dot sqrt_A omega_0 omega m0 a_f0 a_f1 axis n omega_n o_dot_n t_zc weeknum wn_oa')
S5822rsp_bin = '=BBBBfffffffffffffffHH'
# Report data specific to the almanc health response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
S5823rsp_tup = namedtuple('S5823rsp_tup', ' PRN NumBytes weekno_health SVHealth t_oa_health t_oa_current weekno_current')
S5823rsp_bin = '=BBBLBBH'
# Report data specific to the ionosphere data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
S5824rsp_tup = namedtuple('S5824rsp_tup', ' PRN NumBytes Alpha_0 Alpha_1 Alpha_2 Alpha_3 Beta_0 Beta_1 Beta_2 Beta_3')
S5824rsp_bin = '=BBffffffff'
# Report data specific to the UTC data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
S5825rsp_tup = namedtuple('S5825rsp_tup', ' PRN NumBytes A_0 A_1 delta_t_ls t_ot wn_t wn_lsf dn delta_t_lsf')
S5825rsp_bin = '=BBdfHfHHHH'
# Report data specific to the Ephemeris response. This data can arrive in response to command packet 0x38 OR via configuration in command packet 0x7C 0x01. For all following fields, please see their corresponding reference in ICD-GPS-2000
S5826rsp_tup = namedtuple('S5826rsp_tup', ' PRN NumBytes PRNEphemeris t_ephem wn CodeL2 L2Pdata SVacc_raw SV_health IODC T_GD t_oc a_f2 a_f1 a_f0 SVacc IODE fit_interval C_rs Delta_n M_0 C_uc e C_us sqrt_A t_oe C_ic omega_0 C_is i_0 C_rc omega omega_dot i_dot axis n r1me2 omega_n o_dot_n')
S5826rsp_bin = '=BBBfhBBBBhffffffBBffdfdfdffdfdfdffddddd'
# Reports ephemeris status for a specified satellite in response to Command Packet 0x3B.
S5brsp_tup = namedtuple('S5brsp_tup', ' PRN CollectionTime Health IODE t_oe FitIntervalFlag URA')
S5brsp_bin = '=BfBBfBf'
# Reports tracking status for a specified satellite in response to Command Packet 0x3C.
S5crsp_tup = namedtuple('S5crsp_tup', ' PRN ChanAndSlot AcquisitionFlag EphemerisFlag SignalLevel GPSTime Elevation Azimuth OldMeasFlag IntegerMsecFlag BadDataFlag DataCollectFlag')
S5crsp_bin = '=BBBBffffBBBB'
# Indicates whether or not the receiver will output differential correction information.
S6a01rsp_tup = namedtuple('S6a01rsp_tup', ' CorrectionsUsedInFix CorrectionInfo')
S6a01rsp_bin = '=BB'
# Reports the state of the P/V Filter, Static Filter, and/or Altitude Filter in response to Command Packet 0x70.
S70rsp_tup = namedtuple('S70rsp_tup', ' DynamicFilter StaticFilter AltitudeFilter FilterLevel')
S70rsp_bin = '=BBBB'
# Reports the amount of time in seconds that RTCM pseudorange corrections can be propagated in DGPS mode before they are no longer used.
S78rsp_tup = namedtuple('S78rsp_tup', ' MaxPRCAge')
S78rsp_bin = '=H'
# Reports the data reporting options for the NMEA output on the specified port.
S7b07rsp_tup = namedtuple('S7b07rsp_tup', ' Port Options1')
S7b07rsp_bin = '=BB'
# Acknowledges command to set NMEA Extended Port Configuration Options
S7b08ack_tup = namedtuple('S7b08ack_tup', ' Result')
S7b08ack_bin = '=B'
# Reports the data reporting options for the NMEA extended output for a specified port.
S7b08rsp_tup = namedtuple('S7b08rsp_tup', ' Port MessageProtocol MessageInterval OutputMask GGAOptions Precision')
S7b08rsp_bin = '=BBBLBB'
# Reports the NMEA message output interval and the message mask for the current port.
S7b80rsp_tup = namedtuple('S7b80rsp_tup', ' Interval OutputMask')
S7b80rsp_bin = '=BL'
# Reports the GGA option settings for the current port.
S7b8600rsp_tup = namedtuple('S7b8600rsp_tup', ' Options Precision')
S7b8600rsp_bin = '=BB'
# Reports the RMC options and precision for the current port.
S7b860604rsp_tup = namedtuple('S7b860604rsp_tup', ' Options PosPrecision SpeedPrecision')
S7b860604rsp_bin = '=BBB'
# Reports the VTG options for the current port.
S7b8602rsp_tup = namedtuple('S7b8602rsp_tup', ' Options')
S7b8602rsp_bin = '=B'
# Reports the VTG options for the current port.
S7b8603rsp_tup = namedtuple('S7b8603rsp_tup', ' SpeedPrecision')
S7b8603rsp_bin = '=B'
# Reports the VTG options for the current port.
S7b8605rsp_tup = namedtuple('S7b8605rsp_tup', ' HeadingPrecision')
S7b8605rsp_bin = '=B'
# Reports the number of position fixes per second.
S7d00rsp_tup = namedtuple('S7d00rsp_tup', ' ASAPRate')
S7d00rsp_bin = '=B'
# Reports the position fix rate I/O options bytes.
S7d01rsp_tup = namedtuple('S7d01rsp_tup', ' OptionFlags1 OptionFlags2')
S7d01rsp_bin = '=BB'
# Reports the position fix output interval and offset that are used to deterimne output rate in relation to fix rate.
S7d02rsp_tup = namedtuple('S7d02rsp_tup', ' Interval Offset')
S7d02rsp_bin = '=HH'
# Reports the message interval for the specifed port and protocol.
S7d09rsp_tup = namedtuple('S7d09rsp_tup', ' Port MessageProtocol MessageInterval')
S7d09rsp_bin = '=BBB'
# Reports the differential position fix mode of the receiver.
S82rsp_tup = namedtuple('S82rsp_tup', ' Mode')
S82rsp_bin = '=B'
# Reports the differential position fix mode of the receiver.
S82rspv1_tup = namedtuple('S82rspv1_tup', ' Mode RTCMVersion ReferenceStationID')
S82rspv1_bin = '=BBh'
# Reports the current GPS position fix in XYZ ECEF coordinate components. The I/O position option must be set to XYZ ECEF and double-precision must be selected for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm.
S83rsp_tup = namedtuple('S83rsp_tup', ' X Y Z ClockBias TimeOfFix')
S83rsp_bin = '=ddddd'
# Reports the current GPS velocity fix in XYZ ECEF coordinate. The I/O velocity option must be set to XYZ ECEF for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm.
S43rsp_tup = namedtuple('S43rsp_tup', ' X Y Z BiasRate TimeOfFix')
S43rsp_bin = '=ffffd'
# Reports the current GPS position fix in XYZ ECEF coordinate components. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm.
S42rsp_tup = namedtuple('S42rsp_tup', ' X Y Z TimeOfFix')
S42rsp_bin = '=fffd'
# Reports the current GPS time of week and the week number.
S41rsp_tup = namedtuple('S41rsp_tup', ' Time Week Offset')
S41rsp_bin = '=fhf'
# UTC Parameters
S4frsp_tup = namedtuple('S4frsp_tup', ' A_0 A_1 delta_t_LS t_ot WN_t WN_LSF DN delta_t_LSF')
S4frsp_bin = '=dfhfhhhh'
# Reports info about the satellite tracking status and operational health of the receiver.
S46rsp_tup = namedtuple('S46rsp_tup', ' StatusCode ErrorFlags')
S46rsp_bin = '=BB'
# Reports the list of satelliites used for position fixes by the receiver.
S6drsp_tup = namedtuple('S6drsp_tup', ' FixMode PDOP HDOP VDOP TDOP SatsInView')
S6drsp_bin = '=Bffff?B'
# Provides CMR reception statistics for all the available base stations
S893308rsp_tup = namedtuple('S893308rsp_tup', ' NumStations SelStationId StationIds LinkQuality LastCMRTime')
S893308rsp_bin = '=BB?B?B?L'
# Sets the RTK configuration
S8940rsp_tup = namedtuple('S8940rsp_tup', ' PropagationMode VelocityType')
S8940rsp_bin = '=BB'
# Provides RTK Solution Info
S8941rsp_tup = namedtuple('S8941rsp_tup', ' SolutionMode SolutionType SolutionFlags CorrAge HorzErrorEst IonoScintLevel')
S8941rsp_bin = '=BBLddd'
# Provides RTK Aux Settings
S8950rsp_tup = namedtuple('S8950rsp_tup', ' ScintillationMode BackupSource RTKBaseDatum XFillSatFrequency XFillSatBitRate RTKBaseID SatConfigSource')
S8950rsp_bin = '=BBBdfHB'
# Provides RTK Aux Status
S8951rsp_tup = namedtuple('S8951rsp_tup', ' xFillStatus XFillTimeRemaining XFillCorrectionAge')
S8951rsp_bin = '=Bhh'
# 
S8960rspBaseVector_tup = namedtuple('S8960rspBaseVector_tup', ' East North Up')
S8960rspBaseVector_bin = '=ddd'
# Provides RTK Base Info
S8960rsp_tup = namedtuple('S8960rsp_tup', ' BaseId, BaseName BaseFlags DistToBase BaseVector')
S8960rsp_bin = '=H9sLd?B'
# Provides status of managed RTK radio (if any)
S897000rsp_tup = namedtuple('S897000rsp_tup', ' ConnectionStatus Location Type')
S897000rsp_bin = '=BBB'
# 
S8961rspBasePosition_tup = namedtuple('S8961rspBasePosition_tup', ' x y z')
S8961rspBasePosition_bin = '=ddd'
# Provides CMR Info
S8961rsp_tup = namedtuple('S8961rsp_tup', ' CMRId ConnectionTime BasePosition')
S8961rsp_bin = '=HL?B'
# Provides information on the overall disturbance level of the ionosphere
S8962rsp_tup = namedtuple('S8962rsp_tup', ' DisturbanceInfoSource GeofenceActive AmplitudeDisturbance PhaseDisturbance GradientLevel FeatureAllowed')
S8962rsp_bin = '=BBfffB'
# Provides identity of managed RTK radio (if any)
S897001rsp_tup = namedtuple('S897001rsp_tup', ', Product, Version, Date, SerialNumber')
S897001rsp_bin = '=21s21s21s31s'
# Provides capabilities of managed RTK radio (if any)
S897002rsp_tup = namedtuple('S897002rsp_tup', ' CapabilityFlags NumModes SupportedModes NumSingleFreqHops NumCountries SupportedCountries')
S897002rsp_bin = '=BB?BbB?B'
# Provides country info for managed RTK radio (if any)
S897003rsp_tup = namedtuple('S897003rsp_tup', ' Type Code Flags')
S897003rsp_bin = '=bBB'
# Provides config specific to 900MHz RTK radio (if any)
S897004rsp_tup = namedtuple('S897004rsp_tup', ' NetworkId')
S897004rsp_bin = '=B'
# Info for a single channel
S897005rspChannelInfo_tup = namedtuple('S897005rspChannelInfo_tup', ' Id Freq')
S897005rspChannelInfo_bin = '=BL'
# Describes allowed freq range and spacing
S897005rspBanding_tup = namedtuple('S897005rspBanding_tup', ' MinFreq MaxFreq ChannelSpacing')
S897005rspBanding_bin = '=LLL'
# Provides config specific to 450MHz RTK radio (if any)
S897005rsp_tup = namedtuple('S897005rsp_tup', ' ChannelId NumChannels ChannelArray Mode Banding')
S897005rsp_bin = '=BB?S897005rspChannelInfoB?B'
# Acknowledges command to set country code
S897006ack_tup = namedtuple('S897006ack_tup', ' Result')
S897006ack_bin = '=B'
# Acknowledges command to set 900MHz network ID
S897007ack_tup = namedtuple('S897007ack_tup', ' Result')
S897007ack_bin = '=B'
# Acknowledges command to set 450MHz channel ID
S897008ack_tup = namedtuple('S897008ack_tup', ' Result')
S897008ack_bin = '=B'
# Acknowledges command to set 450MHz channel frequency
S897009ack_tup = namedtuple('S897009ack_tup', ' Result')
S897009ack_bin = '=B'
# Acknowledges command to set 450MHz mode
S89700aack_tup = namedtuple('S89700aack_tup', ' Result')
S89700aack_bin = '=B'
# Acknowledges command to restart RTK radio
S89700back_tup = namedtuple('S89700back_tup', ' Result')
S89700back_bin = '=B'
# Acknowledges command to set RTK radio channel bandwidth
S89700cack_tup = namedtuple('S89700cack_tup', ' Result')
S89700cack_bin = '=B'
# Provides RTK radio channel bandwidth info
S89700drsp_tup = namedtuple('S89700drsp_tup', ' Bandwidth')
S89700drsp_bin = '=B'
# For the designated source, retrieve the X, Y, and Z offset values in Fallback RTX. Request packet is 0x69 0x71 0x0. No longer supported, do not use. Packet will always return manual source, and an invalid offset with all zeros
S897100rsp_tup = namedtuple('S897100rsp_tup', ' RTXOffsetSource OffsetValid RTXOffsetBaseId XOffsetValue YOffsetValue ZOffsetValue')
S897100rsp_bin = '=BBBddd'
# Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Result will always be failure.
S897100ack_tup = namedtuple('S897100ack_tup', ' Result')
S897100ack_bin = '=B'
# Reports Fallback RTX mode. Request packet is 0x69 0x71 0x02. No longer supported, do not use. It will always return UnknownMode and manual status.
S897101rsp_tup = namedtuple('S897101rsp_tup', ' FallbackMode RTXOffsetSource ActivateFallbackStatus')
S897101rsp_bin = '=BBB'
# Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Will always return failure.
S897101ack_tup = namedtuple('S897101ack_tup', ' Result')
S897101ack_bin = '=B'
# Reports xFill Premium Status. Request packet is 0x69 0x71 0x03.
S897103rsp_tup = namedtuple('S897103rsp_tup', ' xFillStatus xFillTimeRemaining xFillCorrectionAge ScintillationSwitchRule ActivateHour ActivateMinute DeactivateHour DeactivateMinute xFillPremiumStatus IsForceActivated IsUserActivated IsSubscrValid IsBaseStnPosRecv AreOffsetsAvailable IsConverged HorizErrorEstimate xFillPremiumProgressToReady ManualScintSwitchStatus xFillCorrectionAgeNotActive')
S897103rsp_bin = '=BhhBBBBBBBBBBBBffBh'
# Acknowledges command to set xFill Premium Configuration. Ack is sent in response to 0x69 0x71 0x03
S897103ack_tup = namedtuple('S897103ack_tup', ' Result')
S897103ack_bin = '=B'
# 
S8f7brspBoilerPlate_tup = namedtuple('S8f7brspBoilerPlate_tup', ', SerialNumber, PartNumber, OverrideName, BriefOverrideName ManufactureDay ManufactureMonth ManufactureYear SuperPacketPP')
S8f7brspBoilerPlate_bin = '=22s10s17s6sBBHH'
# 
S8f7brspRxDef_tup = namedtuple('S8f7brspRxDef_tup', ' ProductId CarrierPhaseOption BeaconOption RefStationOption EverestOption ModemControlOption DESubscriptionWeek LBandProviders HardwareType VRSProcessingOption FirmwareNotInstalled DisabledStreamsOption TiltSensorOption GPSDisabledOption WAASOption MaxPosRateOption CMRInputOption PointLineAreaLoggingOption CANSelfAddressingOption CANDisabledOption AgLeaderVariant TNLSubscriptionWeek AntennaGain RTKOption BrandingDisabledOption PrototypeHardware DefDGPSSource')
S8f7brspRxDef_bin = '=BBBBBBHBBBBBBBBBBBBBBHfBBBB'
# 
S8f7brspFixedDef_tup = namedtuple('S8f7brspFixedDef_tup', ' BoilerPlate RxDef')
S8f7brspFixedDef_bin = '=?B?B'
# 
S8f7brspPortConfig_tup = namedtuple('S8f7brspPortConfig_tup', ' InProtocol OutProtocol InBaudRate OutBaudRate Parity DataBits StopBits FlowControl')
S8f7brspPortConfig_bin = '=BBBBBBBB'
# 
S8f7brspUserDef_tup = namedtuple('S8f7brspUserDef_tup', ', PortConfig PVFilterFlags ExtRTCMTimeout Guidance Language DistanceDisplayUnits DisplayContrast SNRDisplayUnits')
S8f7brspUserDef_bin = '=3?S8f7brspPortConfigBBBBBBB'
# 
S8f7brspConfigBlockV3_tup = namedtuple('S8f7brspConfigBlockV3_tup', ' Head CfgBlkVersion StartupCount FixedDef UserDef Tail RxCfgChecksum')
S8f7brspConfigBlockV3_bin = '=BBB?B?BHH'
# The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C.
S8f7brsp_tup = namedtuple('S8f7brsp_tup', ' PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3')
S8f7brsp_bin = '=B20sBBBBB?B'
# sent to acknowledge Command Packet 0x8E 0x7C
S8f7cack_tup = namedtuple('S8f7cack_tup', '')
S8f7cack_bin = '='
# This packet is used to obtain information about the current DGPS service provider. Due to operational differences among the service providers, the decoder state and access information is interpreted slightly differently for each service provider. Racal Service - At all times, the user access information accurately reflects the current access state, where &#8220;Access information available&#8221; indicates that no access information has been received yet. The initial confirmation of user access typically occurs after decoder initialization is complete. Omnistar Service - Once the initialization sequence is complete, the user access information is valid. Before initialization is completed, the access may not accurately reflect the final access state. To help determine whether the user access will become enabled when initialization is complete, the user may wish to look at the activation stop date provided by Report Packet 0x8F 0x8B. If the activation stop date is a future date, user access will become enabled when initialization is completed.
S8f80rsp_tup = namedtuple('S8f80rsp_tup', ' UserAccess UserIDCode FirmwareVersion DecoderState ServiceProvider ErrorsWarnings Reserved')
S8f80rsp_bin = '=BlfBBHB'
# Acknowledges the start and stop of satellite FFT diagnostics.
S8f84ack_tup = namedtuple('S8f84ack_tup', '')
S8f84ack_bin = '='
# Channel data
S8f85rspChannelDataBlock_tup = namedtuple('S8f85rspChannelDataBlock_tup', ' Frequency AcquisitionMode Status RTCMUsed SNR InputLevel BitRate LockIndicator CarrierOffset TimeSinceSynch WordErrorRate_TimeSinceRTCM HealthStatus DGPSAutoSwitchingEnabled NegativeSatelliteWordPolarity SatelliteServiceId')
S8f85rspChannelDataBlock_bin = '=dBBBBBBBlBBBBBH'
# This packet is used to convey the DGPS tracking status for either beacon or satellite differential signals. Some fields have duplicate meanings depending on the Acquisition Mode (beacon or satellite). In addition, channels with Acquisition Mode 255 (Unused), should be ignored. For backwards compatibility, a minimum of two channels of data is always reported, but in a dual DSP receiver such as NH134, three channels of data may be reported. In this case, the channel block (bytes 3&#8211;32) will be repeated a third time for the third channel data. The value in byte 2 indicates how many blocks of channel data are provided in the packet with a minimum of 2 data blocks. If byte 2 is set to zero (backwards compatibility), 2 channels of data will be sent.
S8f85rsp_tup = namedtuple('S8f85rsp_tup', ' NumChannels ChannelDataArray')
S8f85rsp_bin = '=B?S8f85rspChannelDataBlock'
# Indicates current DGPS source and related settings.
S8f89rsp_tup = namedtuple('S8f89rsp_tup', ' DGPSSrcMode BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout CorrectionOptions SatConfigSource')
S8f89rsp_bin = '=BBHHHdfHHBB'
# Acknowledges DGPS source control command.
S8f89ack_tup = namedtuple('S8f89ack_tup', '')
S8f89ack_bin = '='
# Brief information about service provider activation.
S8f8brsp_tup = namedtuple('S8f8brsp_tup', ' ServiceProvider, ActivationCode ActivationMonth ActivationDay ActivationYear DeactivationMonth DeactivationDay DeactivationYear InfoType ElapsedTime')
S8f8brsp_bin = '=B24?BBBBBBBBl'
# Report Packet 0x8F 0x8F is sent when the receiver is powered on and can be sent in response to Command Packet 0x8E 0x8F. The packet indicates the type of receiver and why the receiver restarted if an error caused the receiver to reset.
S8f8frsp_tup = namedtuple('S8f8frsp_tup', ' MachineID ProductID RestartCode')
S8f8frsp_bin = '=BBL'
# Return the guidance configuration information
S8f91rsp_tup = namedtuple('S8f91rsp_tup', ' Units DisplayMode Headland Pattern LookAhead SwathDirection SwathWidth AntennaOffset OutputRate SwathsToSkip')
S8f91rsp_bin = '=BBBBhBffLH'
# Return Guidance Configuration Information
S8f91ack_tup = namedtuple('S8f91ack_tup', '')
S8f91ack_bin = '='
# Sent in response to a File Transfer Listing Request, one for each entry in the directory requested.
S8f931500rsp_tup = namedtuple('S8f931500rsp_tup', ' EntryIndex NumEntries, FilenameLength, Filename')
S8f931500rsp_bin = '=BBB*'
# Info for transfer sent in response to File Transfer Get - Open Request.
S8f93150100rsp_tup = namedtuple('S8f93150100rsp_tup', ' FileId TotalSize, FilenameLength, Filename')
S8f93150100rsp_bin = '=LLB*'
# Block of file data sent in response to File Transfer Get - Data Block Request.
S8f93150101rsp_tup = namedtuple('S8f93150101rsp_tup', ' FileId Offset Size, DataBlockLength, DataBlock')
S8f93150101rsp_bin = '=LLBB*'
# Confirms that requested file has been closed, sent in response to File Transfer Get - Close Request.
S8f93150102rsp_tup = namedtuple('S8f93150102rsp_tup', ' FileId')
S8f93150102rsp_bin = '=L'
# Indicates error that caused request to fail.
S8f93150103rsp_tup = namedtuple('S8f93150103rsp_tup', ' FileId ErrorCode')
S8f93150103rsp_bin = '=LB'
# Hash of the requested file in the fusion file system.
S8f93150104rsp_tup = namedtuple('S8f93150104rsp_tup', ' Result Algorithm HashLength Hash, FilenameLength, Filename')
S8f93150104rsp_bin = '=BBB?BB*'
# Info for transfer sent in response to File Transfer Put - Open Request.
S8f93150200rsp_tup = namedtuple('S8f93150200rsp_tup', ' FileId TotalSize, FilenameLength, Filename')
S8f93150200rsp_bin = '=LLB*'
# Indicates successful file write in response to File Transfer Put - Data Block Request.
S8f93150201rsp_tup = namedtuple('S8f93150201rsp_tup', ' FileId Offset Size')
S8f93150201rsp_bin = '=LLB'
# Confirms that requested file has been closed, sent in response to File Transfer Put - Close Request.
S8f93150202rsp_tup = namedtuple('S8f93150202rsp_tup', ' FileId')
S8f93150202rsp_bin = '=L'
# Indicates error that caused request to fail.
S8f93150203rsp_tup = namedtuple('S8f93150203rsp_tup', ' FileId ErrorCode')
S8f93150203rsp_bin = '=LB'
# Indicates status of file delete, sent in response to File Transfer Delete Request.
S8f931503rsp_tup = namedtuple('S8f931503rsp_tup', ' StatusCode, FilenameLength, Filename')
S8f931503rsp_bin = '=BB*'
# Report Packet 0x8F 0x9A contains information about the last differential correction set that was received and used by the receiver.
S8f9arsp_tup = namedtuple('S8f9arsp_tup', ' DataSource StationID Age PartialFlag Reserved1 Reserved2 RTKFlags')
S8f9arsp_bin = '=HhdBBBH'
# Reports the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be reported.
S8f9ersp_tup = namedtuple('S8f9ersp_tup', ' NumSources SourceInfoArray')
S8f9ersp_bin = '=B?'
# Generic acknowledgement of packet receipt.
S8frsp_tup = namedtuple('S8frsp_tup', '')
S8frsp_bin = '='
# 
S8fa0rsp_tup = namedtuple('S8fa0rsp_tup', ' UpgradeResultFlag, Message')
S8fa0rsp_bin = '=B33s'
# Reports additional information about the current generated position solution. It is sent once in response to a query packet Command Packet 0x8E 0xA2, or automatically if configured using Command Packet 0x6A 0x01.
S8fa2rsp_tup = namedtuple('S8fa2rsp_tup', ' PositionQuality PositionType StationId NumSvs SolutionFlags XFillTimeLeft')
S8fa2rsp_bin = '=BBhBBH'
# The version of the Omnistar XP/HP engine
S8fa300rsp_tup = namedtuple('S8fa300rsp_tup', ', Version')
S8fa300rsp_bin = '=33s'
# The subscription information for the Omnistar XP/HP service
S8fa301rsp_tup = namedtuple('S8fa301rsp_tup', ' StartTime ExpirationTime HourGlass SubscribedMode CurrentMode')
S8fa301rsp_bin = '=LLLll'
# Status information on the current state of the Omnistar XP/HP engine
S8fa302rsp_tup = namedtuple('S8fa302rsp_tup', ' EngineStatus SolutionStatus CorrectionAge EstimatedError AutoseedStatus PositionType GlobalStationId NumStations StationIds')
S8fa302rsp_bin = '=HBffBBlB?l'
# Base station information
S8fa303rspStationInfo_tup = namedtuple('S8fa303rspStationInfo_tup', ' StationId, StationName')
S8fa303rspStationInfo_bin = '=l13s'
# The base stations currently used by the Omnistar XP/HP engine
S8fa303rsp_tup = namedtuple('S8fa303rsp_tup', ' NumStations StationInfoArray')
S8fa303rsp_bin = '=B?S8fa303rspStationInfo'
# Provides information about the current Auto-Seed information held by the receiver. If Auto-Seed functionality is on in the receiver, these values would be used at startup if the receiver was rebooted at this point in time.
S8fa304rsp_tup = namedtuple('S8fa304rsp_tup', ' Confidence Latitude Longitude Height LatitudeVariance LongitudeVariance HeightVariance')
S8fa304rsp_bin = '=fdddfff'
# Provides infomration about the control parameters of the Omnistar XP/HP processor
S8fa305rsp_tup = namedtuple('S8fa305rsp_tup', ' ValidFields SeedOnStartup ConfidenceThreshold VelocityThreshold ConvergenceThreshold StaticConvergence SourceSelector')
S8fa305rsp_bin = '=HBfffBB'
# Provides information about the debugging output of the XP/HP processor
S8fa306rsp_tup = namedtuple('S8fa306rsp_tup', ' Enabled Port')
S8fa306rsp_bin = '=BB'
# Acknowledgment that the XP/HP engine was reset
S8fa307ack_tup = namedtuple('S8fa307ack_tup', '')
S8fa307ack_bin = '='
# Reports Quadratic Bias Filter configuration in response to packet 0x8E 0xA4 0x05.
S8fa405rsp_tup = namedtuple('S8fa405rsp_tup', ' Time Depth MaxPropagationTime State')
S8fa405rsp_bin = '=fffB'
# Reports Kalman Filter configuration in response to packet 0x8E 0xA4 0x06.
S8fa406rsp_tup = namedtuple('S8fa406rsp_tup', ' MaxPropagationTime SpeedSetting State')
S8fa406rsp_bin = '=fBB'
# Reports the current status of Field Level Smoothing. Request Packet: 0x8e 0xa4 0x07
S8fa407rsp_tup = namedtuple('S8fa407rsp_tup', ' EnableStatus')
S8fa407rsp_bin = '=B'
# Information for a particular SBAS satellite
S8fa500rspSBASInfo_tup = namedtuple('S8fa500rspSBASInfo_tup', ' PRN Flags')
S8fa500rspSBASInfo_bin = '=BB'
# Reports the current SBAS settings. This packet can contain a variable number of SBAS SV entries. The request or command packet used to trigger the report will determine the number of entries. A 0x8EA500 request will generate a report for all SVs. A 0x8EA500 command will generate a report for those SVs listed in the command.
S8fa500rsp_tup = namedtuple('S8fa500rsp_tup', ' NumSvs SBASInfoArray')
S8fa500rsp_bin = '=B?S8fa500rspSBASInfo'
# Reports the current SBAS+ settings. Request packet is 0x8E 0xA5 0x01
S8fa501rsp_tup = namedtuple('S8fa501rsp_tup', ' EnableSBASPlus')
S8fa501rsp_bin = '=B'
# Acks SBAS Default Constellation Reset Command 
S8fa502ack_tup = namedtuple('S8fa502ack_tup', '')
S8fa502ack_bin = '='
# Acknowledges the Set External Output Pin state cmd.
S8fa601ack_tup = namedtuple('S8fa601ack_tup', ' Result')
S8fa601ack_bin = '=B'
# Responds with the state of the external input pins.
S8fa602rsp_tup = namedtuple('S8fa602rsp_tup', ' Result NumValidExtInputPins, ExternalInputs')
S8fa602rsp_bin = '=BB17?B'
# Provides the manufacturing information of the unit.
S8fa608rsp_tup = namedtuple('S8fa608rsp_tup', ' Result, SerialNumber UniqueId MfgDay MfgMonth MfgYear VersionMajor VersionMinor VersionBuild VersionType')
S8fa608rsp_bin = '=B16sLBBHBBHB'
# Provides the Omnistar Id for the unit.
S8fa617rsp_tup = namedtuple('S8fa617rsp_tup', ' Result, OmnistarId')
S8fa617rsp_bin = '=B20s'
# Provides MAC addresses (4 max) for the unit.
S8fa622rsp_tup = namedtuple('S8fa622rsp_tup', ' MacCount Mac1Type, Mac1Addr Mac2ype, Mac2Addr Mac3Type, Mac3Addr Mac4Type, Mac4Addr')
S8fa622rsp_bin = '=BB6?BB6?BB6?BB6?B'
# Provides the alternate unique ID for the unit.
S8fa623rsp_tup = namedtuple('S8fa623rsp_tup', ' IdSize, AltUniqueIdField')
S8fa623rsp_bin = '=B20?B'
# Provides unit's extended manufacturing information.
S8fa624rsp_tup = namedtuple('S8fa624rsp_tup', ', ModuleSN, FactoryID')
S8fa624rsp_bin = '=16s20s'
# Acks extended manufacturing information cmd.
S8fa625ack_tup = namedtuple('S8fa625ack_tup', '')
S8fa625ack_bin = '='
# Provides unit's product information.
S8fa626rsp_tup = namedtuple('S8fa626rsp_tup', ', PartNumber, Name, AbbrevName')
S8fa626rsp_bin = '=20s18s6s'
# Acks product information cmd.
S8fa627ack_tup = namedtuple('S8fa627ack_tup', '')
S8fa627ack_bin = '='
# If received,receiver is now in manufacturing test mode.
S8fa628ack_tup = namedtuple('S8fa628ack_tup', ' Result')
S8fa628ack_bin = '=B'
# Responds with the signature at the given offset
S8fa629rsp_tup = namedtuple('S8fa629rsp_tup', ' offset, signature')
S8fa629rsp_bin = '=L32?B'
# Response containing the peak FFT frequency and SNR from the RF spectrum analyzer for GNSS bands. Intended for factory test use only.
S8fa630rsp_tup = namedtuple('S8fa630rsp_tup', ' Result RFBand FilteredPeakFrequency FilteredPeakSNR UnfilteredPeakFrequency UnfilteredPeakSNR')
S8fa630rsp_bin = '=BBdfdf'
# Response containing metadata about the condition of MSS tracking
S8fa631rsp_tup = namedtuple('S8fa631rsp_tup', ' Result MSSPeakFrequency PeakADCSignalLevel MaxMSSADCSignalLevel MinMSSADCSignalLevel MSSAGCGainLevelPercent MSSAGCGainLevelDb')
S8fa631rsp_bin = '=BdfHHff'
# Result of a register read operation to a specific polaris device
S8fa632rsp_tup = namedtuple('S8fa632rsp_tup', ' Result AntennaId PolarisI2CAddr PolarisRegAddr Value')
S8fa632rsp_bin = '=BBBBB'
# Requests a register read operation to a specific polaris device
S8fa632ack_tup = namedtuple('S8fa632ack_tup', ' Result AntennaId PolarisI2CAddr PolarisRegAddr')
S8fa632ack_bin = '=BBBB'
# Result of a RSSI ADC value read operation to a specific polaris device
S8fa633rsp_tup = namedtuple('S8fa633rsp_tup', ' Result AntennaId RFBand RSSIADCValue')
S8fa633rsp_bin = '=BBBd'
# Acknowledges the test request to perform the Polaris full AGC test. If accepted, the receiver will start the test, and then send the 0x8f 0xa6 0x34 response when the test completes. If there is a problem starting the test, the response will be returned in the result field.
S8fa634ack_tup = namedtuple('S8fa634ack_tup', ' Result')
S8fa634ack_bin = '=B'
# Information for a single Antenna+RF Band+Histogram Bank
S8fa634rspBandResult_tup = namedtuple('S8fa634rspBandResult_tup', ' AntennaId BankId RFBand DacReadIMPct DacReadQMPct DacReadISPct DacReadQSPct')
S8fa634rspBandResult_bin = '=BBBffff'
# Response containing the results of the Polaris Full AGC test. Intended for factory test use only.
S8fa634rsp_tup = namedtuple('S8fa634rsp_tup', ' BandsPresent BandResultArray FrequencyOffset')
S8fa634rsp_bin = '=B?S8fa634rspBandResultd'
# Acknowledges the command to enable the PLT Mode for WiFi testing.
S8fa640ack_tup = namedtuple('S8fa640ack_tup', ' Result ErrorCode')
S8fa640ack_bin = '=BB'
# Acknowledges the command to disable the PLT Mode for WiFi testing.
S8fa641ack_tup = namedtuple('S8fa641ack_tup', ' Result ErrorCode')
S8fa641ack_bin = '=BB'
# Acknowledges the command to configure the device to operate in a specific WiFi band and channel.
S8fa642ack_tup = namedtuple('S8fa642ack_tup', ' Result ErrorCode')
S8fa642ack_bin = '=BB'
# Acknowledges the command to set the transmission power of the WL18xx device.
S8fa643ack_tup = namedtuple('S8fa643ack_tup', ' Result ErrorCode')
S8fa643ack_bin = '=BB'
# Acknowledges the command to enable TX test using the start_tx command.
S8fa644ack_tup = namedtuple('S8fa644ack_tup', ' Result ErrorCode')
S8fa644ack_bin = '=BB'
# Acknowledges the command to disable TX test using the stop_tx command.
S8fa645ack_tup = namedtuple('S8fa645ack_tup', ' Result ErrorCode')
S8fa645ack_bin = '=BB'
# Acknowledges the command to start the RX statistics.
S8fa646ack_tup = namedtuple('S8fa646ack_tup', ' Result ErrorCode')
S8fa646ack_bin = '=BB'
# Response containing the RX statistics.
S8fa647rsp_tup = namedtuple('S8fa647rsp_tup', ' Result ErrorCode RXStatsStatus TotalPackets FCSErrors MACMismatch GoodPackets AvgRSSI_SOC AvgRSSI_ANT PER')
S8fa647rsp_bin = '=BBBLLLLhhf'
# Acknowledges the command to stop the RX statistics.
S8fa648ack_tup = namedtuple('S8fa648ack_tup', ' Result ErrorCode')
S8fa648ack_bin = '=BB'
# Acknowledges when the remote display is enabled or disabled, or when a key press message is received.
S8f8cack_tup = namedtuple('S8f8cack_tup', '')
S8f8cack_bin = '='
# Reports the data currently appearing on the display in ASCII format (except for a few special characters) and the cursor position and mode. This packet can be requested for a single output using Command Packet 0x8E 0x8C 0x01 or it can be configured to be output automatically whenever the screen contents changes using Command Packet 0x8E 0x8C 0x03.
S8f8c01rsp_tup = namedtuple('S8f8c01rsp_tup', ' CursorX CursorY CursorMode LineNumber, LineContents Flags')
S8f8c01rsp_bin = '=BBBB17sB'
# Sent by the receiver to control the state of a remote output line, i.e. an alarm. It is sent automatically if the receiver has been configured to drive output lines. For example, the PSO interface allows the user to set criteria for tripping an audible alarm. To control the output line to this alarm remotely (i.e. the output line is not directly connected to the receiver), this packet is sent.
S8f8c02rsp_tup = namedtuple('S8f8c02rsp_tup', ' SetHiMask SetLowMask')
S8f8c02rsp_bin = '=LL'
# Shows the receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03.
S8f8c03rsp_tup = namedtuple('S8f8c03rsp_tup', ' DataLocation')
S8f8c03rsp_bin = '=B'
# Shows the extended receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. This packet includes a text description of what kind of receiver it is, i.e. Ag132, Ag124, etc. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03.
S8f8c04rsp_tup = namedtuple('S8f8c04rsp_tup', ' DataLocation, RemoteId')
S8f8c04rsp_bin = '=B6s'
# Complete measurement report for the L1 GPS frequency
S6f01rsp_tup = namedtuple('S6f01rsp_tup', '')
S6f01rsp_bin = '='
# Complete measurement report for the L2 GPS frequency
S6f10rsp_tup = namedtuple('S6f10rsp_tup', '')
S6f10rsp_bin = '='
# epoch header for the GNSS T01 type 27 style packet
S6f20rsp_tup = namedtuple('S6f20rsp_tup', ' WeekNumber ReceiveTime ClockOffset SVCount MsgCount EpochFlags1 EpochFlags2 GlonassClockOffset RAIMInfo')
S6f20rsp_bin = '=HdfBBBBfB'
# These are the measurement blocks for the GNSS T01 type 27 style packet. Each packet contains up to 6 SVs with each of their submeas (l1, l2, etc.)
S6f21rsp_tup = namedtuple('S6f21rsp_tup', ' PacketLength MeasurementNumber GpsTime NumSVs, PayloadLength, Payload')
S6f21rsp_bin = '=hBdBB*'
# Indicates current state of automatic position sigma reporting
S8b00rsp_tup = namedtuple('S8b00rsp_tup', ' OutputsEnabled')
S8b00rsp_bin = '=B'
# Single position sigma (error) information report
S8b02rsp_tup = namedtuple('S8b02rsp_tup', ' TimeOfFix DataValid RMS SigmaEast SigmaNorth CovEN SigmaUp AxesValid SemiMajorAxis SemiMinorAxis Orientation UnitVariance NumEpochs DOF')
S8b02rsp_bin = '=LBfffffBffffHH'
# Reports primary receiver configuration parameters in response to Command Packet 0xBB 0x00.
Sbb00rsp_tup = namedtuple('Sbb00rsp_tup', ' OperatingDimension DGPSMode DynamicsCode SolutionMode ElevetionMask AMUMask PDOP PDOPSwitch DGPSAgeLimit FoliageMode LowPowerMode ClockHoldMode MeasurementRate PosFixRate')
Sbb00rsp_bin = '=BBBBffffBBBBBB'
# 
S8f7frspBoilerPlate_tup = namedtuple('S8f7frspBoilerPlate_tup', ', SerialNumber, PartNumber, OverrideName, BriefOverrideName ManufactureDay ManufactureMonth ManufactureYear SuperPacketPP')
S8f7frspBoilerPlate_bin = '=22s10s17s6sBBHH'
# 
S8f7frspRxDef_tup = namedtuple('S8f7frspRxDef_tup', ' ProductId CarrierPhaseOption BeaconOption RefStationOption EverestOption ModemControlOption DESubscriptionWeek LBandProviders HardwareType VRSProcessingOption FirmwareNotInstalled DisabledStreamsOption TiltSensorOption GPSDisabledOption WAASOption MaxPosRateOption CMRInputOption PointLineAreaLoggingOption CANSelfAddressingOption CANDisabledOption AgLeaderVariant TNLSubscriptionWeek AntennaGain RTKOption BrandingDisabledOption PrototypeHardware DefDGPSSource')
S8f7frspRxDef_bin = '=BBBBBBHBBBBBBBBBBBBBBHfBBBB'
# 
S8f7frspFixedDef_tup = namedtuple('S8f7frspFixedDef_tup', ' BoilerPlate RxDef')
S8f7frspFixedDef_bin = '=?B?B'
# 
S8f7frspPortConfig_tup = namedtuple('S8f7frspPortConfig_tup', ' InProtocol OutProtocol InBaudRate OutBaudRate Parity DataBits StopBits FlowControl')
S8f7frspPortConfig_bin = '=BBBBBBBB'
# 
S8f7frspUserDef_tup = namedtuple('S8f7frspUserDef_tup', ', PortConfig PVFilterFlags ExtRTCMTimeout Guidance Language DistanceDisplayUnits DisplayContrast SNRDisplayUnits')
S8f7frspUserDef_bin = '=3?S8f7frspPortConfigBBBBBBB'
# 
S8f7frspConfigBlockV3_tup = namedtuple('S8f7frspConfigBlockV3_tup', ' Head CfgBlkVersion StartupCount FixedDef UserDef Tail RxCfgChecksum')
S8f7frspConfigBlockV3_bin = '=BBB?B?BHH'
# The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C.
S8f7frsp_tup = namedtuple('S8f7frsp_tup', ' PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3')
S8f7frsp_bin = '=B20sBBBBB?B'
# Holds the configuration of a particular serial port. This includes the port settings and input and output protocols.
Sbcrsp_tup = namedtuple('Sbcrsp_tup', ' Port InputBaudRate OutputBaudRate DataBits Parity StopBits FlowControl InputProtocol OutputProtocol ProtocolOperation')
Sbcrsp_bin = '=BBBBBBBBBB'
# Report Packet 0x8F 0x77 is generated after Command Packet 0x8E 0x75 is acknowledged with Report Packet 0x8F 0x75. The receiver performs a 1024-point Fast Fourier Transform (FFT) by the number of times specified by the Number of Integrations parameter in Command Packet 0x8E 0x75. Once the FFT report is completed, the receiver begins the next FFT. The FFT reports are generated and sent continuously until the FFT Stop Command (Command Packet 0x8E 0x76) is issued. Because the amount of data contained in the FFT report exceeds 123 bytes, the report is divided into multiple packets (pages). Even if all data bytes are DLEs (which would transmit 2 TSIP bytes for each data byte), the message structure does not overflow the 255 byte TSIP buffer length.
S8f770rsp_tup = namedtuple('S8f770rsp_tup', ' Frequency BinSize InputSquared NumIntegrations NumBins MaxLevel, Sample')
S8f770rsp_bin = '=ddBBHf99?B'
# Sample data for the fft report
S8f77rsp_tup = namedtuple('S8f77rsp_tup', ' PageId, SampleLength, Sample')
S8f77rsp_bin = '=BB*'
# State of TSIP diagnostics output
S5f02rsp_tup = namedtuple('S5f02rsp_tup', ' DiagnosticsEnabled')
S5f02rsp_bin = '=B'
# Diagnostic message output from the receiver
S5f01rsp_tup = namedtuple('S5f01rsp_tup', ', DiagMsgLength, DiagMsg')
S5f01rsp_bin = '=B*'
# Diagnostic data output from the receiver
S5f10rsp_tup = namedtuple('S5f10rsp_tup', ', DiagDataLength, DiagData')
S5f10rsp_bin = '=B*'
# Retrieve the mask used to output Diagnostic data from the receiver
S5f2200rsp_tup = namedtuple('S5f2200rsp_tup', ' Mask')
S5f2200rsp_bin = '=L'
# Diagnostic data output from the receiver
S5f2201rsp_tup = namedtuple('S5f2201rsp_tup', ' Type Time, MsgLength, Msg')
S5f2201rsp_bin = '=BdB*'
# Debugging message output from the receiver
S8f9306rsp_tup = namedtuple('S8f9306rsp_tup', ' Length DebugMsg')
S8f9306rsp_bin = '=H?c'
# Configuration packet response from the Autopilot Navigation Controller
Sbf40rsp_tup = namedtuple('Sbf40rsp_tup', ', PacketDataLength, PacketData')
Sbf40rsp_bin = '=B*'
# Requests App Version(?) configuration from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf400000rsp_base = namedtuple('Sbf400000rsp_base', ' Version fw_year fw_month fw_day fw_config fw_released Entry ImageSize Checksum, Name CompressedSize CompressedChecksum beta_expiration ErrorLogStart ErrorLogEnd FFSStart FFSEnd GuidanceStart GuidanceEnd CfgBlkSect1 CfgBlkSect2 AppStorageStart AppStorageEnd MinFailsafeMonVerson CompressedVersionNumber CompressedVersionNumberHash FOOTER, Length')

# Factory function for backward compatibility
def Sbf400000rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf400000rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf400000rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf400000rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf400000rsp_tup._make = lambda seq: Sbf400000rsp_tup(*seq)
Sbf400000rsp_bin = '=HHBBBBLLL8sLLLLLLLLLLLLLHLLL?'
# Requests options configuration from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf400100rsp_base = namedtuple('Sbf400100rsp_base', ', SerialNumber, OptionsLength, Options, Length')

# Factory function for backward compatibility
def Sbf400100rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf400100rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf400100rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf400100rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf400100rsp_tup._make = lambda seq: Sbf400100rsp_tup(*seq)
Sbf400100rsp_bin = '=16sB*?'
# Configuration packet response to get TAP parameter from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf401400rsp_base = namedtuple('Sbf401400rsp_base', ', TAPStringLength, TAPString, Length')

# Factory function for backward compatibility
def Sbf401400rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf401400rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf401400rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf401400rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf401400rsp_tup._make = lambda seq: Sbf401400rsp_tup(*seq)
Sbf401400rsp_bin = '=B*?'
# Configuration packet response from setting a TAP parameter on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf401401rsp_base = namedtuple('Sbf401401rsp_base', ', TAPStringLength, TAPString, Length')

# Factory function for backward compatibility
def Sbf401401rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf401401rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf401401rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf401401rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf401401rsp_tup._make = lambda seq: Sbf401401rsp_tup(*seq)
Sbf401401rsp_bin = '=B*?'
# File Transfer packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf41rsp_base = namedtuple('Sbf41rsp_base', ' FileId CmdId status PacketNumber, PacketDataLength, PacketData, Length')

# Factory function for backward compatibility
def Sbf41rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf41rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf41rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf41rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf41rsp_tup._make = lambda seq: Sbf41rsp_tup(*seq)
Sbf41rsp_bin = '=BBBHB*?'
# Remote Monitor Engineering Data packet response from the Autopilot Navigation Controller
Sbf42rsp_tup = namedtuple('Sbf42rsp_tup', ', PacketDataLength, PacketData')
Sbf42rsp_bin = '=B*'
# Gets status information for navigation
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4201rsp_base = namedtuple('Sbf4201rsp_base', ' PosEast PosNorth Yaw Roll Speed CrossTrackError Range TargetSteeringAngle, Length')

# Factory function for backward compatibility
def Sbf4201rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4201rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4201rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4201rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4201rsp_tup._make = lambda seq: Sbf4201rsp_tup(*seq)
Sbf4201rsp_bin = '=ffffffff?'
# Gets status information for navigation
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4200rsp_base = namedtuple('Sbf4200rsp_base', ' Time State Error UtcOffset, Length')

# Factory function for backward compatibility
def Sbf4200rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4200rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4200rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4200rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4200rsp_tup._make = lambda seq: Sbf4200rsp_tup(*seq)
Sbf4200rsp_bin = '=LBBH?'
# Gets status information for GNSS
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4202rsp_base = namedtuple('Sbf4202rsp_base', ' Seconds Week NumSatelites PosType PpsOccured AntennaPosEast AntennaPosNorth AntennaPosUp VelHoriz Heading PDOP, Length')

# Factory function for backward compatibility
def Sbf4202rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4202rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4202rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4202rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4202rsp_tup._make = lambda seq: Sbf4202rsp_tup(*seq)
Sbf4202rsp_bin = '=LHBBBdddfff?'
# Remote Monitor Control packet response from the Autopilot Navigation Controller
Sbf43rsp_tup = namedtuple('Sbf43rsp_tup', ', PacketDataLength, PacketData')
Sbf43rsp_bin = '=B*'
# Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets autosteering to enabled/disabled
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4301rsp_base = namedtuple('Sbf4301rsp_base', ' EngageState, Length')

# Factory function for backward compatibility
def Sbf4301rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4301rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4301rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4301rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4301rsp_tup._make = lambda seq: Sbf4301rsp_tup(*seq)
Sbf4301rsp_bin = '=B?'
# Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets logging to enabled/disabled
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4303rsp_base = namedtuple('Sbf4303rsp_base', ' LoggingCommand, Length')

# Factory function for backward compatibility
def Sbf4303rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4303rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4303rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4303rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4303rsp_tup._make = lambda seq: Sbf4303rsp_tup(*seq)
Sbf4303rsp_bin = '=B?'
# Remote Monitor Control packet response from the Autopilot Navigation Controller to control Steering/Speed
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4306rsp_base = namedtuple('Sbf4306rsp_base', ' CommandID Command Value, Length')

# Factory function for backward compatibility
def Sbf4306rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4306rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4306rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4306rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4306rsp_tup._make = lambda seq: Sbf4306rsp_tup(*seq)
Sbf4306rsp_bin = '=BBf?'
# Remote Monitor General Data packet response from the Autopilot Navigation Controller
Sbf44rsp_tup = namedtuple('Sbf44rsp_tup', ', PacketDataLength, PacketData')
Sbf44rsp_bin = '=B*'
# Remote Monitor Waypoint Data packet response from the Autopilot Navigation Controller
Sbf45rsp_tup = namedtuple('Sbf45rsp_tup', ', PacketDataLength, PacketData')
Sbf45rsp_bin = '=B*'
# Boot Monitor packet response from the Autopilot Navigation Controller
Sbf46rsp_tup = namedtuple('Sbf46rsp_tup', ', PacketDataLength, PacketData')
Sbf46rsp_bin = '=B*'
# Debug packet response from the Autopilot Navigation Controller
Sbf47rsp_tup = namedtuple('Sbf47rsp_tup', ', PacketDataLength, PacketData')
Sbf47rsp_bin = '=B*'
# Gets the current diagnostic error type from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470500rsp_base = namedtuple('Sbf470500rsp_base', ' ErrorType, Length')

# Factory function for backward compatibility
def Sbf470500rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470500rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470500rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470500rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470500rsp_tup._make = lambda seq: Sbf470500rsp_tup(*seq)
Sbf470500rsp_bin = '=L?'
# Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470501rsp_base = namedtuple('Sbf470501rsp_base', ', Length')

# Factory function for backward compatibility
def Sbf470501rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470501rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470501rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470501rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470501rsp_tup._make = lambda seq: Sbf470501rsp_tup(*seq)
Sbf470501rsp_bin = '=?'
# Gets a diagnostic record item from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470502rsp_base = namedtuple('Sbf470502rsp_base', ' DiagItemId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved, Length')

# Factory function for backward compatibility
def Sbf470502rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470502rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470502rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470502rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470502rsp_tup._make = lambda seq: Sbf470502rsp_tup(*seq)
Sbf470502rsp_bin = '=HLLLHH3?fHH?'
# Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470503rsp_base = namedtuple('Sbf470503rsp_base', ' DiagItemId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved, Length')

# Factory function for backward compatibility
def Sbf470503rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470503rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470503rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470503rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470503rsp_tup._make = lambda seq: Sbf470503rsp_tup(*seq)
Sbf470503rsp_bin = '=HLLLHH3?fHH?'
# Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470504rsp_base = namedtuple('Sbf470504rsp_base', ' ErrorComponentId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved, Length')

# Factory function for backward compatibility
def Sbf470504rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470504rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470504rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470504rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470504rsp_tup._make = lambda seq: Sbf470504rsp_tup(*seq)
Sbf470504rsp_bin = '=HLLLHH3?fHH?'
# Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470505rsp_base = namedtuple('Sbf470505rsp_base', ' MaxErrorTypes, Length')

# Factory function for backward compatibility
def Sbf470505rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470505rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470505rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470505rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470505rsp_tup._make = lambda seq: Sbf470505rsp_tup(*seq)
Sbf470505rsp_bin = '=H?'
# Gets the description of a diagnostic record item from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470506rsp_base = namedtuple('Sbf470506rsp_base', ' DiagItemId, StringLength, String, Length')

# Factory function for backward compatibility
def Sbf470506rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470506rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470506rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470506rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470506rsp_tup._make = lambda seq: Sbf470506rsp_tup(*seq)
Sbf470506rsp_bin = '=HB*?'
# Acknowledge the current warning on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470507rsp_base = namedtuple('Sbf470507rsp_base', ', Length')

# Factory function for backward compatibility
def Sbf470507rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470507rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470507rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470507rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470507rsp_tup._make = lambda seq: Sbf470507rsp_tup(*seq)
Sbf470507rsp_bin = '=?'
# Gets the maximum number of warnings from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470508rsp_base = namedtuple('Sbf470508rsp_base', ' MaxWarnings, Length')

# Factory function for backward compatibility
def Sbf470508rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470508rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470508rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470508rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470508rsp_tup._make = lambda seq: Sbf470508rsp_tup(*seq)
Sbf470508rsp_bin = '=H?'
# Gets the description of a warning from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470509rsp_base = namedtuple('Sbf470509rsp_base', ' WarningId, StringLength, String, Length')

# Factory function for backward compatibility
def Sbf470509rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470509rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470509rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470509rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470509rsp_tup._make = lambda seq: Sbf470509rsp_tup(*seq)
Sbf470509rsp_bin = '=HB*?'
# Gets the maximum number of messages from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf47050arsp_base = namedtuple('Sbf47050arsp_base', ' MaxMessagesCount, Length')

# Factory function for backward compatibility
def Sbf47050arsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf47050arsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf47050arsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf47050arsp_base(*args)

# Add _make method for compatibility with existing code
Sbf47050arsp_tup._make = lambda seq: Sbf47050arsp_tup(*seq)
Sbf47050arsp_bin = '=H?'
# Gets a message description from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf47050brsp_base = namedtuple('Sbf47050brsp_base', ' MessageId, StringLength, String, Length')

# Factory function for backward compatibility
def Sbf47050brsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf47050brsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf47050brsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf47050brsp_base(*args)

# Add _make method for compatibility with existing code
Sbf47050brsp_tup._make = lambda seq: Sbf47050brsp_tup(*seq)
Sbf47050brsp_bin = '=HB*?'
# Gets ADC data from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4707rsp_base = namedtuple('Sbf4707rsp_base', ', HighPrecisionADC, LowPrecisionADC Time, Length')

# Factory function for backward compatibility
def Sbf4707rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4707rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4707rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4707rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4707rsp_tup._make = lambda seq: Sbf4707rsp_tup(*seq)
Sbf4707rsp_bin = '=8?f17?fL?'
# Debug packet response from the Autopilot Navigation Controller. Contains .dbg file header
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470e06rsp_base = namedtuple('Sbf470e06rsp_base', ' PacketCount PacketNumber PacketSize PacketData, Length')

# Factory function for backward compatibility
def Sbf470e06rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470e06rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470e06rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470e06rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470e06rsp_tup._make = lambda seq: Sbf470e06rsp_tup(*seq)
Sbf470e06rsp_bin = '=BBB?c?'
# Debug packet response from the Autopilot Navigation Controller. Contains .dbg file data
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470e07rsp_base = namedtuple('Sbf470e07rsp_base', ' PacketCount PacketNumber PacketSize PacketData, Length')

# Factory function for backward compatibility
def Sbf470e07rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470e07rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470e07rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470e07rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470e07rsp_tup._make = lambda seq: Sbf470e07rsp_tup(*seq)
Sbf470e07rsp_bin = '=BBB?c?'
# Debug packet response from the Autopilot Navigation Controller. Gets current port function
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470e08rsp_base = namedtuple('Sbf470e08rsp_base', ' PortFunctionId, Length')

# Factory function for backward compatibility
def Sbf470e08rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470e08rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470e08rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470e08rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470e08rsp_tup._make = lambda seq: Sbf470e08rsp_tup(*seq)
Sbf470e08rsp_bin = '=L?'
# Debug packet response from the Autopilot Navigation Controller. Sets current port function
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf470e09rsp_base = namedtuple('Sbf470e09rsp_base', ' PortFunctionId, Length')

# Factory function for backward compatibility
def Sbf470e09rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf470e09rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf470e09rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf470e09rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf470e09rsp_tup._make = lambda seq: Sbf470e09rsp_tup(*seq)
Sbf470e09rsp_bin = '=L?'
# Gets number of internal vdb's from the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf471400rsp_base = namedtuple('Sbf471400rsp_base', ' VDBCount, Length')

# Factory function for backward compatibility
def Sbf471400rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf471400rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf471400rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf471400rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf471400rsp_tup._make = lambda seq: Sbf471400rsp_tup(*seq)
Sbf471400rsp_bin = '=L?'
# Gets a vdb record from the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf471401rsp_base = namedtuple('Sbf471401rsp_base', ' VDBIndex, Name, Model, Length')

# Factory function for backward compatibility
def Sbf471401rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf471401rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf471401rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf471401rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf471401rsp_tup._make = lambda seq: Sbf471401rsp_tup(*seq)
Sbf471401rsp_bin = '=H16s16s?'
# Sets the vdb record on the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf471402rsp_base = namedtuple('Sbf471402rsp_base', ' VDBIndex, Name, Model, Length')

# Factory function for backward compatibility
def Sbf471402rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf471402rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf471402rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf471402rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf471402rsp_tup._make = lambda seq: Sbf471402rsp_tup(*seq)
Sbf471402rsp_bin = '=H16s16s?'
# Gets current IMU data from the Autopilot Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf471ersp_base = namedtuple('Sbf471ersp_base', ' RawTimeNSec RawTimeSec RawGyroX RawGyroY RawGyroZ RawAccelX RawAccelY RawAccelZ RawTemp RawVRef ScaledTimeNSec ScaledTimeSec ScaledGyroX ScaledGyroY ScaledGyroZ ScaledAccelX ScaledAccelY ScaledAccelZ ScaledTemp ScaledVRef, Length')

# Factory function for backward compatibility
def Sbf471ersp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf471ersp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf471ersp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf471ersp_base(*args)

# Add _make method for compatibility with existing code
Sbf471ersp_tup._make = lambda seq: Sbf471ersp_tup(*seq)
Sbf471ersp_bin = '=LLffffffffLLffffffff?'
# Calibration packet response from the Autopilot Navigation Controller
Sbf4arsp_tup = namedtuple('Sbf4arsp_tup', ', PacketDataLength, PacketData')
Sbf4arsp_bin = '=B*'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4a0c00rsp_base = namedtuple('Sbf4a0c00rsp_base', ' TestPGain TestDeadzone TestPWM CommandSteeringAngleDegrees MeasuredSteeringAngleDegrees MeasuredSteeringSlewTimeSeconds MeasuredSteeringOvershootPercent, Length')

# Factory function for backward compatibility
def Sbf4a0c00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4a0c00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4a0c00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4a0c00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4a0c00rsp_tup._make = lambda seq: Sbf4a0c00rsp_tup(*seq)
Sbf4a0c00rsp_bin = '=fffffff?'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4a0c08rsp_base = namedtuple('Sbf4a0c08rsp_base', ' PGainState, Length')

# Factory function for backward compatibility
def Sbf4a0c08rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4a0c08rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4a0c08rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4a0c08rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4a0c08rsp_tup._make = lambda seq: Sbf4a0c08rsp_tup(*seq)
Sbf4a0c08rsp_bin = '=B?'
# Steering angle sensor calibration information response
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4a0b00rsp_base = namedtuple('Sbf4a0b00rsp_base', ' AngleRawVoltage AngleScaledDegrees, Length')

# Factory function for backward compatibility
def Sbf4a0b00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4a0b00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4a0b00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4a0b00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4a0b00rsp_tup._make = lambda seq: Sbf4a0b00rsp_tup(*seq)
Sbf4a0b00rsp_bin = '=ff?'
# 
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4a0b01rsp_base = namedtuple('Sbf4a0b01rsp_base', ' Success, Length')

# Factory function for backward compatibility
def Sbf4a0b01rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4a0b01rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4a0b01rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4a0b01rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4a0b01rsp_tup._make = lambda seq: Sbf4a0b01rsp_tup(*seq)
Sbf4a0b01rsp_bin = '=B?'
# Autotester response to the Autopilot Navigation Controller.
Sbf4brsp_tup = namedtuple('Sbf4brsp_tup', ', PacketDataLength, PacketData')
Sbf4brsp_bin = '=B*'
# External Device packet command to read the manual override info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c00000004rsp_base = namedtuple('Sbf4c00000004rsp_base', ' Raw Scaled, Length')

# Factory function for backward compatibility
def Sbf4c00000004rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c00000004rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c00000004rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c00000004rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c00000004rsp_tup._make = lambda seq: Sbf4c00000004rsp_tup(*seq)
Sbf4c00000004rsp_bin = '=fB?'
# External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c00000104rsp_base = namedtuple('Sbf4c00000104rsp_base', ' Raw Scaled, Length')

# Factory function for backward compatibility
def Sbf4c00000104rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c00000104rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c00000104rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c00000104rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c00000104rsp_tup._make = lambda seq: Sbf4c00000104rsp_tup(*seq)
Sbf4c00000104rsp_bin = '=fB?'
# External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c00000204rsp_base = namedtuple('Sbf4c00000204rsp_base', ' Raw Scaled, Length')

# Factory function for backward compatibility
def Sbf4c00000204rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c00000204rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c00000204rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c00000204rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c00000204rsp_tup._make = lambda seq: Sbf4c00000204rsp_tup(*seq)
Sbf4c00000204rsp_bin = '=fB?'
# External Device packet command to read the Gear lever info from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c00000704rsp_base = namedtuple('Sbf4c00000704rsp_base', ' Raw Scaled, Length')

# Factory function for backward compatibility
def Sbf4c00000704rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c00000704rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c00000704rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c00000704rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c00000704rsp_tup._make = lambda seq: Sbf4c00000704rsp_tup(*seq)
Sbf4c00000704rsp_bin = '=fB?'
# Autopilot Field Computer Heartbeat packet response from the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0101rsp_base = namedtuple('Sbf4c0101rsp_base', ' AutosteerVersion AutosteerState APIVersion SystemState WarningState FaultState WarningLevel PositionFixQuality NoAutoAllowed RoadingStatusBits RowGuidanceMode Reserved1, Length')

# Factory function for backward compatibility
def Sbf4c0101rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0101rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0101rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0101rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0101rsp_tup._make = lambda seq: Sbf4c0101rsp_tup(*seq)
Sbf4c0101rsp_bin = '=BBBBBBBBHBBB?'
# External Device packet command to set close any open field
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0108rsp_base = namedtuple('Sbf4c0108rsp_base', ', ImplementWidthLength, ImplementWidth, Length')

# Factory function for backward compatibility
def Sbf4c0108rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0108rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0108rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0108rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0108rsp_tup._make = lambda seq: Sbf4c0108rsp_tup(*seq)
Sbf4c0108rsp_bin = '=B*?'
# External Device packet command to set close any open field
Sbf4c010arsp_tup = namedtuple('Sbf4c010arsp_tup', ' Result')
Sbf4c010arsp_bin = '=B'
# External Device packet Control State
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c010brsp_base = namedtuple('Sbf4c010brsp_base', ' ControlState, MiscDataLength, MiscData, Length')

# Factory function for backward compatibility
def Sbf4c010brsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c010brsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c010brsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c010brsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c010brsp_tup._make = lambda seq: Sbf4c010brsp_tup(*seq)
Sbf4c010brsp_bin = '=BB*?'
# External Device packet response with Aggressiveness
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c010drsp_base = namedtuple('Sbf4c010drsp_base', ' Aggressiveness, Length')

# Factory function for backward compatibility
def Sbf4c010drsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c010drsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c010drsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c010drsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c010drsp_tup._make = lambda seq: Sbf4c010drsp_tup(*seq)
Sbf4c010drsp_bin = '=B?'
# External Device packet response with Task Delay
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c010ersp_base = namedtuple('Sbf4c010ersp_base', ' TaskDelay, Length')

# Factory function for backward compatibility
def Sbf4c010ersp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c010ersp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c010ersp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c010ersp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c010ersp_tup._make = lambda seq: Sbf4c010ersp_tup(*seq)
Sbf4c010ersp_bin = '=H?'
# External Device packet response with Fix Quality
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c010frsp_base = namedtuple('Sbf4c010frsp_base', ' FixQuality, Length')

# Factory function for backward compatibility
def Sbf4c010frsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c010frsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c010frsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c010frsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c010frsp_tup._make = lambda seq: Sbf4c010frsp_tup(*seq)
Sbf4c010frsp_bin = '=B?'
# External Device packet response to Get Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011000rsp_base = namedtuple('Sbf4c011000rsp_base', ' Nudge, Length')

# Factory function for backward compatibility
def Sbf4c011000rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011000rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011000rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011000rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011000rsp_tup._make = lambda seq: Sbf4c011000rsp_tup(*seq)
Sbf4c011000rsp_bin = '=f?'
# External Device packet response to set Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011001rsp_base = namedtuple('Sbf4c011001rsp_base', ' Nudge, Length')

# Factory function for backward compatibility
def Sbf4c011001rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011001rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011001rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011001rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011001rsp_tup._make = lambda seq: Sbf4c011001rsp_tup(*seq)
Sbf4c011001rsp_bin = '=f?'
# External Device packet response to Apply Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011002rsp_base = namedtuple('Sbf4c011002rsp_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbf4c011002rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011002rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011002rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011002rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011002rsp_tup._make = lambda seq: Sbf4c011002rsp_tup(*seq)
Sbf4c011002rsp_bin = '=B?'
# External Device packet response to Get Total
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011003rsp_base = namedtuple('Sbf4c011003rsp_base', ' Total, Length')

# Factory function for backward compatibility
def Sbf4c011003rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011003rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011003rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011003rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011003rsp_tup._make = lambda seq: Sbf4c011003rsp_tup(*seq)
Sbf4c011003rsp_bin = '=f?'
# External Device response to Set Total Nudge
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011004rsp_base = namedtuple('Sbf4c011004rsp_base', ' Total, Length')

# Factory function for backward compatibility
def Sbf4c011004rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011004rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011004rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011004rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011004rsp_tup._make = lambda seq: Sbf4c011004rsp_tup(*seq)
Sbf4c011004rsp_bin = '=f?'
# External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0111rsp_base = namedtuple('Sbf4c0111rsp_base', ' Mask Rate, Length')

# Factory function for backward compatibility
def Sbf4c0111rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0111rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0111rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0111rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0111rsp_tup._make = lambda seq: Sbf4c0111rsp_tup(*seq)
Sbf4c0111rsp_bin = '=LL?'
# External Device packet response to set the GGA Adjust
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0114rsp_base = namedtuple('Sbf4c0114rsp_base', ' GgaAdjust, Length')

# Factory function for backward compatibility
def Sbf4c0114rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0114rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0114rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0114rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0114rsp_tup._make = lambda seq: Sbf4c0114rsp_tup(*seq)
Sbf4c0114rsp_bin = '=B?'
# Point A geodetic position
Sbf4c011806rspPointA_tup = namedtuple('Sbf4c011806rspPointA_tup', ' Latitude Longitude Altitude')
Sbf4c011806rspPointA_bin = '=ddd'
# Point B geodetic position
Sbf4c011806rspPointB_tup = namedtuple('Sbf4c011806rspPointB_tup', ' Latitude Longitude Altitude')
Sbf4c011806rspPointB_bin = '=ddd'
# Point Center geodetic position
Sbf4c011806rspCenterPoint_tup = namedtuple('Sbf4c011806rspCenterPoint_tup', ' Latitude Longitude Altitude')
Sbf4c011806rspCenterPoint_bin = '=ddd'
# Field computer pattern definition for pivot ACB patterns
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011806rsp_base = namedtuple('Sbf4c011806rsp_base', ' Curvature PointA PointB CenterPoint Radius, Length')

# Factory function for backward compatibility
def Sbf4c011806rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011806rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011806rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011806rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011806rsp_tup._make = lambda seq: Sbf4c011806rsp_tup(*seq)
Sbf4c011806rsp_bin = '=B?B?B?Bd?'
# Swath by swath pattern definition response (PTRN_SWATH_BY_SWATH)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011810rsp_base = namedtuple('Sbf4c011810rsp_base', ' SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode, Length')

# Factory function for backward compatibility
def Sbf4c011810rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011810rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011810rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011810rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011810rsp_tup._make = lambda seq: Sbf4c011810rsp_tup(*seq)
Sbf4c011810rsp_bin = '=hBLBH?'
# Swath section pattern definition response (PTRN_SWATH_SECTION)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011811rsp_base = namedtuple('Sbf4c011811rsp_base', ' SwathNumber SwathNumPoints SectionNumPoints SectionIndex ErrorCode, Length')

# Factory function for backward compatibility
def Sbf4c011811rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011811rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011811rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011811rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011811rsp_tup._make = lambda seq: Sbf4c011811rsp_tup(*seq)
Sbf4c011811rsp_bin = '=hHHHH?'
# Swath by swath fragment pattern definition response (PTRN_SWATH_BY_SWATH_FRAGMENT)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011813rsp_base = namedtuple('Sbf4c011813rsp_base', ' SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode, Length')

# Factory function for backward compatibility
def Sbf4c011813rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011813rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011813rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011813rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011813rsp_tup._make = lambda seq: Sbf4c011813rsp_tup(*seq)
Sbf4c011813rsp_bin = '=hBLBH?'
# Swath by swath FFA pattern definition response (PTRN_SWATH_BY_SWATH_FFA)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011820rsp_base = namedtuple('Sbf4c011820rsp_base', ' SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode, Length')

# Factory function for backward compatibility
def Sbf4c011820rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011820rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011820rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011820rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011820rsp_tup._make = lambda seq: Sbf4c011820rsp_tup(*seq)
Sbf4c011820rsp_bin = '=hBLBH?'
# Swath section FFA pattern definition response (PTRN_SWATH_SECTION_FFA)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011821rsp_base = namedtuple('Sbf4c011821rsp_base', ' SwathNumber SwathNumPoints SectionNumPoints SectionIndex ErrorCode, Length')

# Factory function for backward compatibility
def Sbf4c011821rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011821rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011821rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011821rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011821rsp_tup._make = lambda seq: Sbf4c011821rsp_tup(*seq)
Sbf4c011821rsp_bin = '=hHHHH?'
# Response to the Field Computer Information Command (tsip::Sbe4c0119cmd)
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0119rsp_base = namedtuple('Sbf4c0119rsp_base', ' ManufacturerId ProductId1 ProductId2 FirmwareVersion, Length')

# Factory function for backward compatibility
def Sbf4c0119rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0119rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0119rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0119rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0119rsp_tup._make = lambda seq: Sbf4c0119rsp_tup(*seq)
Sbf4c0119rsp_bin = '=BBBf?'
# Sent by the NAV to the display when updating an opis device, like a SAM-300
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0500rsp_base = namedtuple('Sbf4c0500rsp_base', ' OperationState Progress DeviceType, Length')

# Factory function for backward compatibility
def Sbf4c0500rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0500rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0500rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0500rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0500rsp_tup._make = lambda seq: Sbf4c0500rsp_tup(*seq)
Sbf4c0500rsp_bin = '=BBB?'
# External Device packet response to return the guidance status enable
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c2000rsp_base = namedtuple('Sbf4c2000rsp_base', ' Enabled, Length')

# Factory function for backward compatibility
def Sbf4c2000rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c2000rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c2000rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c2000rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c2000rsp_tup._make = lambda seq: Sbf4c2000rsp_tup(*seq)
Sbf4c2000rsp_bin = '=B?'
# External Device packet response to update the guidance status
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c2001rsp_base = namedtuple('Sbf4c2001rsp_base', ' CanId CanMsgLength CanMsg, Length')

# Factory function for backward compatibility
def Sbf4c2001rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c2001rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c2001rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c2001rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c2001rsp_tup._make = lambda seq: Sbf4c2001rsp_tup(*seq)
Sbf4c2001rsp_bin = '=LB?B?'
# An event.
Sbf4c8000rspSequenceEvent_tup = namedtuple('Sbf4c8000rspSequenceEvent_tup', ' Event1 CountdownSeconds CountdownMeters')
Sbf4c8000rspSequenceEvent_bin = '=BBf'
# Updates the display with FFA status
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c8000rsp_base = namedtuple('Sbf4c8000rsp_base', ' Version Swath RequestedSwath TurnProgress Signal SwathIndicators audibleAlert UIMessage ButtonNextSwathEnable ButtonTrueSwathEnable ButtonLeft ButtonRight ButtonSequenceEndOfRow ButtonSequenceStartOfRow ButtonDismiss ButtonAutoTurn ButtonFFAEngage ButtonAcceptLiability ButtonDeclineLiability ButtonTurnStartAuto ButtonTurnStartManual NumberOfEvents SequenceEvents, Length')

# Factory function for backward compatibility
def Sbf4c8000rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c8000rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c8000rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c8000rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c8000rsp_tup._make = lambda seq: Sbf4c8000rsp_tup(*seq)
Sbf4c8000rsp_bin = '=BBhBBBBBBBBBBBBBBBBBBB?Sbf4c8000rspSequenceEvent?'
# 
Sbf4c8001rsp_tup = namedtuple('Sbf4c8001rsp_tup', ', PacketDataLength, PacketData')
Sbf4c8001rsp_bin = '=B*'
# External Device packet response to update the guidance status
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c8002rsp_base = namedtuple('Sbf4c8002rsp_base', ' SetStartSwathButtonState StandardButtonState BlockButtonState AlternatingBlockButtonState ContinuousBlockButtonState, Length')

# Factory function for backward compatibility
def Sbf4c8002rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c8002rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c8002rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c8002rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c8002rsp_tup._make = lambda seq: Sbf4c8002rsp_tup(*seq)
Sbf4c8002rsp_bin = '=BBBBB?'
# GPS simulation response from the Autopilot Navigation Controller. Used for NAV to NAV communication.
Sbf4drsp_tup = namedtuple('Sbf4drsp_tup', ', PacketDataLength, PacketData')
Sbf4drsp_bin = '=B*'
# Piped message response from the Autopilot Navigation Controller.
Sbf4ersp_tup = namedtuple('Sbf4ersp_tup', ', PacketDataLength, PacketData')
Sbf4ersp_bin = '=B*'
# This is an alias to 0x8f 0xa1.
Sbf4frsp_tup = namedtuple('Sbf4frsp_tup', ', PacketDataLength, PacketData')
Sbf4frsp_bin = '=B*'
# This is an alias to 0x8f 0xa1.
S8fa1rsp_tup = namedtuple('S8fa1rsp_tup', ', PacketDataLength, PacketData')
S8fa1rsp_bin = '=B*'
# Wraps Autopilot API NMEA messages for output in a TSIP stream.
Sbf1arsp_tup = namedtuple('Sbf1arsp_tup', ', PacketDataLength, PacketData')
Sbf1arsp_bin = '=B*'
# TAP packet response to the Autosteer Controller
Sbf5014rsp_tup = namedtuple('Sbf5014rsp_tup', ' CommandID, PacketDataLength, PacketData')
Sbf5014rsp_bin = '=BB*'
# Remote Monitor Control Steering packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf530600rsp_base = namedtuple('Sbf530600rsp_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbf530600rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf530600rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf530600rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf530600rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf530600rsp_tup._make = lambda seq: Sbf530600rsp_tup(*seq)
Sbf530600rsp_bin = '=B?'
# Remote Monitor Control Speed packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf530601rsp_base = namedtuple('Sbf530601rsp_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbf530601rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf530601rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf530601rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf530601rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf530601rsp_tup._make = lambda seq: Sbf530601rsp_tup(*seq)
Sbf530601rsp_bin = '=B?'
# Field Computer Ack Current Warning packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf570507rsp_base = namedtuple('Sbf570507rsp_base', ', Length')

# Factory function for backward compatibility
def Sbf570507rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf570507rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf570507rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf570507rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf570507rsp_tup._make = lambda seq: Sbf570507rsp_tup(*seq)
Sbf570507rsp_bin = '=?'
# Field Computer Heartbeat packet response from the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0101rsp_base = namedtuple('Sbf5c0101rsp_base', ' AutosteerVersion AutosteerState APIVersion SystemState WarningState NoAutoAllowed PositionFixQuality RoadingStatusBits Reserved1 Reserved2, Length')

# Factory function for backward compatibility
def Sbf5c0101rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0101rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0101rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0101rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0101rsp_tup._make = lambda seq: Sbf5c0101rsp_tup(*seq)
Sbf5c0101rsp_bin = '=BBBBLLBBBB?'
# Extended Field Computer Heartbeat packet response from the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c011arsp_base = namedtuple('Sbf4c011arsp_base', ' AutosteerState SystemState WarningState FaultState WarningLevel PositionFixQuality NoAutoAllowedReason RoadingStatusBits RowGuidanceMode TIMStatus VelocityControlState Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 Reserved9 Reserved10 SequenceNumber, Length')

# Factory function for backward compatibility
def Sbf4c011arsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c011arsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c011arsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c011arsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c011arsp_tup._make = lambda seq: Sbf4c011arsp_tup(*seq)
Sbf4c011arsp_bin = '=BBHHBBHBBBBBBBBBBBBBBB?'
# Field Computer Logging On packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0106rsp_base = namedtuple('Sbf5c0106rsp_base', ', Length')

# Factory function for backward compatibility
def Sbf5c0106rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0106rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0106rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0106rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0106rsp_tup._make = lambda seq: Sbf5c0106rsp_tup(*seq)
Sbf5c0106rsp_bin = '=?'
# Field Computer Logging Off packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0107rsp_base = namedtuple('Sbf5c0107rsp_base', ', Length')

# Factory function for backward compatibility
def Sbf5c0107rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0107rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0107rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0107rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0107rsp_tup._make = lambda seq: Sbf5c0107rsp_tup(*seq)
Sbf5c0107rsp_bin = '=?'
# Field Computer Get Nudge packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c011000rsp_base = namedtuple('Sbf5c011000rsp_base', ' NudgeIncrement, Length')

# Factory function for backward compatibility
def Sbf5c011000rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c011000rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c011000rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c011000rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c011000rsp_tup._make = lambda seq: Sbf5c011000rsp_tup(*seq)
Sbf5c011000rsp_bin = '=f?'
# Field Computer Set Nudge packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c011001rsp_base = namedtuple('Sbf5c011001rsp_base', ' NudgeIncrement, Length')

# Factory function for backward compatibility
def Sbf5c011001rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c011001rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c011001rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c011001rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c011001rsp_tup._make = lambda seq: Sbf5c011001rsp_tup(*seq)
Sbf5c011001rsp_bin = '=f?'
# Field Computer Apply Nudge packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c011002rsp_base = namedtuple('Sbf5c011002rsp_base', ' NudgeDirection, Length')

# Factory function for backward compatibility
def Sbf5c011002rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c011002rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c011002rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c011002rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c011002rsp_tup._make = lambda seq: Sbf5c011002rsp_tup(*seq)
Sbf5c011002rsp_bin = '=B?'
# Field Computer Get Total Nudge packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c011003rsp_base = namedtuple('Sbf5c011003rsp_base', ' TotalNudge, Length')

# Factory function for backward compatibility
def Sbf5c011003rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c011003rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c011003rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c011003rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c011003rsp_tup._make = lambda seq: Sbf5c011003rsp_tup(*seq)
Sbf5c011003rsp_bin = '=f?'
# Field Computer Set Total Nudge packet response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c011004rsp_base = namedtuple('Sbf5c011004rsp_base', ' TotalNudge, Length')

# Factory function for backward compatibility
def Sbf5c011004rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c011004rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c011004rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c011004rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c011004rsp_tup._make = lambda seq: Sbf5c011004rsp_tup(*seq)
Sbf5c011004rsp_bin = '=f?'
# Field Computer Control State packet response to the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c010brsp_base = namedtuple('Sbf5c010brsp_base', ' GuidanceType NoAutoAllowedReason, Length')

# Factory function for backward compatibility
def Sbf5c010brsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c010brsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c010brsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c010brsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c010brsp_tup._make = lambda seq: Sbf5c010brsp_tup(*seq)
Sbf5c010brsp_bin = '=BL?'
# Field Computer NMEA configuration packet response to the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0111rsp_base = namedtuple('Sbf5c0111rsp_base', ' NMEAMask OutputInterval, Length')

# Factory function for backward compatibility
def Sbf5c0111rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0111rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0111rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0111rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0111rsp_tup._make = lambda seq: Sbf5c0111rsp_tup(*seq)
Sbf5c0111rsp_bin = '=LL?'
# Field Computer Adjust GGA position response to the Autosteer Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0114rsp_base = namedtuple('Sbf5c0114rsp_base', ' AdjustPosition, Length')

# Factory function for backward compatibility
def Sbf5c0114rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0114rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0114rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0114rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0114rsp_tup._make = lambda seq: Sbf5c0114rsp_tup(*seq)
Sbf5c0114rsp_bin = '=B?'
# Field Computer Pattern Definition packet response to the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0118rsp_base = namedtuple('Sbf5c0118rsp_base', ' PatternType SwathNumber NumSwathPoints NumPacketPoints PointIndex FailureCode, Length')

# Factory function for backward compatibility
def Sbf5c0118rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0118rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0118rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0118rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0118rsp_tup._make = lambda seq: Sbf5c0118rsp_tup(*seq)
Sbf5c0118rsp_bin = '=BHHHHH?'
# Field Computer Information packet response to the Autosteer Client
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf5c0119rsp_base = namedtuple('Sbf5c0119rsp_base', ' ManufacturerID ProductID1 ProductID2 ProductVersion Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8, Length')

# Factory function for backward compatibility
def Sbf5c0119rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf5c0119rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf5c0119rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf5c0119rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf5c0119rsp_tup._make = lambda seq: Sbf5c0119rsp_tup(*seq)
Sbf5c0119rsp_bin = '=BBBfBBBBBBBB?'
# The auto-report settings for the current antenna, sent in response to the corresponding configuration command
S8fa70000rsp_tup = namedtuple('S8fa70000rsp_tup', ' AntennaId')
S8fa70000rsp_bin = '=B'
# The position auto-report settings by engine, sent in response to the corresponding command
S8fa70001rsp_tup = namedtuple('S8fa70001rsp_tup', ' AntennaId NumEngs PositionEngArray')
S8fa70001rsp_bin = '=BB?B'
# The position auto-report settings by type, sent in response to the corresponding command
S8fa70002rsp_tup = namedtuple('S8fa70002rsp_tup', ' AntennaId NumTypes PositionTypeArray')
S8fa70002rsp_bin = '=BB?B'
# The position auto-report settings by flag, sent in response to the corresponding command
S8fa70003rsp_tup = namedtuple('S8fa70003rsp_tup', ' Enable AntennaId SetFlags ClearedFlags')
S8fa70003rsp_bin = '=BBLL'
# A GPS Position packet that provides a useful subset of positioning information, including an id for the antenna it came from.
S8fa70100rsp_tup = namedtuple('S8fa70100rsp_tup', ' GPSSecond AntennaId PositionEngine PositionType Flags Latitude Longitude Height EVelocity NVelocity UVelocity NumSatellites HDOP CorrectionAge')
S8fa70100rsp_bin = '=dBBBLdddfffBff'
# Indicates that a GPS position wasn't generated for the given time period
S8fa70101rsp_tup = namedtuple('S8fa70101rsp_tup', ' GPSSecond AntennaId PositionEngine Flags NumSatellites')
S8fa70101rsp_bin = '=dBBLB'
# Provides the ENU vector between two GPS antennas
S8fa70102rsp_tup = namedtuple('S8fa70102rsp_tup', ' GPSSecond BaseAntennaId RoverAntennaId Magnitude Direction X Y Z')
S8fa70102rsp_bin = '=dBBffddd'
# Response to the 8FA801 packet
S8fa800rsp_tup = namedtuple('S8fa800rsp_tup', ' RSSI ConnectionStatus')
S8fa800rsp_bin = '=bB'
# Ack to NTRIP params set
S8fa801ack_tup = namedtuple('S8fa801ack_tup', ' Result')
S8fa801ack_bin = '=B'
# Report of the current NTRIP params. All strings are not null terminated, and the stringLength value is the number of actual characters
S8fa801rsp_tup = namedtuple('S8fa801rsp_tup', ' IPPort IPAddrLength IPAddress MountPointLength MountPoint UserNameLength UserName PasswordLength Password UseForRTX')
S8fa801rsp_bin = '=HB?cB?cB?cB?cB'
# ACK for the set fo the GPRS Username
S8fa802ack_tup = namedtuple('S8fa802ack_tup', ' Result')
S8fa802ack_bin = '=B'
# Report of the GPRS Username. All strings are not null terminated, and the stringLength value is the number of actual characters
S8fa802rsp_tup = namedtuple('S8fa802rsp_tup', ' result StringLength UserName')
S8fa802rsp_bin = '=BB?c'
# ACK for the set fo the GPRS Password
S8fa803ack_tup = namedtuple('S8fa803ack_tup', ' Result')
S8fa803ack_bin = '=B'
# Report of the GPRS Password. All strings are not null terminated, and the stringLength value is the number of actual characters
S8fa803rsp_tup = namedtuple('S8fa803rsp_tup', ' result StringLength Password')
S8fa803rsp_bin = '=BB?c'
# ACK for the set fo the GPRS InitString
S8fa804ack_tup = namedtuple('S8fa804ack_tup', ' result')
S8fa804ack_bin = '=B'
# Report of the GPRS InitString. All strings are not null terminated, and the stringLength value is the number of actual characters
S8fa804rsp_tup = namedtuple('S8fa804rsp_tup', ' result StringLength InitString')
S8fa804rsp_bin = '=BB?c'
# ACK for the set fo the GPRS CPIN
S8fa805ack_tup = namedtuple('S8fa805ack_tup', ' Result')
S8fa805ack_bin = '=B'
# ACK from the VRS Radio Config command
S8fa806ack_tup = namedtuple('S8fa806ack_tup', ' result')
S8fa806ack_bin = '=B'
# Report of the current radio mode
S8fa806rsp_tup = namedtuple('S8fa806rsp_tup', ' VRSEnabled AutoReportEnabled StreamType')
S8fa806rsp_bin = '=BBB'
# Holds various firmware and hardware version information
S8fa900rsp_tup = namedtuple('S8fa900rsp_tup', ' FirmwareMajorVersion FirmwareMinorVersion FirmwareBuildNum FirmwareBuildType FirmwarePentaVersion FirmwareDay FirmwareMonth FirmwareYear FirmwareExpDay FirmwareExpMonth FirmwareExpYear HardwareRevision HardwarePlatform, AuxInfo')
S8fa900rsp_bin = '=BBHBHBBHBBHBB32s'
# Acknowledges the upgrade command, providing information on how it proceeded.
S8fa90100ack_tup = namedtuple('S8fa90100ack_tup', ' UpgradeStatus')
S8fa90100ack_bin = '=B'
# Provides the progress of the upgrade as it proceeds
S8fa90100rsp_tup = namedtuple('S8fa90100rsp_tup', ' UpgradeOperation Progress')
S8fa90100rsp_bin = '=Bd'
# Acknowledges the logging control, providing information on how it proceeded.
S8fa90101ack_tup = namedtuple('S8fa90101ack_tup', ' LoggingStatus')
S8fa90101ack_bin = '=B'
# Reports the state of the logging control.
S8fa90101rsp_tup = namedtuple('S8fa90101rsp_tup', ' Status filenameLen filename')
S8fa90101rsp_bin = '=BB?c'
# Acknowledges the Log dump request providing information on how the operation proceeded.
S8fa90102ack_tup = namedtuple('S8fa90102ack_tup', ' LogDumpStatus')
S8fa90102ack_bin = '=B'
# A variable length data packet (pong), that is returned in response to a receiver request (ping). This allows a type of serial communication test to occur.
S8fa90103rsp_tup = namedtuple('S8fa90103rsp_tup', ' PongSize Data')
S8fa90103rsp_bin = '=B?B'
# Returns the IP Address and port number for the VRS Daemon.
S8fa90104rsp_tup = namedtuple('S8fa90104rsp_tup', ', IP Port')
S8fa90104rsp_bin = '=20sH'
# Acknowledges the license file has been processed.
S8fa90105ack_tup = namedtuple('S8fa90105ack_tup', ' Status')
S8fa90105ack_bin = '=B'
# Reports the current state of the receiver automatic reboot capability
S8fa90106rsp_tup = namedtuple('S8fa90106rsp_tup', ' Frequency')
S8fa90106rsp_bin = '=B'
# Returns the IP Address and port number for the CLAAS RTK NET modem
S8fa90107rsp_tup = namedtuple('S8fa90107rsp_tup', ', IP Port')
S8fa90107rsp_bin = '=20sH'
# Returns the IP Address for the TNFS Host Address.
S8fa90108rsp_tup = namedtuple('S8fa90108rsp_tup', ', IP')
S8fa90108rsp_bin = '=20s'
# Holds the upgrade/downgrade version floor and related information
S8fa90130rsp_tup = namedtuple('S8fa90130rsp_tup', ' FirmwareVersionStatus DowngradeMajorVersion DowngradeMinorVersion DowngradeBuildNum DowngradeBuildType DowngradeFeatureSpecific')
S8fa90130rsp_bin = '=HBBHBB'
# Returns whether the upgrade/downgrade is allowed
S8fa90131rsp_tup = namedtuple('S8fa90131rsp_tup', ' Result')
S8fa90131rsp_bin = '=b'
# Returns the mux settings of the digital output for a particular port.
S8fa90200rsp_tup = namedtuple('S8fa90200rsp_tup', ' PortId MuxType OutputValue')
S8fa90200rsp_bin = '=BBB'
# Returns the settings of the digital input for a particular port.
S8fa90201rsp_tup = namedtuple('S8fa90201rsp_tup', ' PortId Threshold Pull')
S8fa90201rsp_bin = '=BBB'
# Returns the state of the Pollux FPGA GPO
S8fa90202rsp_tup = namedtuple('S8fa90202rsp_tup', ' GPOSetting')
S8fa90202rsp_bin = '=B'
# Information for an antenna
S8fa90300rspAntennaInfo_tup = namedtuple('S8fa90300rspAntennaInfo_tup', ' AntennaId StateFlags')
S8fa90300rspAntennaInfo_bin = '=BL'
# Provides information about connected Antennas.
S8fa90300rsp_tup = namedtuple('S8fa90300rsp_tup', ' NumAntennas AntennaArray')
S8fa90300rsp_bin = '=B?S8fa90300rspAntennaInfo'
# Retrieves the Radar settings
S8fa90400rsp_tup = namedtuple('S8fa90400rsp_tup', ' Enable FreqSpeedRate')
S8fa90400rsp_bin = '=Bf'
# Acknowledgement in response to TSIP Event Log Command packet: 0x8E 0xA9 0x05.
S8fa905ack_tup = namedtuple('S8fa905ack_tup', '')
S8fa905ack_bin = '='
# Returns the mux of the Module-A digital pins
S8fa90700rsp_tup = namedtuple('S8fa90700rsp_tup', ' DigitalPin MuxType Output')
S8fa90700rsp_bin = '=BBB'
# Returns the PWMON Control Point Status
S8fa90701rsp_tup = namedtuple('S8fa90701rsp_tup', ' CtrlPoint Output')
S8fa90701rsp_bin = '=BB'
# Returns the Video Input selection
S8fa90703rsp_tup = namedtuple('S8fa90703rsp_tup', ' VideoInput Output')
S8fa90703rsp_bin = '=BB'
# Provides Module-A auto shutdown timer settings.
S8fa90704rsp_tup = namedtuple('S8fa90704rsp_tup', ' Delay TimeRemaining')
S8fa90704rsp_bin = '=BB'
# Returns the Module A's network interface settings.
S8fa90705rsp_tup = namedtuple('S8fa90705rsp_tup', ' NetIfaceSettingLife NetIfaceMode IP NetMask Gateway Broadcast')
S8fa90705rsp_bin = '=BBLLLL'
# Converted ADC Channel Reading
S8fa90600rspADCChannelReading_tup = namedtuple('S8fa90600rspADCChannelReading_tup', ' Channel Value')
S8fa90600rspADCChannelReading_bin = '=Bd'
# ADC Readings
S8fa90600rsp_tup = namedtuple('S8fa90600rsp_tup', ' Normalized NumChannels ConvertedADCChannelReadings')
S8fa90600rsp_bin = '=BB?S8fa90600rspADCChannelReading'
# Module-A hardware configuration response
S8fa90706rsp_tup = namedtuple('S8fa90706rsp_tup', ' HardwareConfig')
S8fa90706rsp_bin = '=L'
# The socket uart device configured for Port-D on the Module-A
S8fa90707rsp_tup = namedtuple('S8fa90707rsp_tup', ' TBIPDeviceType, SerialNumber UartId')
S8fa90707rsp_bin = '=L32sB'
# Provides the current state of RTK correction rebroadcasting
S8fa90800rsp_tup = namedtuple('S8fa90800rsp_tup', ' Operation')
S8fa90800rsp_bin = '=B'
# Response with all the enabled features in the Feature Manager
S8fa90a00rsp_tup = namedtuple('S8fa90a00rsp_tup', ' NumFeatures Features')
S8fa90a00rsp_bin = '=B?B'
# Status of a Picus Feature Manager License
S8fa90a01rspLicenseStatus_tup = namedtuple('S8fa90a01rspLicenseStatus_tup', ' License Status')
S8fa90a01rspLicenseStatus_bin = '=BB'
# Response with the status of all installed licenses in the Feature Manager
S8fa90a01rsp_tup = namedtuple('S8fa90a01rsp_tup', ' NumLicenses Licenses')
S8fa90a01rsp_bin = '=B?S8fa90a01rspLicenseStatus'
# Acknowledgement in response to TSIP Command packet: 0x8E 0xA9 0x08 0x00.
S8fa909ack_tup = namedtuple('S8fa909ack_tup', ' Result')
S8fa909ack_bin = '=B'
# Returns the state of the Receiver LED. This is in response to TSIP Request: 0x8E 0xA9 0x08 0x00.
S8fa909rsp_tup = namedtuple('S8fa909rsp_tup', ' RcvrId LEDId LEDState')
S8fa909rsp_bin = '=BBB'
# Unlock status information
S8fa910rspUnlockStatusInfo_tup = namedtuple('S8fa910rspUnlockStatusInfo_tup', ' UnlockType UnlockInstalledFlag SubscriptionExpiryStatus DaysToSubscriptionExpiry')
S8fa910rspUnlockStatusInfo_bin = '=BBBH'
# Receiver Unlock Status Response
S8fa910rsp_tup = namedtuple('S8fa910rsp_tup', ' NumUnlockTypes UnlockStatusInfoArray')
S8fa910rsp_bin = '=B?S8fa910rspUnlockStatusInfo'
# Product Information Response
S8fa911rsp_tup = namedtuple('S8fa911rsp_tup', ', PartNumber, ProductName, BriefProductName')
S8fa911rsp_bin = '=15s20s10s'
# Boot Count Information Response
S8fa912rsp_tup = namedtuple('S8fa912rsp_tup', ' BootCount')
S8fa912rsp_bin = '=H'
# Geoidal Separation Information Response
S8fa913rsp_tup = namedtuple('S8fa913rsp_tup', ' GeoidalSeparation')
S8fa913rsp_bin = '=f'
# Code Bias Calibration Table Information Response
S8fa914rsp_tup = namedtuple('S8fa914rsp_tup', ' CBC_Status RtxDeviceId NVTableVersion Reserved1 Reserved2 Reserved3')
S8fa914rsp_bin = '=BBLBBB'
# Response to SysFileXferInitiate command.
S8fa91500rsp_tup = namedtuple('S8fa91500rsp_tup', ' xferType fileType resultCode fileId fileSize, md5Hash clientFileIdSize clientFileId')
S8fa91500rsp_bin = '=BBBLL16?BB?B'
# Respond to SysFileXferGetBlock request
S8fa91501rsp_tup = namedtuple('S8fa91501rsp_tup', ' fileId offset resultCode blockSize blockData')
S8fa91501rsp_bin = '=LLBB?B'
# Respond with results of SysFileXferPutBlock request
S8fa91502rsp_tup = namedtuple('S8fa91502rsp_tup', ' fileId resultCode offset blockSize')
S8fa91502rsp_bin = '=LBLB'
# Acknowledges close of stream associated with fileId
S8fa91503rsp_tup = namedtuple('S8fa91503rsp_tup', ' fileId resultCode')
S8fa91503rsp_bin = '=LB'
# Sent on errors during a file transfer operation
S8fa91599rsp_tup = namedtuple('S8fa91599rsp_tup', ' fileId errorCode')
S8fa91599rsp_bin = '=LB'
# Returns result of SysFileXferDelete command
S8fa91504rsp_tup = namedtuple('S8fa91504rsp_tup', ' fileType resultCode')
S8fa91504rsp_bin = '=BB'
# Indicates current mux mode of GP uart in Fusion
S8fa9160000rsp_tup = namedtuple('S8fa9160000rsp_tup', ' mode')
S8fa9160000rsp_bin = '=B'
# Indicates current mux mode of Tx port uart in Fusion
S8fa9160001rsp_tup = namedtuple('S8fa9160001rsp_tup', ' mode')
S8fa9160001rsp_bin = '=B'
# Indicates current mux mode of Radio port uart in Fusion
S8fa9160002rsp_tup = namedtuple('S8fa9160002rsp_tup', ' mode')
S8fa9160002rsp_bin = '=B'
# Indicates current mode of the internal AP virtual uart in Fusion
S8fa9160100rsp_tup = namedtuple('S8fa9160100rsp_tup', ' mode')
S8fa9160100rsp_bin = '=B'
# Report Bluetooth state (enabled or disabled)
S8fa91602rsp_tup = namedtuple('S8fa91602rsp_tup', ' enable')
S8fa91602rsp_bin = '=B'
# Report the status of the Clear All Licenses command
S8fa91603rsp_tup = namedtuple('S8fa91603rsp_tup', ' success')
S8fa91603rsp_bin = '=B'
# Report the status of the Remove / Restore Manufacturing Licenses command
S8fa91604rsp_tup = namedtuple('S8fa91604rsp_tup', ' success')
S8fa91604rsp_bin = '=B'
# Remove Licenses By Fragment response
S8fa91605rsp_tup = namedtuple('S8fa91605rsp_tup', ' success')
S8fa91605rsp_bin = '=B'
# Returns UDS diagnostic status
S8fa91606rsp_tup = namedtuple('S8fa91606rsp_tup', ' status')
S8fa91606rsp_bin = '=B'
# Reports the Nav's internal IMU orientation, offsets, and calibration.
S8fa91700rsp_tup = namedtuple('S8fa91700rsp_tup', ' AntLevX AntLevY AntLevZ ImuAngleRoll ImuAnglePitch ImuAngleYaw ImuLevX ImuLevY ImuLevZ ImuRollOffset ImuPitchOffset')
S8fa91700rsp_bin = '=fffffffffff'
# Query if IMU-Corrected positions and streaming are enabled.
S8fa91701rsp_tup = namedtuple('S8fa91701rsp_tup', ' EnableIMUCorrection EnableIMUDetailStream')
S8fa91701rsp_bin = '=BB'
# IMU corrected position including roll, pitch, yaw. Stream of messages enabled by 0x8e 0xa9 0x17 0x00 command.
S8fa91702rsp_tup = namedtuple('S8fa91702rsp_tup', ' GPSSeconds PositionEngine PositionType Latitude Longitude Height LatitudeOriginal LongitudeOriginal HeightOriginal EVelocity NVelocity UVelocity Direction ImuStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites HDOP VDOP ESigma NSigma USigma CorrectionAge StationID')
S8fa91702rsp_bin = '=dBBddddddfffBBffffffBffffffB'
# Reports the current IMU Settings covered by Block 2.
S8fa91703rsp_tup = namedtuple('S8fa91703rsp_tup', ' ProPointEngineMode StaticBenchModeEnable StaticBenchHeading VehicleType')
S8fa91703rsp_bin = '=BBfB'
# Returns the cryptochip configuration CRC value
S8fa918rsp_tup = namedtuple('S8fa918rsp_tup', ' crc status')
S8fa918rsp_bin = '=HB'
# CAN Channel Config
S8f9f00rspCANChannelCfg_tup = namedtuple('S8f9f00rspCANChannelCfg_tup', ' Channel BusSpeed J1939Address J1939ECUInstance J1939FunctionInstance Flags')
S8f9f00rspCANChannelCfg_bin = '=BBBBBB'
# Sets the CAN bus configuration for specified channels
S8f9f00rsp_tup = namedtuple('S8f9f00rsp_tup', ' NumChannels ChannelCfg')
S8f9f00rsp_bin = '=B?S8f9f00rspCANChannelCfg'
# Acknowledgement that the CAN configuration was received
S8f9f00ack_tup = namedtuple('S8f9f00ack_tup', '')
S8f9f00ack_bin = '='
# CAN Channel Config
S8f9f01rspCANChannelCfg_tup = namedtuple('S8f9f01rspCANChannelCfg_tup', ' Channel J1939Address AddressState')
S8f9f01rspCANChannelCfg_bin = '=BBB'
# Provides the current CAN status for the channel
S8f9f01rsp_tup = namedtuple('S8f9f01rsp_tup', ' NumChannels ChannelCfg')
S8f9f01rsp_bin = '=B?S8f9f01rspCANChannelCfg'
# J1939 message configuration
S8f9f02rspMsgCfg_tup = namedtuple('S8f9f02rspMsgCfg_tup', ' MsgType MsgInterval')
S8f9f02rspMsgCfg_bin = '=BH'
# Provides current J1939 message configuration for channel
S8f9f02rsp_tup = namedtuple('S8f9f02rsp_tup', ' Channel NumMessages MsgCfgArray')
S8f9f02rsp_bin = '=BB?S8f9f02rspMsgCfg'
# Acknowledgement that J1939 message configuration was received
S8f9f02ack_tup = namedtuple('S8f9f02ack_tup', '')
S8f9f02ack_bin = '='
# NMEA2K message configuration
S8f9f03rspMsgCfg_tup = namedtuple('S8f9f03rspMsgCfg_tup', ' MsgType MsgInterval')
S8f9f03rspMsgCfg_bin = '=BH'
# Provides current NMEA2K message configuration for channel
S8f9f03rsp_tup = namedtuple('S8f9f03rsp_tup', ' Channel NumMessages MsgCfgArray')
S8f9f03rsp_bin = '=BB?S8f9f03rspMsgCfg'
# Acknowledgement that NMEA2K message configuration was received
S8f9f03ack_tup = namedtuple('S8f9f03ack_tup', '')
S8f9f03ack_bin = '='
# ISO message configuration
S8f9f04rspMsgCfg_tup = namedtuple('S8f9f04rspMsgCfg_tup', ' MsgType MsgInterval')
S8f9f04rspMsgCfg_bin = '=BH'
# Provides current ISO message configuration for channel
S8f9f04rsp_tup = namedtuple('S8f9f04rsp_tup', ' Channel NumMessages MsgCfgArray')
S8f9f04rsp_bin = '=BB?S8f9f04rspMsgCfg'
# Acknowledgement that ISO message configuration was received
S8f9f04ack_tup = namedtuple('S8f9f04ack_tup', '')
S8f9f04ack_bin = '='
# Reports the PPS configuration settings. This acknowleges the 0xB0 0x00 commands.
Sb080rsp_tup = namedtuple('Sb080rsp_tup', ' PPSNumber EnableFlag PPSTimebase PPSPolarity AutoReport Period Offset MaxUncThreshold')
Sb080rsp_bin = '=BBBBBddf'
# Reports whether the specified PPS signal is enabled or disabled. This acknowledges a 0xB0 0x01 command.
Sb081rsp_tup = namedtuple('Sb081rsp_tup', ' PPSNumber EnableFlag')
Sb081rsp_bin = '=BB'
# TAP packet response to the Inertial Nav feature
Sbf6014rsp_tup = namedtuple('Sbf6014rsp_tup', ' CommandID, PacketDataLength, PacketData')
Sbf6014rsp_bin = '=BB*'
# Remote Monitor Control Steering packet response to the Inertial Nav feature
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf630600rsp_base = namedtuple('Sbf630600rsp_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbf630600rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf630600rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf630600rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf630600rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf630600rsp_tup._make = lambda seq: Sbf630600rsp_tup(*seq)
Sbf630600rsp_bin = '=B?'
# Remote Monitor Control Speed packet response to the Inertial Nav feature
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf630601rsp_base = namedtuple('Sbf630601rsp_base', ' Direction, Length')

# Factory function for backward compatibility
def Sbf630601rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf630601rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf630601rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf630601rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf630601rsp_tup._make = lambda seq: Sbf630601rsp_tup(*seq)
Sbf630601rsp_bin = '=B?'
# Roll/Pitch corrected Position and Attitude packet from the Inertial Nav feature.
Sbf6800rsp_tup = namedtuple('Sbf6800rsp_tup', ' GPSSecond INSEngineId AntennaId PositionEngine PositionType PositionFlags Latitude Longitude Height EVelocity NVelocity UVelocity Direction IMUStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites HDOP VDOP ESigma NSigma USigma SemiMajorSigma SemiMinorSigma CorrectionAge StationID')
Sbf6800rsp_bin = '=dBBBBLdddfffBLddddddBffffffffB'
# Indicates that a GPS position wasn't generated for the given time period
Sbf6801rsp_tup = namedtuple('Sbf6801rsp_tup', ' GPSSecond INSEngineId AntennaId PositionEngine PositionFlags Direction IMUStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites StationID')
Sbf6801rsp_bin = '=dBBBLBLddddddBB'
# Publish Parameter Block Hardware Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710000rsp_base = namedtuple('Sbf710000rsp_base', ', ControllerSerNum NumDefinedOptions, Options ControllerSimulatingGPS HWType, Length')

# Factory function for backward compatibility
def Sbf710000rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710000rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710000rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710000rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710000rsp_tup._make = lambda seq: Sbf710000rsp_tup(*seq)
Sbf710000rsp_bin = '=22sB14?BBB?'
# Publish Parameter Block Software Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710100rsp_base = namedtuple('Sbf710100rsp_base', ', ApplicationId AppCodeVersionMajor AppCodeVersionMinor AppCodeVersionBuildNumber AppCodeVersionBuildType AppTestBuildFlag AppCodeVersionYear AppCodeVersionMonth AppCodeVersionDay ExpireGPSWeek, MonitorId MonCodeVersionMajor MonCodeVersionMinor MonCodeVersionMonth MonCodeVersionDay MonCodeVersionYear, Length')

# Factory function for backward compatibility
def Sbf710100rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710100rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710100rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710100rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710100rsp_tup._make = lambda seq: Sbf710100rsp_tup(*seq)
Sbf710100rsp_bin = '=20sBBLBBHBBH20sLLBBH?'
# Publish Parameter Block OPS Config Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710200rsp_base = namedtuple('Sbf710200rsp_base', ' LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset, Length')

# Factory function for backward compatibility
def Sbf710200rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710200rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710200rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710200rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710200rsp_tup._make = lambda seq: Sbf710200rsp_tup(*seq)
Sbf710200rsp_bin = '=fBffff?'
# Publish Parameter Block OPS Config Information packet SET confirmation    response from Autopilot
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710201rsp_base = namedtuple('Sbf710201rsp_base', ' LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset, Length')

# Factory function for backward compatibility
def Sbf710201rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710201rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710201rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710201rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710201rsp_tup._make = lambda seq: Sbf710201rsp_tup(*seq)
Sbf710201rsp_bin = '=fBffff?'
# Publish Parameter Block Platform Config Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710300rsp_base = namedtuple('Sbf710300rsp_base', ', VehicleModel VehicleIndex VehicleType VehicleColor, ExtIOFctArray, VdmIOFctArray UseLowSpeedOperation UseVehicleDirectionEstimator DisableEngageButton SuperLowSpeeedAllowed UseSuperLowSpeeed SafetyMinVelocity GyroSteeringSupport UseAutosenseSensor, Length')

# Factory function for backward compatibility
def Sbf710300rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710300rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710300rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710300rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710300rsp_tup._make = lambda seq: Sbf710300rsp_tup(*seq)
Sbf710300rsp_bin = '=16sLLL14?L12?LBBBBBfBB?'
# Publish Parameter Block Safety Config Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710400rsp_base = namedtuple('Sbf710400rsp_base', ' OperatorAliveSwitchSnooze WarningRowEndDistance MaxEngageSpeedForward MaxEngageSpeedReverse MaxOperatingSpeedForward MaxOperatingSpeedReverse MaxSteeringAngleAllowed, Length')

# Factory function for backward compatibility
def Sbf710400rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710400rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710400rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710400rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710400rsp_tup._make = lambda seq: Sbf710400rsp_tup(*seq)
Sbf710400rsp_bin = '=Lffffff?'
# Publish Parameter Block Version Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710500rsp_base = namedtuple('Sbf710500rsp_base', ' TsipParamApiVersion, ControllerSerNum AppMajorVersion AppMinorVersion, Length')

# Factory function for backward compatibility
def Sbf710500rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710500rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710500rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710500rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710500rsp_tup._make = lambda seq: Sbf710500rsp_tup(*seq)
Sbf710500rsp_bin = '=B22sBB?'
# Publish Parameter Sensor Hyd State Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710600rsp_base = namedtuple('Sbf710600rsp_base', ' OPSState RemoteEngageState ManualOverrideState MeasuredSteeringAngle SystemVoltage PwmRightSide PwmLeftSide PPSIntCount WheelSpeed GearLeverState NeutralSense MeasuredPumpPressureLeft MeasuredPumpPressureRight EngineSpeed, Length')

# Factory function for backward compatibility
def Sbf710600rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710600rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710600rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710600rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710600rsp_tup._make = lambda seq: Sbf710600rsp_tup(*seq)
Sbf710600rsp_bin = '=BBBffffLfBBfff?'
# Publish Parameter Raw Sensor Status Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710700rsp_base = namedtuple('Sbf710700rsp_base', ' OPS RemoteEngage ManualOverride MeasuredSteeringAngle WheelSpeed GearLever MeasurePumpPressureLeft MeasurePumpPressureRight EngineSpeed OutputBalance SteeringFault, Length')

# Factory function for backward compatibility
def Sbf710700rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710700rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710700rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710700rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710700rsp_tup._make = lambda seq: Sbf710700rsp_tup(*seq)
Sbf710700rsp_bin = '=fffffffffff?'
# Publish Parameter Block Selected IMU Status Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710800rsp_base = namedtuple('Sbf710800rsp_base', ' Authenticated FirmwareVersionValid VersionMajor VersionMinor SerialNumberValid, SerialNumber IsTemperatureValid Temperature IsRollValid RollEst IsPitchValid PitchEst DataSourceType DataTimestamp Connected, Length')

# Factory function for backward compatibility
def Sbf710800rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710800rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710800rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710800rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710800rsp_tup._make = lambda seq: Sbf710800rsp_tup(*seq)
Sbf710800rsp_bin = '=BBllB11sBHBfBfLLB?'
# Publish Parameter Block CS Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710900rsp_base = namedtuple('Sbf710900rsp_base', ' ValveControllerType CsNum CSValues, Length')

# Factory function for backward compatibility
def Sbf710900rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710900rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710900rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710900rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710900rsp_tup._make = lambda seq: Sbf710900rsp_tup(*seq)
Sbf710900rsp_bin = '=LL?L?'
# Publish Parameter Block Group1 Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710a00rsp_base = namedtuple('Sbf710a00rsp_base', ' Curvature SteeringAngleFront Frequency Counter, Length')

# Factory function for backward compatibility
def Sbf710a00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710a00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710a00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710a00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710a00rsp_tup._make = lambda seq: Sbf710a00rsp_tup(*seq)
Sbf710a00rsp_bin = '=LffL?'
# Publish Parameter Block Group2 Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710b00rsp_base = namedtuple('Sbf710b00rsp_base', ' RequestReset SteeringInput Readiness Lockout, Length')

# Factory function for backward compatibility
def Sbf710b00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710b00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710b00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710b00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710b00rsp_tup._make = lambda seq: Sbf710b00rsp_tup(*seq)
Sbf710b00rsp_bin = '=BBBB?'
# Publish Parameter Block Group3 Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710c00rsp_base = namedtuple('Sbf710c00rsp_base', ' JDSecurity JDExitCode, Length')

# Factory function for backward compatibility
def Sbf710c00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710c00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710c00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710c00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710c00rsp_tup._make = lambda seq: Sbf710c00rsp_tup(*seq)
Sbf710c00rsp_bin = '=LB?'
# Publish Parameter Block GPS Guidance Status Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710d00rsp_base = namedtuple('Sbf710d00rsp_base', ' AutosteerLockedOut RawXTE SwathOffset ScaledSteeringAngle HeadingError FilteredRoll PathHeading LineAcquisitionState, Length')

# Factory function for backward compatibility
def Sbf710d00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710d00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710d00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710d00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710d00rsp_tup._make = lambda seq: Sbf710d00rsp_tup(*seq)
Sbf710d00rsp_bin = '=BffffffB?'
# Publish Parameter Block GPS Guidance Diag Information packet response from the Autopilot Navigation Controller
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf710e00rsp_base = namedtuple('Sbf710e00rsp_base', ' VehicleDirection FilteredYawRate CommandedSteeringAngle CommandedYawRate CommandedPressureLeft CommandedPressureRight, Length')

# Factory function for backward compatibility
def Sbf710e00rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf710e00rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf710e00rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf710e00rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf710e00rsp_tup._make = lambda seq: Sbf710e00rsp_tup(*seq)
Sbf710e00rsp_bin = '=Bfffff?'
# Publish Parameter Block Group4 Information packet response from the Autopilot Navigation Controller
Sbf710f00rsp_tup = namedtuple('Sbf710f00rsp_tup', ' RearSteeringAngle')
Sbf710f00rsp_bin = '=L'
# 
Sbf4c0120rspPointDiff_tup = namedtuple('Sbf4c0120rspPointDiff_tup', ' LatitudeDiff LongitudeDiff')
Sbf4c0120rspPointDiff_bin = '=ff'
# Path to be plotted on Field Computer map. Reference point is first point of path (only plot for first message). Included with all packets though.
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c0120rsp_base = namedtuple('Sbf4c0120rsp_base', ' PathType NumberOfPoints PacketNumber LastPacket ReferenceLatitude ReferenceLongitude Points, Length')

# Factory function for backward compatibility
def Sbf4c0120rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c0120rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c0120rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c0120rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c0120rsp_tup._make = lambda seq: Sbf4c0120rsp_tup(*seq)
Sbf4c0120rsp_bin = '=BBBBdd?Sbf4c0120rspPointDiff?'
# Overall Secure RTK Status
S890000rspOverallSystemStatus_tup = namedtuple('S890000rspOverallSystemStatus_tup', ' SystemStatus DaysToExpiry')
S890000rspOverallSystemStatus_bin = '=BH'
# Key Slot Information
S890000rspKeyStatus_tup = namedtuple('S890000rspKeyStatus_tup', ' KeyStatus KeyExpiryStatus KeyDayOfExpiry')
S890000rspKeyStatus_bin = '=BBH'
# Status of SecureRTK and the 5 rover keys.
S890000rsp_tup = namedtuple('S890000rsp_tup', ' Version NumberOfKeys OverallSystemStatus, IndividualKeysStatus')
S890000rsp_bin = '=BB?B5?S890000rspKeyStatus'
# Rover Key Data
S890001rsp_tup = namedtuple('S890001rsp_tup', ' KeySlot Version, KeyString, DescriptionString')
S890001rsp_bin = '=BB17s16s'
# Set Rover Key Data Response
S890002rsp_tup = namedtuple('S890002rsp_tup', ' Version KeySlot KeyStatus KeyExpiryStatus KeyDayOfExpiry')
S890002rsp_bin = '=BBBBH'
# Delete Rover Key Data Response
S890003rsp_tup = namedtuple('S890003rsp_tup', ' Version KeySlot Result')
S890003rsp_bin = '=BBB'
# New 27 character passcode upgrade response packet
S8fa9a5rsp_tup = namedtuple('S8fa9a5rsp_tup', ' Success, AckString')
S8fa9a5rsp_bin = '=B65s'
# Provides type of specified antenna.
S8faa00rsp_tup = namedtuple('S8faa00rsp_tup', ' AntennaId AntennaType')
S8faa00rsp_bin = '=BH'
# Reports the status of the RTX subscription and shows which connections are available
S8fab00rsp_tup = namedtuple('S8fab00rsp_tup', ' DaysUntilExpirationFast DaysUntilExpirationStandard AvailableConnections DaysUntilExpirationRangePoint DaysUntilExpirationFallback DaysUntilExpirationXFillP DaysUntilExpirationViewPoint')
S8fab00rsp_bin = '=llBllll'
# Reports Centerpoint RTX fast Network Info
S8fab01rsp_tup = namedtuple('S8fab01rsp_tup', ' Status DistToNetwork Timestamp Zone')
S8fab01rsp_bin = '=BdlB'
# Acknowledgment that RTX std FastRestart has been cancelled
S8fab02ack_tup = namedtuple('S8fab02ack_tup', '')
S8fab02ack_bin = '='
# Reports Centerpoint and RangePoint RTX Status Information
S8fab03rsp_tup = namedtuple('S8fab03rsp_tup', ' ConfiguredRTXSource ActiveRTXSource DeliveryMethod ConvergenceStatus HorizErrorEstimate WetDryStatus Reserved1 Reserved2 Reserved3 CorrectionAge SatTrckStatus RTXSatSNR FastCorrectionSats FastRestartEnabled FastRestartState FastRestartFailureModes FastRestartReady')
S8fab03rsp_bin = '=BBBBfBBBBfBhBBBBB'
# Acknowledgment that RTX FastRestart vehicle movement status has been saved in the receiver 
S8fab04ack_tup = namedtuple('S8fab04ack_tup', ' Result')
S8fab04ack_bin = '=B'
# Custom RTX offset
S8fab05rspRTXOffset_tup = namedtuple('S8fab05rspRTXOffset_tup', ' enabled east north up')
S8fab05rspRTXOffset_bin = '=Bfff'
# Response containing RTX output settings
S8fab05rsp_tup = namedtuple('S8fab05rsp_tup', ' RTXOutputDatum RTXOffset')
S8fab05rsp_bin = '=B?B'
# Reports RTK/RTX Best Type Selection Info
S8fab06rsp_tup = namedtuple('S8fab06rsp_tup', ' Status')
S8fab06rsp_bin = '=B'
# Response containing the current configuration and mode of the MSS Mode Switch
S8fab07rsp_tup = namedtuple('S8fab07rsp_tup', ' MSSControlMode MSSMode')
S8fab07rsp_bin = '=BB'
# Response containing realtime RTK/RTX Offsets
S8fab08rsp_tup = namedtuple('S8fab08rsp_tup', ' realtimeRtkRtxOffsetsStatus realtimeRtkRtxOffsetsAccuracy realtimeRtkRtxOffsetsEast realtimeRtkRtxOffsetsNorth realtimeRtkRtxOffsetsUp')
S8fab08rsp_bin = '=Bffff'
# Response with the configuration for genral parameters
S8fac0100rsp_tup = namedtuple('S8fac0100rsp_tup', ' APIversion enabled targetHeight sprayerSuspensionType sensingMode groundSensitivity canopySensitivity groundFilter canopyFilter chevronThresh maximumHeight minimumHeight minSafeHeightBelowTarget heightStep aggressiveness downSlewLim downGainStabilizer wingPhasingHeightThreshold useKato autoDisableTimeout')
S8fac0100rsp_bin = '=BBdbbBBBBdddddhHHdBL'
# 
S8fac0101rspsensors_tup = namedtuple('S8fac0101rspsensors_tup', ', serialNumber enabled location sideOffset nozzleOffset')
S8fac0101rspsensors_bin = '=11sBbdd'
# Response with the configuration for sensor parameters
S8fac0101rsp_tup = namedtuple('S8fac0101rsp_tup', ' APIversion numberOfSensors sensorsArray')
S8fac0101rsp_bin = '=BB?S8fac0101rspsensors'
# 
S8fac0102rspactuators_tup = namedtuple('S8fac0102rspactuators_tup', ', serialNumber enabled slopeCalibrated deadbandCalibrated zone operation positiveSlope positiveDeadband negativeSlope negativeDeadband calSensorArmLength aggressiveness isInverted fineControlZone')
S8fac0102rspactuators_bin = '=11sBBBBbdddddhBd'
# Response with the configuration for actuator parameters
S8fac0102rsp_tup = namedtuple('S8fac0102rsp_tup', ' APIversion numberOfActuators actuatorsArray')
S8fac0102rsp_bin = '=BB?S8fac0102rspactuators'
# Request for actuator calibration state
S8fac02rsp_tup = namedtuple('S8fac02rsp_tup', ' APIversion CalState ZoneLocation success')
S8fac02rsp_bin = '=BBBB'
# Request for actuator calibration status
S8fac03rsp_tup = namedtuple('S8fac03rsp_tup', ' APIversion CalType CalState ZoneLocation CalProgress SensorHeight ActuatorCmd DeadbandPos DeadbandNeg SlopePos SlopeNeg SensorArmLen isInverted')
S8fac03rsp_bin = '=BBBBffffffffB'
# 
S8fac04rspZoneStatus_tup = namedtuple('S8fac04rspZoneStatus_tup', ' ZoneLocation ZoneState ZoneHeight ZoneCmd')
S8fac04rspZoneStatus_bin = '=BBff'
# 
S8fac04rspSensorStatus_tup = namedtuple('S8fac04rspSensorStatus_tup', ' SensorLocation SensorHeight')
S8fac04rspSensorStatus_bin = '=bf'
# Reports system information including sensor heights, zone states and alerts
S8fac04rsp_tup = namedtuple('S8fac04rsp_tup', ' APIversion SystemMode AlertStatus AvgHeight NumZones ZoneArray NumSensors SensorsArray')
S8fac04rsp_bin = '=BBBfB?S8fac04rspZoneStatusB?S8fac04rspSensorStatus'
# Commands to commit system actions
S8fac05rsp_tup = namedtuple('S8fac05rsp_tup', ' APIversion StateAction ZoneLocation success')
S8fac05rsp_bin = '=BBBB'
# Alert description
S8fac06rspAlertDesc_tup = namedtuple('S8fac06rspAlertDesc_tup', ' AlertID AudibleType, serialNumber Action RESERVED1 RESERVED2')
S8fac06rspAlertDesc_bin = '=BB11sBLL'
# Reponse of a list of all active faults
S8fac06rsp_tup = namedtuple('S8fac06rsp_tup', ' APIversion NumAlerts AlertArray')
S8fac06rsp_bin = '=BB?S8fac06rspAlertDesc'
# Devices
S8fac07rspDevices_tup = namedtuple('S8fac07rspDevices_tup', ' DeviceID ConnectionStatus, serialNumber versionMajor versionMinor ErrorCode RESERVED1 RESERVED2')
S8fac07rspDevices_bin = '=BB11sHHLLL'
# Reponse of a list of all attached devices
S8fac07rsp_tup = namedtuple('S8fac07rsp_tup', ' APIversion RESERVED1 RESERVED2 NumDevices DevicesArray')
S8fac07rsp_bin = '=BLLB?S8fac07rspDevices'
# Reports Centerpoint/Rangepoint RTX Passcode if available. In case no passcodes are available, PasscodeType is set to 255. Request Packet: 0x8e 0xad 0x00
S8fad00rsp_tup = namedtuple('S8fad00rsp_tup', ' PasscodeType PasscodeLength Passcode')
S8fad00rsp_bin = '=BB?B'
# Acknowledges command to clear passcode. Command Packet is 0x8e 0xad 0x01
S8fad01ack_tup = namedtuple('S8fad01ack_tup', '')
S8fad01ack_bin = '='
# Reports Centerpoint/Rangepoint RTX position allowed flag status. Request Packet: 0x8e 0xad 0x02
S8fad02rsp_tup = namedtuple('S8fad02rsp_tup', ' PositionAllowed')
S8fad02rsp_bin = '=B'
# Type and SNR for a single frequency band
Sd500rspFreqBandInfo_tup = namedtuple('Sd500rspFreqBandInfo_tup', ' FreqBand SNR')
Sd500rspFreqBandInfo_bin = '=BH'
# Info for a single satellite
Sd500rspSatInfo_tup = namedtuple('Sd500rspSatInfo_tup', ' SVId System Azimuth Elevation SatFlags, FreqBandArray')
Sd500rspSatInfo_bin = '=HBffH3?Sd500rspFreqBandInfo'
# Reports satellite constellation info. Note that multiple packets may be required to describe entire constellation.
Sd500rsp_tup = namedtuple('Sd500rsp_tup', ' AntennaId NumPackets SequenceId TotalNumSats NumSatsUsedInFix ConstellationFlags NumSatsInPacket SatInfoArray')
Sd500rsp_bin = '=BBBHHHB?Sd500rspSatInfo'
# Report which satellite system is enabled/disabled
Sd502rsp_tup = namedtuple('Sd502rsp_tup', ' SatelliteSystemControlFlag')
Sd502rsp_bin = '=H'
# Acknowledges the success or failure of an authenticated command
Sd6ack_tup = namedtuple('Sd6ack_tup', ' DomainId CmdId Result')
Sd6ack_bin = '=BBb'
# Lock or Unlock all stinger channels. This packet is for diagnostic purposes only and may change without notice. Command Packet: 0xC7 0x00
Sd700ack_tup = namedtuple('Sd700ack_tup', ' AcknowledgeChannelLockId')
Sd700ack_bin = '=B'
# Acknowledge RF Band and Filter Switches setting command.
Sd701ack_tup = namedtuple('Sd701ack_tup', ' Band_Select Filter_Select')
Sd701ack_bin = '=BB'
# Return the RF Band and Filter Switch setting for the signal requested.
Sd701rsp_tup = namedtuple('Sd701rsp_tup', ' Band_Select Filter_Select')
Sd701rsp_bin = '=BB'
# Response to the Bluetooth pairing information request
S8fae00rsp_tup = namedtuple('S8fae00rsp_tup', ' PairingStatus RemainingTime PairedDevicesCount ConnectedDevicesCount')
S8fae00rsp_bin = '=BHBB'
# Response to setting the power state of the Bluetooth module
S8fae01rsp_tup = namedtuple('S8fae01rsp_tup', ' BluetoothPowerState')
S8fae01rsp_bin = '=B'
# Response to setting the Bluetooth pairing state of the receiver
S8fae02rsp_tup = namedtuple('S8fae02rsp_tup', ' BluetoothPairingState RemainingTime')
S8fae02rsp_bin = '=BH'
# Reponse to unpairing all Bluetooth devices
S8fae03rsp_tup = namedtuple('S8fae03rsp_tup', ' ClearedDevicesCount')
S8fae03rsp_bin = '=B'
# Paring state change event
S8fae04rsp_tup = namedtuple('S8fae04rsp_tup', ' BluetoothPairingState RemainingTime')
S8fae04rsp_bin = '=BH'
# A notification for a Bluetooth device pairing or connection event
S8fae05rsp_tup = namedtuple('S8fae05rsp_tup', ' DeviceEventType DeviceNameLength DeviceName')
S8fae05rsp_bin = '=LB?c'
# Acknowledges the request for Bluetooth device event notifications (8eae05)
S8fae05ack_tup = namedtuple('S8fae05ack_tup', ' DeviceEventType')
S8fae05ack_bin = '=L'
# Clothoid New Path Response
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c2300rsp_base = namedtuple('Sbf4c2300rsp_base', ' type, Length')

# Factory function for backward compatibility
def Sbf4c2300rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c2300rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c2300rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c2300rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c2300rsp_tup._make = lambda seq: Sbf4c2300rsp_tup(*seq)
Sbf4c2300rsp_bin = '=B?'
# Clothoid Append Path Response
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c2301rsp_base = namedtuple('Sbf4c2301rsp_base', ' Sequence_Number, Length')

# Factory function for backward compatibility
def Sbf4c2301rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c2301rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c2301rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c2301rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c2301rsp_tup._make = lambda seq: Sbf4c2301rsp_tup(*seq)
Sbf4c2301rsp_bin = '=L?'
# Clothoid Activate Clothoid Guidance Response
# Base namedtuple with Length field for CheckedLengthField compatibility
Sbf4c2302rsp_base = namedtuple('Sbf4c2302rsp_base', ' Activate, Length')

# Factory function for backward compatibility
def Sbf4c2302rsp_tup(*args):
    # If Length field isn't provided, add it with default value 0
    # (Length will be automatically recalculated during encoding)
    num_base_fields = len(Sbf4c2302rsp_base._fields)
    if len(args) < num_base_fields:
        # Pad with 0 for missing Length field
        return Sbf4c2302rsp_base(*args, 0)
    # Otherwise use args as provided
    return Sbf4c2302rsp_base(*args)

# Add _make method for compatibility with existing code
Sbf4c2302rsp_tup._make = lambda seq: Sbf4c2302rsp_tup(*seq)
Sbf4c2302rsp_bin = '=B?'
  #----------------------------------------------------------------------
  #
  #----------------------------------------------------------------------
  # @name Named Tuple List
  
ClientTupleList = [
  S00cmd_tup,
  S1a00cmd_tup,
  S1a0200cmd_tup,
  S1a0201cmd_tup,
  S1a0202cmd_tup,
  S1a0300cmd_tup,
  S1a0301cmd_tup,
  S1e4bcmd_tup,
  S1freq_tup,
  S1freqv1_tup,
  S20req_tup,
  S21req_tup,
  S22cmd_tup,
  S25cmd_tup,
  S26req_tup,
  S27req_tup,
  S2creq_tup,
  S2ccmd_tup,
  S33req_tup,
  S35req_tup,
  S35cmd_tup,
  S38cmd_tup,
  S3breq_tup,
  S3creq_tup,
  S3f02cmd_tup,
  S3f2200req_tup,
  S3f2200cmd_tup,
  S62req_tup,
  S62cmd_tup,
  S65req_tup,
  S690000req_tup,
  S690001req_tup,
  S690002cmd_tup,
  S690003cmd_tup,
  S6932req_tup,
  S6940req_tup,
  S6940cmd_tup,
  S6941req_tup,
  S6950req_tup,
  S6950cmd_tup,
  S6951req_tup,
  S6960req_tup,
  S6961req_tup,
  S6962req_tup,
  S697000req_tup,
  S697001req_tup,
  S697002req_tup,
  S697003req_tup,
  S697004req_tup,
  S697005req_tup,
  S697006cmd_tup,
  S697007cmd_tup,
  S697008cmd_tup,
  S697009cmd_tup,
  S69700acmd_tup,
  S69700bcmd_tup,
  S697100req_tup,
  S697100cmd_tup,
  S697101req_tup,
  S697101cmd_tup,
  S697103req_tup,
  S697103cmd_tup,
  S6a01req_tup,
  S6a01cmd_tup,
  S6b00req_tup,
  S6b00cmd_tup,
  S6b02req_tup,
  S6e03cmd_tup,
  S70cmd_tup,
  S77req_tup,
  S77cmd_tup,
  S7a07req_tup,
  S7a07cmd_tup,
  S7a08req_tup,
  S7a08cmd_tup,
  S7a80req_tup,
  S7a80cmd_tup,
  S7a86req_tup,
  S7a8600cmd_tup,
  S7a8602cmd_tup,
  S7a8603cmd_tup,
  S7a8604cmd_tup,
  S7a8605cmd_tup,
  S7c00req_tup,
  S7c00cmd_tup,
  S7c01req_tup,
  S7c01cmd_tup,
  S7c02req_tup,
  S7c02cmd_tup,
  S7c09req_tup,
  S7c09cmd_tup,
  S8e7breq_tup,
  S8e7ccmd_tup,
  S8e7freq_tup,
  S8e80req_tup,
  S8e81req_tup,
  S8e84cmd_tup,
  S8e85req_tup,
  S8e88req_tup,
  S8e88cmd_tup,
  S8e89req_tup,
  S8e89cmd_tup,
  S8e8breq_tup,
  S8e8c00cmd_tup,
  S8e8c01req_tup,
  S8e8c03req_tup,
  S8e8c03cmd_tup,
  S8e8c04req_tup,
  S8e8c04cmd_tup,
  S8e8c05cmd_tup,
  S8e8freq_tup,
  S8e91req_tup,
  S8e91cmd_tup,
  S8e931500req_tup,
  S8e93150101req_tup,
  S8e93150102req_tup,
  S8e93150103req_tup,
  S8e93150104req_tup,
  S8e93150201req_tup,
  S8e93150202req_tup,
  S8e93150203req_tup,
  S8e931503req_tup,
  S8e9areq_tup,
  S8e9ereq_tup,
  S8e9ecmd_tup,
  S8e9f00req_tup,
  S8e9f00cmd_tup,
  S8e9f01req_tup,
  S8e9f02req_tup,
  S8e9f02cmd_tup,
  S8e9f03req_tup,
  S8e9f03cmd_tup,
  S8e9f04req_tup,
  S8e9f04cmd_tup,
  S8ea0cmd_tup,
  S8ea1cmd_tup,
  S8ea2req_tup,
  S8ea3req_tup,
  S8ea304cmd_tup,
  S8ea305cmd_tup,
  S8ea306cmd_tup,
  S8ea307cmd_tup,
  S8ea4req_tup,
  S8ea405cmd_tup,
  S8ea406cmd_tup,
  S8ea407cmd_tup,
  S8ea500req_tup,
  S8ea500cmd_tup,
  S8ea501req_tup,
  S8ea501cmd_tup,
  S8ea502cmd_tup,
  S8ea601cmd_tup,
  S8ea602req_tup,
  S8ea608req_tup,
  S8ea617req_tup,
  S8ea622req_tup,
  S8ea623req_tup,
  S8ea624req_tup,
  S8ea625cmd_tup,
  S8ea626req_tup,
  S8ea627cmd_tup,
  S8ea628cmd_tup,
  S8ea629req_tup,
  S8ea630req_tup,
  S8ea631req_tup,
  S8ea632req_tup,
  S8ea632cmd_tup,
  S8ea633req_tup,
  S8ea634req_tup,
  S8ea640cmd_tup,
  S8ea641cmd_tup,
  S8ea642cmd_tup,
  S8ea643cmd_tup,
  S8ea644cmd_tup,
  S8ea645cmd_tup,
  S8ea646cmd_tup,
  S8ea647req_tup,
  S8ea648cmd_tup,
  S8ea70000cmd_tup,
  S8ea70001cmd_tup,
  S8ea70002cmd_tup,
  S8ea70003cmd_tup,
  S8ea70100req_tup,
  S8ea70101req_tup,
  S8ea70102req_tup,
  S8ea70103req_tup,
  S8ea800req_tup,
  S8ea801cmd_tup,
  S8ea801req_tup,
  S8ea802cmd_tup,
  S8ea802req_tup,
  S8ea803cmd_tup,
  S8ea803req_tup,
  S8ea804cmd_tup,
  S8ea804req_tup,
  S8ea805cmd_tup,
  S8ea806cmd_tup,
  S8ea806req_tup,
  S8ea900req_tup,
  S8ea90100cmd_tup,
  S8ea90101cmd_tup,
  S8ea90101req_tup,
  S8ea90102cmd_tup,
  S8ea90103cmd_tup,
  S8ea90104req_tup,
  S8ea90104cmd_tup,
  S8ea90105cmd_tup,
  S8ea90106req_tup,
  S8ea90106cmd_tup,
  S8ea90107req_tup,
  S8ea90107cmd_tup,
  S8ea90108req_tup,
  S8ea90108cmd_tup,
  S8ea90130req_tup,
  S8ea90131req_tup,
  S8ea90200req_tup,
  S8ea90200cmd_tup,
  S8ea90201req_tup,
  S8ea90201cmd_tup,
  S8ea90202req_tup,
  S8ea90202cmd_tup,
  S8ea90300req_tup,
  S8ea90301cmd_tup,
  S8ea90400req_tup,
  S8ea90400cmd_tup,
  S8ea905cmd_tup,
  S8ea90600req_tup,
  S8ea90700req_tup,
  S8ea90700cmd_tup,
  S8ea90701req_tup,
  S8ea90701cmd_tup,
  S8ea90703req_tup,
  S8ea90703cmd_tup,
  S8ea90704req_tup,
  S8ea90704cmd_tup,
  S8ea90705req_tup,
  S8ea90705cmd_tup,
  S8ea90706req_tup,
  S8ea90707req_tup,
  S8ea90707cmd_tup,
  S8ea90708req_tup,
  S8ea90800req_tup,
  S8ea90800cmd_tup,
  S8ea909req_tup,
  S8ea909cmd_tup,
  S8ea90a00req_tup,
  S8ea90a01req_tup,
  S8ea910req_tup,
  S8ea911req_tup,
  S8ea912req_tup,
  S8ea913req_tup,
  S8ea91500cmd_tup,
  S8ea91501cmd_tup,
  S8ea91502cmd_tup,
  S8ea91503cmd_tup,
  S8ea91504cmd_tup,
  S8ea9160000req_tup,
  S8ea9160000cmd_tup,
  S8ea9160001req_tup,
  S8ea9160001cmd_tup,
  S8ea9160002req_tup,
  S8ea9160002cmd_tup,
  S8ea9160100req_tup,
  S8ea9160100cmd_tup,
  S8ea91602req_tup,
  S8ea91602cmd_tup,
  S8ea91603cmd_tup,
  S8ea91604cmd_tup,
  S8ea91605cmd_tup,
  S8ea91606req_tup,
  S8ea91700req_tup,
  S8ea91700cmd_tup,
  S8ea91701cmd_tup,
  S8ea91701req_tup,
  S8ea91702req_tup,
  S8ea91703req_tup,
  S8ea91703cmd_tup,
  S8ea918req_tup,
  S8ea9a5req_tup,
  S8eaa00req_tup,
  S8eaa00cmd_tup,
  S8eab00req_tup,
  S8eab01req_tup,
  S8eab02cmd_tup,
  S8eab03req_tup,
  S8eab04cmd_tup,
  S8eab05cmd_tup,
  S8eab05req_tup,
  S8eab06cmd_tup,
  S8eab07req_tup,
  S8eab07cmd_tup,
  S8eab08req_tup,
  S8eac0000cmd_tup,
  S8eac0001cmd_tup,
  S8eac0002cmd_tup,
  S8eac0100req_tup,
  S8eac0101req_tup,
  S8eac0102req_tup,
  S8eac02cmd_tup,
  S8eac03req_tup,
  S8eac04cmd_tup,
  S8eac05cmd_tup,
  S8eac06req_tup,
  S8eac07req_tup,
  S8ead00req_tup,
  S8ead01cmd_tup,
  S8ead02req_tup,
  S8ead03cmd_tup,
  S8eae00req_tup,
  S8eae01cmd_tup,
  S8eae02cmd_tup,
  S8eae03cmd_tup,
  S8eae04req_tup,
  S8eae05req_tup,
  S8fa90708req_tup,
  Sb000req_tup,
  Sb000cmd_tup,
  Sb001cmd_tup,
  Sbb00req_tup,
  Sbb00cmd_tup,
  Sbcreq_tup,
  Sbccmd_tup,
  Sbe40cmd_tup,
  Sbe400000cmd_tup,
  Sbe400003cmd_tup,
  Sbe400100cmd_tup,
  Sbe400103cmd_tup,
  Sbe401400cmd_tup,
  Sbe401401cmd_tup,
  Sbe41cmd_tup,
  Sbe42cmd_tup,
  Sbe4200cmd_tup,
  Sbe4201cmd_tup,
  Sbe4202cmd_tup,
  Sbe4301cmd_tup,
  Sbe4303cmd_tup,
  Sbe4306cmd_tup,
  Sbe43060000cmd_tup,
  Sbe43060001cmd_tup,
  Sbe43060002cmd_tup,
  Sbe43060100cmd_tup,
  Sbe43060101cmd_tup,
  Sbe43060102cmd_tup,
  Sbe430bcmd_tup,
  Sbe430dcmd_tup,
  Sbe44cmd_tup,
  Sbe45cmd_tup,
  Sbe46cmd_tup,
  Sbe4600cmd_tup,
  Sbe47cmd_tup,
  Sbe470500cmd_tup,
  Sbe470501cmd_tup,
  Sbe470502cmd_tup,
  Sbe470503cmd_tup,
  Sbe470504cmd_tup,
  Sbe470505cmd_tup,
  Sbe470506cmd_tup,
  Sbe470507cmd_tup,
  Sbe470508cmd_tup,
  Sbe470509cmd_tup,
  Sbe47050acmd_tup,
  Sbe47050bcmd_tup,
  Sbe4707cmd_tup,
  Sbe470e08cmd_tup,
  Sbe470e09cmd_tup,
  Sbe471400cmd_tup,
  Sbe471401cmd_tup,
  Sbe471402cmd_tup,
  Sbe471ecmd_tup,
  Sbe4acmd_tup,
  Sbe4a0b00cmd_tup,
  Sbe4a0b01cmd_tup,
  Sbe4a0ccmd_tup,
  Sbe4a0c00cmd_tup,
  Sbe4a0c08cmd_tup,
  Sbe4a0c09cmd_tup,
  Sbe4bcmd_tup,
  Sbe4c00000004cmd_tup,
  Sbe4c00000104cmd_tup,
  Sbe4c00000204cmd_tup,
  Sbe4c00000704cmd_tup,
  Sbe4c0100cmd_tup,
  Sbe4c0106cmd_tup,
  Sbe4c0107cmd_tup,
  Sbe4c0108req_tup,
  Sbe4c0108cmd_tup,
  Sbe4c010acmd_tup,
  Sbe4c010breq_tup,
  Sbe4c010bcmd_tup,
  Sbe4c010dreq_tup,
  Sbe4c010dcmd_tup,
  Sbe4c010ereq_tup,
  Sbe4c010ecmd_tup,
  Sbe4c010freq_tup,
  Sbe4c010fcmd_tup,
  Sbe4c011000req_tup,
  Sbe4c011001cmd_tup,
  Sbe4c011002cmd_tup,
  Sbe4c011003req_tup,
  Sbe4c011004cmd_tup,
  Sbe4c0111cmd_tup,
  Sbe4c0114cmd_tup,
  Sbe4c011706cmd_tup,
  Sbe4c011710cmd_tup,
  Sbe4c011711cmd_tup,
  Sbe4c011713cmd_tup,
  Sbe4c011720cmd_tup,
  Sbe4c011721cmd_tup,
  Sbe4c0119cmd_tup,
  Sbe4c011acmd_tup,
  Sbe4c2000req_tup,
  Sbe4c2000cmd_tup,
  Sbe4c2001req_tup,
  Sbe4c2300cmd_tup,
  Sbe4c2301cmd_tup,
  Sbe4c2302req_tup,
  Sbe4c2302cmd_tup,
  Sbe4c8000cmd_tup,
  Sbe4c8001cmd_tup,
  Sbe4dcmd_tup,
  Sbe4ecmd_tup,
  Sbe4fcmd_tup,
  Sbe50cmd_tup,
  Sbe5014cmd_tup,
  Sbe51cmd_tup,
  Sbe52cmd_tup,
  Sbe53cmd_tup,
  Sbe530600cmd_tup,
  Sbe530601cmd_tup,
  Sbe54cmd_tup,
  Sbe55cmd_tup,
  Sbe56cmd_tup,
  Sbe57cmd_tup,
  Sbe570507cmd_tup,
  Sbe5acmd_tup,
  Sbe5ccmd_tup,
  Sbe5c0100cmd_tup,
  Sbe5c0106cmd_tup,
  Sbe5c0107cmd_tup,
  Sbe5c010acmd_tup,
  Sbe5c010bcmd_tup,
  Sbe5c011000cmd_tup,
  Sbe5c011001cmd_tup,
  Sbe5c011002cmd_tup,
  Sbe5c011003cmd_tup,
  Sbe5c011004cmd_tup,
  Sbe5c0111cmd_tup,
  Sbe5c0114cmd_tup,
  Sbe5c011700cmd_tup,
  Sbe5c011706cmd_tup,
  Sbe5c011710cmd_tup,
  Sbe5c011711cmd_tup,
  Sbe5c011713cmd_tup,
  Sbe5c0119cmd_tup,
  Sbe60cmd_tup,
  Sbe6014cmd_tup,
  Sbe630600cmd_tup,
  Sbe630601cmd_tup,
  Sbe710000req_tup,
  Sbe710100req_tup,
  Sbe710200req_tup,
  Sbe710201req_tup,
  Sbe710300req_tup,
  Sbe710400req_tup,
  Sbe710500req_tup,
  Sbe710600req_tup,
  Sbe710700req_tup,
  Sbe710800req_tup,
  Sbe710900req_tup,
  Sbe710a00req_tup,
  Sbe710b00req_tup,
  Sbe710c00req_tup,
  Sbe710d00req_tup,
  Sbe710e00req_tup,
  Sbe710f00req_tup,
  Sbe8000cmd_tup,
  Sc500req_tup,
  Sc501cmd_tup,
  Sc502req_tup,
  Sc60000cmd_tup,
  Sc60100cmd_tup,
  Sc60200cmd_tup,
  Sc60400cmd_tup,
  Sc700cmd_tup,
  Sc701req_tup,
  Sc701cmd_tup,
0
]

ServerTupleList = [
  S00rsp_tup,
  S13rsp_tup,
  S1a01rsp_tup,
  S1a0200rsp_tup,
  S1a0201rsp_tup,
  S1a0300rsp_tup,
  S1a0301rsp_tup,
  S40rsp_tup,
  S41rsp_tup,
  S42rsp_tup,
  S43rsp_tup,
  S45rsp_tup,
  S45rspv1_tup,
  S46rsp_tup,
  S47rsp_tup,
  S48rsp_tup,
  S4arsp_tup,
  S4arspv1_tup,
  S4arspv2_tup,
  S4brsp_tup,
  S4crsp_tup,
  S4frsp_tup,
  S53rsp_tup,
  S55rsp_tup,
  S58rsp_tup,
  S5822rsp_tup,
  S5823rsp_tup,
  S5824rsp_tup,
  S5825rsp_tup,
  S5826rsp_tup,
  S5brsp_tup,
  S5crsp_tup,
  S5f01rsp_tup,
  S5f02rsp_tup,
  S5f10rsp_tup,
  S5f2200rsp_tup,
  S5f2201rsp_tup,
  S6a01rsp_tup,
  S6drsp_tup,
  S6f01rsp_tup,
  S6f10rsp_tup,
  S6f20rsp_tup,
  S6f21rsp_tup,
  S70rsp_tup,
  S78rsp_tup,
  S7b07rsp_tup,
  S7b08ack_tup,
  S7b08rsp_tup,
  S7b80rsp_tup,
  S7b8600rsp_tup,
  S7b8602rsp_tup,
  S7b8603rsp_tup,
  S7b8605rsp_tup,
  S7b860604rsp_tup,
  S7d00rsp_tup,
  S7d01rsp_tup,
  S7d02rsp_tup,
  S7d09rsp_tup,
  S82rsp_tup,
  S82rspv1_tup,
  S83rsp_tup,
  S890000rsp_tup,
  S890001rsp_tup,
  S890002rsp_tup,
  S890003rsp_tup,
  S893308rsp_tup,
  S8940rsp_tup,
  S8941rsp_tup,
  S8950rsp_tup,
  S8951rsp_tup,
  S8960rsp_tup,
  S8961rsp_tup,
  S8962rsp_tup,
  S897000rsp_tup,
  S897001rsp_tup,
  S897002rsp_tup,
  S897003rsp_tup,
  S897004rsp_tup,
  S897005rsp_tup,
  S897006ack_tup,
  S897007ack_tup,
  S897008ack_tup,
  S897009ack_tup,
  S89700aack_tup,
  S89700back_tup,
  S89700cack_tup,
  S89700drsp_tup,
  S897100rsp_tup,
  S897100ack_tup,
  S897101rsp_tup,
  S897101ack_tup,
  S897103rsp_tup,
  S897103ack_tup,
  S8b00rsp_tup,
  S8b02rsp_tup,
  S8frsp_tup,
  S8f77rsp_tup,
  S8f770rsp_tup,
  S8f7brsp_tup,
  S8f7cack_tup,
  S8f7frsp_tup,
  S8f80rsp_tup,
  S8f84ack_tup,
  S8f85rsp_tup,
  S8f89rsp_tup,
  S8f89ack_tup,
  S8f8brsp_tup,
  S8f8cack_tup,
  S8f8c01rsp_tup,
  S8f8c02rsp_tup,
  S8f8c03rsp_tup,
  S8f8c04rsp_tup,
  S8f8frsp_tup,
  S8f91rsp_tup,
  S8f91ack_tup,
  S8f9306rsp_tup,
  S8f931500rsp_tup,
  S8f93150100rsp_tup,
  S8f93150101rsp_tup,
  S8f93150102rsp_tup,
  S8f93150103rsp_tup,
  S8f93150104rsp_tup,
  S8f93150200rsp_tup,
  S8f93150201rsp_tup,
  S8f93150202rsp_tup,
  S8f93150203rsp_tup,
  S8f931503rsp_tup,
  S8f9arsp_tup,
  S8f9ersp_tup,
  S8f9f00rsp_tup,
  S8f9f00ack_tup,
  S8f9f01rsp_tup,
  S8f9f02rsp_tup,
  S8f9f02ack_tup,
  S8f9f03rsp_tup,
  S8f9f03ack_tup,
  S8f9f04rsp_tup,
  S8f9f04ack_tup,
  S8fa0rsp_tup,
  S8fa1rsp_tup,
  S8fa2rsp_tup,
  S8fa300rsp_tup,
  S8fa301rsp_tup,
  S8fa302rsp_tup,
  S8fa303rsp_tup,
  S8fa304rsp_tup,
  S8fa305rsp_tup,
  S8fa306rsp_tup,
  S8fa307ack_tup,
  S8fa405rsp_tup,
  S8fa406rsp_tup,
  S8fa407rsp_tup,
  S8fa500rsp_tup,
  S8fa501rsp_tup,
  S8fa502ack_tup,
  S8fa601ack_tup,
  S8fa602rsp_tup,
  S8fa608rsp_tup,
  S8fa617rsp_tup,
  S8fa622rsp_tup,
  S8fa623rsp_tup,
  S8fa624rsp_tup,
  S8fa625ack_tup,
  S8fa626rsp_tup,
  S8fa627ack_tup,
  S8fa628ack_tup,
  S8fa629rsp_tup,
  S8fa630rsp_tup,
  S8fa631rsp_tup,
  S8fa632rsp_tup,
  S8fa632ack_tup,
  S8fa633rsp_tup,
  S8fa634ack_tup,
  S8fa634rsp_tup,
  S8fa640ack_tup,
  S8fa641ack_tup,
  S8fa642ack_tup,
  S8fa643ack_tup,
  S8fa644ack_tup,
  S8fa645ack_tup,
  S8fa646ack_tup,
  S8fa647rsp_tup,
  S8fa648ack_tup,
  S8fa70000rsp_tup,
  S8fa70001rsp_tup,
  S8fa70002rsp_tup,
  S8fa70003rsp_tup,
  S8fa70100rsp_tup,
  S8fa70101rsp_tup,
  S8fa70102rsp_tup,
  S8fa800rsp_tup,
  S8fa801ack_tup,
  S8fa801rsp_tup,
  S8fa802ack_tup,
  S8fa802rsp_tup,
  S8fa803ack_tup,
  S8fa803rsp_tup,
  S8fa804ack_tup,
  S8fa804rsp_tup,
  S8fa805ack_tup,
  S8fa806ack_tup,
  S8fa806rsp_tup,
  S8fa900rsp_tup,
  S8fa90100ack_tup,
  S8fa90100rsp_tup,
  S8fa90101ack_tup,
  S8fa90101rsp_tup,
  S8fa90102ack_tup,
  S8fa90103rsp_tup,
  S8fa90104rsp_tup,
  S8fa90105ack_tup,
  S8fa90106rsp_tup,
  S8fa90107rsp_tup,
  S8fa90108rsp_tup,
  S8fa90130rsp_tup,
  S8fa90131rsp_tup,
  S8fa90200rsp_tup,
  S8fa90201rsp_tup,
  S8fa90202rsp_tup,
  S8fa90300rsp_tup,
  S8fa90400rsp_tup,
  S8fa905ack_tup,
  S8fa90600rsp_tup,
  S8fa90700rsp_tup,
  S8fa90701rsp_tup,
  S8fa90703rsp_tup,
  S8fa90704rsp_tup,
  S8fa90705rsp_tup,
  S8fa90706rsp_tup,
  S8fa90707rsp_tup,
  S8fa90800rsp_tup,
  S8fa909ack_tup,
  S8fa909rsp_tup,
  S8fa90a00rsp_tup,
  S8fa90a01rsp_tup,
  S8fa910rsp_tup,
  S8fa911rsp_tup,
  S8fa912rsp_tup,
  S8fa913rsp_tup,
  S8fa914rsp_tup,
  S8fa91500rsp_tup,
  S8fa91501rsp_tup,
  S8fa91502rsp_tup,
  S8fa91503rsp_tup,
  S8fa91504rsp_tup,
  S8fa91599rsp_tup,
  S8fa9160000rsp_tup,
  S8fa9160001rsp_tup,
  S8fa9160002rsp_tup,
  S8fa9160100rsp_tup,
  S8fa91602rsp_tup,
  S8fa91603rsp_tup,
  S8fa91604rsp_tup,
  S8fa91605rsp_tup,
  S8fa91606rsp_tup,
  S8fa91700rsp_tup,
  S8fa91701rsp_tup,
  S8fa91702rsp_tup,
  S8fa91703rsp_tup,
  S8fa918rsp_tup,
  S8fa9a5rsp_tup,
  S8faa00rsp_tup,
  S8fab00rsp_tup,
  S8fab01rsp_tup,
  S8fab02ack_tup,
  S8fab03rsp_tup,
  S8fab04ack_tup,
  S8fab05rsp_tup,
  S8fab06rsp_tup,
  S8fab07rsp_tup,
  S8fab08rsp_tup,
  S8fac0100rsp_tup,
  S8fac0101rsp_tup,
  S8fac0102rsp_tup,
  S8fac02rsp_tup,
  S8fac03rsp_tup,
  S8fac04rsp_tup,
  S8fac05rsp_tup,
  S8fac06rsp_tup,
  S8fac07rsp_tup,
  S8fad00rsp_tup,
  S8fad01ack_tup,
  S8fad02rsp_tup,
  S8fae00rsp_tup,
  S8fae01rsp_tup,
  S8fae02rsp_tup,
  S8fae03rsp_tup,
  S8fae04rsp_tup,
  S8fae05rsp_tup,
  S8fae05ack_tup,
  Sb080rsp_tup,
  Sb081rsp_tup,
  Sbb00rsp_tup,
  Sbcrsp_tup,
  Sbf1arsp_tup,
  Sbf40rsp_tup,
  Sbf400000rsp_tup,
  Sbf400100rsp_tup,
  Sbf401400rsp_tup,
  Sbf401401rsp_tup,
  Sbf41rsp_tup,
  Sbf42rsp_tup,
  Sbf4200rsp_tup,
  Sbf4201rsp_tup,
  Sbf4202rsp_tup,
  Sbf43rsp_tup,
  Sbf4301rsp_tup,
  Sbf4303rsp_tup,
  Sbf4306rsp_tup,
  Sbf44rsp_tup,
  Sbf45rsp_tup,
  Sbf46rsp_tup,
  Sbf47rsp_tup,
  Sbf470500rsp_tup,
  Sbf470501rsp_tup,
  Sbf470502rsp_tup,
  Sbf470503rsp_tup,
  Sbf470504rsp_tup,
  Sbf470505rsp_tup,
  Sbf470506rsp_tup,
  Sbf470507rsp_tup,
  Sbf470508rsp_tup,
  Sbf470509rsp_tup,
  Sbf47050arsp_tup,
  Sbf47050brsp_tup,
  Sbf4707rsp_tup,
  Sbf470e06rsp_tup,
  Sbf470e07rsp_tup,
  Sbf470e08rsp_tup,
  Sbf470e09rsp_tup,
  Sbf471400rsp_tup,
  Sbf471401rsp_tup,
  Sbf471402rsp_tup,
  Sbf471ersp_tup,
  Sbf4arsp_tup,
  Sbf4a0b00rsp_tup,
  Sbf4a0b01rsp_tup,
  Sbf4a0c00rsp_tup,
  Sbf4a0c08rsp_tup,
  Sbf4brsp_tup,
  Sbf4c00000004rsp_tup,
  Sbf4c00000104rsp_tup,
  Sbf4c00000204rsp_tup,
  Sbf4c00000704rsp_tup,
  Sbf4c0101rsp_tup,
  Sbf4c0108rsp_tup,
  Sbf4c010arsp_tup,
  Sbf4c010brsp_tup,
  Sbf4c010drsp_tup,
  Sbf4c010ersp_tup,
  Sbf4c010frsp_tup,
  Sbf4c011000rsp_tup,
  Sbf4c011001rsp_tup,
  Sbf4c011002rsp_tup,
  Sbf4c011003rsp_tup,
  Sbf4c011004rsp_tup,
  Sbf4c0111rsp_tup,
  Sbf4c0114rsp_tup,
  Sbf4c011806rsp_tup,
  Sbf4c011810rsp_tup,
  Sbf4c011811rsp_tup,
  Sbf4c011813rsp_tup,
  Sbf4c011820rsp_tup,
  Sbf4c011821rsp_tup,
  Sbf4c0119rsp_tup,
  Sbf4c011arsp_tup,
  Sbf4c0120rsp_tup,
  Sbf4c0500rsp_tup,
  Sbf4c2000rsp_tup,
  Sbf4c2001rsp_tup,
  Sbf4c2300rsp_tup,
  Sbf4c2301rsp_tup,
  Sbf4c2302rsp_tup,
  Sbf4c8000rsp_tup,
  Sbf4c8001rsp_tup,
  Sbf4c8002rsp_tup,
  Sbf4drsp_tup,
  Sbf4ersp_tup,
  Sbf4frsp_tup,
  Sbf5014rsp_tup,
  Sbf530600rsp_tup,
  Sbf530601rsp_tup,
  Sbf570507rsp_tup,
  Sbf5c0101rsp_tup,
  Sbf5c0106rsp_tup,
  Sbf5c0107rsp_tup,
  Sbf5c010brsp_tup,
  Sbf5c011000rsp_tup,
  Sbf5c011001rsp_tup,
  Sbf5c011002rsp_tup,
  Sbf5c011003rsp_tup,
  Sbf5c011004rsp_tup,
  Sbf5c0111rsp_tup,
  Sbf5c0114rsp_tup,
  Sbf5c0118rsp_tup,
  Sbf5c0119rsp_tup,
  Sbf6014rsp_tup,
  Sbf630600rsp_tup,
  Sbf630601rsp_tup,
  Sbf6800rsp_tup,
  Sbf6801rsp_tup,
  Sbf710000rsp_tup,
  Sbf710100rsp_tup,
  Sbf710200rsp_tup,
  Sbf710201rsp_tup,
  Sbf710300rsp_tup,
  Sbf710400rsp_tup,
  Sbf710500rsp_tup,
  Sbf710600rsp_tup,
  Sbf710700rsp_tup,
  Sbf710800rsp_tup,
  Sbf710900rsp_tup,
  Sbf710a00rsp_tup,
  Sbf710b00rsp_tup,
  Sbf710c00rsp_tup,
  Sbf710d00rsp_tup,
  Sbf710e00rsp_tup,
  Sbf710f00rsp_tup,
  Sd500rsp_tup,
  Sd502rsp_tup,
  Sd6ack_tup,
  Sd700ack_tup,
  Sd701ack_tup,
  Sd701rsp_tup,
0
]

  #----------------------------------------------------------------------
  #
  #----------------------------------------------------------------------
  # @name Binary Struct List
  
ClientStructList = [
  S00cmd_bin,
  S1a00cmd_bin,
  S1a0200cmd_bin,
  S1a0201cmd_bin,
  S1a0202cmd_bin,
  S1a0300cmd_bin,
  S1a0301cmd_bin,
  S1e4bcmd_bin,
  S1freq_bin,
  S1freqv1_bin,
  S20req_bin,
  S21req_bin,
  S22cmd_bin,
  S25cmd_bin,
  S26req_bin,
  S27req_bin,
  S2creq_bin,
  S2ccmd_bin,
  S33req_bin,
  S35req_bin,
  S35cmd_bin,
  S38cmd_bin,
  S3breq_bin,
  S3creq_bin,
  S3f02cmd_bin,
  S3f2200req_bin,
  S3f2200cmd_bin,
  S62req_bin,
  S62cmd_bin,
  S65req_bin,
  S690000req_bin,
  S690001req_bin,
  S690002cmd_bin,
  S690003cmd_bin,
  S6932req_bin,
  S6940req_bin,
  S6940cmd_bin,
  S6941req_bin,
  S6950req_bin,
  S6950cmd_bin,
  S6951req_bin,
  S6960req_bin,
  S6961req_bin,
  S6962req_bin,
  S697000req_bin,
  S697001req_bin,
  S697002req_bin,
  S697003req_bin,
  S697004req_bin,
  S697005req_bin,
  S697006cmd_bin,
  S697007cmd_bin,
  S697008cmd_bin,
  S697009cmd_bin,
  S69700acmd_bin,
  S69700bcmd_bin,
  S697100req_bin,
  S697100cmd_bin,
  S697101req_bin,
  S697101cmd_bin,
  S697103req_bin,
  S697103cmd_bin,
  S6a01req_bin,
  S6a01cmd_bin,
  S6b00req_bin,
  S6b00cmd_bin,
  S6b02req_bin,
  S6e03cmd_bin,
  S70cmd_bin,
  S77req_bin,
  S77cmd_bin,
  S7a07req_bin,
  S7a07cmd_bin,
  S7a08req_bin,
  S7a08cmd_bin,
  S7a80req_bin,
  S7a80cmd_bin,
  S7a86req_bin,
  S7a8600cmd_bin,
  S7a8602cmd_bin,
  S7a8603cmd_bin,
  S7a8604cmd_bin,
  S7a8605cmd_bin,
  S7c00req_bin,
  S7c00cmd_bin,
  S7c01req_bin,
  S7c01cmd_bin,
  S7c02req_bin,
  S7c02cmd_bin,
  S7c09req_bin,
  S7c09cmd_bin,
  S8e7breq_bin,
  S8e7ccmd_bin,
  S8e7freq_bin,
  S8e80req_bin,
  S8e81req_bin,
  S8e84cmd_bin,
  S8e85req_bin,
  S8e88req_bin,
  S8e88cmd_bin,
  S8e89req_bin,
  S8e89cmd_bin,
  S8e8breq_bin,
  S8e8c00cmd_bin,
  S8e8c01req_bin,
  S8e8c03req_bin,
  S8e8c03cmd_bin,
  S8e8c04req_bin,
  S8e8c04cmd_bin,
  S8e8c05cmd_bin,
  S8e8freq_bin,
  S8e91req_bin,
  S8e91cmd_bin,
  S8e931500req_bin,
  S8e93150101req_bin,
  S8e93150102req_bin,
  S8e93150103req_bin,
  S8e93150104req_bin,
  S8e93150201req_bin,
  S8e93150202req_bin,
  S8e93150203req_bin,
  S8e931503req_bin,
  S8e9areq_bin,
  S8e9ereq_bin,
  S8e9ecmd_bin,
  S8e9f00req_bin,
  S8e9f00cmd_bin,
  S8e9f01req_bin,
  S8e9f02req_bin,
  S8e9f02cmd_bin,
  S8e9f03req_bin,
  S8e9f03cmd_bin,
  S8e9f04req_bin,
  S8e9f04cmd_bin,
  S8ea0cmd_bin,
  S8ea1cmd_bin,
  S8ea2req_bin,
  S8ea3req_bin,
  S8ea304cmd_bin,
  S8ea305cmd_bin,
  S8ea306cmd_bin,
  S8ea307cmd_bin,
  S8ea4req_bin,
  S8ea405cmd_bin,
  S8ea406cmd_bin,
  S8ea407cmd_bin,
  S8ea500req_bin,
  S8ea500cmd_bin,
  S8ea501req_bin,
  S8ea501cmd_bin,
  S8ea502cmd_bin,
  S8ea601cmd_bin,
  S8ea602req_bin,
  S8ea608req_bin,
  S8ea617req_bin,
  S8ea622req_bin,
  S8ea623req_bin,
  S8ea624req_bin,
  S8ea625cmd_bin,
  S8ea626req_bin,
  S8ea627cmd_bin,
  S8ea628cmd_bin,
  S8ea629req_bin,
  S8ea630req_bin,
  S8ea631req_bin,
  S8ea632req_bin,
  S8ea632cmd_bin,
  S8ea633req_bin,
  S8ea634req_bin,
  S8ea640cmd_bin,
  S8ea641cmd_bin,
  S8ea642cmd_bin,
  S8ea643cmd_bin,
  S8ea644cmd_bin,
  S8ea645cmd_bin,
  S8ea646cmd_bin,
  S8ea647req_bin,
  S8ea648cmd_bin,
  S8ea70000cmd_bin,
  S8ea70001cmd_bin,
  S8ea70002cmd_bin,
  S8ea70003cmd_bin,
  S8ea70100req_bin,
  S8ea70101req_bin,
  S8ea70102req_bin,
  S8ea70103req_bin,
  S8ea800req_bin,
  S8ea801cmd_bin,
  S8ea801req_bin,
  S8ea802cmd_bin,
  S8ea802req_bin,
  S8ea803cmd_bin,
  S8ea803req_bin,
  S8ea804cmd_bin,
  S8ea804req_bin,
  S8ea805cmd_bin,
  S8ea806cmd_bin,
  S8ea806req_bin,
  S8ea900req_bin,
  S8ea90100cmd_bin,
  S8ea90101cmd_bin,
  S8ea90101req_bin,
  S8ea90102cmd_bin,
  S8ea90103cmd_bin,
  S8ea90104req_bin,
  S8ea90104cmd_bin,
  S8ea90105cmd_bin,
  S8ea90106req_bin,
  S8ea90106cmd_bin,
  S8ea90107req_bin,
  S8ea90107cmd_bin,
  S8ea90108req_bin,
  S8ea90108cmd_bin,
  S8ea90130req_bin,
  S8ea90131req_bin,
  S8ea90200req_bin,
  S8ea90200cmd_bin,
  S8ea90201req_bin,
  S8ea90201cmd_bin,
  S8ea90202req_bin,
  S8ea90202cmd_bin,
  S8ea90300req_bin,
  S8ea90301cmd_bin,
  S8ea90400req_bin,
  S8ea90400cmd_bin,
  S8ea905cmd_bin,
  S8ea90600req_bin,
  S8ea90700req_bin,
  S8ea90700cmd_bin,
  S8ea90701req_bin,
  S8ea90701cmd_bin,
  S8ea90703req_bin,
  S8ea90703cmd_bin,
  S8ea90704req_bin,
  S8ea90704cmd_bin,
  S8ea90705req_bin,
  S8ea90705cmd_bin,
  S8ea90706req_bin,
  S8ea90707req_bin,
  S8ea90707cmd_bin,
  S8ea90708req_bin,
  S8ea90800req_bin,
  S8ea90800cmd_bin,
  S8ea909req_bin,
  S8ea909cmd_bin,
  S8ea90a00req_bin,
  S8ea90a01req_bin,
  S8ea910req_bin,
  S8ea911req_bin,
  S8ea912req_bin,
  S8ea913req_bin,
  S8ea91500cmd_bin,
  S8ea91501cmd_bin,
  S8ea91502cmd_bin,
  S8ea91503cmd_bin,
  S8ea91504cmd_bin,
  S8ea9160000req_bin,
  S8ea9160000cmd_bin,
  S8ea9160001req_bin,
  S8ea9160001cmd_bin,
  S8ea9160002req_bin,
  S8ea9160002cmd_bin,
  S8ea9160100req_bin,
  S8ea9160100cmd_bin,
  S8ea91602req_bin,
  S8ea91602cmd_bin,
  S8ea91603cmd_bin,
  S8ea91604cmd_bin,
  S8ea91605cmd_bin,
  S8ea91606req_bin,
  S8ea91700req_bin,
  S8ea91700cmd_bin,
  S8ea91701cmd_bin,
  S8ea91701req_bin,
  S8ea91702req_bin,
  S8ea91703req_bin,
  S8ea91703cmd_bin,
  S8ea918req_bin,
  S8ea9a5req_bin,
  S8eaa00req_bin,
  S8eaa00cmd_bin,
  S8eab00req_bin,
  S8eab01req_bin,
  S8eab02cmd_bin,
  S8eab03req_bin,
  S8eab04cmd_bin,
  S8eab05cmd_bin,
  S8eab05req_bin,
  S8eab06cmd_bin,
  S8eab07req_bin,
  S8eab07cmd_bin,
  S8eab08req_bin,
  S8eac0000cmd_bin,
  S8eac0001cmd_bin,
  S8eac0002cmd_bin,
  S8eac0100req_bin,
  S8eac0101req_bin,
  S8eac0102req_bin,
  S8eac02cmd_bin,
  S8eac03req_bin,
  S8eac04cmd_bin,
  S8eac05cmd_bin,
  S8eac06req_bin,
  S8eac07req_bin,
  S8ead00req_bin,
  S8ead01cmd_bin,
  S8ead02req_bin,
  S8ead03cmd_bin,
  S8eae00req_bin,
  S8eae01cmd_bin,
  S8eae02cmd_bin,
  S8eae03cmd_bin,
  S8eae04req_bin,
  S8eae05req_bin,
  S8fa90708req_bin,
  Sb000req_bin,
  Sb000cmd_bin,
  Sb001cmd_bin,
  Sbb00req_bin,
  Sbb00cmd_bin,
  Sbcreq_bin,
  Sbccmd_bin,
  Sbe40cmd_bin,
  Sbe400000cmd_bin,
  Sbe400003cmd_bin,
  Sbe400100cmd_bin,
  Sbe400103cmd_bin,
  Sbe401400cmd_bin,
  Sbe401401cmd_bin,
  Sbe41cmd_bin,
  Sbe42cmd_bin,
  Sbe4200cmd_bin,
  Sbe4201cmd_bin,
  Sbe4202cmd_bin,
  Sbe4301cmd_bin,
  Sbe4303cmd_bin,
  Sbe4306cmd_bin,
  Sbe43060000cmd_bin,
  Sbe43060001cmd_bin,
  Sbe43060002cmd_bin,
  Sbe43060100cmd_bin,
  Sbe43060101cmd_bin,
  Sbe43060102cmd_bin,
  Sbe430bcmd_bin,
  Sbe430dcmd_bin,
  Sbe44cmd_bin,
  Sbe45cmd_bin,
  Sbe46cmd_bin,
  Sbe4600cmd_bin,
  Sbe47cmd_bin,
  Sbe470500cmd_bin,
  Sbe470501cmd_bin,
  Sbe470502cmd_bin,
  Sbe470503cmd_bin,
  Sbe470504cmd_bin,
  Sbe470505cmd_bin,
  Sbe470506cmd_bin,
  Sbe470507cmd_bin,
  Sbe470508cmd_bin,
  Sbe470509cmd_bin,
  Sbe47050acmd_bin,
  Sbe47050bcmd_bin,
  Sbe4707cmd_bin,
  Sbe470e08cmd_bin,
  Sbe470e09cmd_bin,
  Sbe471400cmd_bin,
  Sbe471401cmd_bin,
  Sbe471402cmd_bin,
  Sbe471ecmd_bin,
  Sbe4acmd_bin,
  Sbe4a0b00cmd_bin,
  Sbe4a0b01cmd_bin,
  Sbe4a0ccmd_bin,
  Sbe4a0c00cmd_bin,
  Sbe4a0c08cmd_bin,
  Sbe4a0c09cmd_bin,
  Sbe4bcmd_bin,
  Sbe4c00000004cmd_bin,
  Sbe4c00000104cmd_bin,
  Sbe4c00000204cmd_bin,
  Sbe4c00000704cmd_bin,
  Sbe4c0100cmd_bin,
  Sbe4c0106cmd_bin,
  Sbe4c0107cmd_bin,
  Sbe4c0108req_bin,
  Sbe4c0108cmd_bin,
  Sbe4c010acmd_bin,
  Sbe4c010breq_bin,
  Sbe4c010bcmd_bin,
  Sbe4c010dreq_bin,
  Sbe4c010dcmd_bin,
  Sbe4c010ereq_bin,
  Sbe4c010ecmd_bin,
  Sbe4c010freq_bin,
  Sbe4c010fcmd_bin,
  Sbe4c011000req_bin,
  Sbe4c011001cmd_bin,
  Sbe4c011002cmd_bin,
  Sbe4c011003req_bin,
  Sbe4c011004cmd_bin,
  Sbe4c0111cmd_bin,
  Sbe4c0114cmd_bin,
  Sbe4c011706cmd_bin,
  Sbe4c011710cmd_bin,
  Sbe4c011711cmd_bin,
  Sbe4c011713cmd_bin,
  Sbe4c011720cmd_bin,
  Sbe4c011721cmd_bin,
  Sbe4c0119cmd_bin,
  Sbe4c011acmd_bin,
  Sbe4c2000req_bin,
  Sbe4c2000cmd_bin,
  Sbe4c2001req_bin,
  Sbe4c2300cmd_bin,
  Sbe4c2301cmd_bin,
  Sbe4c2302req_bin,
  Sbe4c2302cmd_bin,
  Sbe4c8000cmd_bin,
  Sbe4c8001cmd_bin,
  Sbe4dcmd_bin,
  Sbe4ecmd_bin,
  Sbe4fcmd_bin,
  Sbe50cmd_bin,
  Sbe5014cmd_bin,
  Sbe51cmd_bin,
  Sbe52cmd_bin,
  Sbe53cmd_bin,
  Sbe530600cmd_bin,
  Sbe530601cmd_bin,
  Sbe54cmd_bin,
  Sbe55cmd_bin,
  Sbe56cmd_bin,
  Sbe57cmd_bin,
  Sbe570507cmd_bin,
  Sbe5acmd_bin,
  Sbe5ccmd_bin,
  Sbe5c0100cmd_bin,
  Sbe5c0106cmd_bin,
  Sbe5c0107cmd_bin,
  Sbe5c010acmd_bin,
  Sbe5c010bcmd_bin,
  Sbe5c011000cmd_bin,
  Sbe5c011001cmd_bin,
  Sbe5c011002cmd_bin,
  Sbe5c011003cmd_bin,
  Sbe5c011004cmd_bin,
  Sbe5c0111cmd_bin,
  Sbe5c0114cmd_bin,
  Sbe5c011700cmd_bin,
  Sbe5c011706cmd_bin,
  Sbe5c011710cmd_bin,
  Sbe5c011711cmd_bin,
  Sbe5c011713cmd_bin,
  Sbe5c0119cmd_bin,
  Sbe60cmd_bin,
  Sbe6014cmd_bin,
  Sbe630600cmd_bin,
  Sbe630601cmd_bin,
  Sbe710000req_bin,
  Sbe710100req_bin,
  Sbe710200req_bin,
  Sbe710201req_bin,
  Sbe710300req_bin,
  Sbe710400req_bin,
  Sbe710500req_bin,
  Sbe710600req_bin,
  Sbe710700req_bin,
  Sbe710800req_bin,
  Sbe710900req_bin,
  Sbe710a00req_bin,
  Sbe710b00req_bin,
  Sbe710c00req_bin,
  Sbe710d00req_bin,
  Sbe710e00req_bin,
  Sbe710f00req_bin,
  Sbe8000cmd_bin,
  Sc500req_bin,
  Sc501cmd_bin,
  Sc502req_bin,
  Sc60000cmd_bin,
  Sc60100cmd_bin,
  Sc60200cmd_bin,
  Sc60400cmd_bin,
  Sc700cmd_bin,
  Sc701req_bin,
  Sc701cmd_bin,
0
]

ServerStructList = [
  S00rsp_bin,
  S13rsp_bin,
  S1a01rsp_bin,
  S1a0200rsp_bin,
  S1a0201rsp_bin,
  S1a0300rsp_bin,
  S1a0301rsp_bin,
  S40rsp_bin,
  S41rsp_bin,
  S42rsp_bin,
  S43rsp_bin,
  S45rsp_bin,
  S45rspv1_bin,
  S46rsp_bin,
  S47rsp_bin,
  S48rsp_bin,
  S4arsp_bin,
  S4arspv1_bin,
  S4arspv2_bin,
  S4brsp_bin,
  S4crsp_bin,
  S4frsp_bin,
  S53rsp_bin,
  S55rsp_bin,
  S58rsp_bin,
  S5822rsp_bin,
  S5823rsp_bin,
  S5824rsp_bin,
  S5825rsp_bin,
  S5826rsp_bin,
  S5brsp_bin,
  S5crsp_bin,
  S5f01rsp_bin,
  S5f02rsp_bin,
  S5f10rsp_bin,
  S5f2200rsp_bin,
  S5f2201rsp_bin,
  S6a01rsp_bin,
  S6drsp_bin,
  S6f01rsp_bin,
  S6f10rsp_bin,
  S6f20rsp_bin,
  S6f21rsp_bin,
  S70rsp_bin,
  S78rsp_bin,
  S7b07rsp_bin,
  S7b08ack_bin,
  S7b08rsp_bin,
  S7b80rsp_bin,
  S7b8600rsp_bin,
  S7b8602rsp_bin,
  S7b8603rsp_bin,
  S7b8605rsp_bin,
  S7b860604rsp_bin,
  S7d00rsp_bin,
  S7d01rsp_bin,
  S7d02rsp_bin,
  S7d09rsp_bin,
  S82rsp_bin,
  S82rspv1_bin,
  S83rsp_bin,
  S890000rsp_bin,
  S890001rsp_bin,
  S890002rsp_bin,
  S890003rsp_bin,
  S893308rsp_bin,
  S8940rsp_bin,
  S8941rsp_bin,
  S8950rsp_bin,
  S8951rsp_bin,
  S8960rsp_bin,
  S8961rsp_bin,
  S8962rsp_bin,
  S897000rsp_bin,
  S897001rsp_bin,
  S897002rsp_bin,
  S897003rsp_bin,
  S897004rsp_bin,
  S897005rsp_bin,
  S897006ack_bin,
  S897007ack_bin,
  S897008ack_bin,
  S897009ack_bin,
  S89700aack_bin,
  S89700back_bin,
  S89700cack_bin,
  S89700drsp_bin,
  S897100rsp_bin,
  S897100ack_bin,
  S897101rsp_bin,
  S897101ack_bin,
  S897103rsp_bin,
  S897103ack_bin,
  S8b00rsp_bin,
  S8b02rsp_bin,
  S8frsp_bin,
  S8f77rsp_bin,
  S8f770rsp_bin,
  S8f7brsp_bin,
  S8f7cack_bin,
  S8f7frsp_bin,
  S8f80rsp_bin,
  S8f84ack_bin,
  S8f85rsp_bin,
  S8f89rsp_bin,
  S8f89ack_bin,
  S8f8brsp_bin,
  S8f8cack_bin,
  S8f8c01rsp_bin,
  S8f8c02rsp_bin,
  S8f8c03rsp_bin,
  S8f8c04rsp_bin,
  S8f8frsp_bin,
  S8f91rsp_bin,
  S8f91ack_bin,
  S8f9306rsp_bin,
  S8f931500rsp_bin,
  S8f93150100rsp_bin,
  S8f93150101rsp_bin,
  S8f93150102rsp_bin,
  S8f93150103rsp_bin,
  S8f93150104rsp_bin,
  S8f93150200rsp_bin,
  S8f93150201rsp_bin,
  S8f93150202rsp_bin,
  S8f93150203rsp_bin,
  S8f931503rsp_bin,
  S8f9arsp_bin,
  S8f9ersp_bin,
  S8f9f00rsp_bin,
  S8f9f00ack_bin,
  S8f9f01rsp_bin,
  S8f9f02rsp_bin,
  S8f9f02ack_bin,
  S8f9f03rsp_bin,
  S8f9f03ack_bin,
  S8f9f04rsp_bin,
  S8f9f04ack_bin,
  S8fa0rsp_bin,
  S8fa1rsp_bin,
  S8fa2rsp_bin,
  S8fa300rsp_bin,
  S8fa301rsp_bin,
  S8fa302rsp_bin,
  S8fa303rsp_bin,
  S8fa304rsp_bin,
  S8fa305rsp_bin,
  S8fa306rsp_bin,
  S8fa307ack_bin,
  S8fa405rsp_bin,
  S8fa406rsp_bin,
  S8fa407rsp_bin,
  S8fa500rsp_bin,
  S8fa501rsp_bin,
  S8fa502ack_bin,
  S8fa601ack_bin,
  S8fa602rsp_bin,
  S8fa608rsp_bin,
  S8fa617rsp_bin,
  S8fa622rsp_bin,
  S8fa623rsp_bin,
  S8fa624rsp_bin,
  S8fa625ack_bin,
  S8fa626rsp_bin,
  S8fa627ack_bin,
  S8fa628ack_bin,
  S8fa629rsp_bin,
  S8fa630rsp_bin,
  S8fa631rsp_bin,
  S8fa632rsp_bin,
  S8fa632ack_bin,
  S8fa633rsp_bin,
  S8fa634ack_bin,
  S8fa634rsp_bin,
  S8fa640ack_bin,
  S8fa641ack_bin,
  S8fa642ack_bin,
  S8fa643ack_bin,
  S8fa644ack_bin,
  S8fa645ack_bin,
  S8fa646ack_bin,
  S8fa647rsp_bin,
  S8fa648ack_bin,
  S8fa70000rsp_bin,
  S8fa70001rsp_bin,
  S8fa70002rsp_bin,
  S8fa70003rsp_bin,
  S8fa70100rsp_bin,
  S8fa70101rsp_bin,
  S8fa70102rsp_bin,
  S8fa800rsp_bin,
  S8fa801ack_bin,
  S8fa801rsp_bin,
  S8fa802ack_bin,
  S8fa802rsp_bin,
  S8fa803ack_bin,
  S8fa803rsp_bin,
  S8fa804ack_bin,
  S8fa804rsp_bin,
  S8fa805ack_bin,
  S8fa806ack_bin,
  S8fa806rsp_bin,
  S8fa900rsp_bin,
  S8fa90100ack_bin,
  S8fa90100rsp_bin,
  S8fa90101ack_bin,
  S8fa90101rsp_bin,
  S8fa90102ack_bin,
  S8fa90103rsp_bin,
  S8fa90104rsp_bin,
  S8fa90105ack_bin,
  S8fa90106rsp_bin,
  S8fa90107rsp_bin,
  S8fa90108rsp_bin,
  S8fa90130rsp_bin,
  S8fa90131rsp_bin,
  S8fa90200rsp_bin,
  S8fa90201rsp_bin,
  S8fa90202rsp_bin,
  S8fa90300rsp_bin,
  S8fa90400rsp_bin,
  S8fa905ack_bin,
  S8fa90600rsp_bin,
  S8fa90700rsp_bin,
  S8fa90701rsp_bin,
  S8fa90703rsp_bin,
  S8fa90704rsp_bin,
  S8fa90705rsp_bin,
  S8fa90706rsp_bin,
  S8fa90707rsp_bin,
  S8fa90800rsp_bin,
  S8fa909ack_bin,
  S8fa909rsp_bin,
  S8fa90a00rsp_bin,
  S8fa90a01rsp_bin,
  S8fa910rsp_bin,
  S8fa911rsp_bin,
  S8fa912rsp_bin,
  S8fa913rsp_bin,
  S8fa914rsp_bin,
  S8fa91500rsp_bin,
  S8fa91501rsp_bin,
  S8fa91502rsp_bin,
  S8fa91503rsp_bin,
  S8fa91504rsp_bin,
  S8fa91599rsp_bin,
  S8fa9160000rsp_bin,
  S8fa9160001rsp_bin,
  S8fa9160002rsp_bin,
  S8fa9160100rsp_bin,
  S8fa91602rsp_bin,
  S8fa91603rsp_bin,
  S8fa91604rsp_bin,
  S8fa91605rsp_bin,
  S8fa91606rsp_bin,
  S8fa91700rsp_bin,
  S8fa91701rsp_bin,
  S8fa91702rsp_bin,
  S8fa91703rsp_bin,
  S8fa918rsp_bin,
  S8fa9a5rsp_bin,
  S8faa00rsp_bin,
  S8fab00rsp_bin,
  S8fab01rsp_bin,
  S8fab02ack_bin,
  S8fab03rsp_bin,
  S8fab04ack_bin,
  S8fab05rsp_bin,
  S8fab06rsp_bin,
  S8fab07rsp_bin,
  S8fab08rsp_bin,
  S8fac0100rsp_bin,
  S8fac0101rsp_bin,
  S8fac0102rsp_bin,
  S8fac02rsp_bin,
  S8fac03rsp_bin,
  S8fac04rsp_bin,
  S8fac05rsp_bin,
  S8fac06rsp_bin,
  S8fac07rsp_bin,
  S8fad00rsp_bin,
  S8fad01ack_bin,
  S8fad02rsp_bin,
  S8fae00rsp_bin,
  S8fae01rsp_bin,
  S8fae02rsp_bin,
  S8fae03rsp_bin,
  S8fae04rsp_bin,
  S8fae05rsp_bin,
  S8fae05ack_bin,
  Sb080rsp_bin,
  Sb081rsp_bin,
  Sbb00rsp_bin,
  Sbcrsp_bin,
  Sbf1arsp_bin,
  Sbf40rsp_bin,
  Sbf400000rsp_bin,
  Sbf400100rsp_bin,
  Sbf401400rsp_bin,
  Sbf401401rsp_bin,
  Sbf41rsp_bin,
  Sbf42rsp_bin,
  Sbf4200rsp_bin,
  Sbf4201rsp_bin,
  Sbf4202rsp_bin,
  Sbf43rsp_bin,
  Sbf4301rsp_bin,
  Sbf4303rsp_bin,
  Sbf4306rsp_bin,
  Sbf44rsp_bin,
  Sbf45rsp_bin,
  Sbf46rsp_bin,
  Sbf47rsp_bin,
  Sbf470500rsp_bin,
  Sbf470501rsp_bin,
  Sbf470502rsp_bin,
  Sbf470503rsp_bin,
  Sbf470504rsp_bin,
  Sbf470505rsp_bin,
  Sbf470506rsp_bin,
  Sbf470507rsp_bin,
  Sbf470508rsp_bin,
  Sbf470509rsp_bin,
  Sbf47050arsp_bin,
  Sbf47050brsp_bin,
  Sbf4707rsp_bin,
  Sbf470e06rsp_bin,
  Sbf470e07rsp_bin,
  Sbf470e08rsp_bin,
  Sbf470e09rsp_bin,
  Sbf471400rsp_bin,
  Sbf471401rsp_bin,
  Sbf471402rsp_bin,
  Sbf471ersp_bin,
  Sbf4arsp_bin,
  Sbf4a0b00rsp_bin,
  Sbf4a0b01rsp_bin,
  Sbf4a0c00rsp_bin,
  Sbf4a0c08rsp_bin,
  Sbf4brsp_bin,
  Sbf4c00000004rsp_bin,
  Sbf4c00000104rsp_bin,
  Sbf4c00000204rsp_bin,
  Sbf4c00000704rsp_bin,
  Sbf4c0101rsp_bin,
  Sbf4c0108rsp_bin,
  Sbf4c010arsp_bin,
  Sbf4c010brsp_bin,
  Sbf4c010drsp_bin,
  Sbf4c010ersp_bin,
  Sbf4c010frsp_bin,
  Sbf4c011000rsp_bin,
  Sbf4c011001rsp_bin,
  Sbf4c011002rsp_bin,
  Sbf4c011003rsp_bin,
  Sbf4c011004rsp_bin,
  Sbf4c0111rsp_bin,
  Sbf4c0114rsp_bin,
  Sbf4c011806rsp_bin,
  Sbf4c011810rsp_bin,
  Sbf4c011811rsp_bin,
  Sbf4c011813rsp_bin,
  Sbf4c011820rsp_bin,
  Sbf4c011821rsp_bin,
  Sbf4c0119rsp_bin,
  Sbf4c011arsp_bin,
  Sbf4c0120rsp_bin,
  Sbf4c0500rsp_bin,
  Sbf4c2000rsp_bin,
  Sbf4c2001rsp_bin,
  Sbf4c2300rsp_bin,
  Sbf4c2301rsp_bin,
  Sbf4c2302rsp_bin,
  Sbf4c8000rsp_bin,
  Sbf4c8001rsp_bin,
  Sbf4c8002rsp_bin,
  Sbf4drsp_bin,
  Sbf4ersp_bin,
  Sbf4frsp_bin,
  Sbf5014rsp_bin,
  Sbf530600rsp_bin,
  Sbf530601rsp_bin,
  Sbf570507rsp_bin,
  Sbf5c0101rsp_bin,
  Sbf5c0106rsp_bin,
  Sbf5c0107rsp_bin,
  Sbf5c010brsp_bin,
  Sbf5c011000rsp_bin,
  Sbf5c011001rsp_bin,
  Sbf5c011002rsp_bin,
  Sbf5c011003rsp_bin,
  Sbf5c011004rsp_bin,
  Sbf5c0111rsp_bin,
  Sbf5c0114rsp_bin,
  Sbf5c0118rsp_bin,
  Sbf5c0119rsp_bin,
  Sbf6014rsp_bin,
  Sbf630600rsp_bin,
  Sbf630601rsp_bin,
  Sbf6800rsp_bin,
  Sbf6801rsp_bin,
  Sbf710000rsp_bin,
  Sbf710100rsp_bin,
  Sbf710200rsp_bin,
  Sbf710201rsp_bin,
  Sbf710300rsp_bin,
  Sbf710400rsp_bin,
  Sbf710500rsp_bin,
  Sbf710600rsp_bin,
  Sbf710700rsp_bin,
  Sbf710800rsp_bin,
  Sbf710900rsp_bin,
  Sbf710a00rsp_bin,
  Sbf710b00rsp_bin,
  Sbf710c00rsp_bin,
  Sbf710d00rsp_bin,
  Sbf710e00rsp_bin,
  Sbf710f00rsp_bin,
  Sd500rsp_bin,
  Sd502rsp_bin,
  Sd6ack_bin,
  Sd700ack_bin,
  Sd701ack_bin,
  Sd701rsp_bin,
0
]

  #----------------------------------------------------------------------
  #
  #----------------------------------------------------------------------
  # @name TSIP Packet Groupings
  
  # Client-side TSIP packet enumeration.
class EClientPackets(Enum):
  def __new__(cls, value, doc: str):
    obj = object.__new__(cls)
    obj._value_ = value
    obj.__doc__ = doc
    return obj

  e00cmd: int = (0, "This is used so we can get to the raw data [Fields: PacketDataLength, PacketData]")
  """This is used so we can get to the raw data [Fields: PacketDataLength, PacketData]"""
  e1a00cmd: int = (1, "Wraps RTCM data for output in a TSIP stream. [Fields: RTCMDataLength, RTCMData]")
  """Wraps RTCM data for output in a TSIP stream. [Fields: RTCMDataLength, RTCMData]"""
  e1a0200cmd: int = (2, "Controls forwarding of DCOL packets to connected port [Fields: NumTypes DCOLTypes]")
  """Controls forwarding of DCOL packets to connected port [Fields: NumTypes DCOLTypes]"""
  e1a0201cmd: int = (3, "TSIP wrapped DCOL message command to device. [Fields: NumBytes DCOLMessage]")
  """TSIP wrapped DCOL message command to device. [Fields: NumBytes DCOLMessage]"""
  e1a0202cmd: int = (4, "Wraps DCOL messages for processing in a TSIP stream. [Fields: NumBytes DCOLMessage]")
  """Wraps DCOL messages for processing in a TSIP stream. [Fields: NumBytes DCOLMessage]"""
  e1a0300cmd: int = (5, "Controls forwarding of CAN messages from connected [Fields: CanPort NumIDs CanIds]")
  """Controls forwarding of CAN messages from connected [Fields: CanPort NumIDs CanIds]"""
  e1a0301cmd: int = (6, "TSIP wrapped CAN message to forward to CAN device [Fields: CanPort CanId CanMsgLength CanMsg]")
  """TSIP wrapped CAN message to forward to CAN device [Fields: CanPort CanId CanMsgLength CanMsg]"""
  e1e4bcmd: int = (7, "Clears all battery-backed data and performs a software reset to initiate a cold start of the receiver. [Fields: ]")
  """Clears all battery-backed data and performs a software reset to initiate a cold start of the receiver. [Fields: ]"""
  e1freq: int = (8, "Requests the firmware information from the receiver. Responds with the 0x45 packet. [Fields: ]")
  """Requests the firmware information from the receiver. Responds with the 0x45 packet. [Fields: ]"""
  e1freqv1: int = (9, "Requests the firmware information from the receiver. Responds with the 0x45 packet. [Fields: MachineId RequestType]")
  """Requests the firmware information from the receiver. Responds with the 0x45 packet. [Fields: MachineId RequestType]"""
  e20req: int = (10, "Requests almanac data for one satellite from the receiver [Fields: SatNumber]")
  """Requests almanac data for one satellite from the receiver [Fields: SatNumber]"""
  e21req: int = (11, "Requests current GPS time from the receiver. Report packet 0x41 is sent in response. [Fields: ]")
  """Requests current GPS time from the receiver. Report packet 0x41 is sent in response. [Fields: ]"""
  e22cmd: int = (12, "Configures the receiver to operate in a specific position fix mode and stores the new mode setting in battery-backed memory. [Fields: PositionFixMode]")
  """Configures the receiver to operate in a specific position fix mode and stores the new mode setting in battery-backed memory. [Fields: PositionFixMode]"""
  e25cmd: int = (13, "Initiates a software reset for the receiver, causing the receiver to perform the equivalent of powering off and then on. The receiver performs a self-test during the reset routine. Command Packet 0x25 contains no data bytes. [Fields: ]")
  """Initiates a software reset for the receiver, causing the receiver to perform the equivalent of powering off and then on. The receiver performs a self-test during the reset routine. Command Packet 0x25 contains no data bytes. [Fields: ]"""
  e26req: int = (14, "Requests health and status information from the receiver. Report packets 0x46 and 0x4B are sent in response. [Fields: ]")
  """Requests health and status information from the receiver. Report packets 0x46 and 0x4B are sent in response. [Fields: ]"""
  e27req: int = (15, "Requests signal levels for all satellites currently being tracked. Report packet 0x47 is sent in response. [Fields: ]")
  """Requests signal levels for all satellites currently being tracked. Report packet 0x47 is sent in response. [Fields: ]"""
  e2creq: int = (16, "Request the current operating parameter values of the receiver, which responds with Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory. [Fields: ]")
  """Request the current operating parameter values of the receiver, which responds with Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory. [Fields: ]"""
  e2ccmd: int = (17, "Sets the operating parameter values of a receiver or requests the current parameter values, and the receiver responds by sending the parameter values in Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory. [Fields: DynamicsCode ElevationMask SignalLevelMask PDOPMask PDOPSwitch]")
  """Sets the operating parameter values of a receiver or requests the current parameter values, and the receiver responds by sending the parameter values in Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory. [Fields: DynamicsCode ElevationMask SignalLevelMask PDOPMask PDOPSwitch]"""
  e33req: int = (18, "Requests analog to digital readings from receiver [Fields: ]")
  """Requests analog to digital readings from receiver [Fields: ]"""
  e35req: int = (19, "Requests the current I/O option flags. The receiver responds by sending Report Packet 0x55. [Fields: ]")
  """Requests the current I/O option flags. The receiver responds by sending Report Packet 0x55. [Fields: ]"""
  e35cmd: int = (20, "Sets the current I/O option flags. The receiver records the I/O option flags settings in battery-backed memory and sends Report Packet 0x55 in response. [Fields: PosFlags VelocityFlags TimingFlags AuxFlags]")
  """Sets the current I/O option flags. The receiver records the I/O option flags settings in battery-backed memory and sends Report Packet 0x55 in response. [Fields: PosFlags VelocityFlags TimingFlags AuxFlags]"""
  e38cmd: int = (21, "Command Packet 0x38 downloads satellite data from one receiver, and uploads the data to another receiver. The receiver acknowledges a download operation by sending the requested data in Report Packet 0x58. The process of downloading satellite data from one receiver and uploading it to another decreases the amount of time required for the receiver to initialize from a cold start (battery-backed memory cleared). Note that the receiver can initialize itself without uploading data, it merely takes longer. To download data from one receiver, use only bytes 0&#8211;2. To upload the data to another receiver, use all bytes. [Fields: Operation DataType SVPRN]")
  """Command Packet 0x38 downloads satellite data from one receiver, and uploads the data to another receiver. The receiver acknowledges a download operation by sending the requested data in Report Packet 0x58. The process of downloading satellite data from one receiver and uploading it to another decreases the amount of time required for the receiver to initialize from a cold start (battery-backed memory cleared). Note that the receiver can initialize itself without uploading data, it merely takes longer. To download data from one receiver, use only bytes 0&#8211;2. To upload the data to another receiver, use all bytes. [Fields: Operation DataType SVPRN]"""
  e3breq: int = (22, "Command Packet 0x3B requests the current status of satellite ephemeris data. The receiver acknowledges with Report Packet 0x5B when data is available. [Fields: SatNumber]")
  """Command Packet 0x3B requests the current status of satellite ephemeris data. The receiver acknowledges with Report Packet 0x5B when data is available. [Fields: SatNumber]"""
  e3creq: int = (23, "Requests the current satellite tracking status. The receiver acknowledges with Report Packet 0x5C when data is available. [Fields: SatNumber]")
  """Requests the current satellite tracking status. The receiver acknowledges with Report Packet 0x5C when data is available. [Fields: SatNumber]"""
  e3f02cmd: int = (24, "Controls output of Engineering Diagnostics [Fields: DebugEnabled]")
  """Controls output of Engineering Diagnostics [Fields: DebugEnabled]"""
  e3f2200req: int = (25, "Gets the mask controlling diagnostic types output [Fields: ]")
  """Gets the mask controlling diagnostic types output [Fields: ]"""
  e3f2200cmd: int = (26, "Sets the mask controlling diagnostic types output [Fields: Mask]")
  """Sets the mask controlling diagnostic types output [Fields: Mask]"""
  e62req: int = (27, "Requests the differential GPS position fix mode. Report packet 0x82 is sent in response [Fields: ]")
  """Requests the differential GPS position fix mode. Report packet 0x82 is sent in response [Fields: ]"""
  e62cmd: int = (28, "Sets the differential GPS position fix mode. Report packet 0x82 is sent in response [Fields: FixMode]")
  """Sets the differential GPS position fix mode. Report packet 0x82 is sent in response [Fields: FixMode]"""
  e65req: int = (29, "Requests DGPS corrections for given SVID [Fields: SVID]")
  """Requests DGPS corrections for given SVID [Fields: SVID]"""
  e690000req: int = (30, "Requests the status of SecureRTK and the 5 rover keys. [Fields: Version]")
  """Requests the status of SecureRTK and the 5 rover keys. [Fields: Version]"""
  e690001req: int = (31, "Rover Key Data [Fields: Version KeySlot]")
  """Rover Key Data [Fields: Version KeySlot]"""
  e690002cmd: int = (32, "Set Rover Key Data [Fields: Version KeySlot, KeyString, DescriptionString]")
  """Set Rover Key Data [Fields: Version KeySlot, KeyString, DescriptionString]"""
  e690003cmd: int = (33, "Delete Rover Key Data [Fields: Version KeySlot]")
  """Delete Rover Key Data [Fields: Version KeySlot]"""
  e6932req: int = (34, "Requests one of several RTK stats reports. A variant of report packet 0x89 0x33 is sent in response, with the second report packet byte indicating the type of stats. [Fields: StatsType Control]")
  """Requests one of several RTK stats reports. A variant of report packet 0x89 0x33 is sent in response, with the second report packet byte indicating the type of stats. [Fields: StatsType Control]"""
  e6940req: int = (35, "Requests the RTK configuration [Fields: ]")
  """Requests the RTK configuration [Fields: ]"""
  e6940cmd: int = (36, "Sets the RTK configuration [Fields: PropagationMode VelocityType]")
  """Sets the RTK configuration [Fields: PropagationMode VelocityType]"""
  e6941req: int = (37, "Requests RTK solution info. Report packet 0x89 0x41 is sent in response. [Fields: ]")
  """Requests RTK solution info. Report packet 0x89 0x41 is sent in response. [Fields: ]"""
  e6950req: int = (38, "Requests the RTK auxilliary settings. Report packet 0x89 0x50 is sent in response. [Fields: ]")
  """Requests the RTK auxilliary settings. Report packet 0x89 0x50 is sent in response. [Fields: ]"""
  e6950cmd: int = (39, "Updates RTK auxilliary settings. Report packet 0x89 0x50 is sent in response. [Fields: ScintillationMode BackupSource RTKBaseDatum XFillSatFrequency XFillSatBitRate RTKBaseID SatConfigSource]")
  """Updates RTK auxilliary settings. Report packet 0x89 0x50 is sent in response. [Fields: ScintillationMode BackupSource RTKBaseDatum XFillSatFrequency XFillSatBitRate RTKBaseID SatConfigSource]"""
  e6951req: int = (40, "Requests the RTK auxilliary status. Report packet 0x89 0x51 is sent in response. [Fields: ]")
  """Requests the RTK auxilliary status. Report packet 0x89 0x51 is sent in response. [Fields: ]"""
  e6960req: int = (41, "Requests RTK base info. Report packet 0x89 0x60 is sent in response. [Fields: ]")
  """Requests RTK base info. Report packet 0x89 0x60 is sent in response. [Fields: ]"""
  e6961req: int = (42, "Requests CMR info. Report packet 0x89 0x61 is sent in response. [Fields: ]")
  """Requests CMR info. Report packet 0x89 0x61 is sent in response. [Fields: ]"""
  e6962req: int = (43, "Requests Ionospheric disturbance info. Report packet 0x89 0x62 is sent in response. [Fields: ]")
  """Requests Ionospheric disturbance info. Report packet 0x89 0x62 is sent in response. [Fields: ]"""
  e697000req: int = (44, "Requests RTK radio status. Report packet 0x89 0x70 0x00 is sent in response. [Fields: ]")
  """Requests RTK radio status. Report packet 0x89 0x70 0x00 is sent in response. [Fields: ]"""
  e697001req: int = (45, "Requests RTK radio identity. Report packet 0x89 0x70 0x01 is sent in response. [Fields: ]")
  """Requests RTK radio identity. Report packet 0x89 0x70 0x01 is sent in response. [Fields: ]"""
  e697002req: int = (46, "Requests RTK radio capabilities. Report packet 0x89 0x70 0x02 is sent in response. [Fields: ]")
  """Requests RTK radio capabilities. Report packet 0x89 0x70 0x02 is sent in response. [Fields: ]"""
  e697003req: int = (47, "Requests RTK radio country info. Report packet 0x89 0x70 0x03 is sent in response. [Fields: ]")
  """Requests RTK radio country info. Report packet 0x89 0x70 0x03 is sent in response. [Fields: ]"""
  e697004req: int = (48, "Requests config specific to 900MHz RTK radio. Report packet 0x89 0x70 0x04 is sent in response. [Fields: ]")
  """Requests config specific to 900MHz RTK radio. Report packet 0x89 0x70 0x04 is sent in response. [Fields: ]"""
  e697005req: int = (49, "Requests config specific to 450MHz RTK radio. Report packet 0x89 0x70 0x05 is sent in response. [Fields: ]")
  """Requests config specific to 450MHz RTK radio. Report packet 0x89 0x70 0x05 is sent in response. [Fields: ]"""
  e697006cmd: int = (50, "Sets RTK radio country code. Ack packet 0x89 0x70 0x06 is sent in response. [Fields: CountryCode]")
  """Sets RTK radio country code. Ack packet 0x89 0x70 0x06 is sent in response. [Fields: CountryCode]"""
  e697007cmd: int = (51, "Sets 900MHz RTK radio network ID. Ack packet 0x89 0x70 0x07 is sent in response. [Fields: NetworkId]")
  """Sets 900MHz RTK radio network ID. Ack packet 0x89 0x70 0x07 is sent in response. [Fields: NetworkId]"""
  e697008cmd: int = (52, "Sets 450MHz RTK radio channel ID. Ack packet 0x89 0x70 0x08 is sent in response. [Fields: ChannelId]")
  """Sets 450MHz RTK radio channel ID. Ack packet 0x89 0x70 0x08 is sent in response. [Fields: ChannelId]"""
  e697009cmd: int = (53, "Sets 450MHz RTK radio channel frequency. Ack packet 0x89 0x70 0x09 is sent in response. [Fields: ChannelId Freq]")
  """Sets 450MHz RTK radio channel frequency. Ack packet 0x89 0x70 0x09 is sent in response. [Fields: ChannelId Freq]"""
  e69700acmd: int = (54, "Sets 450MHz RTK radio mode. Ack packet 0x89 0x70 0x0a is sent in response. [Fields: Mode]")
  """Sets 450MHz RTK radio mode. Ack packet 0x89 0x70 0x0a is sent in response. [Fields: Mode]"""
  e69700bcmd: int = (55, "Restart connected RTK radio and re-establish communication. Ack packet 0x89 0x70 0x0b is sent in response. [Fields: ]")
  """Restart connected RTK radio and re-establish communication. Ack packet 0x89 0x70 0x0b is sent in response. [Fields: ]"""
  e697100req: int = (56, "Requests Fallback RTX: X, Y, and Z offsets for the designated source. Response packet is 0x89 0x71 0x00. No longer supported, do not use. [Fields: RTXOffsetSource]")
  """Requests Fallback RTX: X, Y, and Z offsets for the designated source. Response packet is 0x89 0x71 0x00. No longer supported, do not use. [Fields: RTXOffsetSource]"""
  e697100cmd: int = (57, "Set the X, Y, and Z user offsets. ACK packet is 0x89 0x71 0x01. No longer supported, do not use. [Fields: XOffsetValue YOffsetValue ZOffsetValue]")
  """Set the X, Y, and Z user offsets. ACK packet is 0x89 0x71 0x01. No longer supported, do not use. [Fields: XOffsetValue YOffsetValue ZOffsetValue]"""
  e697101req: int = (58, "Requests the Fallback RTX configuration mode and the offset source. Response packet is 0x89 0x71 0x01. No longer supported, do not use. [Fields: ]")
  """Requests the Fallback RTX configuration mode and the offset source. Response packet is 0x89 0x71 0x01. No longer supported, do not use. [Fields: ]"""
  e697101cmd: int = (59, "Sets Fallback RTX mode and offset source. ACK packet is 0x89 0x71 0x03. No longer supported, do not use. [Fields: FallbackMode RTXOffsetSource]")
  """Sets Fallback RTX mode and offset source. ACK packet is 0x89 0x71 0x03. No longer supported, do not use. [Fields: FallbackMode RTXOffsetSource]"""
  e697103req: int = (60, "Requests xFill Premium configuration. Response packet is 0x89 0x71 0x03. [Fields: ]")
  """Requests xFill Premium configuration. Response packet is 0x89 0x71 0x03. [Fields: ]"""
  e697103cmd: int = (61, "Sets xFill Premium Configuration. ACK packet is 0x89 0x71 0x03. [Fields: ScintillationSwitchRule ActivateXFillPremium ActivateHour ActivateMinute DeactivateHour DeactivateMinute RecalXFill]")
  """Sets xFill Premium Configuration. ACK packet is 0x89 0x71 0x03. [Fields: ScintillationSwitchRule ActivateXFillPremium ActivateHour ActivateMinute DeactivateHour DeactivateMinute RecalXFill]"""
  e6a01req: int = (62, "Requests current differential corrections output control settings. [Fields: ]")
  """Requests current differential corrections output control settings. [Fields: ]"""
  e6a01cmd: int = (63, "Controls whether or not the receiver will output differential correction information. [Fields: CorrectionsUsedInFix CorrectionInfo]")
  """Controls whether or not the receiver will output differential correction information. [Fields: CorrectionsUsedInFix CorrectionInfo]"""
  e6b00req: int = (64, "Requests current state of automatic position sigma reporting [Fields: ]")
  """Requests current state of automatic position sigma reporting [Fields: ]"""
  e6b00cmd: int = (65, "Controls automatic reporting of position sigma [Fields: EnableOutputs]")
  """Controls automatic reporting of position sigma [Fields: EnableOutputs]"""
  e6b02req: int = (66, "Requests a single position sigma (error) information report, automatic reporting can be set up with command 0x6B 0x00 [Fields: ]")
  """Requests a single position sigma (error) information report, automatic reporting can be set up with command 0x6B 0x00 [Fields: ]"""
  e6e03cmd: int = (67, " [Fields: Enable OutputInterval]")
  """ [Fields: Enable OutputInterval]"""
  e70cmd: int = (68, "Enables or disables the P/V Filter, Static Filter, and/or Altitude Filter. [Fields: DynamicFilter StaticFilter AltitudeFilter FilterLevel]")
  """Enables or disables the P/V Filter, Static Filter, and/or Altitude Filter. [Fields: DynamicFilter StaticFilter AltitudeFilter FilterLevel]"""
  e77req: int = (69, "Requests the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode. The receiver acknowledges with Report Packet 0x78. [Fields: ]")
  """Requests the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode. The receiver acknowledges with Report Packet 0x78. [Fields: ]"""
  e77cmd: int = (70, "Sets the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode. [Fields: MaxPRCAge]")
  """Sets the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode. [Fields: MaxPRCAge]"""
  e7a07req: int = (71, "Requests the data reporting options for the NMEA output on the specified port. The receiver responds with Report Packet 0x7B 0x07. [Fields: Port]")
  """Requests the data reporting options for the NMEA output on the specified port. The receiver responds with Report Packet 0x7B 0x07. [Fields: Port]"""
  e7a07cmd: int = (72, "Sets the data reporting options for the NMEA output on the specified port. [Fields: Port Options1]")
  """Sets the data reporting options for the NMEA output on the specified port. [Fields: Port Options1]"""
  e7a08req: int = (73, "Requests the data reporting options for NMEA on the specified receiver port. The receiver responds with Report Packet 0x7B 0x08. [Fields: Port]")
  """Requests the data reporting options for NMEA on the specified receiver port. The receiver responds with Report Packet 0x7B 0x08. [Fields: Port]"""
  e7a08cmd: int = (74, "Each Ag Receivers supports a varying number of serial ports that can transmit NMEA messages. This command configures various parameters of the NMEA for the specified serial port (if supported) on the receiver. This command supersedes other NMEA configuration commands and is designed to be used stand-alone (and not in conjunction with other NMEA Configuration command packets). The receiver acknowledges with 0x7B 0x08. [Fields: Port MessageProtocol MessageInterval OutputMask GGAOptions Precision]")
  """Each Ag Receivers supports a varying number of serial ports that can transmit NMEA messages. This command configures various parameters of the NMEA for the specified serial port (if supported) on the receiver. This command supersedes other NMEA configuration commands and is designed to be used stand-alone (and not in conjunction with other NMEA Configuration command packets). The receiver acknowledges with 0x7B 0x08. [Fields: Port MessageProtocol MessageInterval OutputMask GGAOptions Precision]"""
  e7a80req: int = (75, "Requests the NMEA message transmission interval or a combination of the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response. [Fields: ]")
  """Requests the NMEA message transmission interval or a combination of the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response. [Fields: ]"""
  e7a80cmd: int = (76, "Sets the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response. [Fields: Interval OutputMask]")
  """Sets the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response. [Fields: Interval OutputMask]"""
  e7a86req: int = (77, "Requests the data reporting options for the NMEA GGA, GGL, VTG, and RMC message sentences for the current port. Report Packet 0x7B 0x86 is sent in response. [Fields: MsgType]")
  """Requests the data reporting options for the NMEA GGA, GGL, VTG, and RMC message sentences for the current port. Report Packet 0x7B 0x86 is sent in response. [Fields: MsgType]"""
  e7a8600cmd: int = (78, "Sets the GGA options and precision for the current port. [Fields: Options Precision]")
  """Sets the GGA options and precision for the current port. [Fields: Options Precision]"""
  e7a8602cmd: int = (79, "Sets the VTG options for the current port. [Fields: Options]")
  """Sets the VTG options for the current port. [Fields: Options]"""
  e7a8603cmd: int = (80, "Sets the VTG speed precision for the current port. [Fields: SpeedPrecision]")
  """Sets the VTG speed precision for the current port. [Fields: SpeedPrecision]"""
  e7a8604cmd: int = (81, "Sets the RMC options and precision for the current port. [Fields: Options PosPrecision SpeedPrecision]")
  """Sets the RMC options and precision for the current port. [Fields: Options PosPrecision SpeedPrecision]"""
  e7a8605cmd: int = (82, "Sets the VTG Heading Precision for the current port. [Fields: HeadingPrecision]")
  """Sets the VTG Heading Precision for the current port. [Fields: HeadingPrecision]"""
  e7c00req: int = (83, "Requests the rate for computing position fixes. Report Packet 0x7D 0x00 is sent in response. [Fields: ]")
  """Requests the rate for computing position fixes. Report Packet 0x7D 0x00 is sent in response. [Fields: ]"""
  e7c00cmd: int = (84, "Sets the rate for computing position fixes. [Fields: ASAPRate]")
  """Sets the rate for computing position fixes. [Fields: ASAPRate]"""
  e7c01req: int = (85, "Requests the position fix rate I/O option bytes. Report Packet 0x7D 0x01 is sent in response. [Fields: ]")
  """Requests the position fix rate I/O option bytes. Report Packet 0x7D 0x01 is sent in response. [Fields: ]"""
  e7c01cmd: int = (86, "Sets the position fix rate I/O options bytes. [Fields: OptionFlags1 OptionFlags2]")
  """Sets the position fix rate I/O options bytes. [Fields: OptionFlags1 OptionFlags2]"""
  e7c02req: int = (87, "Requests the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. Report Packet 0x7D 0x02 is sent in response. [Fields: ]")
  """Requests the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. Report Packet 0x7D 0x02 is sent in response. [Fields: ]"""
  e7c02cmd: int = (88, "Sets the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. [Fields: Interval Offset]")
  """Sets the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. [Fields: Interval Offset]"""
  e7c09req: int = (89, "Requests the message interval for the specified port and protocol. [Fields: Port MessageProtocol]")
  """Requests the message interval for the specified port and protocol. [Fields: Port MessageProtocol]"""
  e7c09cmd: int = (90, "Sets the message interval for the specifed port and protocol. [Fields: Port MessageProtocol MessageInterval]")
  """Sets the message interval for the specifed port and protocol. [Fields: Port MessageProtocol MessageInterval]"""
  e8e7breq: int = (91, "Requests a report containing the current receiver configuration parameter settings and software version number. Report Packet 0x8F 0x7B is sent in response. [Fields: ]")
  """Requests a report containing the current receiver configuration parameter settings and software version number. Report Packet 0x8F 0x7B is sent in response. [Fields: ]"""
  e8e7ccmd: int = (92, "Used to set the receiver configuration parameters stored in battery-backed RAM (Random Access Memory). Report Packet 0x8F 0x7C is sent in response. [Fields: PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3]")
  """Used to set the receiver configuration parameters stored in battery-backed RAM (Random Access Memory). Report Packet 0x8F 0x7C is sent in response. [Fields: PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3]"""
  e8e7freq: int = (93, "Request DGPS Receiver ROM Configuration Block Report [Fields: ]")
  """Request DGPS Receiver ROM Configuration Block Report [Fields: ]"""
  e8e80req: int = (94, "requests the current status of the DGPS service provider. Report packet 0x8f 0x80 is sent in response. [Fields: Provider Reserved]")
  """requests the current status of the DGPS service provider. Report packet 0x8f 0x80 is sent in response. [Fields: Provider Reserved]"""
  e8e81req: int = (95, "Get spot station info [Fields: ]")
  """Get spot station info [Fields: ]"""
  e8e84cmd: int = (96, "Starts or stops the satellite FFT (Fast Fourier Transform) diagnostics and sets the FFT diagnostic options. Acknowledged with Report Packet 0x8F 0x84. [Fields: Mode OscillatorOffset FFTPlotType InputSquared CenterFreq NumIntegrations]")
  """Starts or stops the satellite FFT (Fast Fourier Transform) diagnostics and sets the FFT diagnostic options. Acknowledged with Report Packet 0x8F 0x84. [Fields: Mode OscillatorOffset FFTPlotType InputSquared CenterFreq NumIntegrations]"""
  e8e85req: int = (97, "requests the tracking status for the source of DGPS corrections (either beacon or satellite). Report packet 0x8f 0x85 is sent in response. [Fields: ]")
  """requests the tracking status for the source of DGPS corrections (either beacon or satellite). Report packet 0x8f 0x85 is sent in response. [Fields: ]"""
  e8e88req: int = (98, "Requests current  [Fields: StreamId]")
  """Requests current  [Fields: StreamId]"""
  e8e88cmd: int = (99, "Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response. [Fields: StreamId OptionsFlags]")
  """Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response. [Fields: StreamId OptionsFlags]"""
  e8e89req: int = (100, "Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response. [Fields: ]")
  """Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response. [Fields: ]"""
  e8e89cmd: int = (101, "Controls DGPS source and related settings. Acknowledgement packet 0x8F 0x89 is sent in response. [Fields: DGPSSrcMode BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout CorrectionOptions SatConfigSource]")
  """Controls DGPS source and related settings. Acknowledgement packet 0x8F 0x89 is sent in response. [Fields: DGPSSrcMode BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout CorrectionOptions SatConfigSource]"""
  e8e8breq: int = (102, "Requests service provider activation information. Report Packet 0x8F 0x8B is sent in response. [Fields: ServiceProvider InfoType]")
  """Requests service provider activation information. Report Packet 0x8F 0x8B is sent in response. [Fields: ServiceProvider InfoType]"""
  e8e8c00cmd: int = (103, "The key press command packet simulates sending a key press to the display. Whenever the end user application wants to move around the remote display (i.e. in response to a key press on its own terminal, touch screen, etc.), this packet is sent to the receiver to indicate that the receiver should process the specified key press action. The receiver will acknowledge the key press command by sending Report Packet 0x8F 0x8C. [Fields: KeyPress]")
  """The key press command packet simulates sending a key press to the display. Whenever the end user application wants to move around the remote display (i.e. in response to a key press on its own terminal, touch screen, etc.), this packet is sent to the receiver to indicate that the receiver should process the specified key press action. The receiver will acknowledge the key press command by sending Report Packet 0x8F 0x8C. [Fields: KeyPress]"""
  e8e8c01req: int = (104, "Requests the remote display screen contents once. The receiver will respond by sending Report Packet 0x8F 0x8C 0x01. If automatic reporting of the screen contents is configured, this packet must be sent once per minute to maintain that configuration (version 1.40 and later). This provides a timeout mechanism if the receiver is disconnected from the user terminal so the automatic reporting does not continue indefinitely if not needed. [Fields: ]")
  """Requests the remote display screen contents once. The receiver will respond by sending Report Packet 0x8F 0x8C 0x01. If automatic reporting of the screen contents is configured, this packet must be sent once per minute to maintain that configuration (version 1.40 and later). This provides a timeout mechanism if the receiver is disconnected from the user terminal so the automatic reporting does not continue indefinitely if not needed. [Fields: ]"""
  e8e8c03req: int = (105, "Requests the remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x03 [Fields: ]")
  """Requests the remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x03 [Fields: ]"""
  e8e8c03cmd: int = (106, "Sets the remote display configuration [Fields: DataLocation]")
  """Sets the remote display configuration [Fields: DataLocation]"""
  e8e8c04req: int = (107, "Requests the extended remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x04 [Fields: ]")
  """Requests the extended remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x04 [Fields: ]"""
  e8e8c04cmd: int = (108, "Sets the extended remote display configuration [Fields: DataLocation]")
  """Sets the extended remote display configuration [Fields: DataLocation]"""
  e8e8c05cmd: int = (109, "Indicates that one of the event lines into the remote display has changed state. [Fields: EventPort LineState]")
  """Indicates that one of the event lines into the remote display has changed state. [Fields: EventPort LineState]"""
  e8e8freq: int = (110, "Requests a report containing the receiver's Machine ID and Product ID used to uniquely identify the receiver architecture. Report Packet 0x8F 0x8F is sent in response. [Fields: ]")
  """Requests a report containing the receiver's Machine ID and Product ID used to uniquely identify the receiver architecture. Report Packet 0x8F 0x8F is sent in response. [Fields: ]"""
  e8e91req: int = (111, "Request the Guidance Configuration Information [Fields: ]")
  """Request the Guidance Configuration Information [Fields: ]"""
  e8e91cmd: int = (112, "Set the guidance configuration information [Fields: Units DisplayMode Headland Pattern LookAhead SwathDirection SwathWidth AntennaOffset OutputRate SwathsToSkip]")
  """Set the guidance configuration information [Fields: Units DisplayMode Headland Pattern LookAhead SwathDirection SwathWidth AntennaOffset OutputRate SwathsToSkip]"""
  e8e931500req: int = (113, "Requests a list of files found in the specified directory. A File Transfer Listing Reponse packet is sent for each file in the directory (empty directory will produce no response). [Fields: PathLength, Path]")
  """Requests a list of files found in the specified directory. A File Transfer Listing Reponse packet is sent for each file in the directory (empty directory will produce no response). [Fields: PathLength, Path]"""
  e8e93150101req: int = (114, "Requests that file be opened for reading. File Transfer Get - Open Response is sent with info needed for the transfer. [Fields: FilenameLength, Filename]")
  """Requests that file be opened for reading. File Transfer Get - Open Response is sent with info needed for the transfer. [Fields: FilenameLength, Filename]"""
  e8e93150102req: int = (115, "Requests to read block of data from open file. If successful File Transfer Get - Data Block Response is sent with the data, otherwise File Transfer Get - Close Response or File Transfer Get - Error Response is sent. [Fields: FileId Offset Size]")
  """Requests to read block of data from open file. If successful File Transfer Get - Data Block Response is sent with the data, otherwise File Transfer Get - Close Response or File Transfer Get - Error Response is sent. [Fields: FileId Offset Size]"""
  e8e93150103req: int = (116, "Requests to close previously opened file. If successful File Transfer Get - Close Response is sent, otherwise File Transfer Get - Error Response is sent. [Fields: FileId]")
  """Requests to close previously opened file. If successful File Transfer Get - Close Response is sent, otherwise File Transfer Get - Error Response is sent. [Fields: FileId]"""
  e8e93150104req: int = (117, "Requests an Hash of the specified file in the fusion file system. The receiver will respond with an Hash response packet (8f930104...) [Fields: Algorithm, FilenameLength, Filename]")
  """Requests an Hash of the specified file in the fusion file system. The receiver will respond with an Hash response packet (8f930104...) [Fields: Algorithm, FilenameLength, Filename]"""
  e8e93150201req: int = (118, "Requests that file be opened for writing. File Transfer Put - Open Response is sent with info needed for the transfer. [Fields: FilenameLength, Filename]")
  """Requests that file be opened for writing. File Transfer Put - Open Response is sent with info needed for the transfer. [Fields: FilenameLength, Filename]"""
  e8e93150202req: int = (119, "Requests to write block of data to open file. If successful File Transfer Put - Data Block Response is sent with the data, otherwise File Transfer Put - Close Response or File Transfer Put - Error Response is sent. [Fields: FileId Offset Size, DataBlockLength, DataBlock]")
  """Requests to write block of data to open file. If successful File Transfer Put - Data Block Response is sent with the data, otherwise File Transfer Put - Close Response or File Transfer Put - Error Response is sent. [Fields: FileId Offset Size, DataBlockLength, DataBlock]"""
  e8e93150203req: int = (120, "Requests to close previously opened file. If successful File Transfer Put - Close Response is sent, otherwise File Transfer Put - Error Response is sent. [Fields: FileId]")
  """Requests to close previously opened file. If successful File Transfer Put - Close Response is sent, otherwise File Transfer Put - Error Response is sent. [Fields: FileId]"""
  e8e931503req: int = (121, "Requests delete of specified file. File Transfer Delete Response is sent to indicate status. [Fields: FilenameLength, Filename]")
  """Requests delete of specified file. File Transfer Delete Response is sent to indicate status. [Fields: FilenameLength, Filename]"""
  e8e9areq: int = (122, "Requests a report containing differential correction information. Report Packet 0x8F 0x9A is sent in response. [Fields: ]")
  """Requests a report containing differential correction information. Report Packet 0x8F 0x9A is sent in response. [Fields: ]"""
  e8e9ereq: int = (123, "Requests a report containing DGPS source priorities. Report Packet 0x8F 0x9E is sent in response. [Fields: ]")
  """Requests a report containing DGPS source priorities. Report Packet 0x8F 0x9E is sent in response. [Fields: ]"""
  e8e9ecmd: int = (124, "Sets the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be set. The resulting receiver configuration is returned in the response packet 0x8F 0x9E. [Fields: NumSources SourceInfoArray]")
  """Sets the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be set. The resulting receiver configuration is returned in the response packet 0x8F 0x9E. [Fields: NumSources SourceInfoArray]"""
  e8e9f00req: int = (125, "Request information on the CAN bus configuration [Fields: ]")
  """Request information on the CAN bus configuration [Fields: ]"""
  e8e9f00cmd: int = (126, "Sets the CAN bus configuration for specified channels [Fields: NumChannels ChannelCfg]")
  """Sets the CAN bus configuration for specified channels [Fields: NumChannels ChannelCfg]"""
  e8e9f01req: int = (127, "Request information on the CAN bus status [Fields: ]")
  """Request information on the CAN bus status [Fields: ]"""
  e8e9f02req: int = (128, "Request current J1939 message configuration for channel [Fields: Channel]")
  """Request current J1939 message configuration for channel [Fields: Channel]"""
  e8e9f02cmd: int = (129, "Configures one or more J1939 messages for channel [Fields: Channel NumMessages MsgCfgArray]")
  """Configures one or more J1939 messages for channel [Fields: Channel NumMessages MsgCfgArray]"""
  e8e9f03req: int = (130, "Request current NMEA2K message configuration for channel [Fields: Channel]")
  """Request current NMEA2K message configuration for channel [Fields: Channel]"""
  e8e9f03cmd: int = (131, "Configures one or more NMEA2K messages for channel [Fields: Channel NumMessages MsgCfgArray]")
  """Configures one or more NMEA2K messages for channel [Fields: Channel NumMessages MsgCfgArray]"""
  e8e9f04req: int = (132, "Request current ISO message configuration for channel [Fields: Channel]")
  """Request current ISO message configuration for channel [Fields: Channel]"""
  e8e9f04cmd: int = (133, "Configures one or more ISO messages for channel [Fields: Channel NumMessages MsgCfgArray]")
  """Configures one or more ISO messages for channel [Fields: Channel NumMessages MsgCfgArray]"""
  e8ea0cmd: int = (134, "Request an option upgrade via a supplied password. The receiver respond by sending Response Packet 0x8F 0xA0. [Fields: Password]")
  """Request an option upgrade via a supplied password. The receiver respond by sending Response Packet 0x8F 0xA0. [Fields: Password]"""
  e8ea1cmd: int = (135, "This is an alias to 0x8e 0xa1. [Fields: PacketDataLength, PacketData]")
  """This is an alias to 0x8e 0xa1. [Fields: PacketDataLength, PacketData]"""
  e8ea2req: int = (136, "Requests a Position Solution Status 0x8F 0xA2 report. [Fields: ]")
  """Requests a Position Solution Status 0x8F 0xA2 report. [Fields: ]"""
  e8ea3req: int = (137, "Requests specific information about the Omnistar XP/HP process [Fields: Type]")
  """Requests specific information about the Omnistar XP/HP process [Fields: Type]"""
  e8ea304cmd: int = (138, "Sets Auto-Seed information held by the receiver. If the Auto-Seed functionality is turned on in the receiver, these values will be used at startup when the receiver is rebooted. [Fields: Confidence Latitude Longitude Height LatitudeVariance LongitudeVariance HeightVariance]")
  """Sets Auto-Seed information held by the receiver. If the Auto-Seed functionality is turned on in the receiver, these values will be used at startup when the receiver is rebooted. [Fields: Confidence Latitude Longitude Height LatitudeVariance LongitudeVariance HeightVariance]"""
  e8ea305cmd: int = (139, "Sets various control parameters of the Omnistar XP/HP processor [Fields: ValidFields SeedOnStartup ConfidenceThreshold VelocityThreshold ConvergenceThreshold StaticConvergence SourceSelector]")
  """Sets various control parameters of the Omnistar XP/HP processor [Fields: ValidFields SeedOnStartup ConfidenceThreshold VelocityThreshold ConvergenceThreshold StaticConvergence SourceSelector]"""
  e8ea306cmd: int = (140, "Sets up the debugging output of the XP/HP processor [Fields: Enabled Port]")
  """Sets up the debugging output of the XP/HP processor [Fields: Enabled Port]"""
  e8ea307cmd: int = (141, "Resets the XP/HP engine [Fields: ]")
  """Resets the XP/HP engine [Fields: ]"""
  e8ea4req: int = (142, "Requests Filter configuration. Report Packet 0x8F 0xA4 is sent in response. [Fields: Type]")
  """Requests Filter configuration. Report Packet 0x8F 0xA4 is sent in response. [Fields: Type]"""
  e8ea405cmd: int = (143, "Sets Quadratic Bias Filter configuration. Report Packet 0x8F 0xA4 0x05 is sent in response. [Fields: Time Depth MaxPropagationTime State]")
  """Sets Quadratic Bias Filter configuration. Report Packet 0x8F 0xA4 0x05 is sent in response. [Fields: Time Depth MaxPropagationTime State]"""
  e8ea406cmd: int = (144, "Sets Kalman Filter configuration. Report Packet 0x8F 0xA4 0x06 is sent in response. [Fields: MaxPropagationTime SpeedSetting State]")
  """Sets Kalman Filter configuration. Report Packet 0x8F 0xA4 0x06 is sent in response. [Fields: MaxPropagationTime SpeedSetting State]"""
  e8ea407cmd: int = (145, "Command to enable or disable Field Level Smoothing. Response (ACK) Packet is 0x8f 0xa4 0x07 [Fields: SmoothingEnable]")
  """Command to enable or disable Field Level Smoothing. Response (ACK) Packet is 0x8f 0xa4 0x07 [Fields: SmoothingEnable]"""
  e8ea500req: int = (146, "Requests and sets the current SBAS settings. The command and report packets can each contain a variable number of SBAS SV entries. [Fields: ]")
  """Requests and sets the current SBAS settings. The command and report packets can each contain a variable number of SBAS SV entries. [Fields: ]"""
  e8ea500cmd: int = (147, "Sets the current SBAS settings. This packet can contain a variable number of SBAS SV entries. SV entries not listed in the command packet will not be updated. [Fields: NumSvs SBASInfoArray]")
  """Sets the current SBAS settings. This packet can contain a variable number of SBAS SV entries. SV entries not listed in the command packet will not be updated. [Fields: NumSvs SBASInfoArray]"""
  e8ea501req: int = (148, "Requests the current 'Use SBAS+' settings. Response packet is 0x8F 0xA5 0x01 [Fields: ]")
  """Requests the current 'Use SBAS+' settings. Response packet is 0x8F 0xA5 0x01 [Fields: ]"""
  e8ea501cmd: int = (149, "Sets the 'Use SBAS+' configuration settings. SBAS+ mode uses as much SBAS correction information as possible and as many satellites as possible to improve yield and accuracy when positioning in SBAS mode. Response packet is 0x8F 0xA5 0x01 [Fields: UseSBASPlus]")
  """Sets the 'Use SBAS+' configuration settings. SBAS+ mode uses as much SBAS correction information as possible and as many satellites as possible to improve yield and accuracy when positioning in SBAS mode. Response packet is 0x8F 0xA5 0x01 [Fields: UseSBASPlus]"""
  e8ea502cmd: int = (150, "Resets the receiver's SBAS constellation tracking scheme to the defaults. [Fields: ResetSBASTrackingDefaults]")
  """Resets the receiver's SBAS constellation tracking scheme to the defaults. [Fields: ResetSBASTrackingDefaults]"""
  e8ea601cmd: int = (151, "Sets the state of a Output pin. [Fields: ProductId OutputPin0 OutputPin1 OutputPin2 OutputPin3]")
  """Sets the state of a Output pin. [Fields: ProductId OutputPin0 OutputPin1 OutputPin2 OutputPin3]"""
  e8ea602req: int = (152, "Request the state of an external input pin. [Fields: ProductId]")
  """Request the state of an external input pin. [Fields: ProductId]"""
  e8ea608req: int = (153, "Requests the manufacturing information of the unit. [Fields: ]")
  """Requests the manufacturing information of the unit. [Fields: ]"""
  e8ea617req: int = (154, "Requests Omnistar Id from the unit. [Fields: ]")
  """Requests Omnistar Id from the unit. [Fields: ]"""
  e8ea622req: int = (155, "Requests MAC addresses from the unit. [Fields: ]")
  """Requests MAC addresses from the unit. [Fields: ]"""
  e8ea623req: int = (156, "Requests the alternate unique ID from the unit. [Fields: ]")
  """Requests the alternate unique ID from the unit. [Fields: ]"""
  e8ea624req: int = (157, "Requests unit's extended manufacturing information. [Fields: ]")
  """Requests unit's extended manufacturing information. [Fields: ]"""
  e8ea625cmd: int = (158, "Sets unit's extended manufacturing information. [Fields: ModuleSN, FactoryID]")
  """Sets unit's extended manufacturing information. [Fields: ModuleSN, FactoryID]"""
  e8ea626req: int = (159, "Requests unit's product information. [Fields: ]")
  """Requests unit's product information. [Fields: ]"""
  e8ea627cmd: int = (160, "Sets unit's product information. [Fields: PartNumber, Name, AbbrevName]")
  """Sets unit's product information. [Fields: PartNumber, Name, AbbrevName]"""
  e8ea628cmd: int = (161, "Put the receiver into manufacturing test mode. [Fields: key]")
  """Put the receiver into manufacturing test mode. [Fields: key]"""
  e8ea629req: int = (162, "Request the firmware signature at the given offset. [Fields: Offset]")
  """Request the firmware signature at the given offset. [Fields: Offset]"""
  e8ea630req: int = (163, "Requests the peak FFT frequency from the RF spectrum analyzer for GNSS bands. Intended for factory test use only. [Fields: ProductId RFBand]")
  """Requests the peak FFT frequency from the RF spectrum analyzer for GNSS bands. Intended for factory test use only. [Fields: ProductId RFBand]"""
  e8ea631req: int = (164, "Requests metadata about the MSS tracking, including the peak value of the FFT, min/max signal level and gain in db/%  [Fields: ProductId]")
  """Requests metadata about the MSS tracking, including the peak value of the FFT, min/max signal level and gain in db/%  [Fields: ProductId]"""
  e8ea632req: int = (165, "Requests a register read operation to a specific polaris device [Fields: ProductId AntennaId PolarisI2CAddr PolarisRegAddr]")
  """Requests a register read operation to a specific polaris device [Fields: ProductId AntennaId PolarisI2CAddr PolarisRegAddr]"""
  e8ea632cmd: int = (166, "Writes a value to a specific polaris device's register [Fields: ProductId AntennaId PolarisI2CAddr PolarisRegAddr WriteData]")
  """Writes a value to a specific polaris device's register [Fields: ProductId AntennaId PolarisI2CAddr PolarisRegAddr WriteData]"""
  e8ea633req: int = (167, "Requests a ADC read of the RSSI on a specific polaris device [Fields: ProductId AntennaId RFBand]")
  """Requests a ADC read of the RSSI on a specific polaris device [Fields: ProductId AntennaId RFBand]"""
  e8ea634req: int = (168, "Requests the receiver to perform the Polaris full AGC test. The receiver will acknowledge the request, and then send the 0x8f 0xa6 0x34 response when the test completes. [Fields: ProductId]")
  """Requests the receiver to perform the Polaris full AGC test. The receiver will acknowledge the request, and then send the 0x8f 0xa6 0x34 response when the test completes. [Fields: ProductId]"""
  e8ea640cmd: int = (169, "Enables the PLT (Production Line Test) Mode for WiFi testing. [Fields: ProductId]")
  """Enables the PLT (Production Line Test) Mode for WiFi testing. [Fields: ProductId]"""
  e8ea641cmd: int = (170, "Disables the PLT (Production Line Test) Mode for WiFi testing. [Fields: ProductId]")
  """Disables the PLT (Production Line Test) Mode for WiFi testing. [Fields: ProductId]"""
  e8ea642cmd: int = (171, "Configures the device to operate in a specific WiFi band and channel. [Fields: ProductId Channel Band Bandwidth]")
  """Configures the device to operate in a specific WiFi band and channel. [Fields: ProductId Channel Band Bandwidth]"""
  e8ea643cmd: int = (172, "Sets the transmission power of the WL18xx device. [Fields: ProductId OutputPower Level Band Channel Bandwidth Antenna NonServingChannel ChannelLimitation GainCalculationMode AnalogGainControl]")
  """Sets the transmission power of the WL18xx device. [Fields: ProductId OutputPower Level Band Channel Bandwidth Antenna NonServingChannel ChannelLimitation GainCalculationMode AnalogGainControl]"""
  e8ea644cmd: int = (173, "Enables TX test using the start_tx command. [Fields: ProductId Delay Rate Size Mode GuardInterval Options1 Options2, SourceMAC, DestMAC ChannelWidth]")
  """Enables TX test using the start_tx command. [Fields: ProductId Delay Rate Size Mode GuardInterval Options1 Options2, SourceMAC, DestMAC ChannelWidth]"""
  e8ea645cmd: int = (174, "Disables TX test using the stop_tx command. [Fields: ProductId]")
  """Disables TX test using the stop_tx command. [Fields: ProductId]"""
  e8ea646cmd: int = (175, "Starts calculations of RX statistics. [Fields: ProductId, SourceMAC, DestMAC]")
  """Starts calculations of RX statistics. [Fields: ProductId, SourceMAC, DestMAC]"""
  e8ea647req: int = (176, "Requests the RX statistics. [Fields: ProductId]")
  """Requests the RX statistics. [Fields: ProductId]"""
  e8ea648cmd: int = (177, "Stops calculations of the RX statistics. [Fields: ProductId]")
  """Stops calculations of the RX statistics. [Fields: ProductId]"""
  e8ea70000cmd: int = (178, "Sets up default automatic reports for a selected antenna. This will output the position used internally by the receiver. [Fields: Enable AntennaId]")
  """Sets up default automatic reports for a selected antenna. This will output the position used internally by the receiver. [Fields: Enable AntennaId]"""
  e8ea70001cmd: int = (179, "Sets up automatic reports for a selected antenna based on the position engine used to generate the solution. Only positions of from the specified engines will be output [Fields: Enable AntennaId NumEngs PositionEngArray]")
  """Sets up automatic reports for a selected antenna based on the position engine used to generate the solution. Only positions of from the specified engines will be output [Fields: Enable AntennaId NumEngs PositionEngArray]"""
  e8ea70002cmd: int = (180, "Sets up automatic reports for a selected antenna based on the position type produced. Only positions of those types will be output. [Fields: Enable AntennaId NumTypes PositionTypeArray]")
  """Sets up automatic reports for a selected antenna based on the position type produced. Only positions of those types will be output. [Fields: Enable AntennaId NumTypes PositionTypeArray]"""
  e8ea70003cmd: int = (181, "Sets up automatic reports for a selected antenna based on the position flags assigned. Only positions with the given flags will be output. [Fields: Enable AntennaId SetFlags ClearedFlags]")
  """Sets up automatic reports for a selected antenna based on the position flags assigned. Only positions with the given flags will be output. [Fields: Enable AntennaId SetFlags ClearedFlags]"""
  e8ea70100req: int = (182, "Requests the last position from for a specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId]")
  """Requests the last position from for a specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId]"""
  e8ea70101req: int = (183, "Requests the last position from the given engine on the specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId PositionEng]")
  """Requests the last position from the given engine on the specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId PositionEng]"""
  e8ea70102req: int = (184, "Requests the last position of the given type from the specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId PositionType]")
  """Requests the last position of the given type from the specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId PositionType]"""
  e8ea70103req: int = (185, "Requests the last position matching the provided flags from the specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId SetFlags ClearedFlags]")
  """Requests the last position matching the provided flags from the specified antenna. If the last position wasn't valid, a no position is output instead [Fields: AntennaId SetFlags ClearedFlags]"""
  e8ea800req: int = (186, "Request the VRS Radio Status [Fields: ]")
  """Request the VRS Radio Status [Fields: ]"""
  e8ea801cmd: int = (187, "Set the NTRIP parameters for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: IPPort IPAddrLength IPAddress MountPointLength MountPoint UserNameLength UserName PasswordLength Password UseForRTX]")
  """Set the NTRIP parameters for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: IPPort IPAddrLength IPAddress MountPointLength MountPoint UserNameLength UserName PasswordLength Password UseForRTX]"""
  e8ea801req: int = (188, "Request the NTRIP parameters for the VRS Radio [Fields: ]")
  """Request the NTRIP parameters for the VRS Radio [Fields: ]"""
  e8ea802cmd: int = (189, "Set the GPRS Username for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength UserName]")
  """Set the GPRS Username for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength UserName]"""
  e8ea802req: int = (190, "Request the GPRS Username for the VRS Radio [Fields: ]")
  """Request the GPRS Username for the VRS Radio [Fields: ]"""
  e8ea803cmd: int = (191, "Set the GPRS Password for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength Password]")
  """Set the GPRS Password for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength Password]"""
  e8ea803req: int = (192, "Request the GPRS Password for the VRS Radio [Fields: ]")
  """Request the GPRS Password for the VRS Radio [Fields: ]"""
  e8ea804cmd: int = (193, "Set the GPRS InitString for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength InitString]")
  """Set the GPRS InitString for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength InitString]"""
  e8ea804req: int = (194, "Request the GPRS InitString for the VRS Radio [Fields: ]")
  """Request the GPRS InitString for the VRS Radio [Fields: ]"""
  e8ea805cmd: int = (195, "Set the GPRS CPIN for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength CPIN]")
  """Set the GPRS CPIN for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: StringLength CPIN]"""
  e8ea806cmd: int = (196, "Configure the VRS Radio [Fields: EnableVRS EnableAutoReport StreamType]")
  """Configure the VRS Radio [Fields: EnableVRS EnableAutoReport StreamType]"""
  e8ea806req: int = (197, "Request the VRS Radio Config [Fields: ]")
  """Request the VRS Radio Config [Fields: ]"""
  e8ea900req: int = (198, "Requests the various firmware and hardware version information [Fields: ]")
  """Requests the various firmware and hardware version information [Fields: ]"""
  e8ea90100cmd: int = (199, "Requests that the receiver begin upgrading with the provided file. The upgrading performed by the receiver will depend on the hardware, but it is expected to begin upgrading if possible. The receiver will respond with information regarding whether the request was carried out. [Fields: ImageType FilenameLen Filename]")
  """Requests that the receiver begin upgrading with the provided file. The upgrading performed by the receiver will depend on the hardware, but it is expected to begin upgrading if possible. The receiver will respond with information regarding whether the request was carried out. [Fields: ImageType FilenameLen Filename]"""
  e8ea90101cmd: int = (200, "Allows the user to start and stop logging, and provide the location to log to. [Fields: Action prefixLen prefix]")
  """Allows the user to start and stop logging, and provide the location to log to. [Fields: Action prefixLen prefix]"""
  e8ea90101req: int = (201, "Requests the current status of the logging control [Fields: ]")
  """Requests the current status of the logging control [Fields: ]"""
  e8ea90102cmd: int = (202, "Requests a particular log be dumped to specified path. [Fields: LogType FilenameLen Filename]")
  """Requests a particular log be dumped to specified path. [Fields: LogType FilenameLen Filename]"""
  e8ea90103cmd: int = (203, "Sends a variable length data packet (ping), that will be returned by the receiver (pong). This allows a type of serial communication test to occur. [Fields: PingSize Data]")
  """Sends a variable length data packet (ping), that will be returned by the receiver (pong). This allows a type of serial communication test to occur. [Fields: PingSize Data]"""
  e8ea90104req: int = (204, "Request the IP Address and port number for the VRS Daemon [Fields: ]")
  """Request the IP Address and port number for the VRS Daemon [Fields: ]"""
  e8ea90104cmd: int = (205, "Set the IP Address and port number for the VRS Daemon [Fields: IP Port]")
  """Set the IP Address and port number for the VRS Daemon [Fields: IP Port]"""
  e8ea90105cmd: int = (206, "Requests that the receiver install licenses with a given file [Fields: FilenameLen Filename]")
  """Requests that the receiver install licenses with a given file [Fields: FilenameLen Filename]"""
  e8ea90106req: int = (207, "Request the current state of the receiver automatic reboot capability [Fields: ]")
  """Request the current state of the receiver automatic reboot capability [Fields: ]"""
  e8ea90106cmd: int = (208, "Control the frequency at which the receiver will automatically reboot [Fields: Frequency]")
  """Control the frequency at which the receiver will automatically reboot [Fields: Frequency]"""
  e8ea90107req: int = (209, "Request the IP Address and port number for the CLAAS RTK NET modem [Fields: ]")
  """Request the IP Address and port number for the CLAAS RTK NET modem [Fields: ]"""
  e8ea90107cmd: int = (210, "Set the IP Address and port number for the CLAAS RTK NET modem [Fields: IP Port]")
  """Set the IP Address and port number for the CLAAS RTK NET modem [Fields: IP Port]"""
  e8ea90108req: int = (211, "Request the TNFS Host Address [Fields: ]")
  """Request the TNFS Host Address [Fields: ]"""
  e8ea90108cmd: int = (212, "Set the IP Address for the TNFS Host Address [Fields: IP]")
  """Set the IP Address for the TNFS Host Address [Fields: IP]"""
  e8ea90130req: int = (213, "Requests the upgrade/downgrade version floor of the receiver [Fields: ]")
  """Requests the upgrade/downgrade version floor of the receiver [Fields: ]"""
  e8ea90131req: int = (214, "Checks if an upgrade/downgrade to the given version is allowed [Fields: MajorVersion MinorVersion BuildNum BuildType FeatureSpecific]")
  """Checks if an upgrade/downgrade to the given version is allowed [Fields: MajorVersion MinorVersion BuildNum BuildType FeatureSpecific]"""
  e8ea90200req: int = (215, "Request the mux settings of the digital output of a particular port. [Fields: PortId]")
  """Request the mux settings of the digital output of a particular port. [Fields: PortId]"""
  e8ea90200cmd: int = (216, "Sets the mux behaviour of the digital output for a particular port. [Fields: PortId MuxType OutputValue]")
  """Sets the mux behaviour of the digital output for a particular port. [Fields: PortId MuxType OutputValue]"""
  e8ea90201req: int = (217, "Request the settings of the digital input of a particular port. [Fields: PortId]")
  """Request the settings of the digital input of a particular port. [Fields: PortId]"""
  e8ea90201cmd: int = (218, "Sets the behaviour of the digital input for a particular port. [Fields: PortId Threshold Pull]")
  """Sets the behaviour of the digital input for a particular port. [Fields: PortId Threshold Pull]"""
  e8ea90202req: int = (219, "Request the settings of the Pollux FPGA GPO. [Fields: ]")
  """Request the settings of the Pollux FPGA GPO. [Fields: ]"""
  e8ea90202cmd: int = (220, "Sets the behaviour of the GPO for the Pollux FPGA. [Fields: GPOSetting]")
  """Sets the behaviour of the GPO for the Pollux FPGA. [Fields: GPOSetting]"""
  e8ea90300req: int = (221, "Requests information about connected Antennas. [Fields: ]")
  """Requests information about connected Antennas. [Fields: ]"""
  e8ea90301cmd: int = (222, "Commands the power state of an antenna. The command is acknowledged with the Antenna info packet. [Fields: AntennaId PowerOn]")
  """Commands the power state of an antenna. The command is acknowledged with the Antenna info packet. [Fields: AntennaId PowerOn]"""
  e8ea90400req: int = (223, "Requests information on the Radar setup [Fields: ]")
  """Requests information on the Radar setup [Fields: ]"""
  e8ea90400cmd: int = (224, "Configures the Radar setup [Fields: Enable FreqSpeedRate]")
  """Configures the Radar setup [Fields: Enable FreqSpeedRate]"""
  e8ea905cmd: int = (225, "Place a string command into the receiver program log. Responds with a simple ack. [Fields: TimeStamp EventType Length LogMessage]")
  """Place a string command into the receiver program log. Responds with a simple ack. [Fields: TimeStamp EventType Length LogMessage]"""
  e8ea90600req: int = (226, "Requests the reading of the given ADC Channel [Fields: Normalized Channel]")
  """Requests the reading of the given ADC Channel [Fields: Normalized Channel]"""
  e8ea90700req: int = (227, "Requests the settings of the Module-A Digital Pin Muxing. [Fields: DigitalPin]")
  """Requests the settings of the Module-A Digital Pin Muxing. [Fields: DigitalPin]"""
  e8ea90700cmd: int = (228, "Sets the Module-A Digital Pin Muxing. [Fields: DigitalPin MuxType Output]")
  """Sets the Module-A Digital Pin Muxing. [Fields: DigitalPin MuxType Output]"""
  e8ea90701req: int = (229, "Requests the settings of the pwmon control point. [Fields: CtrlPoint]")
  """Requests the settings of the pwmon control point. [Fields: CtrlPoint]"""
  e8ea90701cmd: int = (230, "Sets the Module-A power monitor options. [Fields: CtrlPoint CtrlCmd]")
  """Sets the Module-A power monitor options. [Fields: CtrlPoint CtrlCmd]"""
  e8ea90703req: int = (231, "Requests the settings Video Input Mux. [Fields: VideoInput]")
  """Requests the settings Video Input Mux. [Fields: VideoInput]"""
  e8ea90703cmd: int = (232, "Sets the Module-A Video Mux options. [Fields: VideoInput MuxInputValue Output]")
  """Sets the Module-A Video Mux options. [Fields: VideoInput MuxInputValue Output]"""
  e8ea90704req: int = (233, "Requests Module-A auto shutdown timer settings. [Fields: ]")
  """Requests Module-A auto shutdown timer settings. [Fields: ]"""
  e8ea90704cmd: int = (234, "Sets Module-A auto shutdown timer delay. [Fields: Delay]")
  """Sets Module-A auto shutdown timer delay. [Fields: Delay]"""
  e8ea90705req: int = (235, "Gets the network interface configuration info. [Fields: NetIfaceSettingLife]")
  """Gets the network interface configuration info. [Fields: NetIfaceSettingLife]"""
  e8ea90705cmd: int = (236, "Sets the Module A's network interface to a specific setting. [Fields: NetIfaceSettingLife NetIfaceMode IP NetMask Gateway Broadcast]")
  """Sets the Module A's network interface to a specific setting. [Fields: NetIfaceSettingLife NetIfaceMode IP NetMask Gateway Broadcast]"""
  e8ea90706req: int = (237, "Requests Module-A hardware configuration [Fields: ]")
  """Requests Module-A hardware configuration [Fields: ]"""
  e8ea90707req: int = (238, "Requests the socket uart device details configured for Port-D on the Module-A [Fields: ]")
  """Requests the socket uart device details configured for Port-D on the Module-A [Fields: ]"""
  e8ea90707cmd: int = (239, "Sets the socket uart device to be used for Port-D on the Module-A.  The device must be a TBIP device that supports the socket-uart protocol. [Fields: TBIPDeviceType, SerialNumber UartId]")
  """Sets the socket uart device to be used for Port-D on the Module-A.  The device must be a TBIP device that supports the socket-uart protocol. [Fields: TBIPDeviceType, SerialNumber UartId]"""
  e8ea90708req: int = (240, "Retrieves the current counters statistics for a port on the switch [Fields: Port]")
  """Retrieves the current counters statistics for a port on the switch [Fields: Port]"""
  e8ea90800req: int = (241, "Requests the current state of RTK correction rebroadcasting [Fields: ]")
  """Requests the current state of RTK correction rebroadcasting [Fields: ]"""
  e8ea90800cmd: int = (242, "Sets the state of RTK correction rebroadcasting [Fields: Operation]")
  """Sets the state of RTK correction rebroadcasting [Fields: Operation]"""
  e8ea909req: int = (243, "Request the status of the Receiver LEDs (if supported). This request invokes a response TSIP packet: 0x8F 0xA9 0x08 0x00. [Fields: RcvrId LEDId]")
  """Request the status of the Receiver LEDs (if supported). This request invokes a response TSIP packet: 0x8F 0xA9 0x08 0x00. [Fields: RcvrId LEDId]"""
  e8ea909cmd: int = (244, "Sets the behaviour of Receiver LEDs. This command is acknowledged with TSIP Packet 0x8F 0xA9 0xA8 0x00. [Fields: RcvrId EnableTSIPControl LEDId LEDState]")
  """Sets the behaviour of Receiver LEDs. This command is acknowledged with TSIP Packet 0x8F 0xA9 0xA8 0x00. [Fields: RcvrId EnableTSIPControl LEDId LEDState]"""
  e8ea90a00req: int = (245, "Requests all the enabled features in the Feature Manager [Fields: ]")
  """Requests all the enabled features in the Feature Manager [Fields: ]"""
  e8ea90a01req: int = (246, "Requests the license status from the Feature Manager [Fields: ]")
  """Requests the license status from the Feature Manager [Fields: ]"""
  e8ea910req: int = (247, "Requests the status of receiver unlocks [Fields: ]")
  """Requests the status of receiver unlocks [Fields: ]"""
  e8ea911req: int = (248, "Product Information Request [Fields: ]")
  """Product Information Request [Fields: ]"""
  e8ea912req: int = (249, "Boot Count Information Request [Fields: ]")
  """Boot Count Information Request [Fields: ]"""
  e8ea913req: int = (250, "Geoidal Separation Information Request [Fields: ]")
  """Geoidal Separation Information Request [Fields: ]"""
  e8ea91500cmd: int = (251, "Initiates transfer operation (get or put) for the given file type. [Fields: xferType fileType fileSize clientFileIdSize clientFileId]")
  """Initiates transfer operation (get or put) for the given file type. [Fields: xferType fileType fileSize clientFileIdSize clientFileId]"""
  e8ea91501cmd: int = (252, "Request to get a block from a system file [Fields: fileId offset]")
  """Request to get a block from a system file [Fields: fileId offset]"""
  e8ea91502cmd: int = (253, "Request to put block to a system file [Fields: fileId offset blockSize blockData]")
  """Request to put block to a system file [Fields: fileId offset blockSize blockData]"""
  e8ea91503cmd: int = (254, "Closes the open stream identified by fileId [Fields: fileId]")
  """Closes the open stream identified by fileId [Fields: fileId]"""
  e8ea91504cmd: int = (255, "Requests deletion of the specified system file [Fields: fileType]")
  """Requests deletion of the specified system file [Fields: fileType]"""
  e8ea9160000req: int = (256, "Get the mode of the GP uart mux [Fields: ]")
  """Get the mode of the GP uart mux [Fields: ]"""
  e8ea9160000cmd: int = (257, "Change internal routing of the General Purpose UART port in Fusion [Fields: mode]")
  """Change internal routing of the General Purpose UART port in Fusion [Fields: mode]"""
  e8ea9160001req: int = (258, "Get the mux mode of the TX UART port in Fusion [Fields: ]")
  """Get the mux mode of the TX UART port in Fusion [Fields: ]"""
  e8ea9160001cmd: int = (259, "Change internal routing of the TX UART port in Fusion [Fields: mode]")
  """Change internal routing of the TX UART port in Fusion [Fields: mode]"""
  e8ea9160002req: int = (260, "Request the mux mode of the Radio port uart in Fusion [Fields: ]")
  """Request the mux mode of the Radio port uart in Fusion [Fields: ]"""
  e8ea9160002cmd: int = (261, "Change internal routing of the Radio port uart in Fusion [Fields: mode]")
  """Change internal routing of the Radio port uart in Fusion [Fields: mode]"""
  e8ea9160100req: int = (262, "Request the mode of the internal AP virtual uart in Fusion [Fields: ]")
  """Request the mode of the internal AP virtual uart in Fusion [Fields: ]"""
  e8ea9160100cmd: int = (263, "Sets the mode of the internal AP virtual uart in Fusion [Fields: mode]")
  """Sets the mode of the internal AP virtual uart in Fusion [Fields: mode]"""
  e8ea91602req: int = (264, "Request Bluetooth state (enabled or disabled) [Fields: ]")
  """Request Bluetooth state (enabled or disabled) [Fields: ]"""
  e8ea91602cmd: int = (265, "Enable/disable Bluetooth [Fields: enable]")
  """Enable/disable Bluetooth [Fields: enable]"""
  e8ea91603cmd: int = (266, "Clear All Licenses installed via user entry and factory installation [Fields: ]")
  """Clear All Licenses installed via user entry and factory installation [Fields: ]"""
  e8ea91604cmd: int = (267, "Remove / Restore Manufacturing Licenses [Fields: ClearType]")
  """Remove / Restore Manufacturing Licenses [Fields: ClearType]"""
  e8ea91605cmd: int = (268, "Remove Licenses By Fragment command [Fields: FragmentLen Fragment]")
  """Remove Licenses By Fragment command [Fields: FragmentLen Fragment]"""
  e8ea91606req: int = (269, "Requests UDS diagnostic status [Fields: ]")
  """Requests UDS diagnostic status [Fields: ]"""
  e8ea91700req: int = (270, "Request the IMU settings. Expects response of 0x8f 0xa9 0x17 0x00. [Fields: ]")
  """Request the IMU settings. Expects response of 0x8f 0xa9 0x17 0x00. [Fields: ]"""
  e8ea91700cmd: int = (271, "Send IMU settings to configure pitch and roll corrected positions. Expects response of 0x8f 0xa9 0x17 0x00. [Fields: AntLevX AntLevY AntLevZ ImuAngleRoll ImuAnglePitch ImuAngleYaw ImuLevX ImuLevY ImuLevZ ImuRollOffset ImuPitchOffset]")
  """Send IMU settings to configure pitch and roll corrected positions. Expects response of 0x8f 0xa9 0x17 0x00. [Fields: AntLevX AntLevY AntLevZ ImuAngleRoll ImuAnglePitch ImuAngleYaw ImuLevX ImuLevY ImuLevZ ImuRollOffset ImuPitchOffset]"""
  e8ea91701cmd: int = (272, "Enable Fusion position correction based on IMU values. [Fields: EnableIMUCorrection EnableIMUDetailStream]")
  """Enable Fusion position correction based on IMU values. [Fields: EnableIMUCorrection EnableIMUDetailStream]"""
  e8ea91701req: int = (273, "Query if IMU-Corrected positions and streaming are enabled. [Fields: ]")
  """Query if IMU-Corrected positions and streaming are enabled. [Fields: ]"""
  e8ea91702req: int = (274, "Get the position details in case streaming is off; IMU-corrected if enabled. [Fields: ]")
  """Get the position details in case streaming is off; IMU-corrected if enabled. [Fields: ]"""
  e8ea91703req: int = (275, "Request the IMU settings Block 2. Expects response of 0x8f 0xa9 0x17 0x03. [Fields: ]")
  """Request the IMU settings Block 2. Expects response of 0x8f 0xa9 0x17 0x03. [Fields: ]"""
  e8ea91703cmd: int = (276, "Send IMU settings to configure extra settings related to the Fusion IMU supported features. Expects response of 0x8f 0xa9 0x17 0x03. [Fields: ProPointEngineMode StaticBenchModeEnable StaticBenchHeading VehicleType]")
  """Send IMU settings to configure extra settings related to the Fusion IMU supported features. Expects response of 0x8f 0xa9 0x17 0x03. [Fields: ProPointEngineMode StaticBenchModeEnable StaticBenchHeading VehicleType]"""
  e8ea918req: int = (277, "Requests the cryptochip configuration CRC value [Fields: ]")
  """Requests the cryptochip configuration CRC value [Fields: ]"""
  e8ea9a5req: int = (278, "New 27 character passcode upgrade request packet [Fields: PasscodeString]")
  """New 27 character passcode upgrade request packet [Fields: PasscodeString]"""
  e8eaa00req: int = (279, "Requests type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response. [Fields: AntennaId]")
  """Requests type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response. [Fields: AntennaId]"""
  e8eaa00cmd: int = (280, "Command to set type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response. [Fields: AntennaId AntennaType]")
  """Command to set type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response. [Fields: AntennaId AntennaType]"""
  e8eab00req: int = (281, "Checks the RTX subscription on the receiver and shows which connections are available [Fields: ]")
  """Checks the RTX subscription on the receiver and shows which connections are available [Fields: ]"""
  e8eab01req: int = (282, "Requests the Centerpoint RTX fast Network Info from the receiver. Packet 0x8f 0xab 0x01 is sent in response. [Fields: ]")
  """Requests the Centerpoint RTX fast Network Info from the receiver. Packet 0x8f 0xab 0x01 is sent in response. [Fields: ]"""
  e8eab02cmd: int = (283, "Cancels RTX std FastRestart. The command is acknowledged with packet 0x8f 0xab 0x02. [Fields: ]")
  """Cancels RTX std FastRestart. The command is acknowledged with packet 0x8f 0xab 0x02. [Fields: ]"""
  e8eab03req: int = (284, "Requests CenterPoint RTX status. The command is acknowledged with packet 0x8f 0xab 0x03. [Fields: ]")
  """Requests CenterPoint RTX status. The command is acknowledged with packet 0x8f 0xab 0x03. [Fields: ]"""
  e8eab04cmd: int = (285, "Allows TSIP to confirm whether vehicle has moved post reboot on FastRestart enabled Ag receivers. The command is acknowledged with packet 0x8f 0xab 0x04. [Fields: HasVehicleMoved]")
  """Allows TSIP to confirm whether vehicle has moved post reboot on FastRestart enabled Ag receivers. The command is acknowledged with packet 0x8f 0xab 0x04. [Fields: HasVehicleMoved]"""
  e8eab05cmd: int = (286, "Allows the RTX output settings to be selected using TSIP. The command is acknowledged with packet 0x8f 0xab 0x05. [Fields: RTXOutputDatum RTXOffset]")
  """Allows the RTX output settings to be selected using TSIP. The command is acknowledged with packet 0x8f 0xab 0x05. [Fields: RTXOutputDatum RTXOffset]"""
  e8eab05req: int = (287, "Requests the current RTX output settings using TSIP. The request is acknowledged with packet 0x8f 0xab 0x05. [Fields: ]")
  """Requests the current RTX output settings using TSIP. The request is acknowledged with packet 0x8f 0xab 0x05. [Fields: ]"""
  e8eab06cmd: int = (288, "If RTK is unlocked, function automatically determines what Centerpoint RTX (FAST/STD) to be used based on what Centerpoint license is available. If RTK and/or RTX unlock(s) are not found, convergence is autoamtically set to SBAS. The request is acknowledged with packet 0x8f 0xab 0x06. [Fields: ]")
  """If RTK is unlocked, function automatically determines what Centerpoint RTX (FAST/STD) to be used based on what Centerpoint license is available. If RTK and/or RTX unlock(s) are not found, convergence is autoamtically set to SBAS. The request is acknowledged with packet 0x8f 0xab 0x06. [Fields: ]"""
  e8eab07req: int = (289, "Request the current configuration and mode of the MSS Mode Switch [Fields: ]")
  """Request the current configuration and mode of the MSS Mode Switch [Fields: ]"""
  e8eab07cmd: int = (290, "Control the MSS Mode Switch [Fields: MSSControlMode]")
  """Control the MSS Mode Switch [Fields: MSSControlMode]"""
  e8eab08req: int = (291, "Requests the realtime RTK/RTX Custom Offsets using TSIP. The request is acknowledged with packet 0x8f 0xab 0x08. [Fields: RtkRtxCustomOffsetRequest]")
  """Requests the realtime RTK/RTX Custom Offsets using TSIP. The request is acknowledged with packet 0x8f 0xab 0x08. [Fields: RtkRtxCustomOffsetRequest]"""
  e8eac0000cmd: int = (292, "Sets the configuration for genral parameters of the boom height system [Fields: APIversion enabled targetHeight sprayerSuspensionType sensingMode groundSensitivity canopySensitivity groundFilter canopyFilter chevronThresh maximumHeight minimumHeight minSafeHeightBelowTarget heightStep aggressiveness downSlewLim downGainStabilizer wingPhasingHeightThreshold useKato autoDisableTimeout]")
  """Sets the configuration for genral parameters of the boom height system [Fields: APIversion enabled targetHeight sprayerSuspensionType sensingMode groundSensitivity canopySensitivity groundFilter canopyFilter chevronThresh maximumHeight minimumHeight minSafeHeightBelowTarget heightStep aggressiveness downSlewLim downGainStabilizer wingPhasingHeightThreshold useKato autoDisableTimeout]"""
  e8eac0001cmd: int = (293, "Sets the configuration for sensor parameters of the boom height system [Fields: APIversion numberOfSensors sensorsArray]")
  """Sets the configuration for sensor parameters of the boom height system [Fields: APIversion numberOfSensors sensorsArray]"""
  e8eac0002cmd: int = (294, "Sets the configuration for actuator parameters of the boom height system [Fields: APIversion numberOfActuators actuatorsArray]")
  """Sets the configuration for actuator parameters of the boom height system [Fields: APIversion numberOfActuators actuatorsArray]"""
  e8eac0100req: int = (295, "Requests the configuration for genral parameters [Fields: APIversion]")
  """Requests the configuration for genral parameters [Fields: APIversion]"""
  e8eac0101req: int = (296, "Requests the configuration for sensor parameters [Fields: APIversion]")
  """Requests the configuration for sensor parameters [Fields: APIversion]"""
  e8eac0102req: int = (297, "Requests the configuration for actuator parameters [Fields: APIversion]")
  """Requests the configuration for actuator parameters [Fields: APIversion]"""
  e8eac02cmd: int = (298, "Commands to initiate actuator calibration modes [Fields: APIversion CalType ChangeStateAction ZoneLocation]")
  """Commands to initiate actuator calibration modes [Fields: APIversion CalType ChangeStateAction ZoneLocation]"""
  e8eac03req: int = (299, "Request for actuator status [Fields: APIversion]")
  """Request for actuator status [Fields: APIversion]"""
  e8eac04cmd: int = (300, "Sets the Boom Height control state system including various parameters. This is typically sent periodically at 5Hz [Fields: APIversion TargetHeight SystemAggr SensorMode SensorSensitivity NumManZones ManualZoneArray]")
  """Sets the Boom Height control state system including various parameters. This is typically sent periodically at 5Hz [Fields: APIversion TargetHeight SystemAggr SensorMode SensorSensitivity NumManZones ManualZoneArray]"""
  e8eac05cmd: int = (301, "Commands to commit system actions [Fields: APIversion StateAction ZoneLocation]")
  """Commands to commit system actions [Fields: APIversion StateAction ZoneLocation]"""
  e8eac06req: int = (302, "Requests alert statuses [Fields: APIversion]")
  """Requests alert statuses [Fields: APIversion]"""
  e8eac07req: int = (303, "Request list of attached devices [Fields: APIversion]")
  """Request list of attached devices [Fields: APIversion]"""
  e8ead00req: int = (304, "Retrieve Centerpoint or Rangepoint RTX Passcodes on the receiver if a subscription is available. Response Packet: 0x8f 0xad 0x00 [Fields: ]")
  """Retrieve Centerpoint or Rangepoint RTX Passcodes on the receiver if a subscription is available. Response Packet: 0x8f 0xad 0x00 [Fields: ]"""
  e8ead01cmd: int = (305, "Command to erase/clear Centerpoint/Rangepoint RTX Passcodes installed in the receiver. ACK Packet is 0x8f 0xad 0x01 [Fields: PasscodeType]")
  """Command to erase/clear Centerpoint/Rangepoint RTX Passcodes installed in the receiver. ACK Packet is 0x8f 0xad 0x01 [Fields: PasscodeType]"""
  e8ead02req: int = (306, "Retrieve RTX Position Allowed Status on the receiver. Response Packet: 0x8f 0xad 0x02 [Fields: ]")
  """Retrieve RTX Position Allowed Status on the receiver. Response Packet: 0x8f 0xad 0x02 [Fields: ]"""
  e8ead03cmd: int = (307, "Command to set or clear the RTX position allowed flag status. Response Packet: 0x8f 0xad 0x02 [Fields: RTXPositionAllowed]")
  """Command to set or clear the RTX position allowed flag status. Response Packet: 0x8f 0xad 0x02 [Fields: RTXPositionAllowed]"""
  e8eae00req: int = (308, "Requests the Bluetooth pairing information from the receiver [Fields: ]")
  """Requests the Bluetooth pairing information from the receiver [Fields: ]"""
  e8eae01cmd: int = (309, "Commands the power state of the Bluetooth module [Fields: Parameter]")
  """Commands the power state of the Bluetooth module [Fields: Parameter]"""
  e8eae02cmd: int = (310, "Commands the Bluetooth pairing state of the receiver [Fields: Parameter]")
  """Commands the Bluetooth pairing state of the receiver [Fields: Parameter]"""
  e8eae03cmd: int = (311, "Commands the receiver to unpair all Bluetooth devices [Fields: ]")
  """Commands the receiver to unpair all Bluetooth devices [Fields: ]"""
  e8eae04req: int = (312, "Request the NAV to report pairing state changes [Fields: ]")
  """Request the NAV to report pairing state changes [Fields: ]"""
  e8eae05req: int = (313, "Request notifications for Bluetooth device pairing and connection events [Fields: DeviceEventType]")
  """Request notifications for Bluetooth device pairing and connection events [Fields: DeviceEventType]"""
  e8fa90708req: int = (314, "The current counters statistics for a port on the switch [Fields: Port rxLoPriorityByte rxHiPriorityByte rxUndersizePkt rxFragments rxOversize rxJabbers rxSymbolError rxCRCError rxAlignmentError rxControl8808Pkts rxPausePkts rxBroadcast rxMulticast rxUnicast rx64Octets rx65To127Octets rx128To255Octets rx256To511Octets rx512To1023Octets rx1024To1522Octets txLoPriorityByte txHiPriorityByte txLateCollision txPausePkts txBroadcastPkts txMulticastPackets txUnicastPackets txDeferred txTotalCollision txExcessiveCollision txSingleCollision txMultipleCollision txDroppedPackets rxDroppedPackets]")
  """The current counters statistics for a port on the switch [Fields: Port rxLoPriorityByte rxHiPriorityByte rxUndersizePkt rxFragments rxOversize rxJabbers rxSymbolError rxCRCError rxAlignmentError rxControl8808Pkts rxPausePkts rxBroadcast rxMulticast rxUnicast rx64Octets rx65To127Octets rx128To255Octets rx256To511Octets rx512To1023Octets rx1024To1522Octets txLoPriorityByte txHiPriorityByte txLateCollision txPausePkts txBroadcastPkts txMulticastPackets txUnicastPackets txDeferred txTotalCollision txExcessiveCollision txSingleCollision txMultipleCollision txDroppedPackets rxDroppedPackets]"""
  eb000req: int = (315, "Requests the PPS configuration settings. The response is sent in 0xB0 0x80. [Fields: PPSNumber]")
  """Requests the PPS configuration settings. The response is sent in 0xB0 0x80. [Fields: PPSNumber]"""
  eb000cmd: int = (316, "Sets the PPS configuration settings. The command is acknowleged with a 0xB0 0x80 response. [Fields: PPSNumber EnableFlag PPSTimebase PPSPolarity AutoReport Frequency Offset MaxUncThreshold]")
  """Sets the PPS configuration settings. The command is acknowleged with a 0xB0 0x80 response. [Fields: PPSNumber EnableFlag PPSTimebase PPSPolarity AutoReport Frequency Offset MaxUncThreshold]"""
  eb001cmd: int = (317, "Enables or disables the specified PPS signal. The command is acknowledged with a 0xB0 0x81 response. [Fields: PPSNumber EnableFlag]")
  """Enables or disables the specified PPS signal. The command is acknowledged with a 0xB0 0x81 response. [Fields: PPSNumber EnableFlag]"""
  ebb00req: int = (318, "Requests primary receiver configuration block. [Fields: ]")
  """Requests primary receiver configuration block. [Fields: ]"""
  ebb00cmd: int = (319, "Sets primary receiver configuration block. [Fields: OperatingDimension DGPSMode DynamicsCode SolutionMode ElevetionMask AMUMask PDOP PDOPSwitch DGPSAgeLimit FoliageMode LowPowerMode ClockHoldMode MeasurementRate PosFixRate]")
  """Sets primary receiver configuration block. [Fields: OperatingDimension DGPSMode DynamicsCode SolutionMode ElevetionMask AMUMask PDOP PDOPSwitch DGPSAgeLimit FoliageMode LowPowerMode ClockHoldMode MeasurementRate PosFixRate]"""
  ebcreq: int = (320, "Requests the configuration of a particular serial port [Fields: Port]")
  """Requests the configuration of a particular serial port [Fields: Port]"""
  ebccmd: int = (321, "Sets the configuration of a particular serial port. This includes the port settings and input and output protocols. [Fields: Port InputBaudRate OutputBaudRate DataBits Parity StopBits FlowControl InputProtocol OutputProtocol ProtocolOperation]")
  """Sets the configuration of a particular serial port. This includes the port settings and input and output protocols. [Fields: Port InputBaudRate OutputBaudRate DataBits Parity StopBits FlowControl InputProtocol OutputProtocol ProtocolOperation]"""
  ebe40cmd: int = (322, "Configuration packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Configuration packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe400000cmd: int = (323, "Requests App Version(?) configuration from the Autopilot Navigation Controller [Fields: ]")
  """Requests App Version(?) configuration from the Autopilot Navigation Controller [Fields: ]"""
  ebe400003cmd: int = (324, "Requests the App Version Config version from the Autopilot Navigation Controller [Fields: ]")
  """Requests the App Version Config version from the Autopilot Navigation Controller [Fields: ]"""
  ebe400100cmd: int = (325, "Requests options configuration from the Autopilot Navigation Controller [Fields: ]")
  """Requests options configuration from the Autopilot Navigation Controller [Fields: ]"""
  ebe400103cmd: int = (326, "Requests Options(?) config version from the Autopilot Navigation Controller [Fields: ]")
  """Requests Options(?) config version from the Autopilot Navigation Controller [Fields: ]"""
  ebe401400cmd: int = (327, "Configuration packet command to get TAP parameter on the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]")
  """Configuration packet command to get TAP parameter on the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]"""
  ebe401401cmd: int = (328, "Configuration packet command to set TAP parameter on the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]")
  """Configuration packet command to set TAP parameter on the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]"""
  ebe41cmd: int = (329, "File Transfer packet command to the Autopilot Navigation Controller [Fields: FileId CmdId PacketNumber, PacketDataLength, PacketData]")
  """File Transfer packet command to the Autopilot Navigation Controller [Fields: FileId CmdId PacketNumber, PacketDataLength, PacketData]"""
  ebe42cmd: int = (330, "Remote Monitor Engineering Data packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Engineering Data packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe4200cmd: int = (331, "Gets status information for navigation [Fields: ]")
  """Gets status information for navigation [Fields: ]"""
  ebe4201cmd: int = (332, "Gets status information for navigation [Fields: ]")
  """Gets status information for navigation [Fields: ]"""
  ebe4202cmd: int = (333, "Gets status information for GNSS [Fields: ]")
  """Gets status information for GNSS [Fields: ]"""
  ebe4301cmd: int = (334, "Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets autosteering to enabled/disabled [Fields: EngageCommand]")
  """Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets autosteering to enabled/disabled [Fields: EngageCommand]"""
  ebe4303cmd: int = (335, "Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets logging to enabled/disabled [Fields: PaddingForBackwardsCompatibility1 PaddingForBackwardsCompatibility2 LoggingCommand]")
  """Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets logging to enabled/disabled [Fields: PaddingForBackwardsCompatibility1 PaddingForBackwardsCompatibility2 LoggingCommand]"""
  ebe4306cmd: int = (336, "Remote Monitor Control packet command to the Autopilot Navigation Controller to control Steering/Speed [Fields: CommandID Command Value]")
  """Remote Monitor Control packet command to the Autopilot Navigation Controller to control Steering/Speed [Fields: CommandID Command Value]"""
  ebe43060000cmd: int = (337, "Steers left in the simulation (angle is defined in receiver firmware) [Fields: ]")
  """Steers left in the simulation (angle is defined in receiver firmware) [Fields: ]"""
  ebe43060001cmd: int = (338, "Steers right in the simulation (angle is defined in receiver firmware) [Fields: ]")
  """Steers right in the simulation (angle is defined in receiver firmware) [Fields: ]"""
  ebe43060002cmd: int = (339, "Sets the Simulation Steer Angle to a specific value [Fields: SteerAngleDegrees]")
  """Sets the Simulation Steer Angle to a specific value [Fields: SteerAngleDegrees]"""
  ebe43060100cmd: int = (340, "Increases the Simulation Speed (increment is defined in receiver firmware) [Fields: ]")
  """Increases the Simulation Speed (increment is defined in receiver firmware) [Fields: ]"""
  ebe43060101cmd: int = (341, "Decreases the Simulation Speed (increment is defined in receiver firmware) [Fields: ]")
  """Decreases the Simulation Speed (increment is defined in receiver firmware) [Fields: ]"""
  ebe43060102cmd: int = (342, "Sets the Simulation Speed to a specific value [Fields: SpeedMetersPerSecond]")
  """Sets the Simulation Speed to a specific value [Fields: SpeedMetersPerSecond]"""
  ebe430bcmd: int = (343, " [Fields: ]")
  """ [Fields: ]"""
  ebe430dcmd: int = (344, "Enables/disables simulating a GPS outage in the simulation. [Fields: ]")
  """Enables/disables simulating a GPS outage in the simulation. [Fields: ]"""
  ebe44cmd: int = (345, "Remote Monitor General Data packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor General Data packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe45cmd: int = (346, "Remote Monitor Waypoint Data packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Waypoint Data packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe46cmd: int = (347, "Boot Monitor packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Boot Monitor packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe4600cmd: int = (348, "Used to reset the steering controller on the receiver. The AGL currently first sends the SwitchToApp command, followed by ReturnMode after a delay. [Fields: Command]")
  """Used to reset the steering controller on the receiver. The AGL currently first sends the SwitchToApp command, followed by ReturnMode after a delay. [Fields: Command]"""
  ebe47cmd: int = (349, "Debug packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Debug packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe470500cmd: int = (350, "Gets the current diagnostic error type from the Autopilot Navigation Controller [Fields: ]")
  """Gets the current diagnostic error type from the Autopilot Navigation Controller [Fields: ]"""
  ebe470501cmd: int = (351, "Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller [Fields: ]")
  """Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller [Fields: ]"""
  ebe470502cmd: int = (352, "Gets a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId]")
  """Gets a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId]"""
  ebe470503cmd: int = (353, "Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller [Fields: DiagItemId]")
  """Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller [Fields: DiagItemId]"""
  ebe470504cmd: int = (354, "Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller [Fields: ErrorComponentId]")
  """Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller [Fields: ErrorComponentId]"""
  ebe470505cmd: int = (355, "Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller [Fields: ]")
  """Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller [Fields: ]"""
  ebe470506cmd: int = (356, "Gets the description of a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId]")
  """Gets the description of a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId]"""
  ebe470507cmd: int = (357, "Acknowledge the current warning on the Autopilot Navigation Controller [Fields: ]")
  """Acknowledge the current warning on the Autopilot Navigation Controller [Fields: ]"""
  ebe470508cmd: int = (358, "Gets the maximum number of warnings from the Autopilot Navigation Controller [Fields: ]")
  """Gets the maximum number of warnings from the Autopilot Navigation Controller [Fields: ]"""
  ebe470509cmd: int = (359, "Gets the description of a warning from the Autopilot Navigation Controller [Fields: WarningId]")
  """Gets the description of a warning from the Autopilot Navigation Controller [Fields: WarningId]"""
  ebe47050acmd: int = (360, "Gets the maximum number of messages from the Autopilot Navigation Controller [Fields: ]")
  """Gets the maximum number of messages from the Autopilot Navigation Controller [Fields: ]"""
  ebe47050bcmd: int = (361, "Gets a message description from the Autopilot Navigation Controller [Fields: MessageId]")
  """Gets a message description from the Autopilot Navigation Controller [Fields: MessageId]"""
  ebe4707cmd: int = (362, "Gets ADC data from the Autopilot Navigation Controller [Fields: ]")
  """Gets ADC data from the Autopilot Navigation Controller [Fields: ]"""
  ebe470e08cmd: int = (363, "Debug packet command to the Autopilot Navigation Controller. Gets current port function [Fields: ]")
  """Debug packet command to the Autopilot Navigation Controller. Gets current port function [Fields: ]"""
  ebe470e09cmd: int = (364, "Debug packet command to the Autopilot Navigation Controller. Sets current port function [Fields: PortFunctionId]")
  """Debug packet command to the Autopilot Navigation Controller. Sets current port function [Fields: PortFunctionId]"""
  ebe471400cmd: int = (365, "Gets number of internal vdb's from the Autopilot Controller [Fields: ]")
  """Gets number of internal vdb's from the Autopilot Controller [Fields: ]"""
  ebe471401cmd: int = (366, "Gets a vdb record from the Autopilot Controller [Fields: VDBIndex]")
  """Gets a vdb record from the Autopilot Controller [Fields: VDBIndex]"""
  ebe471402cmd: int = (367, "Sets the vdb record on the Autopilot Controller [Fields: VDBIndex]")
  """Sets the vdb record on the Autopilot Controller [Fields: VDBIndex]"""
  ebe471ecmd: int = (368, "Gets current IMU data from the Autopilot Controller [Fields: ]")
  """Gets current IMU data from the Autopilot Controller [Fields: ]"""
  ebe4acmd: int = (369, "Calibration packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Calibration packet command to the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebe4a0b00cmd: int = (370, "Steering angle sensor calibration information request [Fields: ]")
  """Steering angle sensor calibration information request [Fields: ]"""
  ebe4a0b01cmd: int = (371, " [Fields: Command]")
  """ [Fields: Command]"""
  ebe4a0ccmd: int = (372, "PGain Commands which do not take any additional request data [Fields: Command]")
  """PGain Commands which do not take any additional request data [Fields: Command]"""
  ebe4a0c00cmd: int = (373, "Steering (P-gain) Calibration Information request [Fields: ]")
  """Steering (P-gain) Calibration Information request [Fields: ]"""
  ebe4a0c08cmd: int = (374, "Steering (P-gain) Calibration Information request (part2) [Fields: ]")
  """Steering (P-gain) Calibration Information request (part2) [Fields: ]"""
  ebe4a0c09cmd: int = (375, " [Fields: PGain]")
  """ [Fields: PGain]"""
  ebe4bcmd: int = (376, "Autotester command to the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]")
  """Autotester command to the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]"""
  ebe4c00000004cmd: int = (377, "External Device packet command to read the manual override info from the Autopilot Navigation Controller [Fields: ]")
  """External Device packet command to read the manual override info from the Autopilot Navigation Controller [Fields: ]"""
  ebe4c00000104cmd: int = (378, "External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller [Fields: ]")
  """External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller [Fields: ]"""
  ebe4c00000204cmd: int = (379, "External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller [Fields: ]")
  """External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller [Fields: ]"""
  ebe4c00000704cmd: int = (380, "External Device packet command to read the Gear lever info from the Autopilot Navigation Controller [Fields: ]")
  """External Device packet command to read the Gear lever info from the Autopilot Navigation Controller [Fields: ]"""
  ebe4c0100cmd: int = (381, "Autopilot Field Computer Heartbeat packet command to the Autosteer Controller [Fields: FieldComputerVersion FieldComputerFieldState]")
  """Autopilot Field Computer Heartbeat packet command to the Autosteer Controller [Fields: FieldComputerVersion FieldComputerFieldState]"""
  ebe4c0106cmd: int = (382, "External Device packet command to turn logging on on the Autopilot Navigation Controller [Fields: ]")
  """External Device packet command to turn logging on on the Autopilot Navigation Controller [Fields: ]"""
  ebe4c0107cmd: int = (383, "External Device packet command to turn logging off on the Autopilot Navigation Controller [Fields: ]")
  """External Device packet command to turn logging off on the Autopilot Navigation Controller [Fields: ]"""
  ebe4c0108req: int = (384, "External Device request to get implement width [Fields: ]")
  """External Device request to get implement width [Fields: ]"""
  ebe4c0108cmd: int = (385, "External Device packet command to set Implement Width [Fields: ImplementWidthLength, ImplementWidth]")
  """External Device packet command to set Implement Width [Fields: ImplementWidthLength, ImplementWidth]"""
  ebe4c010acmd: int = (386, "External Device packet command to set close any open field [Fields: ]")
  """External Device packet command to set close any open field [Fields: ]"""
  ebe4c010breq: int = (387, "External Device packet request to get Control State [Fields: ]")
  """External Device packet request to get Control State [Fields: ]"""
  ebe4c010bcmd: int = (388, "External Device packet Control State [Fields: ControlState, MiscDataLength, MiscData]")
  """External Device packet Control State [Fields: ControlState, MiscDataLength, MiscData]"""
  ebe4c010dreq: int = (389, "External Device packet request to get Aggressiveness [Fields: ]")
  """External Device packet request to get Aggressiveness [Fields: ]"""
  ebe4c010dcmd: int = (390, "External Device packet command to set Aggressiveness [Fields: Aggressiveness]")
  """External Device packet command to set Aggressiveness [Fields: Aggressiveness]"""
  ebe4c010ereq: int = (391, "External Device packet request to get Task Delay [Fields: ]")
  """External Device packet request to get Task Delay [Fields: ]"""
  ebe4c010ecmd: int = (392, "External Device packet command to set Task Delay [Fields: TaskDelay]")
  """External Device packet command to set Task Delay [Fields: TaskDelay]"""
  ebe4c010freq: int = (393, "External Device packet request to get Fix Quality [Fields: ]")
  """External Device packet request to get Fix Quality [Fields: ]"""
  ebe4c010fcmd: int = (394, "External Device packet command to set Fix Quality [Fields: FixQuality]")
  """External Device packet command to set Fix Quality [Fields: FixQuality]"""
  ebe4c011000req: int = (395, "External Device packet command to Get the Nudge [Fields: ]")
  """External Device packet command to Get the Nudge [Fields: ]"""
  ebe4c011001cmd: int = (396, "External Device packet command to set the Nudge [Fields: Nudge]")
  """External Device packet command to set the Nudge [Fields: Nudge]"""
  ebe4c011002cmd: int = (397, "External Device packet command Apply Nudge [Fields: Direction]")
  """External Device packet command Apply Nudge [Fields: Direction]"""
  ebe4c011003req: int = (398, "External Device packet request Get Nudge Total [Fields: ]")
  """External Device packet request Get Nudge Total [Fields: ]"""
  ebe4c011004cmd: int = (399, "External Device packet response to Set Total Nudge [Fields: Total]")
  """External Device packet response to Set Total Nudge [Fields: Total]"""
  ebe4c0111cmd: int = (400, "External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller [Fields: Mask Rate]")
  """External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller [Fields: Mask Rate]"""
  ebe4c0114cmd: int = (401, "External Device packet command to set the GGA Adjust [Fields: GgaAdjust]")
  """External Device packet command to set the GGA Adjust [Fields: GgaAdjust]"""
  ebe4c011706cmd: int = (402, "Field computer pattern definition for pivot ACB patterns [Fields: Curvature PointA PointB CenterPoint Radius]")
  """Field computer pattern definition for pivot ACB patterns [Fields: Curvature PointA PointB CenterPoint Radius]"""
  ebe4c011710cmd: int = (403, "Swath by swath pattern definition command (PTRN_SWATH_BY_SWATH) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB]")
  """Swath by swath pattern definition command (PTRN_SWATH_BY_SWATH) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB]"""
  ebe4c011711cmd: int = (404, "Swath section pattern definition command (PTRN_SWATH_SECTION) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex Points]")
  """Swath section pattern definition command (PTRN_SWATH_SECTION) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex Points]"""
  ebe4c011713cmd: int = (405, "Swath by swath fragment pattern definition command (PTRN_SWATH_BY_SWATH_FRAGMENT) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB]")
  """Swath by swath fragment pattern definition command (PTRN_SWATH_BY_SWATH_FRAGMENT) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB]"""
  ebe4c011720cmd: int = (406, "Swath by swath FFA pattern definition command (PTRN_SWATH_BY_SWATH_FFA) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB]")
  """Swath by swath FFA pattern definition command (PTRN_SWATH_BY_SWATH_FFA) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin PointA PointB]"""
  ebe4c011721cmd: int = (407, "Swath section FFA pattern definition command (PTRN_SWATH_SECTION_FFA) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex Points]")
  """Swath section FFA pattern definition command (PTRN_SWATH_SECTION_FFA) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex Points]"""
  ebe4c0119cmd: int = (408, " This packet should be sent from the Field Computer to the Controller when communication is established. It allows the controller to identify what hardware it is connected to and allows the Field Computer (from the Controller's response) to know what sort of Controller the Field Computer is connected to [Fields: ManufacturerId DisplayId ProductId FirmwareVersion]")
  """ This packet should be sent from the Field Computer to the Controller when communication is established. It allows the controller to identify what hardware it is connected to and allows the Field Computer (from the Controller's response) to know what sort of Controller the Field Computer is connected to [Fields: ManufacturerId DisplayId ProductId FirmwareVersion]"""
  ebe4c011acmd: int = (409, "Extended Field Computer Heartbeat packet command to the Autosteer Controller [Fields: FieldComputerFieldState AutosteerAllowed SequenceNumber]")
  """Extended Field Computer Heartbeat packet command to the Autosteer Controller [Fields: FieldComputerFieldState AutosteerAllowed SequenceNumber]"""
  ebe4c2000req: int = (410, "External Device packet to request the enable state of the guidance status message [Fields: ]")
  """External Device packet to request the enable state of the guidance status message [Fields: ]"""
  ebe4c2000cmd: int = (411, "External Device packet command to set the automatic update of the guidance status message [Fields: Enabled]")
  """External Device packet command to set the automatic update of the guidance status message [Fields: Enabled]"""
  ebe4c2001req: int = (412, "External Device packet to request the guidance status message [Fields: ]")
  """External Device packet to request the guidance status message [Fields: ]"""
  ebe4c2300cmd: int = (413, "New Path command starts a new guidance path. Set points to be interpreted as Polyline or Clothoid points [Fields: type]")
  """New Path command starts a new guidance path. Set points to be interpreted as Polyline or Clothoid points [Fields: type]"""
  ebe4c2301cmd: int = (414, "Extend the guidance path by 1 point. Each point has a position XYZ and optional parameters for Clothoids [Fields: Sequence_Number X Y Z Heading Speed]")
  """Extend the guidance path by 1 point. Each point has a position XYZ and optional parameters for Clothoids [Fields: Sequence_Number X Y Z Heading Speed]"""
  ebe4c2302req: int = (415, "Query the usage of the clothoid guidance path for steering the vehicle. [Fields: ]")
  """Query the usage of the clothoid guidance path for steering the vehicle. [Fields: ]"""
  ebe4c2302cmd: int = (416, "Send to configure usage of the clothoid guidance path for steering the vehicle. [Fields: Activate]")
  """Send to configure usage of the clothoid guidance path for steering the vehicle. [Fields: Activate]"""
  ebe4c8000cmd: int = (417, "Informs the NAV that a Nextswath related button was pressed on the display [Fields: Reserved FfaButton]")
  """Informs the NAV that a Nextswath related button was pressed on the display [Fields: Reserved FfaButton]"""
  ebe4c8001cmd: int = (418, " [Fields: InnerHeadlandExists OuterHeadlandExists BoundaryCount NumberOfExclusionZones]")
  """ [Fields: InnerHeadlandExists OuterHeadlandExists BoundaryCount NumberOfExclusionZones]"""
  ebe4dcmd: int = (419, "GPS simulation command to the Autopilot Navigation Controller. Used for NAV to NAV communication. [Fields: PacketDataLength, PacketData]")
  """GPS simulation command to the Autopilot Navigation Controller. Used for NAV to NAV communication. [Fields: PacketDataLength, PacketData]"""
  ebe4ecmd: int = (420, "Piped message command to the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]")
  """Piped message command to the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]"""
  ebe4fcmd: int = (421, "This is an alias to 0x8e 0xa1. [Fields: PacketDataLength, PacketData]")
  """This is an alias to 0x8e 0xa1. [Fields: PacketDataLength, PacketData]"""
  ebe50cmd: int = (422, "Configuration packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Configuration packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe5014cmd: int = (423, "TAP packet command to the Autosteer Controller [Fields: CommandID, PacketDataLength, PacketData]")
  """TAP packet command to the Autosteer Controller [Fields: CommandID, PacketDataLength, PacketData]"""
  ebe51cmd: int = (424, "File Transfer packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """File Transfer packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe52cmd: int = (425, "Remote Monitor Engineering Data packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Engineering Data packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe53cmd: int = (426, "Remote Monitor Control packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Control packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe530600cmd: int = (427, "Remote Monitor Control Steering packet command to the Autosteer Controller [Fields: Direction]")
  """Remote Monitor Control Steering packet command to the Autosteer Controller [Fields: Direction]"""
  ebe530601cmd: int = (428, "Remote Monitor Control Speed packet command to the Autosteer Controller [Fields: Direction]")
  """Remote Monitor Control Speed packet command to the Autosteer Controller [Fields: Direction]"""
  ebe54cmd: int = (429, "Remote Monitor General Data packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor General Data packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe55cmd: int = (430, "Remote Monitor Waypoint Data packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Waypoint Data packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe56cmd: int = (431, "Boot Monitor packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Boot Monitor packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe57cmd: int = (432, "Debug packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Debug packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe570507cmd: int = (433, "Field Computer Ack Current Warning packet command to the Autosteer Controller [Fields: ]")
  """Field Computer Ack Current Warning packet command to the Autosteer Controller [Fields: ]"""
  ebe5acmd: int = (434, "Calibration packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """Calibration packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe5ccmd: int = (435, "External Device packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]")
  """External Device packet command to the Autosteer Controller [Fields: PacketDataLength, PacketData]"""
  ebe5c0100cmd: int = (436, "Field Computer Heartbeat packet command to the Autosteer Controller [Fields: FieldComputerVersion FieldComputerFieldState]")
  """Field Computer Heartbeat packet command to the Autosteer Controller [Fields: FieldComputerVersion FieldComputerFieldState]"""
  ebe5c0106cmd: int = (437, "Field Computer Logging On packet command to the Autosteer Controller [Fields: ]")
  """Field Computer Logging On packet command to the Autosteer Controller [Fields: ]"""
  ebe5c0107cmd: int = (438, "Field Computer Logging Off packet command to the Autosteer Controller [Fields: ]")
  """Field Computer Logging Off packet command to the Autosteer Controller [Fields: ]"""
  ebe5c010acmd: int = (439, "Field Computer Close Field packet command to the Autosteer Controller [Fields: ]")
  """Field Computer Close Field packet command to the Autosteer Controller [Fields: ]"""
  ebe5c010bcmd: int = (440, "Field Computer Control State packet command to the Autosteer Controller [Fields: GuidanceType]")
  """Field Computer Control State packet command to the Autosteer Controller [Fields: GuidanceType]"""
  ebe5c011000cmd: int = (441, "Field Computer Get Nudge packet command to the Autosteer Controller [Fields: ]")
  """Field Computer Get Nudge packet command to the Autosteer Controller [Fields: ]"""
  ebe5c011001cmd: int = (442, "Field Computer Set Nudge packet command to the Autosteer Controller [Fields: NudgeIncrement]")
  """Field Computer Set Nudge packet command to the Autosteer Controller [Fields: NudgeIncrement]"""
  ebe5c011002cmd: int = (443, "Field Computer Apply Nudge packet command to the Autosteer Controller [Fields: NudgeDirection]")
  """Field Computer Apply Nudge packet command to the Autosteer Controller [Fields: NudgeDirection]"""
  ebe5c011003cmd: int = (444, "Field Computer Get Total Nudge packet command to the Autosteer Controller [Fields: ]")
  """Field Computer Get Total Nudge packet command to the Autosteer Controller [Fields: ]"""
  ebe5c011004cmd: int = (445, "Field Computer Set Total Nudge packet command to the Autosteer Controller [Fields: TotalNudge]")
  """Field Computer Set Total Nudge packet command to the Autosteer Controller [Fields: TotalNudge]"""
  ebe5c0111cmd: int = (446, "Field Computer NMEA configuration packet command to the Autosteer Controller [Fields: NMEAMask OutputInterval]")
  """Field Computer NMEA configuration packet command to the Autosteer Controller [Fields: NMEAMask OutputInterval]"""
  ebe5c0114cmd: int = (447, "Field Computer Adjust GGA position command to the Autosteer Controller [Fields: AdjustPosition]")
  """Field Computer Adjust GGA position command to the Autosteer Controller [Fields: AdjustPosition]"""
  ebe5c011700cmd: int = (448, "Field Computer Pattern Definition Parallel A/B packet command to the Autosteer Controller [Fields: SwathNumber Direction NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude]")
  """Field Computer Pattern Definition Parallel A/B packet command to the Autosteer Controller [Fields: SwathNumber Direction NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude]"""
  ebe5c011706cmd: int = (449, "Field Computer Pattern Definition Pivot packet command to the Autosteer Controller [Fields: SwathNumber PivotDirection NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude CenterPointLatitude CenterPointLongitude CenterPointAltitude PivotRadius Unused1 Unused2]")
  """Field Computer Pattern Definition Pivot packet command to the Autosteer Controller [Fields: SwathNumber PivotDirection NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude CenterPointLatitude CenterPointLongitude CenterPointAltitude PivotRadius Unused1 Unused2]"""
  ebe5c011710cmd: int = (450, "Field Computer Pattern Definition Swath By Swath packet command to the Autosteer Controller [Fields: SwathNumber SwathType NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude]")
  """Field Computer Pattern Definition Swath By Swath packet command to the Autosteer Controller [Fields: SwathNumber SwathType NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude]"""
  ebe5c011711cmd: int = (451, "Field Computer Pattern Definition Swath Section packet command to the Autosteer Controller [Fields: SwathNumber NumSwathPoints NumSectionPoints SectionIndex Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7, PacketDataLength, PacketData]")
  """Field Computer Pattern Definition Swath Section packet command to the Autosteer Controller [Fields: SwathNumber NumSwathPoints NumSectionPoints SectionIndex Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7, PacketDataLength, PacketData]"""
  ebe5c011713cmd: int = (452, "Field Computer Pattern Definition Swath By Swath Fragment packet command to the Autosteer Controller [Fields: SwathNumber SwathType NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude]")
  """Field Computer Pattern Definition Swath By Swath Fragment packet command to the Autosteer Controller [Fields: SwathNumber SwathType NumberOfPoints Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 PointALatitude PointALongitude PointAAltitude PointBLatitude PointBLongitude PointBAltitude]"""
  ebe5c0119cmd: int = (453, "Field Computer Information packet command to the Autosteer Controller [Fields: ManufacturerID ProductID1 ProductID2 ProductVersion Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8]")
  """Field Computer Information packet command to the Autosteer Controller [Fields: ManufacturerID ProductID1 ProductID2 ProductVersion Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8]"""
  ebe60cmd: int = (454, "Configuration packet command to the INS feature [Fields: PacketDataLength, PacketData]")
  """Configuration packet command to the INS feature [Fields: PacketDataLength, PacketData]"""
  ebe6014cmd: int = (455, "TAP packet command to the Inertial Nav feature [Fields: CommandID, PacketDataLength, PacketData]")
  """TAP packet command to the Inertial Nav feature [Fields: CommandID, PacketDataLength, PacketData]"""
  ebe630600cmd: int = (456, "Remote Monitor Control Steering packet command to the Inertial Nav feature [Fields: Direction]")
  """Remote Monitor Control Steering packet command to the Inertial Nav feature [Fields: Direction]"""
  ebe630601cmd: int = (457, "Remote Monitor Control Speed packet command to the Inertial Nav feature [Fields: Direction]")
  """Remote Monitor Control Speed packet command to the Inertial Nav feature [Fields: Direction]"""
  ebe710000req: int = (458, "Publish Parameter Block Hardware Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Hardware Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710100req: int = (459, "Publish Parameter Block Software Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Software Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710200req: int = (460, "Publish Parameter Block OPS Config Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block OPS Config Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710201req: int = (461, "Publish Parameter Block OPS Config Information packet SET from the Display    to Autopilot Nudge and Draft [Fields: LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset]")
  """Publish Parameter Block OPS Config Information packet SET from the Display    to Autopilot Nudge and Draft [Fields: LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset]"""
  ebe710300req: int = (462, "Publish Parameter Block Platform Config Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Platform Config Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710400req: int = (463, "Publish Parameter Block Safety Config Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Safety Config Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710500req: int = (464, "Publish Parameter Block Version Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Version Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710600req: int = (465, "Publish Parameter Block Sensor Hyd Status Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Sensor Hyd Status Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710700req: int = (466, "Publish Parameter Block Raw Sensor Status Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Raw Sensor Status Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710800req: int = (467, "Publish Parameter Block Selected IMU Status Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Selected IMU Status Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710900req: int = (468, "Publish Parameter Block CS Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block CS Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710a00req: int = (469, "Publish Parameter Block Group1 Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Group1 Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710b00req: int = (470, "Publish Parameter Block Group2 Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Group2 Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710c00req: int = (471, "Publish Parameter Block Group3 Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Group3 Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710d00req: int = (472, "Publish Parameter Block GPS Guidance Status Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block GPS Guidance Status Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710e00req: int = (473, "Publish Parameter Block GPS Guidance Diag Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block GPS Guidance Diag Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe710f00req: int = (474, "Publish Parameter Block Group4 Information packet request from the Autopilot Navigation Controller [Fields: ]")
  """Publish Parameter Block Group4 Information packet request from the Autopilot Navigation Controller [Fields: ]"""
  ebe8000cmd: int = (475, "FFA command to Autopilot Navigation Controller. [Fields: Version Button]")
  """FFA command to Autopilot Navigation Controller. [Fields: Version Button]"""
  ec500req: int = (476, "Requests satellite constellation report from receiver. One or more 0xd5 0x00 packets are sent in response. [Fields: AntennaId]")
  """Requests satellite constellation report from receiver. One or more 0xd5 0x00 packets are sent in response. [Fields: AntennaId]"""
  ec501cmd: int = (477, "Set which satellite systems are enabled/disabled [Fields: SatelliteSystemControlFlag]")
  """Set which satellite systems are enabled/disabled [Fields: SatelliteSystemControlFlag]"""
  ec502req: int = (478, "Request report which satellite system is enabled/disabled [Fields: ]")
  """Request report which satellite system is enabled/disabled [Fields: ]"""
  ec60000cmd: int = (479, "TBIP authenticated command to set the allowed GeoFencing Regions. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse RegionProtectMask, Digest]")
  """TBIP authenticated command to set the allowed GeoFencing Regions. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse RegionProtectMask, Digest]"""
  ec60100cmd: int = (480, "TBIP authenticated command to set list of authorized SecureRTK bases. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse, AuthorizedBaseArray, Digest]")
  """TBIP authenticated command to set list of authorized SecureRTK bases. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse, AuthorizedBaseArray, Digest]"""
  ec60200cmd: int = (481, "TBIP authenticated command to authorize the output of GPS fix engines (per antenna) by accuracy level. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse, AuthorizedFixEngineArray, Digest]")
  """TBIP authenticated command to authorize the output of GPS fix engines (per antenna) by accuracy level. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse, AuthorizedFixEngineArray, Digest]"""
  ec60400cmd: int = (482, "TBIP authenticated command to allow RTX datum selection. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse AuthorizedRTXAdvDatum, Digest]")
  """TBIP authenticated command to allow RTX datum selection. [Fields: KeyIndex DeviceType, SerialNumber, ChallengeResponse AuthorizedRTXAdvDatum, Digest]"""
  ec700cmd: int = (483, "Lock or Unlock all stinger channels. The action is persistent unless a command forces the existing state to change. This packet is for diagnostic purposes only and may change without notice. Acknowledge Packet: 0xD7 0x00 [Fields: ChannelInformation LockChannel]")
  """Lock or Unlock all stinger channels. The action is persistent unless a command forces the existing state to change. This packet is for diagnostic purposes only and may change without notice. Acknowledge Packet: 0xD7 0x00 [Fields: ChannelInformation LockChannel]"""
  ec701req: int = (484, "Request setting of Band and Filter switches for a signal. [Fields: Band_Select]")
  """Request setting of Band and Filter switches for a signal. [Fields: Band_Select]"""
  ec701cmd: int = (485, "Set Band and Filter switches for a signal.  0xd7 0x01 is the acknowledge packet. [Fields: Band_Select Filter_Select]")
  """Set Band and Filter switches for a signal.  0xd7 0x01 is the acknowledge packet. [Fields: Band_Select Filter_Select]"""
  kInvalidClientPacket: int = (-1, "Invalid packet [Fields:]")
  """Invalid packet [Fields:]"""

kNumClientPackets = len(EClientPackets) # Number of Client packets

# Client-side TSIP packets structure.
# union UClientPackets


# Server-side TSIP packet enumeration.
class EServerPackets(Enum):
  def __new__(cls, value, doc: str):
    obj = object.__new__(cls)
    obj._value_ = value
    obj.__doc__ = doc
    return obj

  e00rsp: int = (0, "This is used so we can get to the raw data [Fields: PacketDataLength, PacketData]")
  """This is used so we can get to the raw data [Fields: PacketDataLength, PacketData]"""
  e13rsp: int = (1, "Packet 0x13 is sent to notify the calling software when the receiver cannot parse the data sent in a command packet. The contents of the problem packet are included in the report. [Fields: PacketId, PacketDataLength, PacketData]")
  """Packet 0x13 is sent to notify the calling software when the receiver cannot parse the data sent in a command packet. The contents of the problem packet are included in the report. [Fields: PacketId, PacketDataLength, PacketData]"""
  e1a01rsp: int = (2, "Wraps NMEA messages for output in a TSIP stream. Command Packet 0x7A 0x07 configures the output of the NMEA wrapped data on a particular port. [Fields: NumBytes NMEAData]")
  """Wraps NMEA messages for output in a TSIP stream. Command Packet 0x7A 0x07 configures the output of the NMEA wrapped data on a particular port. [Fields: NumBytes NMEAData]"""
  e1a0200rsp: int = (3, "Indicates current settings for forwarding DCOL packets to connected port [Fields: NumTypes DCOLTypes]")
  """Indicates current settings for forwarding DCOL packets to connected port [Fields: NumTypes DCOLTypes]"""
  e1a0201rsp: int = (4, "TSIP wrapped DCOL message response from device. [Fields: NumBytes DCOLMessage]")
  """TSIP wrapped DCOL message response from device. [Fields: NumBytes DCOLMessage]"""
  e1a0300rsp: int = (5, "TSIP wrapped CAN message [Fields: CanPort NumIDs CanIds]")
  """TSIP wrapped CAN message [Fields: CanPort NumIDs CanIds]"""
  e1a0301rsp: int = (6, "TSIP wrapped CAN message forwarded from device [Fields: CanId CanMsgLength CanMsg]")
  """TSIP wrapped CAN message forwarded from device [Fields: CanId CanMsgLength CanMsg]"""
  e40rsp: int = (7, "reports the almanac data for a single satellite [Fields: SatNumber T_zc Week Eccentricity T_oa i_o Omega_dot sqrt_A Omega_o Omega m_o]")
  """reports the almanac data for a single satellite [Fields: SatNumber T_zc Week Eccentricity T_oa i_o Omega_dot sqrt_A Omega_o Omega m_o]"""
  e41rsp: int = (8, "Reports the current GPS time of week and the week number. [Fields: Time Week Offset]")
  """Reports the current GPS time of week and the week number. [Fields: Time Week Offset]"""
  e42rsp: int = (9, "Reports the current GPS position fix in XYZ ECEF coordinate components. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm. [Fields: X Y Z TimeOfFix]")
  """Reports the current GPS position fix in XYZ ECEF coordinate components. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm. [Fields: X Y Z TimeOfFix]"""
  e43rsp: int = (10, "Reports the current GPS velocity fix in XYZ ECEF coordinate. The I/O velocity option must be set to XYZ ECEF for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm. [Fields: X Y Z BiasRate TimeOfFix]")
  """Reports the current GPS velocity fix in XYZ ECEF coordinate. The I/O velocity option must be set to XYZ ECEF for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm. [Fields: X Y Z BiasRate TimeOfFix]"""
  e45rsp: int = (11, "Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F. [Fields: NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear]")
  """Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F. [Fields: NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear]"""
  e45rspv1: int = (12, "Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F. [Fields: NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear, BCDSerialNumber BCDChecksum Revision ConfigLength NumChannels RTCMInput RTCMOutput FixRate SynchMeas Miscellaneous NMEAOutput PPSOutput ProductId]")
  """Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F. [Fields: NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear, BCDSerialNumber BCDChecksum Revision ConfigLength NumChannels RTCMInput RTCMOutput FixRate SynchMeas Miscellaneous NMEAOutput PPSOutput ProductId]"""
  e46rsp: int = (13, "Reports info about the satellite tracking status and operational health of the receiver. [Fields: StatusCode ErrorFlags]")
  """Reports info about the satellite tracking status and operational health of the receiver. [Fields: StatusCode ErrorFlags]"""
  e47rsp: int = (14, "Reports signal levels for all satellites currently being tracked in response to packet 0x27. [Fields: NumSats SignalLevelsInfoArray]")
  """Reports signal levels for all satellites currently being tracked in response to packet 0x27. [Fields: NumSats SignalLevelsInfoArray]"""
  e48rsp: int = (15, "GPS system message [Fields: LineContents]")
  """GPS system message [Fields: LineContents]"""
  e4arsp: int = (16, "Provides the single precision lls fix values stored in the receiver [Fields: Altitude InverseVariance Flags]")
  """Provides the single precision lls fix values stored in the receiver [Fields: Altitude InverseVariance Flags]"""
  e4arspv1: int = (17, "Provides the single precision lls fix values stored in the receiver [Fields: LLH_0 LLH_1 LLH_2 ClockBias Time]")
  """Provides the single precision lls fix values stored in the receiver [Fields: LLH_0 LLH_1 LLH_2 ClockBias Time]"""
  e4arspv2: int = (18, "Provides the single precision lls fix values stored in the receiver [Fields: LLH_0 LLH_1 LLH_2 ClockBias Time]")
  """Provides the single precision lls fix values stored in the receiver [Fields: LLH_0 LLH_1 LLH_2 ClockBias Time]"""
  e4brsp: int = (19, "Reports receiver's machine ID and additional status info in response to packet 0x26. [Fields: MachineId StatusFlags1 StatusFlags2]")
  """Reports receiver's machine ID and additional status info in response to packet 0x26. [Fields: MachineId StatusFlags1 StatusFlags2]"""
  e4crsp: int = (20, "Provides the operating parameter values of a receiver or requests the current parameter values stored in the receiver [Fields: DynamicsCode ElevationMask SignalLevelMask PDOPMask PDOPSwitch]")
  """Provides the operating parameter values of a receiver or requests the current parameter values stored in the receiver [Fields: DynamicsCode ElevationMask SignalLevelMask PDOPMask PDOPSwitch]"""
  e4frsp: int = (21, "UTC Parameters [Fields: A_0 A_1 delta_t_LS t_ot WN_t WN_LSF DN delta_t_LSF]")
  """UTC Parameters [Fields: A_0 A_1 delta_t_LS t_ot WN_t WN_LSF DN delta_t_LSF]"""
  e53rsp: int = (22, "Analog to digital readings from receiver [Fields: Temp Unused1 Unused2 AgcVoltage BatteryVotage Unused3 Unused4 Unused5]")
  """Analog to digital readings from receiver [Fields: Temp Unused1 Unused2 AgcVoltage BatteryVotage Unused3 Unused4 Unused5]"""
  e55rsp: int = (23, "Reports current I/O options in response to Command Packet 0x35. [Fields: PosFlags VelocityFlags TimingFlags AuxFlags]")
  """Reports current I/O options in response to Command Packet 0x35. [Fields: PosFlags VelocityFlags TimingFlags AuxFlags]"""
  e58rsp: int = (24, "Report Packet 0x58 provides GPS data (almanac, ephemeris, etc.). The receiver sends this packet on request or in response to Command Packet 0x38 (acknowledging the loading of data). To get ionosphere or ephemeris, this report packet must be used [Fields: Operation DataType PRN NumBytes SVData]")
  """Report Packet 0x58 provides GPS data (almanac, ephemeris, etc.). The receiver sends this packet on request or in response to Command Packet 0x38 (acknowledging the loading of data). To get ionosphere or ephemeris, this report packet must be used [Fields: Operation DataType PRN NumBytes SVData]"""
  e5822rsp: int = (25, "Report data specific to the almanc response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes t_oa_raw SV_HEALTH e t_oa i_io omega_dot sqrt_A omega_0 omega m0 a_f0 a_f1 axis n omega_n o_dot_n t_zc weeknum wn_oa]")
  """Report data specific to the almanc response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes t_oa_raw SV_HEALTH e t_oa i_io omega_dot sqrt_A omega_0 omega m0 a_f0 a_f1 axis n omega_n o_dot_n t_zc weeknum wn_oa]"""
  e5823rsp: int = (26, "Report data specific to the almanc health response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes weekno_health SVHealth t_oa_health t_oa_current weekno_current]")
  """Report data specific to the almanc health response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes weekno_health SVHealth t_oa_health t_oa_current weekno_current]"""
  e5824rsp: int = (27, "Report data specific to the ionosphere data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes Alpha_0 Alpha_1 Alpha_2 Alpha_3 Beta_0 Beta_1 Beta_2 Beta_3]")
  """Report data specific to the ionosphere data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes Alpha_0 Alpha_1 Alpha_2 Alpha_3 Beta_0 Beta_1 Beta_2 Beta_3]"""
  e5825rsp: int = (28, "Report data specific to the UTC data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes A_0 A_1 delta_t_ls t_ot wn_t wn_lsf dn delta_t_lsf]")
  """Report data specific to the UTC data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes A_0 A_1 delta_t_ls t_ot wn_t wn_lsf dn delta_t_lsf]"""
  e5826rsp: int = (29, "Report data specific to the Ephemeris response. This data can arrive in response to command packet 0x38 OR via configuration in command packet 0x7C 0x01. For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes PRNEphemeris t_ephem wn CodeL2 L2Pdata SVacc_raw SV_health IODC T_GD t_oc a_f2 a_f1 a_f0 SVacc IODE fit_interval C_rs Delta_n M_0 C_uc e C_us sqrt_A t_oe C_ic omega_0 C_is i_0 C_rc omega omega_dot i_dot axis n r1me2 omega_n o_dot_n]")
  """Report data specific to the Ephemeris response. This data can arrive in response to command packet 0x38 OR via configuration in command packet 0x7C 0x01. For all following fields, please see their corresponding reference in ICD-GPS-2000 [Fields: PRN NumBytes PRNEphemeris t_ephem wn CodeL2 L2Pdata SVacc_raw SV_health IODC T_GD t_oc a_f2 a_f1 a_f0 SVacc IODE fit_interval C_rs Delta_n M_0 C_uc e C_us sqrt_A t_oe C_ic omega_0 C_is i_0 C_rc omega omega_dot i_dot axis n r1me2 omega_n o_dot_n]"""
  e5brsp: int = (30, "Reports ephemeris status for a specified satellite in response to Command Packet 0x3B. [Fields: PRN CollectionTime Health IODE t_oe FitIntervalFlag URA]")
  """Reports ephemeris status for a specified satellite in response to Command Packet 0x3B. [Fields: PRN CollectionTime Health IODE t_oe FitIntervalFlag URA]"""
  e5crsp: int = (31, "Reports tracking status for a specified satellite in response to Command Packet 0x3C. [Fields: PRN ChanAndSlot AcquisitionFlag EphemerisFlag SignalLevel GPSTime Elevation Azimuth OldMeasFlag IntegerMsecFlag BadDataFlag DataCollectFlag]")
  """Reports tracking status for a specified satellite in response to Command Packet 0x3C. [Fields: PRN ChanAndSlot AcquisitionFlag EphemerisFlag SignalLevel GPSTime Elevation Azimuth OldMeasFlag IntegerMsecFlag BadDataFlag DataCollectFlag]"""
  e5f01rsp: int = (32, "Diagnostic message output from the receiver [Fields: DiagMsgLength, DiagMsg]")
  """Diagnostic message output from the receiver [Fields: DiagMsgLength, DiagMsg]"""
  e5f02rsp: int = (33, "State of TSIP diagnostics output [Fields: DiagnosticsEnabled]")
  """State of TSIP diagnostics output [Fields: DiagnosticsEnabled]"""
  e5f10rsp: int = (34, "Diagnostic data output from the receiver [Fields: DiagDataLength, DiagData]")
  """Diagnostic data output from the receiver [Fields: DiagDataLength, DiagData]"""
  e5f2200rsp: int = (35, "Retrieve the mask used to output Diagnostic data from the receiver [Fields: Mask]")
  """Retrieve the mask used to output Diagnostic data from the receiver [Fields: Mask]"""
  e5f2201rsp: int = (36, "Diagnostic data output from the receiver [Fields: Type Time, MsgLength, Msg]")
  """Diagnostic data output from the receiver [Fields: Type Time, MsgLength, Msg]"""
  e6a01rsp: int = (37, "Indicates whether or not the receiver will output differential correction information. [Fields: CorrectionsUsedInFix CorrectionInfo]")
  """Indicates whether or not the receiver will output differential correction information. [Fields: CorrectionsUsedInFix CorrectionInfo]"""
  e6drsp: int = (38, "Reports the list of satelliites used for position fixes by the receiver. [Fields: FixMode PDOP HDOP VDOP TDOP SatsInView]")
  """Reports the list of satelliites used for position fixes by the receiver. [Fields: FixMode PDOP HDOP VDOP TDOP SatsInView]"""
  e6f01rsp: int = (39, "Complete measurement report for the L1 GPS frequency [Fields: ]")
  """Complete measurement report for the L1 GPS frequency [Fields: ]"""
  e6f10rsp: int = (40, "Complete measurement report for the L2 GPS frequency [Fields: ]")
  """Complete measurement report for the L2 GPS frequency [Fields: ]"""
  e6f20rsp: int = (41, "epoch header for the GNSS T01 type 27 style packet [Fields: WeekNumber ReceiveTime ClockOffset SVCount MsgCount EpochFlags1 EpochFlags2 GlonassClockOffset RAIMInfo]")
  """epoch header for the GNSS T01 type 27 style packet [Fields: WeekNumber ReceiveTime ClockOffset SVCount MsgCount EpochFlags1 EpochFlags2 GlonassClockOffset RAIMInfo]"""
  e6f21rsp: int = (42, "These are the measurement blocks for the GNSS T01 type 27 style packet. Each packet contains up to 6 SVs with each of their submeas (l1, l2, etc.) [Fields: PacketLength MeasurementNumber GpsTime NumSVs, PayloadLength, Payload]")
  """These are the measurement blocks for the GNSS T01 type 27 style packet. Each packet contains up to 6 SVs with each of their submeas (l1, l2, etc.) [Fields: PacketLength MeasurementNumber GpsTime NumSVs, PayloadLength, Payload]"""
  e70rsp: int = (43, "Reports the state of the P/V Filter, Static Filter, and/or Altitude Filter in response to Command Packet 0x70. [Fields: DynamicFilter StaticFilter AltitudeFilter FilterLevel]")
  """Reports the state of the P/V Filter, Static Filter, and/or Altitude Filter in response to Command Packet 0x70. [Fields: DynamicFilter StaticFilter AltitudeFilter FilterLevel]"""
  e78rsp: int = (44, "Reports the amount of time in seconds that RTCM pseudorange corrections can be propagated in DGPS mode before they are no longer used. [Fields: MaxPRCAge]")
  """Reports the amount of time in seconds that RTCM pseudorange corrections can be propagated in DGPS mode before they are no longer used. [Fields: MaxPRCAge]"""
  e7b07rsp: int = (45, "Reports the data reporting options for the NMEA output on the specified port. [Fields: Port Options1]")
  """Reports the data reporting options for the NMEA output on the specified port. [Fields: Port Options1]"""
  e7b08ack: int = (46, "Acknowledges command to set NMEA Extended Port Configuration Options [Fields: Result]")
  """Acknowledges command to set NMEA Extended Port Configuration Options [Fields: Result]"""
  e7b08rsp: int = (47, "Reports the data reporting options for the NMEA extended output for a specified port. [Fields: Port MessageProtocol MessageInterval OutputMask GGAOptions Precision]")
  """Reports the data reporting options for the NMEA extended output for a specified port. [Fields: Port MessageProtocol MessageInterval OutputMask GGAOptions Precision]"""
  e7b80rsp: int = (48, "Reports the NMEA message output interval and the message mask for the current port. [Fields: Interval OutputMask]")
  """Reports the NMEA message output interval and the message mask for the current port. [Fields: Interval OutputMask]"""
  e7b8600rsp: int = (49, "Reports the GGA option settings for the current port. [Fields: Options Precision]")
  """Reports the GGA option settings for the current port. [Fields: Options Precision]"""
  e7b8602rsp: int = (50, "Reports the VTG options for the current port. [Fields: Options]")
  """Reports the VTG options for the current port. [Fields: Options]"""
  e7b8603rsp: int = (51, "Reports the VTG options for the current port. [Fields: SpeedPrecision]")
  """Reports the VTG options for the current port. [Fields: SpeedPrecision]"""
  e7b8605rsp: int = (52, "Reports the VTG options for the current port. [Fields: HeadingPrecision]")
  """Reports the VTG options for the current port. [Fields: HeadingPrecision]"""
  e7b860604rsp: int = (53, "Reports the RMC options and precision for the current port. [Fields: Options PosPrecision SpeedPrecision]")
  """Reports the RMC options and precision for the current port. [Fields: Options PosPrecision SpeedPrecision]"""
  e7d00rsp: int = (54, "Reports the number of position fixes per second. [Fields: ASAPRate]")
  """Reports the number of position fixes per second. [Fields: ASAPRate]"""
  e7d01rsp: int = (55, "Reports the position fix rate I/O options bytes. [Fields: OptionFlags1 OptionFlags2]")
  """Reports the position fix rate I/O options bytes. [Fields: OptionFlags1 OptionFlags2]"""
  e7d02rsp: int = (56, "Reports the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. [Fields: Interval Offset]")
  """Reports the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. [Fields: Interval Offset]"""
  e7d09rsp: int = (57, "Reports the message interval for the specifed port and protocol. [Fields: Port MessageProtocol MessageInterval]")
  """Reports the message interval for the specifed port and protocol. [Fields: Port MessageProtocol MessageInterval]"""
  e82rsp: int = (58, "Reports the differential position fix mode of the receiver. [Fields: Mode]")
  """Reports the differential position fix mode of the receiver. [Fields: Mode]"""
  e82rspv1: int = (59, "Reports the differential position fix mode of the receiver. [Fields: Mode RTCMVersion ReferenceStationID]")
  """Reports the differential position fix mode of the receiver. [Fields: Mode RTCMVersion ReferenceStationID]"""
  e83rsp: int = (60, "Reports the current GPS position fix in XYZ ECEF coordinate components. The I/O position option must be set to XYZ ECEF and double-precision must be selected for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm. [Fields: X Y Z ClockBias TimeOfFix]")
  """Reports the current GPS position fix in XYZ ECEF coordinate components. The I/O position option must be set to XYZ ECEF and double-precision must be selected for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm. [Fields: X Y Z ClockBias TimeOfFix]"""
  e890000rsp: int = (61, "Status of SecureRTK and the 5 rover keys. [Fields: Version NumberOfKeys OverallSystemStatus, IndividualKeysStatus]")
  """Status of SecureRTK and the 5 rover keys. [Fields: Version NumberOfKeys OverallSystemStatus, IndividualKeysStatus]"""
  e890001rsp: int = (62, "Rover Key Data [Fields: KeySlot Version, KeyString, DescriptionString]")
  """Rover Key Data [Fields: KeySlot Version, KeyString, DescriptionString]"""
  e890002rsp: int = (63, "Set Rover Key Data Response [Fields: Version KeySlot KeyStatus KeyExpiryStatus KeyDayOfExpiry]")
  """Set Rover Key Data Response [Fields: Version KeySlot KeyStatus KeyExpiryStatus KeyDayOfExpiry]"""
  e890003rsp: int = (64, "Delete Rover Key Data Response [Fields: Version KeySlot Result]")
  """Delete Rover Key Data Response [Fields: Version KeySlot Result]"""
  e893308rsp: int = (65, "Provides CMR reception statistics for all the available base stations [Fields: NumStations SelStationId StationIds LinkQuality LastCMRTime]")
  """Provides CMR reception statistics for all the available base stations [Fields: NumStations SelStationId StationIds LinkQuality LastCMRTime]"""
  e8940rsp: int = (66, "Sets the RTK configuration [Fields: PropagationMode VelocityType]")
  """Sets the RTK configuration [Fields: PropagationMode VelocityType]"""
  e8941rsp: int = (67, "Provides RTK Solution Info [Fields: SolutionMode SolutionType SolutionFlags CorrAge HorzErrorEst IonoScintLevel]")
  """Provides RTK Solution Info [Fields: SolutionMode SolutionType SolutionFlags CorrAge HorzErrorEst IonoScintLevel]"""
  e8950rsp: int = (68, "Provides RTK Aux Settings [Fields: ScintillationMode BackupSource RTKBaseDatum XFillSatFrequency XFillSatBitRate RTKBaseID SatConfigSource]")
  """Provides RTK Aux Settings [Fields: ScintillationMode BackupSource RTKBaseDatum XFillSatFrequency XFillSatBitRate RTKBaseID SatConfigSource]"""
  e8951rsp: int = (69, "Provides RTK Aux Status [Fields: xFillStatus XFillTimeRemaining XFillCorrectionAge]")
  """Provides RTK Aux Status [Fields: xFillStatus XFillTimeRemaining XFillCorrectionAge]"""
  e8960rsp: int = (70, "Provides RTK Base Info [Fields: BaseId, BaseName BaseFlags DistToBase BaseVector]")
  """Provides RTK Base Info [Fields: BaseId, BaseName BaseFlags DistToBase BaseVector]"""
  e8961rsp: int = (71, "Provides CMR Info [Fields: CMRId ConnectionTime BasePosition]")
  """Provides CMR Info [Fields: CMRId ConnectionTime BasePosition]"""
  e8962rsp: int = (72, "Provides information on the overall disturbance level of the ionosphere [Fields: DisturbanceInfoSource GeofenceActive AmplitudeDisturbance PhaseDisturbance GradientLevel FeatureAllowed]")
  """Provides information on the overall disturbance level of the ionosphere [Fields: DisturbanceInfoSource GeofenceActive AmplitudeDisturbance PhaseDisturbance GradientLevel FeatureAllowed]"""
  e897000rsp: int = (73, "Provides status of managed RTK radio (if any) [Fields: ConnectionStatus Location Type]")
  """Provides status of managed RTK radio (if any) [Fields: ConnectionStatus Location Type]"""
  e897001rsp: int = (74, "Provides identity of managed RTK radio (if any) [Fields: Product, Version, Date, SerialNumber]")
  """Provides identity of managed RTK radio (if any) [Fields: Product, Version, Date, SerialNumber]"""
  e897002rsp: int = (75, "Provides capabilities of managed RTK radio (if any) [Fields: CapabilityFlags NumModes SupportedModes NumSingleFreqHops NumCountries SupportedCountries]")
  """Provides capabilities of managed RTK radio (if any) [Fields: CapabilityFlags NumModes SupportedModes NumSingleFreqHops NumCountries SupportedCountries]"""
  e897003rsp: int = (76, "Provides country info for managed RTK radio (if any) [Fields: Type Code Flags]")
  """Provides country info for managed RTK radio (if any) [Fields: Type Code Flags]"""
  e897004rsp: int = (77, "Provides config specific to 900MHz RTK radio (if any) [Fields: NetworkId]")
  """Provides config specific to 900MHz RTK radio (if any) [Fields: NetworkId]"""
  e897005rsp: int = (78, "Provides config specific to 450MHz RTK radio (if any) [Fields: ChannelId NumChannels ChannelArray Mode Banding]")
  """Provides config specific to 450MHz RTK radio (if any) [Fields: ChannelId NumChannels ChannelArray Mode Banding]"""
  e897006ack: int = (79, "Acknowledges command to set country code [Fields: Result]")
  """Acknowledges command to set country code [Fields: Result]"""
  e897007ack: int = (80, "Acknowledges command to set 900MHz network ID [Fields: Result]")
  """Acknowledges command to set 900MHz network ID [Fields: Result]"""
  e897008ack: int = (81, "Acknowledges command to set 450MHz channel ID [Fields: Result]")
  """Acknowledges command to set 450MHz channel ID [Fields: Result]"""
  e897009ack: int = (82, "Acknowledges command to set 450MHz channel frequency [Fields: Result]")
  """Acknowledges command to set 450MHz channel frequency [Fields: Result]"""
  e89700aack: int = (83, "Acknowledges command to set 450MHz mode [Fields: Result]")
  """Acknowledges command to set 450MHz mode [Fields: Result]"""
  e89700back: int = (84, "Acknowledges command to restart RTK radio [Fields: Result]")
  """Acknowledges command to restart RTK radio [Fields: Result]"""
  e89700cack: int = (85, "Acknowledges command to set RTK radio channel bandwidth [Fields: Result]")
  """Acknowledges command to set RTK radio channel bandwidth [Fields: Result]"""
  e89700drsp: int = (86, "Provides RTK radio channel bandwidth info [Fields: Bandwidth]")
  """Provides RTK radio channel bandwidth info [Fields: Bandwidth]"""
  e897100rsp: int = (87, "For the designated source, retrieve the X, Y, and Z offset values in Fallback RTX. Request packet is 0x69 0x71 0x0. No longer supported, do not use. Packet will always return manual source, and an invalid offset with all zeros [Fields: RTXOffsetSource OffsetValid RTXOffsetBaseId XOffsetValue YOffsetValue ZOffsetValue]")
  """For the designated source, retrieve the X, Y, and Z offset values in Fallback RTX. Request packet is 0x69 0x71 0x0. No longer supported, do not use. Packet will always return manual source, and an invalid offset with all zeros [Fields: RTXOffsetSource OffsetValid RTXOffsetBaseId XOffsetValue YOffsetValue ZOffsetValue]"""
  e897100ack: int = (88, "Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Result will always be failure. [Fields: Result]")
  """Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Result will always be failure. [Fields: Result]"""
  e897101rsp: int = (89, "Reports Fallback RTX mode. Request packet is 0x69 0x71 0x02. No longer supported, do not use. It will always return UnknownMode and manual status. [Fields: FallbackMode RTXOffsetSource ActivateFallbackStatus]")
  """Reports Fallback RTX mode. Request packet is 0x69 0x71 0x02. No longer supported, do not use. It will always return UnknownMode and manual status. [Fields: FallbackMode RTXOffsetSource ActivateFallbackStatus]"""
  e897101ack: int = (90, "Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Will always return failure. [Fields: Result]")
  """Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Will always return failure. [Fields: Result]"""
  e897103rsp: int = (91, "Reports xFill Premium Status. Request packet is 0x69 0x71 0x03. [Fields: xFillStatus xFillTimeRemaining xFillCorrectionAge ScintillationSwitchRule ActivateHour ActivateMinute DeactivateHour DeactivateMinute xFillPremiumStatus IsForceActivated IsUserActivated IsSubscrValid IsBaseStnPosRecv AreOffsetsAvailable IsConverged HorizErrorEstimate xFillPremiumProgressToReady ManualScintSwitchStatus xFillCorrectionAgeNotActive]")
  """Reports xFill Premium Status. Request packet is 0x69 0x71 0x03. [Fields: xFillStatus xFillTimeRemaining xFillCorrectionAge ScintillationSwitchRule ActivateHour ActivateMinute DeactivateHour DeactivateMinute xFillPremiumStatus IsForceActivated IsUserActivated IsSubscrValid IsBaseStnPosRecv AreOffsetsAvailable IsConverged HorizErrorEstimate xFillPremiumProgressToReady ManualScintSwitchStatus xFillCorrectionAgeNotActive]"""
  e897103ack: int = (92, "Acknowledges command to set xFill Premium Configuration. Ack is sent in response to 0x69 0x71 0x03 [Fields: Result]")
  """Acknowledges command to set xFill Premium Configuration. Ack is sent in response to 0x69 0x71 0x03 [Fields: Result]"""
  e8b00rsp: int = (93, "Indicates current state of automatic position sigma reporting [Fields: OutputsEnabled]")
  """Indicates current state of automatic position sigma reporting [Fields: OutputsEnabled]"""
  e8b02rsp: int = (94, "Single position sigma (error) information report [Fields: TimeOfFix DataValid RMS SigmaEast SigmaNorth CovEN SigmaUp AxesValid SemiMajorAxis SemiMinorAxis Orientation UnitVariance NumEpochs DOF]")
  """Single position sigma (error) information report [Fields: TimeOfFix DataValid RMS SigmaEast SigmaNorth CovEN SigmaUp AxesValid SemiMajorAxis SemiMinorAxis Orientation UnitVariance NumEpochs DOF]"""
  e8frsp: int = (95, "Generic acknowledgement of packet receipt. [Fields: ]")
  """Generic acknowledgement of packet receipt. [Fields: ]"""
  e8f77rsp: int = (96, "Sample data for the fft report [Fields: PageId, SampleLength, Sample]")
  """Sample data for the fft report [Fields: PageId, SampleLength, Sample]"""
  e8f770rsp: int = (97, "Report Packet 0x8F 0x77 is generated after Command Packet 0x8E 0x75 is acknowledged with Report Packet 0x8F 0x75. The receiver performs a 1024-point Fast Fourier Transform (FFT) by the number of times specified by the Number of Integrations parameter in Command Packet 0x8E 0x75. Once the FFT report is completed, the receiver begins the next FFT. The FFT reports are generated and sent continuously until the FFT Stop Command (Command Packet 0x8E 0x76) is issued. Because the amount of data contained in the FFT report exceeds 123 bytes, the report is divided into multiple packets (pages). Even if all data bytes are DLEs (which would transmit 2 TSIP bytes for each data byte), the message structure does not overflow the 255 byte TSIP buffer length. [Fields: Frequency BinSize InputSquared NumIntegrations NumBins MaxLevel, Sample]")
  """Report Packet 0x8F 0x77 is generated after Command Packet 0x8E 0x75 is acknowledged with Report Packet 0x8F 0x75. The receiver performs a 1024-point Fast Fourier Transform (FFT) by the number of times specified by the Number of Integrations parameter in Command Packet 0x8E 0x75. Once the FFT report is completed, the receiver begins the next FFT. The FFT reports are generated and sent continuously until the FFT Stop Command (Command Packet 0x8E 0x76) is issued. Because the amount of data contained in the FFT report exceeds 123 bytes, the report is divided into multiple packets (pages). Even if all data bytes are DLEs (which would transmit 2 TSIP bytes for each data byte), the message structure does not overflow the 255 byte TSIP buffer length. [Fields: Frequency BinSize InputSquared NumIntegrations NumBins MaxLevel, Sample]"""
  e8f7brsp: int = (98, "The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C. [Fields: PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3]")
  """The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C. [Fields: PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3]"""
  e8f7cack: int = (99, "sent to acknowledge Command Packet 0x8E 0x7C [Fields: ]")
  """sent to acknowledge Command Packet 0x8E 0x7C [Fields: ]"""
  e8f7frsp: int = (100, "The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C. [Fields: PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3]")
  """The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C. [Fields: PortNumber, Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear ConfigBlockV3]"""
  e8f80rsp: int = (101, "This packet is used to obtain information about the current DGPS service provider. Due to operational differences among the service providers, the decoder state and access information is interpreted slightly differently for each service provider. Racal Service - At all times, the user access information accurately reflects the current access state, where &#8220;Access information available&#8221; indicates that no access information has been received yet. The initial confirmation of user access typically occurs after decoder initialization is complete. Omnistar Service - Once the initialization sequence is complete, the user access information is valid. Before initialization is completed, the access may not accurately reflect the final access state. To help determine whether the user access will become enabled when initialization is complete, the user may wish to look at the activation stop date provided by Report Packet 0x8F 0x8B. If the activation stop date is a future date, user access will become enabled when initialization is completed. [Fields: UserAccess UserIDCode FirmwareVersion DecoderState ServiceProvider ErrorsWarnings Reserved]")
  """This packet is used to obtain information about the current DGPS service provider. Due to operational differences among the service providers, the decoder state and access information is interpreted slightly differently for each service provider. Racal Service - At all times, the user access information accurately reflects the current access state, where &#8220;Access information available&#8221; indicates that no access information has been received yet. The initial confirmation of user access typically occurs after decoder initialization is complete. Omnistar Service - Once the initialization sequence is complete, the user access information is valid. Before initialization is completed, the access may not accurately reflect the final access state. To help determine whether the user access will become enabled when initialization is complete, the user may wish to look at the activation stop date provided by Report Packet 0x8F 0x8B. If the activation stop date is a future date, user access will become enabled when initialization is completed. [Fields: UserAccess UserIDCode FirmwareVersion DecoderState ServiceProvider ErrorsWarnings Reserved]"""
  e8f84ack: int = (102, "Acknowledges the start and stop of satellite FFT diagnostics. [Fields: ]")
  """Acknowledges the start and stop of satellite FFT diagnostics. [Fields: ]"""
  e8f85rsp: int = (103, "This packet is used to convey the DGPS tracking status for either beacon or satellite differential signals. Some fields have duplicate meanings depending on the Acquisition Mode (beacon or satellite). In addition, channels with Acquisition Mode 255 (Unused), should be ignored. For backwards compatibility, a minimum of two channels of data is always reported, but in a dual DSP receiver such as NH134, three channels of data may be reported. In this case, the channel block (bytes 3&#8211;32) will be repeated a third time for the third channel data. The value in byte 2 indicates how many blocks of channel data are provided in the packet with a minimum of 2 data blocks. If byte 2 is set to zero (backwards compatibility), 2 channels of data will be sent. [Fields: NumChannels ChannelDataArray]")
  """This packet is used to convey the DGPS tracking status for either beacon or satellite differential signals. Some fields have duplicate meanings depending on the Acquisition Mode (beacon or satellite). In addition, channels with Acquisition Mode 255 (Unused), should be ignored. For backwards compatibility, a minimum of two channels of data is always reported, but in a dual DSP receiver such as NH134, three channels of data may be reported. In this case, the channel block (bytes 3&#8211;32) will be repeated a third time for the third channel data. The value in byte 2 indicates how many blocks of channel data are provided in the packet with a minimum of 2 data blocks. If byte 2 is set to zero (backwards compatibility), 2 channels of data will be sent. [Fields: NumChannels ChannelDataArray]"""
  e8f89rsp: int = (104, "Indicates current DGPS source and related settings. [Fields: DGPSSrcMode BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout CorrectionOptions SatConfigSource]")
  """Indicates current DGPS source and related settings. [Fields: DGPSSrcMode BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout CorrectionOptions SatConfigSource]"""
  e8f89ack: int = (105, "Acknowledges DGPS source control command. [Fields: ]")
  """Acknowledges DGPS source control command. [Fields: ]"""
  e8f8brsp: int = (106, "Brief information about service provider activation. [Fields: ServiceProvider, ActivationCode ActivationMonth ActivationDay ActivationYear DeactivationMonth DeactivationDay DeactivationYear InfoType ElapsedTime]")
  """Brief information about service provider activation. [Fields: ServiceProvider, ActivationCode ActivationMonth ActivationDay ActivationYear DeactivationMonth DeactivationDay DeactivationYear InfoType ElapsedTime]"""
  e8f8cack: int = (107, "Acknowledges when the remote display is enabled or disabled, or when a key press message is received. [Fields: ]")
  """Acknowledges when the remote display is enabled or disabled, or when a key press message is received. [Fields: ]"""
  e8f8c01rsp: int = (108, "Reports the data currently appearing on the display in ASCII format (except for a few special characters) and the cursor position and mode. This packet can be requested for a single output using Command Packet 0x8E 0x8C 0x01 or it can be configured to be output automatically whenever the screen contents changes using Command Packet 0x8E 0x8C 0x03. [Fields: CursorX CursorY CursorMode LineNumber, LineContents Flags]")
  """Reports the data currently appearing on the display in ASCII format (except for a few special characters) and the cursor position and mode. This packet can be requested for a single output using Command Packet 0x8E 0x8C 0x01 or it can be configured to be output automatically whenever the screen contents changes using Command Packet 0x8E 0x8C 0x03. [Fields: CursorX CursorY CursorMode LineNumber, LineContents Flags]"""
  e8f8c02rsp: int = (109, "Sent by the receiver to control the state of a remote output line, i.e. an alarm. It is sent automatically if the receiver has been configured to drive output lines. For example, the PSO interface allows the user to set criteria for tripping an audible alarm. To control the output line to this alarm remotely (i.e. the output line is not directly connected to the receiver), this packet is sent. [Fields: SetHiMask SetLowMask]")
  """Sent by the receiver to control the state of a remote output line, i.e. an alarm. It is sent automatically if the receiver has been configured to drive output lines. For example, the PSO interface allows the user to set criteria for tripping an audible alarm. To control the output line to this alarm remotely (i.e. the output line is not directly connected to the receiver), this packet is sent. [Fields: SetHiMask SetLowMask]"""
  e8f8c03rsp: int = (110, "Shows the receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03. [Fields: DataLocation]")
  """Shows the receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03. [Fields: DataLocation]"""
  e8f8c04rsp: int = (111, "Shows the extended receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. This packet includes a text description of what kind of receiver it is, i.e. Ag132, Ag124, etc. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03. [Fields: DataLocation, RemoteId]")
  """Shows the extended receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. This packet includes a text description of what kind of receiver it is, i.e. Ag132, Ag124, etc. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03. [Fields: DataLocation, RemoteId]"""
  e8f8frsp: int = (112, "Report Packet 0x8F 0x8F is sent when the receiver is powered on and can be sent in response to Command Packet 0x8E 0x8F. The packet indicates the type of receiver and why the receiver restarted if an error caused the receiver to reset. [Fields: MachineID ProductID RestartCode]")
  """Report Packet 0x8F 0x8F is sent when the receiver is powered on and can be sent in response to Command Packet 0x8E 0x8F. The packet indicates the type of receiver and why the receiver restarted if an error caused the receiver to reset. [Fields: MachineID ProductID RestartCode]"""
  e8f91rsp: int = (113, "Return the guidance configuration information [Fields: Units DisplayMode Headland Pattern LookAhead SwathDirection SwathWidth AntennaOffset OutputRate SwathsToSkip]")
  """Return the guidance configuration information [Fields: Units DisplayMode Headland Pattern LookAhead SwathDirection SwathWidth AntennaOffset OutputRate SwathsToSkip]"""
  e8f91ack: int = (114, "Return Guidance Configuration Information [Fields: ]")
  """Return Guidance Configuration Information [Fields: ]"""
  e8f9306rsp: int = (115, "Debugging message output from the receiver [Fields: Length DebugMsg]")
  """Debugging message output from the receiver [Fields: Length DebugMsg]"""
  e8f931500rsp: int = (116, "Sent in response to a File Transfer Listing Request, one for each entry in the directory requested. [Fields: EntryIndex NumEntries, FilenameLength, Filename]")
  """Sent in response to a File Transfer Listing Request, one for each entry in the directory requested. [Fields: EntryIndex NumEntries, FilenameLength, Filename]"""
  e8f93150100rsp: int = (117, "Info for transfer sent in response to File Transfer Get - Open Request. [Fields: FileId TotalSize, FilenameLength, Filename]")
  """Info for transfer sent in response to File Transfer Get - Open Request. [Fields: FileId TotalSize, FilenameLength, Filename]"""
  e8f93150101rsp: int = (118, "Block of file data sent in response to File Transfer Get - Data Block Request. [Fields: FileId Offset Size, DataBlockLength, DataBlock]")
  """Block of file data sent in response to File Transfer Get - Data Block Request. [Fields: FileId Offset Size, DataBlockLength, DataBlock]"""
  e8f93150102rsp: int = (119, "Confirms that requested file has been closed, sent in response to File Transfer Get - Close Request. [Fields: FileId]")
  """Confirms that requested file has been closed, sent in response to File Transfer Get - Close Request. [Fields: FileId]"""
  e8f93150103rsp: int = (120, "Indicates error that caused request to fail. [Fields: FileId ErrorCode]")
  """Indicates error that caused request to fail. [Fields: FileId ErrorCode]"""
  e8f93150104rsp: int = (121, "Hash of the requested file in the fusion file system. [Fields: Result Algorithm HashLength Hash, FilenameLength, Filename]")
  """Hash of the requested file in the fusion file system. [Fields: Result Algorithm HashLength Hash, FilenameLength, Filename]"""
  e8f93150200rsp: int = (122, "Info for transfer sent in response to File Transfer Put - Open Request. [Fields: FileId TotalSize, FilenameLength, Filename]")
  """Info for transfer sent in response to File Transfer Put - Open Request. [Fields: FileId TotalSize, FilenameLength, Filename]"""
  e8f93150201rsp: int = (123, "Indicates successful file write in response to File Transfer Put - Data Block Request. [Fields: FileId Offset Size]")
  """Indicates successful file write in response to File Transfer Put - Data Block Request. [Fields: FileId Offset Size]"""
  e8f93150202rsp: int = (124, "Confirms that requested file has been closed, sent in response to File Transfer Put - Close Request. [Fields: FileId]")
  """Confirms that requested file has been closed, sent in response to File Transfer Put - Close Request. [Fields: FileId]"""
  e8f93150203rsp: int = (125, "Indicates error that caused request to fail. [Fields: FileId ErrorCode]")
  """Indicates error that caused request to fail. [Fields: FileId ErrorCode]"""
  e8f931503rsp: int = (126, "Indicates status of file delete, sent in response to File Transfer Delete Request. [Fields: StatusCode, FilenameLength, Filename]")
  """Indicates status of file delete, sent in response to File Transfer Delete Request. [Fields: StatusCode, FilenameLength, Filename]"""
  e8f9arsp: int = (127, "Report Packet 0x8F 0x9A contains information about the last differential correction set that was received and used by the receiver. [Fields: DataSource StationID Age PartialFlag Reserved1 Reserved2 RTKFlags]")
  """Report Packet 0x8F 0x9A contains information about the last differential correction set that was received and used by the receiver. [Fields: DataSource StationID Age PartialFlag Reserved1 Reserved2 RTKFlags]"""
  e8f9ersp: int = (128, "Reports the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be reported. [Fields: NumSources SourceInfoArray]")
  """Reports the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be reported. [Fields: NumSources SourceInfoArray]"""
  e8f9f00rsp: int = (129, "Sets the CAN bus configuration for specified channels [Fields: NumChannels ChannelCfg]")
  """Sets the CAN bus configuration for specified channels [Fields: NumChannels ChannelCfg]"""
  e8f9f00ack: int = (130, "Acknowledgement that the CAN configuration was received [Fields: ]")
  """Acknowledgement that the CAN configuration was received [Fields: ]"""
  e8f9f01rsp: int = (131, "Provides the current CAN status for the channel [Fields: NumChannels ChannelCfg]")
  """Provides the current CAN status for the channel [Fields: NumChannels ChannelCfg]"""
  e8f9f02rsp: int = (132, "Provides current J1939 message configuration for channel [Fields: Channel NumMessages MsgCfgArray]")
  """Provides current J1939 message configuration for channel [Fields: Channel NumMessages MsgCfgArray]"""
  e8f9f02ack: int = (133, "Acknowledgement that J1939 message configuration was received [Fields: ]")
  """Acknowledgement that J1939 message configuration was received [Fields: ]"""
  e8f9f03rsp: int = (134, "Provides current NMEA2K message configuration for channel [Fields: Channel NumMessages MsgCfgArray]")
  """Provides current NMEA2K message configuration for channel [Fields: Channel NumMessages MsgCfgArray]"""
  e8f9f03ack: int = (135, "Acknowledgement that NMEA2K message configuration was received [Fields: ]")
  """Acknowledgement that NMEA2K message configuration was received [Fields: ]"""
  e8f9f04rsp: int = (136, "Provides current ISO message configuration for channel [Fields: Channel NumMessages MsgCfgArray]")
  """Provides current ISO message configuration for channel [Fields: Channel NumMessages MsgCfgArray]"""
  e8f9f04ack: int = (137, "Acknowledgement that ISO message configuration was received [Fields: ]")
  """Acknowledgement that ISO message configuration was received [Fields: ]"""
  e8fa0rsp: int = (138, " [Fields: UpgradeResultFlag, Message]")
  """ [Fields: UpgradeResultFlag, Message]"""
  e8fa1rsp: int = (139, "This is an alias to 0x8f 0xa1. [Fields: PacketDataLength, PacketData]")
  """This is an alias to 0x8f 0xa1. [Fields: PacketDataLength, PacketData]"""
  e8fa2rsp: int = (140, "Reports additional information about the current generated position solution. It is sent once in response to a query packet Command Packet 0x8E 0xA2, or automatically if configured using Command Packet 0x6A 0x01. [Fields: PositionQuality PositionType StationId NumSvs SolutionFlags XFillTimeLeft]")
  """Reports additional information about the current generated position solution. It is sent once in response to a query packet Command Packet 0x8E 0xA2, or automatically if configured using Command Packet 0x6A 0x01. [Fields: PositionQuality PositionType StationId NumSvs SolutionFlags XFillTimeLeft]"""
  e8fa300rsp: int = (141, "The version of the Omnistar XP/HP engine [Fields: Version]")
  """The version of the Omnistar XP/HP engine [Fields: Version]"""
  e8fa301rsp: int = (142, "The subscription information for the Omnistar XP/HP service [Fields: StartTime ExpirationTime HourGlass SubscribedMode CurrentMode]")
  """The subscription information for the Omnistar XP/HP service [Fields: StartTime ExpirationTime HourGlass SubscribedMode CurrentMode]"""
  e8fa302rsp: int = (143, "Status information on the current state of the Omnistar XP/HP engine [Fields: EngineStatus SolutionStatus CorrectionAge EstimatedError AutoseedStatus PositionType GlobalStationId NumStations StationIds]")
  """Status information on the current state of the Omnistar XP/HP engine [Fields: EngineStatus SolutionStatus CorrectionAge EstimatedError AutoseedStatus PositionType GlobalStationId NumStations StationIds]"""
  e8fa303rsp: int = (144, "The base stations currently used by the Omnistar XP/HP engine [Fields: NumStations StationInfoArray]")
  """The base stations currently used by the Omnistar XP/HP engine [Fields: NumStations StationInfoArray]"""
  e8fa304rsp: int = (145, "Provides information about the current Auto-Seed information held by the receiver. If Auto-Seed functionality is on in the receiver, these values would be used at startup if the receiver was rebooted at this point in time. [Fields: Confidence Latitude Longitude Height LatitudeVariance LongitudeVariance HeightVariance]")
  """Provides information about the current Auto-Seed information held by the receiver. If Auto-Seed functionality is on in the receiver, these values would be used at startup if the receiver was rebooted at this point in time. [Fields: Confidence Latitude Longitude Height LatitudeVariance LongitudeVariance HeightVariance]"""
  e8fa305rsp: int = (146, "Provides infomration about the control parameters of the Omnistar XP/HP processor [Fields: ValidFields SeedOnStartup ConfidenceThreshold VelocityThreshold ConvergenceThreshold StaticConvergence SourceSelector]")
  """Provides infomration about the control parameters of the Omnistar XP/HP processor [Fields: ValidFields SeedOnStartup ConfidenceThreshold VelocityThreshold ConvergenceThreshold StaticConvergence SourceSelector]"""
  e8fa306rsp: int = (147, "Provides information about the debugging output of the XP/HP processor [Fields: Enabled Port]")
  """Provides information about the debugging output of the XP/HP processor [Fields: Enabled Port]"""
  e8fa307ack: int = (148, "Acknowledgment that the XP/HP engine was reset [Fields: ]")
  """Acknowledgment that the XP/HP engine was reset [Fields: ]"""
  e8fa405rsp: int = (149, "Reports Quadratic Bias Filter configuration in response to packet 0x8E 0xA4 0x05. [Fields: Time Depth MaxPropagationTime State]")
  """Reports Quadratic Bias Filter configuration in response to packet 0x8E 0xA4 0x05. [Fields: Time Depth MaxPropagationTime State]"""
  e8fa406rsp: int = (150, "Reports Kalman Filter configuration in response to packet 0x8E 0xA4 0x06. [Fields: MaxPropagationTime SpeedSetting State]")
  """Reports Kalman Filter configuration in response to packet 0x8E 0xA4 0x06. [Fields: MaxPropagationTime SpeedSetting State]"""
  e8fa407rsp: int = (151, "Reports the current status of Field Level Smoothing. Request Packet: 0x8e 0xa4 0x07 [Fields: EnableStatus]")
  """Reports the current status of Field Level Smoothing. Request Packet: 0x8e 0xa4 0x07 [Fields: EnableStatus]"""
  e8fa500rsp: int = (152, "Reports the current SBAS settings. This packet can contain a variable number of SBAS SV entries. The request or command packet used to trigger the report will determine the number of entries. A 0x8EA500 request will generate a report for all SVs. A 0x8EA500 command will generate a report for those SVs listed in the command. [Fields: NumSvs SBASInfoArray]")
  """Reports the current SBAS settings. This packet can contain a variable number of SBAS SV entries. The request or command packet used to trigger the report will determine the number of entries. A 0x8EA500 request will generate a report for all SVs. A 0x8EA500 command will generate a report for those SVs listed in the command. [Fields: NumSvs SBASInfoArray]"""
  e8fa501rsp: int = (153, "Reports the current SBAS+ settings. Request packet is 0x8E 0xA5 0x01 [Fields: EnableSBASPlus]")
  """Reports the current SBAS+ settings. Request packet is 0x8E 0xA5 0x01 [Fields: EnableSBASPlus]"""
  e8fa502ack: int = (154, "Acks SBAS Default Constellation Reset Command  [Fields: ]")
  """Acks SBAS Default Constellation Reset Command  [Fields: ]"""
  e8fa601ack: int = (155, "Acknowledges the Set External Output Pin state cmd. [Fields: Result]")
  """Acknowledges the Set External Output Pin state cmd. [Fields: Result]"""
  e8fa602rsp: int = (156, "Responds with the state of the external input pins. [Fields: Result NumValidExtInputPins, ExternalInputs]")
  """Responds with the state of the external input pins. [Fields: Result NumValidExtInputPins, ExternalInputs]"""
  e8fa608rsp: int = (157, "Provides the manufacturing information of the unit. [Fields: Result, SerialNumber UniqueId MfgDay MfgMonth MfgYear VersionMajor VersionMinor VersionBuild VersionType]")
  """Provides the manufacturing information of the unit. [Fields: Result, SerialNumber UniqueId MfgDay MfgMonth MfgYear VersionMajor VersionMinor VersionBuild VersionType]"""
  e8fa617rsp: int = (158, "Provides the Omnistar Id for the unit. [Fields: Result, OmnistarId]")
  """Provides the Omnistar Id for the unit. [Fields: Result, OmnistarId]"""
  e8fa622rsp: int = (159, "Provides MAC addresses (4 max) for the unit. [Fields: MacCount Mac1Type, Mac1Addr Mac2ype, Mac2Addr Mac3Type, Mac3Addr Mac4Type, Mac4Addr]")
  """Provides MAC addresses (4 max) for the unit. [Fields: MacCount Mac1Type, Mac1Addr Mac2ype, Mac2Addr Mac3Type, Mac3Addr Mac4Type, Mac4Addr]"""
  e8fa623rsp: int = (160, "Provides the alternate unique ID for the unit. [Fields: IdSize, AltUniqueIdField]")
  """Provides the alternate unique ID for the unit. [Fields: IdSize, AltUniqueIdField]"""
  e8fa624rsp: int = (161, "Provides unit's extended manufacturing information. [Fields: ModuleSN, FactoryID]")
  """Provides unit's extended manufacturing information. [Fields: ModuleSN, FactoryID]"""
  e8fa625ack: int = (162, "Acks extended manufacturing information cmd. [Fields: ]")
  """Acks extended manufacturing information cmd. [Fields: ]"""
  e8fa626rsp: int = (163, "Provides unit's product information. [Fields: PartNumber, Name, AbbrevName]")
  """Provides unit's product information. [Fields: PartNumber, Name, AbbrevName]"""
  e8fa627ack: int = (164, "Acks product information cmd. [Fields: ]")
  """Acks product information cmd. [Fields: ]"""
  e8fa628ack: int = (165, "If received,receiver is now in manufacturing test mode. [Fields: Result]")
  """If received,receiver is now in manufacturing test mode. [Fields: Result]"""
  e8fa629rsp: int = (166, "Responds with the signature at the given offset [Fields: offset, signature]")
  """Responds with the signature at the given offset [Fields: offset, signature]"""
  e8fa630rsp: int = (167, "Response containing the peak FFT frequency and SNR from the RF spectrum analyzer for GNSS bands. Intended for factory test use only. [Fields: Result RFBand FilteredPeakFrequency FilteredPeakSNR UnfilteredPeakFrequency UnfilteredPeakSNR]")
  """Response containing the peak FFT frequency and SNR from the RF spectrum analyzer for GNSS bands. Intended for factory test use only. [Fields: Result RFBand FilteredPeakFrequency FilteredPeakSNR UnfilteredPeakFrequency UnfilteredPeakSNR]"""
  e8fa631rsp: int = (168, "Response containing metadata about the condition of MSS tracking [Fields: Result MSSPeakFrequency PeakADCSignalLevel MaxMSSADCSignalLevel MinMSSADCSignalLevel MSSAGCGainLevelPercent MSSAGCGainLevelDb]")
  """Response containing metadata about the condition of MSS tracking [Fields: Result MSSPeakFrequency PeakADCSignalLevel MaxMSSADCSignalLevel MinMSSADCSignalLevel MSSAGCGainLevelPercent MSSAGCGainLevelDb]"""
  e8fa632rsp: int = (169, "Result of a register read operation to a specific polaris device [Fields: Result AntennaId PolarisI2CAddr PolarisRegAddr Value]")
  """Result of a register read operation to a specific polaris device [Fields: Result AntennaId PolarisI2CAddr PolarisRegAddr Value]"""
  e8fa632ack: int = (170, "Requests a register read operation to a specific polaris device [Fields: Result AntennaId PolarisI2CAddr PolarisRegAddr]")
  """Requests a register read operation to a specific polaris device [Fields: Result AntennaId PolarisI2CAddr PolarisRegAddr]"""
  e8fa633rsp: int = (171, "Result of a RSSI ADC value read operation to a specific polaris device [Fields: Result AntennaId RFBand RSSIADCValue]")
  """Result of a RSSI ADC value read operation to a specific polaris device [Fields: Result AntennaId RFBand RSSIADCValue]"""
  e8fa634ack: int = (172, "Acknowledges the test request to perform the Polaris full AGC test. If accepted, the receiver will start the test, and then send the 0x8f 0xa6 0x34 response when the test completes. If there is a problem starting the test, the response will be returned in the result field. [Fields: Result]")
  """Acknowledges the test request to perform the Polaris full AGC test. If accepted, the receiver will start the test, and then send the 0x8f 0xa6 0x34 response when the test completes. If there is a problem starting the test, the response will be returned in the result field. [Fields: Result]"""
  e8fa634rsp: int = (173, "Response containing the results of the Polaris Full AGC test. Intended for factory test use only. [Fields: BandsPresent BandResultArray FrequencyOffset]")
  """Response containing the results of the Polaris Full AGC test. Intended for factory test use only. [Fields: BandsPresent BandResultArray FrequencyOffset]"""
  e8fa640ack: int = (174, "Acknowledges the command to enable the PLT Mode for WiFi testing. [Fields: Result ErrorCode]")
  """Acknowledges the command to enable the PLT Mode for WiFi testing. [Fields: Result ErrorCode]"""
  e8fa641ack: int = (175, "Acknowledges the command to disable the PLT Mode for WiFi testing. [Fields: Result ErrorCode]")
  """Acknowledges the command to disable the PLT Mode for WiFi testing. [Fields: Result ErrorCode]"""
  e8fa642ack: int = (176, "Acknowledges the command to configure the device to operate in a specific WiFi band and channel. [Fields: Result ErrorCode]")
  """Acknowledges the command to configure the device to operate in a specific WiFi band and channel. [Fields: Result ErrorCode]"""
  e8fa643ack: int = (177, "Acknowledges the command to set the transmission power of the WL18xx device. [Fields: Result ErrorCode]")
  """Acknowledges the command to set the transmission power of the WL18xx device. [Fields: Result ErrorCode]"""
  e8fa644ack: int = (178, "Acknowledges the command to enable TX test using the start_tx command. [Fields: Result ErrorCode]")
  """Acknowledges the command to enable TX test using the start_tx command. [Fields: Result ErrorCode]"""
  e8fa645ack: int = (179, "Acknowledges the command to disable TX test using the stop_tx command. [Fields: Result ErrorCode]")
  """Acknowledges the command to disable TX test using the stop_tx command. [Fields: Result ErrorCode]"""
  e8fa646ack: int = (180, "Acknowledges the command to start the RX statistics. [Fields: Result ErrorCode]")
  """Acknowledges the command to start the RX statistics. [Fields: Result ErrorCode]"""
  e8fa647rsp: int = (181, "Response containing the RX statistics. [Fields: Result ErrorCode RXStatsStatus TotalPackets FCSErrors MACMismatch GoodPackets AvgRSSI_SOC AvgRSSI_ANT PER]")
  """Response containing the RX statistics. [Fields: Result ErrorCode RXStatsStatus TotalPackets FCSErrors MACMismatch GoodPackets AvgRSSI_SOC AvgRSSI_ANT PER]"""
  e8fa648ack: int = (182, "Acknowledges the command to stop the RX statistics. [Fields: Result ErrorCode]")
  """Acknowledges the command to stop the RX statistics. [Fields: Result ErrorCode]"""
  e8fa70000rsp: int = (183, "The auto-report settings for the current antenna, sent in response to the corresponding configuration command [Fields: AntennaId]")
  """The auto-report settings for the current antenna, sent in response to the corresponding configuration command [Fields: AntennaId]"""
  e8fa70001rsp: int = (184, "The position auto-report settings by engine, sent in response to the corresponding command [Fields: AntennaId NumEngs PositionEngArray]")
  """The position auto-report settings by engine, sent in response to the corresponding command [Fields: AntennaId NumEngs PositionEngArray]"""
  e8fa70002rsp: int = (185, "The position auto-report settings by type, sent in response to the corresponding command [Fields: AntennaId NumTypes PositionTypeArray]")
  """The position auto-report settings by type, sent in response to the corresponding command [Fields: AntennaId NumTypes PositionTypeArray]"""
  e8fa70003rsp: int = (186, "The position auto-report settings by flag, sent in response to the corresponding command [Fields: Enable AntennaId SetFlags ClearedFlags]")
  """The position auto-report settings by flag, sent in response to the corresponding command [Fields: Enable AntennaId SetFlags ClearedFlags]"""
  e8fa70100rsp: int = (187, "A GPS Position packet that provides a useful subset of positioning information, including an id for the antenna it came from. [Fields: GPSSecond AntennaId PositionEngine PositionType Flags Latitude Longitude Height EVelocity NVelocity UVelocity NumSatellites HDOP CorrectionAge]")
  """A GPS Position packet that provides a useful subset of positioning information, including an id for the antenna it came from. [Fields: GPSSecond AntennaId PositionEngine PositionType Flags Latitude Longitude Height EVelocity NVelocity UVelocity NumSatellites HDOP CorrectionAge]"""
  e8fa70101rsp: int = (188, "Indicates that a GPS position wasn't generated for the given time period [Fields: GPSSecond AntennaId PositionEngine Flags NumSatellites]")
  """Indicates that a GPS position wasn't generated for the given time period [Fields: GPSSecond AntennaId PositionEngine Flags NumSatellites]"""
  e8fa70102rsp: int = (189, "Provides the ENU vector between two GPS antennas [Fields: GPSSecond BaseAntennaId RoverAntennaId Magnitude Direction X Y Z]")
  """Provides the ENU vector between two GPS antennas [Fields: GPSSecond BaseAntennaId RoverAntennaId Magnitude Direction X Y Z]"""
  e8fa800rsp: int = (190, "Response to the 8FA801 packet [Fields: RSSI ConnectionStatus]")
  """Response to the 8FA801 packet [Fields: RSSI ConnectionStatus]"""
  e8fa801ack: int = (191, "Ack to NTRIP params set [Fields: Result]")
  """Ack to NTRIP params set [Fields: Result]"""
  e8fa801rsp: int = (192, "Report of the current NTRIP params. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: IPPort IPAddrLength IPAddress MountPointLength MountPoint UserNameLength UserName PasswordLength Password UseForRTX]")
  """Report of the current NTRIP params. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: IPPort IPAddrLength IPAddress MountPointLength MountPoint UserNameLength UserName PasswordLength Password UseForRTX]"""
  e8fa802ack: int = (193, "ACK for the set fo the GPRS Username [Fields: Result]")
  """ACK for the set fo the GPRS Username [Fields: Result]"""
  e8fa802rsp: int = (194, "Report of the GPRS Username. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: result StringLength UserName]")
  """Report of the GPRS Username. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: result StringLength UserName]"""
  e8fa803ack: int = (195, "ACK for the set fo the GPRS Password [Fields: Result]")
  """ACK for the set fo the GPRS Password [Fields: Result]"""
  e8fa803rsp: int = (196, "Report of the GPRS Password. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: result StringLength Password]")
  """Report of the GPRS Password. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: result StringLength Password]"""
  e8fa804ack: int = (197, "ACK for the set fo the GPRS InitString [Fields: result]")
  """ACK for the set fo the GPRS InitString [Fields: result]"""
  e8fa804rsp: int = (198, "Report of the GPRS InitString. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: result StringLength InitString]")
  """Report of the GPRS InitString. All strings are not null terminated, and the stringLength value is the number of actual characters [Fields: result StringLength InitString]"""
  e8fa805ack: int = (199, "ACK for the set fo the GPRS CPIN [Fields: Result]")
  """ACK for the set fo the GPRS CPIN [Fields: Result]"""
  e8fa806ack: int = (200, "ACK from the VRS Radio Config command [Fields: result]")
  """ACK from the VRS Radio Config command [Fields: result]"""
  e8fa806rsp: int = (201, "Report of the current radio mode [Fields: VRSEnabled AutoReportEnabled StreamType]")
  """Report of the current radio mode [Fields: VRSEnabled AutoReportEnabled StreamType]"""
  e8fa900rsp: int = (202, "Holds various firmware and hardware version information [Fields: FirmwareMajorVersion FirmwareMinorVersion FirmwareBuildNum FirmwareBuildType FirmwarePentaVersion FirmwareDay FirmwareMonth FirmwareYear FirmwareExpDay FirmwareExpMonth FirmwareExpYear HardwareRevision HardwarePlatform, AuxInfo]")
  """Holds various firmware and hardware version information [Fields: FirmwareMajorVersion FirmwareMinorVersion FirmwareBuildNum FirmwareBuildType FirmwarePentaVersion FirmwareDay FirmwareMonth FirmwareYear FirmwareExpDay FirmwareExpMonth FirmwareExpYear HardwareRevision HardwarePlatform, AuxInfo]"""
  e8fa90100ack: int = (203, "Acknowledges the upgrade command, providing information on how it proceeded. [Fields: UpgradeStatus]")
  """Acknowledges the upgrade command, providing information on how it proceeded. [Fields: UpgradeStatus]"""
  e8fa90100rsp: int = (204, "Provides the progress of the upgrade as it proceeds [Fields: UpgradeOperation Progress]")
  """Provides the progress of the upgrade as it proceeds [Fields: UpgradeOperation Progress]"""
  e8fa90101ack: int = (205, "Acknowledges the logging control, providing information on how it proceeded. [Fields: LoggingStatus]")
  """Acknowledges the logging control, providing information on how it proceeded. [Fields: LoggingStatus]"""
  e8fa90101rsp: int = (206, "Reports the state of the logging control. [Fields: Status filenameLen filename]")
  """Reports the state of the logging control. [Fields: Status filenameLen filename]"""
  e8fa90102ack: int = (207, "Acknowledges the Log dump request providing information on how the operation proceeded. [Fields: LogDumpStatus]")
  """Acknowledges the Log dump request providing information on how the operation proceeded. [Fields: LogDumpStatus]"""
  e8fa90103rsp: int = (208, "A variable length data packet (pong), that is returned in response to a receiver request (ping). This allows a type of serial communication test to occur. [Fields: PongSize Data]")
  """A variable length data packet (pong), that is returned in response to a receiver request (ping). This allows a type of serial communication test to occur. [Fields: PongSize Data]"""
  e8fa90104rsp: int = (209, "Returns the IP Address and port number for the VRS Daemon. [Fields: IP Port]")
  """Returns the IP Address and port number for the VRS Daemon. [Fields: IP Port]"""
  e8fa90105ack: int = (210, "Acknowledges the license file has been processed. [Fields: Status]")
  """Acknowledges the license file has been processed. [Fields: Status]"""
  e8fa90106rsp: int = (211, "Reports the current state of the receiver automatic reboot capability [Fields: Frequency]")
  """Reports the current state of the receiver automatic reboot capability [Fields: Frequency]"""
  e8fa90107rsp: int = (212, "Returns the IP Address and port number for the CLAAS RTK NET modem [Fields: IP Port]")
  """Returns the IP Address and port number for the CLAAS RTK NET modem [Fields: IP Port]"""
  e8fa90108rsp: int = (213, "Returns the IP Address for the TNFS Host Address. [Fields: IP]")
  """Returns the IP Address for the TNFS Host Address. [Fields: IP]"""
  e8fa90130rsp: int = (214, "Holds the upgrade/downgrade version floor and related information [Fields: FirmwareVersionStatus DowngradeMajorVersion DowngradeMinorVersion DowngradeBuildNum DowngradeBuildType DowngradeFeatureSpecific]")
  """Holds the upgrade/downgrade version floor and related information [Fields: FirmwareVersionStatus DowngradeMajorVersion DowngradeMinorVersion DowngradeBuildNum DowngradeBuildType DowngradeFeatureSpecific]"""
  e8fa90131rsp: int = (215, "Returns whether the upgrade/downgrade is allowed [Fields: Result]")
  """Returns whether the upgrade/downgrade is allowed [Fields: Result]"""
  e8fa90200rsp: int = (216, "Returns the mux settings of the digital output for a particular port. [Fields: PortId MuxType OutputValue]")
  """Returns the mux settings of the digital output for a particular port. [Fields: PortId MuxType OutputValue]"""
  e8fa90201rsp: int = (217, "Returns the settings of the digital input for a particular port. [Fields: PortId Threshold Pull]")
  """Returns the settings of the digital input for a particular port. [Fields: PortId Threshold Pull]"""
  e8fa90202rsp: int = (218, "Returns the state of the Pollux FPGA GPO [Fields: GPOSetting]")
  """Returns the state of the Pollux FPGA GPO [Fields: GPOSetting]"""
  e8fa90300rsp: int = (219, "Provides information about connected Antennas. [Fields: NumAntennas AntennaArray]")
  """Provides information about connected Antennas. [Fields: NumAntennas AntennaArray]"""
  e8fa90400rsp: int = (220, "Retrieves the Radar settings [Fields: Enable FreqSpeedRate]")
  """Retrieves the Radar settings [Fields: Enable FreqSpeedRate]"""
  e8fa905ack: int = (221, "Acknowledgement in response to TSIP Event Log Command packet: 0x8E 0xA9 0x05. [Fields: ]")
  """Acknowledgement in response to TSIP Event Log Command packet: 0x8E 0xA9 0x05. [Fields: ]"""
  e8fa90600rsp: int = (222, "ADC Readings [Fields: Normalized NumChannels ConvertedADCChannelReadings]")
  """ADC Readings [Fields: Normalized NumChannels ConvertedADCChannelReadings]"""
  e8fa90700rsp: int = (223, "Returns the mux of the Module-A digital pins [Fields: DigitalPin MuxType Output]")
  """Returns the mux of the Module-A digital pins [Fields: DigitalPin MuxType Output]"""
  e8fa90701rsp: int = (224, "Returns the PWMON Control Point Status [Fields: CtrlPoint Output]")
  """Returns the PWMON Control Point Status [Fields: CtrlPoint Output]"""
  e8fa90703rsp: int = (225, "Returns the Video Input selection [Fields: VideoInput Output]")
  """Returns the Video Input selection [Fields: VideoInput Output]"""
  e8fa90704rsp: int = (226, "Provides Module-A auto shutdown timer settings. [Fields: Delay TimeRemaining]")
  """Provides Module-A auto shutdown timer settings. [Fields: Delay TimeRemaining]"""
  e8fa90705rsp: int = (227, "Returns the Module A's network interface settings. [Fields: NetIfaceSettingLife NetIfaceMode IP NetMask Gateway Broadcast]")
  """Returns the Module A's network interface settings. [Fields: NetIfaceSettingLife NetIfaceMode IP NetMask Gateway Broadcast]"""
  e8fa90706rsp: int = (228, "Module-A hardware configuration response [Fields: HardwareConfig]")
  """Module-A hardware configuration response [Fields: HardwareConfig]"""
  e8fa90707rsp: int = (229, "The socket uart device configured for Port-D on the Module-A [Fields: TBIPDeviceType, SerialNumber UartId]")
  """The socket uart device configured for Port-D on the Module-A [Fields: TBIPDeviceType, SerialNumber UartId]"""
  e8fa90800rsp: int = (230, "Provides the current state of RTK correction rebroadcasting [Fields: Operation]")
  """Provides the current state of RTK correction rebroadcasting [Fields: Operation]"""
  e8fa909ack: int = (231, "Acknowledgement in response to TSIP Command packet: 0x8E 0xA9 0x08 0x00. [Fields: Result]")
  """Acknowledgement in response to TSIP Command packet: 0x8E 0xA9 0x08 0x00. [Fields: Result]"""
  e8fa909rsp: int = (232, "Returns the state of the Receiver LED. This is in response to TSIP Request: 0x8E 0xA9 0x08 0x00. [Fields: RcvrId LEDId LEDState]")
  """Returns the state of the Receiver LED. This is in response to TSIP Request: 0x8E 0xA9 0x08 0x00. [Fields: RcvrId LEDId LEDState]"""
  e8fa90a00rsp: int = (233, "Response with all the enabled features in the Feature Manager [Fields: NumFeatures Features]")
  """Response with all the enabled features in the Feature Manager [Fields: NumFeatures Features]"""
  e8fa90a01rsp: int = (234, "Response with the status of all installed licenses in the Feature Manager [Fields: NumLicenses Licenses]")
  """Response with the status of all installed licenses in the Feature Manager [Fields: NumLicenses Licenses]"""
  e8fa910rsp: int = (235, "Receiver Unlock Status Response [Fields: NumUnlockTypes UnlockStatusInfoArray]")
  """Receiver Unlock Status Response [Fields: NumUnlockTypes UnlockStatusInfoArray]"""
  e8fa911rsp: int = (236, "Product Information Response [Fields: PartNumber, ProductName, BriefProductName]")
  """Product Information Response [Fields: PartNumber, ProductName, BriefProductName]"""
  e8fa912rsp: int = (237, "Boot Count Information Response [Fields: BootCount]")
  """Boot Count Information Response [Fields: BootCount]"""
  e8fa913rsp: int = (238, "Geoidal Separation Information Response [Fields: GeoidalSeparation]")
  """Geoidal Separation Information Response [Fields: GeoidalSeparation]"""
  e8fa914rsp: int = (239, "Code Bias Calibration Table Information Response [Fields: CBC_Status RtxDeviceId NVTableVersion Reserved1 Reserved2 Reserved3]")
  """Code Bias Calibration Table Information Response [Fields: CBC_Status RtxDeviceId NVTableVersion Reserved1 Reserved2 Reserved3]"""
  e8fa91500rsp: int = (240, "Response to SysFileXferInitiate command. [Fields: xferType fileType resultCode fileId fileSize, md5Hash clientFileIdSize clientFileId]")
  """Response to SysFileXferInitiate command. [Fields: xferType fileType resultCode fileId fileSize, md5Hash clientFileIdSize clientFileId]"""
  e8fa91501rsp: int = (241, "Respond to SysFileXferGetBlock request [Fields: fileId offset resultCode blockSize blockData]")
  """Respond to SysFileXferGetBlock request [Fields: fileId offset resultCode blockSize blockData]"""
  e8fa91502rsp: int = (242, "Respond with results of SysFileXferPutBlock request [Fields: fileId resultCode offset blockSize]")
  """Respond with results of SysFileXferPutBlock request [Fields: fileId resultCode offset blockSize]"""
  e8fa91503rsp: int = (243, "Acknowledges close of stream associated with fileId [Fields: fileId resultCode]")
  """Acknowledges close of stream associated with fileId [Fields: fileId resultCode]"""
  e8fa91504rsp: int = (244, "Returns result of SysFileXferDelete command [Fields: fileType resultCode]")
  """Returns result of SysFileXferDelete command [Fields: fileType resultCode]"""
  e8fa91599rsp: int = (245, "Sent on errors during a file transfer operation [Fields: fileId errorCode]")
  """Sent on errors during a file transfer operation [Fields: fileId errorCode]"""
  e8fa9160000rsp: int = (246, "Indicates current mux mode of GP uart in Fusion [Fields: mode]")
  """Indicates current mux mode of GP uart in Fusion [Fields: mode]"""
  e8fa9160001rsp: int = (247, "Indicates current mux mode of Tx port uart in Fusion [Fields: mode]")
  """Indicates current mux mode of Tx port uart in Fusion [Fields: mode]"""
  e8fa9160002rsp: int = (248, "Indicates current mux mode of Radio port uart in Fusion [Fields: mode]")
  """Indicates current mux mode of Radio port uart in Fusion [Fields: mode]"""
  e8fa9160100rsp: int = (249, "Indicates current mode of the internal AP virtual uart in Fusion [Fields: mode]")
  """Indicates current mode of the internal AP virtual uart in Fusion [Fields: mode]"""
  e8fa91602rsp: int = (250, "Report Bluetooth state (enabled or disabled) [Fields: enable]")
  """Report Bluetooth state (enabled or disabled) [Fields: enable]"""
  e8fa91603rsp: int = (251, "Report the status of the Clear All Licenses command [Fields: success]")
  """Report the status of the Clear All Licenses command [Fields: success]"""
  e8fa91604rsp: int = (252, "Report the status of the Remove / Restore Manufacturing Licenses command [Fields: success]")
  """Report the status of the Remove / Restore Manufacturing Licenses command [Fields: success]"""
  e8fa91605rsp: int = (253, "Remove Licenses By Fragment response [Fields: success]")
  """Remove Licenses By Fragment response [Fields: success]"""
  e8fa91606rsp: int = (254, "Returns UDS diagnostic status [Fields: status]")
  """Returns UDS diagnostic status [Fields: status]"""
  e8fa91700rsp: int = (255, "Reports the Nav's internal IMU orientation, offsets, and calibration. [Fields: AntLevX AntLevY AntLevZ ImuAngleRoll ImuAnglePitch ImuAngleYaw ImuLevX ImuLevY ImuLevZ ImuRollOffset ImuPitchOffset]")
  """Reports the Nav's internal IMU orientation, offsets, and calibration. [Fields: AntLevX AntLevY AntLevZ ImuAngleRoll ImuAnglePitch ImuAngleYaw ImuLevX ImuLevY ImuLevZ ImuRollOffset ImuPitchOffset]"""
  e8fa91701rsp: int = (256, "Query if IMU-Corrected positions and streaming are enabled. [Fields: EnableIMUCorrection EnableIMUDetailStream]")
  """Query if IMU-Corrected positions and streaming are enabled. [Fields: EnableIMUCorrection EnableIMUDetailStream]"""
  e8fa91702rsp: int = (257, "IMU corrected position including roll, pitch, yaw. Stream of messages enabled by 0x8e 0xa9 0x17 0x00 command. [Fields: GPSSeconds PositionEngine PositionType Latitude Longitude Height LatitudeOriginal LongitudeOriginal HeightOriginal EVelocity NVelocity UVelocity Direction ImuStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites HDOP VDOP ESigma NSigma USigma CorrectionAge StationID]")
  """IMU corrected position including roll, pitch, yaw. Stream of messages enabled by 0x8e 0xa9 0x17 0x00 command. [Fields: GPSSeconds PositionEngine PositionType Latitude Longitude Height LatitudeOriginal LongitudeOriginal HeightOriginal EVelocity NVelocity UVelocity Direction ImuStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites HDOP VDOP ESigma NSigma USigma CorrectionAge StationID]"""
  e8fa91703rsp: int = (258, "Reports the current IMU Settings covered by Block 2. [Fields: ProPointEngineMode StaticBenchModeEnable StaticBenchHeading VehicleType]")
  """Reports the current IMU Settings covered by Block 2. [Fields: ProPointEngineMode StaticBenchModeEnable StaticBenchHeading VehicleType]"""
  e8fa918rsp: int = (259, "Returns the cryptochip configuration CRC value [Fields: crc status]")
  """Returns the cryptochip configuration CRC value [Fields: crc status]"""
  e8fa9a5rsp: int = (260, "New 27 character passcode upgrade response packet [Fields: Success, AckString]")
  """New 27 character passcode upgrade response packet [Fields: Success, AckString]"""
  e8faa00rsp: int = (261, "Provides type of specified antenna. [Fields: AntennaId AntennaType]")
  """Provides type of specified antenna. [Fields: AntennaId AntennaType]"""
  e8fab00rsp: int = (262, "Reports the status of the RTX subscription and shows which connections are available [Fields: DaysUntilExpirationFast DaysUntilExpirationStandard AvailableConnections DaysUntilExpirationRangePoint DaysUntilExpirationFallback DaysUntilExpirationXFillP DaysUntilExpirationViewPoint]")
  """Reports the status of the RTX subscription and shows which connections are available [Fields: DaysUntilExpirationFast DaysUntilExpirationStandard AvailableConnections DaysUntilExpirationRangePoint DaysUntilExpirationFallback DaysUntilExpirationXFillP DaysUntilExpirationViewPoint]"""
  e8fab01rsp: int = (263, "Reports Centerpoint RTX fast Network Info [Fields: Status DistToNetwork Timestamp Zone]")
  """Reports Centerpoint RTX fast Network Info [Fields: Status DistToNetwork Timestamp Zone]"""
  e8fab02ack: int = (264, "Acknowledgment that RTX std FastRestart has been cancelled [Fields: ]")
  """Acknowledgment that RTX std FastRestart has been cancelled [Fields: ]"""
  e8fab03rsp: int = (265, "Reports Centerpoint and RangePoint RTX Status Information [Fields: ConfiguredRTXSource ActiveRTXSource DeliveryMethod ConvergenceStatus HorizErrorEstimate WetDryStatus Reserved1 Reserved2 Reserved3 CorrectionAge SatTrckStatus RTXSatSNR FastCorrectionSats FastRestartEnabled FastRestartState FastRestartFailureModes FastRestartReady]")
  """Reports Centerpoint and RangePoint RTX Status Information [Fields: ConfiguredRTXSource ActiveRTXSource DeliveryMethod ConvergenceStatus HorizErrorEstimate WetDryStatus Reserved1 Reserved2 Reserved3 CorrectionAge SatTrckStatus RTXSatSNR FastCorrectionSats FastRestartEnabled FastRestartState FastRestartFailureModes FastRestartReady]"""
  e8fab04ack: int = (266, "Acknowledgment that RTX FastRestart vehicle movement status has been saved in the receiver  [Fields: Result]")
  """Acknowledgment that RTX FastRestart vehicle movement status has been saved in the receiver  [Fields: Result]"""
  e8fab05rsp: int = (267, "Response containing RTX output settings [Fields: RTXOutputDatum RTXOffset]")
  """Response containing RTX output settings [Fields: RTXOutputDatum RTXOffset]"""
  e8fab06rsp: int = (268, "Reports RTK/RTX Best Type Selection Info [Fields: Status]")
  """Reports RTK/RTX Best Type Selection Info [Fields: Status]"""
  e8fab07rsp: int = (269, "Response containing the current configuration and mode of the MSS Mode Switch [Fields: MSSControlMode MSSMode]")
  """Response containing the current configuration and mode of the MSS Mode Switch [Fields: MSSControlMode MSSMode]"""
  e8fab08rsp: int = (270, "Response containing realtime RTK/RTX Offsets [Fields: realtimeRtkRtxOffsetsStatus realtimeRtkRtxOffsetsAccuracy realtimeRtkRtxOffsetsEast realtimeRtkRtxOffsetsNorth realtimeRtkRtxOffsetsUp]")
  """Response containing realtime RTK/RTX Offsets [Fields: realtimeRtkRtxOffsetsStatus realtimeRtkRtxOffsetsAccuracy realtimeRtkRtxOffsetsEast realtimeRtkRtxOffsetsNorth realtimeRtkRtxOffsetsUp]"""
  e8fac0100rsp: int = (271, "Response with the configuration for genral parameters [Fields: APIversion enabled targetHeight sprayerSuspensionType sensingMode groundSensitivity canopySensitivity groundFilter canopyFilter chevronThresh maximumHeight minimumHeight minSafeHeightBelowTarget heightStep aggressiveness downSlewLim downGainStabilizer wingPhasingHeightThreshold useKato autoDisableTimeout]")
  """Response with the configuration for genral parameters [Fields: APIversion enabled targetHeight sprayerSuspensionType sensingMode groundSensitivity canopySensitivity groundFilter canopyFilter chevronThresh maximumHeight minimumHeight minSafeHeightBelowTarget heightStep aggressiveness downSlewLim downGainStabilizer wingPhasingHeightThreshold useKato autoDisableTimeout]"""
  e8fac0101rsp: int = (272, "Response with the configuration for sensor parameters [Fields: APIversion numberOfSensors sensorsArray]")
  """Response with the configuration for sensor parameters [Fields: APIversion numberOfSensors sensorsArray]"""
  e8fac0102rsp: int = (273, "Response with the configuration for actuator parameters [Fields: APIversion numberOfActuators actuatorsArray]")
  """Response with the configuration for actuator parameters [Fields: APIversion numberOfActuators actuatorsArray]"""
  e8fac02rsp: int = (274, "Request for actuator calibration state [Fields: APIversion CalState ZoneLocation success]")
  """Request for actuator calibration state [Fields: APIversion CalState ZoneLocation success]"""
  e8fac03rsp: int = (275, "Request for actuator calibration status [Fields: APIversion CalType CalState ZoneLocation CalProgress SensorHeight ActuatorCmd DeadbandPos DeadbandNeg SlopePos SlopeNeg SensorArmLen isInverted]")
  """Request for actuator calibration status [Fields: APIversion CalType CalState ZoneLocation CalProgress SensorHeight ActuatorCmd DeadbandPos DeadbandNeg SlopePos SlopeNeg SensorArmLen isInverted]"""
  e8fac04rsp: int = (276, "Reports system information including sensor heights, zone states and alerts [Fields: APIversion SystemMode AlertStatus AvgHeight NumZones ZoneArray NumSensors SensorsArray]")
  """Reports system information including sensor heights, zone states and alerts [Fields: APIversion SystemMode AlertStatus AvgHeight NumZones ZoneArray NumSensors SensorsArray]"""
  e8fac05rsp: int = (277, "Commands to commit system actions [Fields: APIversion StateAction ZoneLocation success]")
  """Commands to commit system actions [Fields: APIversion StateAction ZoneLocation success]"""
  e8fac06rsp: int = (278, "Reponse of a list of all active faults [Fields: APIversion NumAlerts AlertArray]")
  """Reponse of a list of all active faults [Fields: APIversion NumAlerts AlertArray]"""
  e8fac07rsp: int = (279, "Reponse of a list of all attached devices [Fields: APIversion RESERVED1 RESERVED2 NumDevices DevicesArray]")
  """Reponse of a list of all attached devices [Fields: APIversion RESERVED1 RESERVED2 NumDevices DevicesArray]"""
  e8fad00rsp: int = (280, "Reports Centerpoint/Rangepoint RTX Passcode if available. In case no passcodes are available, PasscodeType is set to 255. Request Packet: 0x8e 0xad 0x00 [Fields: PasscodeType PasscodeLength Passcode]")
  """Reports Centerpoint/Rangepoint RTX Passcode if available. In case no passcodes are available, PasscodeType is set to 255. Request Packet: 0x8e 0xad 0x00 [Fields: PasscodeType PasscodeLength Passcode]"""
  e8fad01ack: int = (281, "Acknowledges command to clear passcode. Command Packet is 0x8e 0xad 0x01 [Fields: ]")
  """Acknowledges command to clear passcode. Command Packet is 0x8e 0xad 0x01 [Fields: ]"""
  e8fad02rsp: int = (282, "Reports Centerpoint/Rangepoint RTX position allowed flag status. Request Packet: 0x8e 0xad 0x02 [Fields: PositionAllowed]")
  """Reports Centerpoint/Rangepoint RTX position allowed flag status. Request Packet: 0x8e 0xad 0x02 [Fields: PositionAllowed]"""
  e8fae00rsp: int = (283, "Response to the Bluetooth pairing information request [Fields: PairingStatus RemainingTime PairedDevicesCount ConnectedDevicesCount]")
  """Response to the Bluetooth pairing information request [Fields: PairingStatus RemainingTime PairedDevicesCount ConnectedDevicesCount]"""
  e8fae01rsp: int = (284, "Response to setting the power state of the Bluetooth module [Fields: BluetoothPowerState]")
  """Response to setting the power state of the Bluetooth module [Fields: BluetoothPowerState]"""
  e8fae02rsp: int = (285, "Response to setting the Bluetooth pairing state of the receiver [Fields: BluetoothPairingState RemainingTime]")
  """Response to setting the Bluetooth pairing state of the receiver [Fields: BluetoothPairingState RemainingTime]"""
  e8fae03rsp: int = (286, "Reponse to unpairing all Bluetooth devices [Fields: ClearedDevicesCount]")
  """Reponse to unpairing all Bluetooth devices [Fields: ClearedDevicesCount]"""
  e8fae04rsp: int = (287, "Paring state change event [Fields: BluetoothPairingState RemainingTime]")
  """Paring state change event [Fields: BluetoothPairingState RemainingTime]"""
  e8fae05rsp: int = (288, "A notification for a Bluetooth device pairing or connection event [Fields: DeviceEventType DeviceNameLength DeviceName]")
  """A notification for a Bluetooth device pairing or connection event [Fields: DeviceEventType DeviceNameLength DeviceName]"""
  e8fae05ack: int = (289, "Acknowledges the request for Bluetooth device event notifications (8eae05) [Fields: DeviceEventType]")
  """Acknowledges the request for Bluetooth device event notifications (8eae05) [Fields: DeviceEventType]"""
  eb080rsp: int = (290, "Reports the PPS configuration settings. This acknowleges the 0xB0 0x00 commands. [Fields: PPSNumber EnableFlag PPSTimebase PPSPolarity AutoReport Period Offset MaxUncThreshold]")
  """Reports the PPS configuration settings. This acknowleges the 0xB0 0x00 commands. [Fields: PPSNumber EnableFlag PPSTimebase PPSPolarity AutoReport Period Offset MaxUncThreshold]"""
  eb081rsp: int = (291, "Reports whether the specified PPS signal is enabled or disabled. This acknowledges a 0xB0 0x01 command. [Fields: PPSNumber EnableFlag]")
  """Reports whether the specified PPS signal is enabled or disabled. This acknowledges a 0xB0 0x01 command. [Fields: PPSNumber EnableFlag]"""
  ebb00rsp: int = (292, "Reports primary receiver configuration parameters in response to Command Packet 0xBB 0x00. [Fields: OperatingDimension DGPSMode DynamicsCode SolutionMode ElevetionMask AMUMask PDOP PDOPSwitch DGPSAgeLimit FoliageMode LowPowerMode ClockHoldMode MeasurementRate PosFixRate]")
  """Reports primary receiver configuration parameters in response to Command Packet 0xBB 0x00. [Fields: OperatingDimension DGPSMode DynamicsCode SolutionMode ElevetionMask AMUMask PDOP PDOPSwitch DGPSAgeLimit FoliageMode LowPowerMode ClockHoldMode MeasurementRate PosFixRate]"""
  ebcrsp: int = (293, "Holds the configuration of a particular serial port. This includes the port settings and input and output protocols. [Fields: Port InputBaudRate OutputBaudRate DataBits Parity StopBits FlowControl InputProtocol OutputProtocol ProtocolOperation]")
  """Holds the configuration of a particular serial port. This includes the port settings and input and output protocols. [Fields: Port InputBaudRate OutputBaudRate DataBits Parity StopBits FlowControl InputProtocol OutputProtocol ProtocolOperation]"""
  ebf1arsp: int = (294, "Wraps Autopilot API NMEA messages for output in a TSIP stream. [Fields: PacketDataLength, PacketData]")
  """Wraps Autopilot API NMEA messages for output in a TSIP stream. [Fields: PacketDataLength, PacketData]"""
  ebf40rsp: int = (295, "Configuration packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Configuration packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf400000rsp: int = (296, "Requests App Version(?) configuration from the Autopilot Navigation Controller [Fields: Version fw_year fw_month fw_day fw_config fw_released Entry ImageSize Checksum, Name CompressedSize CompressedChecksum beta_expiration ErrorLogStart ErrorLogEnd FFSStart FFSEnd GuidanceStart GuidanceEnd CfgBlkSect1 CfgBlkSect2 AppStorageStart AppStorageEnd MinFailsafeMonVerson CompressedVersionNumber CompressedVersionNumberHash FOOTER]")
  """Requests App Version(?) configuration from the Autopilot Navigation Controller [Fields: Version fw_year fw_month fw_day fw_config fw_released Entry ImageSize Checksum, Name CompressedSize CompressedChecksum beta_expiration ErrorLogStart ErrorLogEnd FFSStart FFSEnd GuidanceStart GuidanceEnd CfgBlkSect1 CfgBlkSect2 AppStorageStart AppStorageEnd MinFailsafeMonVerson CompressedVersionNumber CompressedVersionNumberHash FOOTER]"""
  ebf400100rsp: int = (297, "Requests options configuration from the Autopilot Navigation Controller [Fields: SerialNumber, OptionsLength, Options]")
  """Requests options configuration from the Autopilot Navigation Controller [Fields: SerialNumber, OptionsLength, Options]"""
  ebf401400rsp: int = (298, "Configuration packet response to get TAP parameter from the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]")
  """Configuration packet response to get TAP parameter from the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]"""
  ebf401401rsp: int = (299, "Configuration packet response from setting a TAP parameter on the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]")
  """Configuration packet response from setting a TAP parameter on the Autopilot Navigation Controller [Fields: TAPStringLength, TAPString]"""
  ebf41rsp: int = (300, "File Transfer packet response from the Autopilot Navigation Controller [Fields: FileId CmdId status PacketNumber, PacketDataLength, PacketData]")
  """File Transfer packet response from the Autopilot Navigation Controller [Fields: FileId CmdId status PacketNumber, PacketDataLength, PacketData]"""
  ebf42rsp: int = (301, "Remote Monitor Engineering Data packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Engineering Data packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf4200rsp: int = (302, "Gets status information for navigation [Fields: Time State Error UtcOffset]")
  """Gets status information for navigation [Fields: Time State Error UtcOffset]"""
  ebf4201rsp: int = (303, "Gets status information for navigation [Fields: PosEast PosNorth Yaw Roll Speed CrossTrackError Range TargetSteeringAngle]")
  """Gets status information for navigation [Fields: PosEast PosNorth Yaw Roll Speed CrossTrackError Range TargetSteeringAngle]"""
  ebf4202rsp: int = (304, "Gets status information for GNSS [Fields: Seconds Week NumSatelites PosType PpsOccured AntennaPosEast AntennaPosNorth AntennaPosUp VelHoriz Heading PDOP]")
  """Gets status information for GNSS [Fields: Seconds Week NumSatelites PosType PpsOccured AntennaPosEast AntennaPosNorth AntennaPosUp VelHoriz Heading PDOP]"""
  ebf43rsp: int = (305, "Remote Monitor Control packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Control packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf4301rsp: int = (306, "Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets autosteering to enabled/disabled [Fields: EngageState]")
  """Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets autosteering to enabled/disabled [Fields: EngageState]"""
  ebf4303rsp: int = (307, "Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets logging to enabled/disabled [Fields: LoggingCommand]")
  """Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets logging to enabled/disabled [Fields: LoggingCommand]"""
  ebf4306rsp: int = (308, "Remote Monitor Control packet response from the Autopilot Navigation Controller to control Steering/Speed [Fields: CommandID Command Value]")
  """Remote Monitor Control packet response from the Autopilot Navigation Controller to control Steering/Speed [Fields: CommandID Command Value]"""
  ebf44rsp: int = (309, "Remote Monitor General Data packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor General Data packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf45rsp: int = (310, "Remote Monitor Waypoint Data packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Remote Monitor Waypoint Data packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf46rsp: int = (311, "Boot Monitor packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Boot Monitor packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf47rsp: int = (312, "Debug packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Debug packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf470500rsp: int = (313, "Gets the current diagnostic error type from the Autopilot Navigation Controller [Fields: ErrorType]")
  """Gets the current diagnostic error type from the Autopilot Navigation Controller [Fields: ErrorType]"""
  ebf470501rsp: int = (314, "Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller [Fields: ]")
  """Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller [Fields: ]"""
  ebf470502rsp: int = (315, "Gets a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved]")
  """Gets a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved]"""
  ebf470503rsp: int = (316, "Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller [Fields: DiagItemId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved]")
  """Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller [Fields: DiagItemId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved]"""
  ebf470504rsp: int = (317, "Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller [Fields: ErrorComponentId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved]")
  """Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller [Fields: ErrorComponentId ErrorType ErrorLevel ErrorComponent ErrorCount ErrorTimeout, ErrorValues DescriptionID Reserved]"""
  ebf470505rsp: int = (318, "Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller [Fields: MaxErrorTypes]")
  """Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller [Fields: MaxErrorTypes]"""
  ebf470506rsp: int = (319, "Gets the description of a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId, StringLength, String]")
  """Gets the description of a diagnostic record item from the Autopilot Navigation Controller [Fields: DiagItemId, StringLength, String]"""
  ebf470507rsp: int = (320, "Acknowledge the current warning on the Autopilot Navigation Controller [Fields: ]")
  """Acknowledge the current warning on the Autopilot Navigation Controller [Fields: ]"""
  ebf470508rsp: int = (321, "Gets the maximum number of warnings from the Autopilot Navigation Controller [Fields: MaxWarnings]")
  """Gets the maximum number of warnings from the Autopilot Navigation Controller [Fields: MaxWarnings]"""
  ebf470509rsp: int = (322, "Gets the description of a warning from the Autopilot Navigation Controller [Fields: WarningId, StringLength, String]")
  """Gets the description of a warning from the Autopilot Navigation Controller [Fields: WarningId, StringLength, String]"""
  ebf47050arsp: int = (323, "Gets the maximum number of messages from the Autopilot Navigation Controller [Fields: MaxMessagesCount]")
  """Gets the maximum number of messages from the Autopilot Navigation Controller [Fields: MaxMessagesCount]"""
  ebf47050brsp: int = (324, "Gets a message description from the Autopilot Navigation Controller [Fields: MessageId, StringLength, String]")
  """Gets a message description from the Autopilot Navigation Controller [Fields: MessageId, StringLength, String]"""
  ebf4707rsp: int = (325, "Gets ADC data from the Autopilot Navigation Controller [Fields: HighPrecisionADC, LowPrecisionADC Time]")
  """Gets ADC data from the Autopilot Navigation Controller [Fields: HighPrecisionADC, LowPrecisionADC Time]"""
  ebf470e06rsp: int = (326, "Debug packet response from the Autopilot Navigation Controller. Contains .dbg file header [Fields: PacketCount PacketNumber PacketSize PacketData]")
  """Debug packet response from the Autopilot Navigation Controller. Contains .dbg file header [Fields: PacketCount PacketNumber PacketSize PacketData]"""
  ebf470e07rsp: int = (327, "Debug packet response from the Autopilot Navigation Controller. Contains .dbg file data [Fields: PacketCount PacketNumber PacketSize PacketData]")
  """Debug packet response from the Autopilot Navigation Controller. Contains .dbg file data [Fields: PacketCount PacketNumber PacketSize PacketData]"""
  ebf470e08rsp: int = (328, "Debug packet response from the Autopilot Navigation Controller. Gets current port function [Fields: PortFunctionId]")
  """Debug packet response from the Autopilot Navigation Controller. Gets current port function [Fields: PortFunctionId]"""
  ebf470e09rsp: int = (329, "Debug packet response from the Autopilot Navigation Controller. Sets current port function [Fields: PortFunctionId]")
  """Debug packet response from the Autopilot Navigation Controller. Sets current port function [Fields: PortFunctionId]"""
  ebf471400rsp: int = (330, "Gets number of internal vdb's from the Autopilot Controller [Fields: VDBCount]")
  """Gets number of internal vdb's from the Autopilot Controller [Fields: VDBCount]"""
  ebf471401rsp: int = (331, "Gets a vdb record from the Autopilot Controller [Fields: VDBIndex, Name, Model]")
  """Gets a vdb record from the Autopilot Controller [Fields: VDBIndex, Name, Model]"""
  ebf471402rsp: int = (332, "Sets the vdb record on the Autopilot Controller [Fields: VDBIndex, Name, Model]")
  """Sets the vdb record on the Autopilot Controller [Fields: VDBIndex, Name, Model]"""
  ebf471ersp: int = (333, "Gets current IMU data from the Autopilot Controller [Fields: RawTimeNSec RawTimeSec RawGyroX RawGyroY RawGyroZ RawAccelX RawAccelY RawAccelZ RawTemp RawVRef ScaledTimeNSec ScaledTimeSec ScaledGyroX ScaledGyroY ScaledGyroZ ScaledAccelX ScaledAccelY ScaledAccelZ ScaledTemp ScaledVRef]")
  """Gets current IMU data from the Autopilot Controller [Fields: RawTimeNSec RawTimeSec RawGyroX RawGyroY RawGyroZ RawAccelX RawAccelY RawAccelZ RawTemp RawVRef ScaledTimeNSec ScaledTimeSec ScaledGyroX ScaledGyroY ScaledGyroZ ScaledAccelX ScaledAccelY ScaledAccelZ ScaledTemp ScaledVRef]"""
  ebf4arsp: int = (334, "Calibration packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]")
  """Calibration packet response from the Autopilot Navigation Controller [Fields: PacketDataLength, PacketData]"""
  ebf4a0b00rsp: int = (335, "Steering angle sensor calibration information response [Fields: AngleRawVoltage AngleScaledDegrees]")
  """Steering angle sensor calibration information response [Fields: AngleRawVoltage AngleScaledDegrees]"""
  ebf4a0b01rsp: int = (336, " [Fields: Success]")
  """ [Fields: Success]"""
  ebf4a0c00rsp: int = (337, " [Fields: TestPGain TestDeadzone TestPWM CommandSteeringAngleDegrees MeasuredSteeringAngleDegrees MeasuredSteeringSlewTimeSeconds MeasuredSteeringOvershootPercent]")
  """ [Fields: TestPGain TestDeadzone TestPWM CommandSteeringAngleDegrees MeasuredSteeringAngleDegrees MeasuredSteeringSlewTimeSeconds MeasuredSteeringOvershootPercent]"""
  ebf4a0c08rsp: int = (338, " [Fields: PGainState]")
  """ [Fields: PGainState]"""
  ebf4brsp: int = (339, "Autotester response to the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]")
  """Autotester response to the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]"""
  ebf4c00000004rsp: int = (340, "External Device packet command to read the manual override info from the Autopilot Navigation Controller [Fields: Raw Scaled]")
  """External Device packet command to read the manual override info from the Autopilot Navigation Controller [Fields: Raw Scaled]"""
  ebf4c00000104rsp: int = (341, "External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller [Fields: Raw Scaled]")
  """External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller [Fields: Raw Scaled]"""
  ebf4c00000204rsp: int = (342, "External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller [Fields: Raw Scaled]")
  """External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller [Fields: Raw Scaled]"""
  ebf4c00000704rsp: int = (343, "External Device packet command to read the Gear lever info from the Autopilot Navigation Controller [Fields: Raw Scaled]")
  """External Device packet command to read the Gear lever info from the Autopilot Navigation Controller [Fields: Raw Scaled]"""
  ebf4c0101rsp: int = (344, "Autopilot Field Computer Heartbeat packet response from the Autosteer Client [Fields: AutosteerVersion AutosteerState APIVersion SystemState WarningState FaultState WarningLevel PositionFixQuality NoAutoAllowed RoadingStatusBits RowGuidanceMode Reserved1]")
  """Autopilot Field Computer Heartbeat packet response from the Autosteer Client [Fields: AutosteerVersion AutosteerState APIVersion SystemState WarningState FaultState WarningLevel PositionFixQuality NoAutoAllowed RoadingStatusBits RowGuidanceMode Reserved1]"""
  ebf4c0108rsp: int = (345, "External Device packet command to set close any open field [Fields: ImplementWidthLength, ImplementWidth]")
  """External Device packet command to set close any open field [Fields: ImplementWidthLength, ImplementWidth]"""
  ebf4c010arsp: int = (346, "External Device packet command to set close any open field [Fields: Result]")
  """External Device packet command to set close any open field [Fields: Result]"""
  ebf4c010brsp: int = (347, "External Device packet Control State [Fields: ControlState, MiscDataLength, MiscData]")
  """External Device packet Control State [Fields: ControlState, MiscDataLength, MiscData]"""
  ebf4c010drsp: int = (348, "External Device packet response with Aggressiveness [Fields: Aggressiveness]")
  """External Device packet response with Aggressiveness [Fields: Aggressiveness]"""
  ebf4c010ersp: int = (349, "External Device packet response with Task Delay [Fields: TaskDelay]")
  """External Device packet response with Task Delay [Fields: TaskDelay]"""
  ebf4c010frsp: int = (350, "External Device packet response with Fix Quality [Fields: FixQuality]")
  """External Device packet response with Fix Quality [Fields: FixQuality]"""
  ebf4c011000rsp: int = (351, "External Device packet response to Get Nudge [Fields: Nudge]")
  """External Device packet response to Get Nudge [Fields: Nudge]"""
  ebf4c011001rsp: int = (352, "External Device packet response to set Nudge [Fields: Nudge]")
  """External Device packet response to set Nudge [Fields: Nudge]"""
  ebf4c011002rsp: int = (353, "External Device packet response to Apply Nudge [Fields: Direction]")
  """External Device packet response to Apply Nudge [Fields: Direction]"""
  ebf4c011003rsp: int = (354, "External Device packet response to Get Total [Fields: Total]")
  """External Device packet response to Get Total [Fields: Total]"""
  ebf4c011004rsp: int = (355, "External Device response to Set Total Nudge [Fields: Total]")
  """External Device response to Set Total Nudge [Fields: Total]"""
  ebf4c0111rsp: int = (356, "External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller [Fields: Mask Rate]")
  """External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller [Fields: Mask Rate]"""
  ebf4c0114rsp: int = (357, "External Device packet response to set the GGA Adjust [Fields: GgaAdjust]")
  """External Device packet response to set the GGA Adjust [Fields: GgaAdjust]"""
  ebf4c011806rsp: int = (358, "Field computer pattern definition for pivot ACB patterns [Fields: Curvature PointA PointB CenterPoint Radius]")
  """Field computer pattern definition for pivot ACB patterns [Fields: Curvature PointA PointB CenterPoint Radius]"""
  ebf4c011810rsp: int = (359, "Swath by swath pattern definition response (PTRN_SWATH_BY_SWATH) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode]")
  """Swath by swath pattern definition response (PTRN_SWATH_BY_SWATH) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode]"""
  ebf4c011811rsp: int = (360, "Swath section pattern definition response (PTRN_SWATH_SECTION) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex ErrorCode]")
  """Swath section pattern definition response (PTRN_SWATH_SECTION) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex ErrorCode]"""
  ebf4c011813rsp: int = (361, "Swath by swath fragment pattern definition response (PTRN_SWATH_BY_SWATH_FRAGMENT) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode]")
  """Swath by swath fragment pattern definition response (PTRN_SWATH_BY_SWATH_FRAGMENT) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode]"""
  ebf4c011820rsp: int = (362, "Swath by swath FFA pattern definition response (PTRN_SWATH_BY_SWATH_FFA) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode]")
  """Swath by swath FFA pattern definition response (PTRN_SWATH_BY_SWATH_FFA) [Fields: SwathNumber SwathType NumPoints ResetLtpOrigin ErrorCode]"""
  ebf4c011821rsp: int = (363, "Swath section FFA pattern definition response (PTRN_SWATH_SECTION_FFA) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex ErrorCode]")
  """Swath section FFA pattern definition response (PTRN_SWATH_SECTION_FFA) [Fields: SwathNumber SwathNumPoints SectionNumPoints SectionIndex ErrorCode]"""
  ebf4c0119rsp: int = (364, "Response to the Field Computer Information Command (tsip::Sbe4c0119cmd) [Fields: ManufacturerId ProductId1 ProductId2 FirmwareVersion]")
  """Response to the Field Computer Information Command (tsip::Sbe4c0119cmd) [Fields: ManufacturerId ProductId1 ProductId2 FirmwareVersion]"""
  ebf4c011arsp: int = (365, "Extended Field Computer Heartbeat packet response from the Autosteer Client [Fields: AutosteerState SystemState WarningState FaultState WarningLevel PositionFixQuality NoAutoAllowedReason RoadingStatusBits RowGuidanceMode TIMStatus VelocityControlState Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 Reserved9 Reserved10 SequenceNumber]")
  """Extended Field Computer Heartbeat packet response from the Autosteer Client [Fields: AutosteerState SystemState WarningState FaultState WarningLevel PositionFixQuality NoAutoAllowedReason RoadingStatusBits RowGuidanceMode TIMStatus VelocityControlState Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8 Reserved9 Reserved10 SequenceNumber]"""
  ebf4c0120rsp: int = (366, "Path to be plotted on Field Computer map. Reference point is first point of path (only plot for first message). Included with all packets though. [Fields: PathType NumberOfPoints PacketNumber LastPacket ReferenceLatitude ReferenceLongitude Points]")
  """Path to be plotted on Field Computer map. Reference point is first point of path (only plot for first message). Included with all packets though. [Fields: PathType NumberOfPoints PacketNumber LastPacket ReferenceLatitude ReferenceLongitude Points]"""
  ebf4c0500rsp: int = (367, "Sent by the NAV to the display when updating an opis device, like a SAM-300 [Fields: OperationState Progress DeviceType]")
  """Sent by the NAV to the display when updating an opis device, like a SAM-300 [Fields: OperationState Progress DeviceType]"""
  ebf4c2000rsp: int = (368, "External Device packet response to return the guidance status enable [Fields: Enabled]")
  """External Device packet response to return the guidance status enable [Fields: Enabled]"""
  ebf4c2001rsp: int = (369, "External Device packet response to update the guidance status [Fields: CanId CanMsgLength CanMsg]")
  """External Device packet response to update the guidance status [Fields: CanId CanMsgLength CanMsg]"""
  ebf4c2300rsp: int = (370, "Clothoid New Path Response [Fields: type]")
  """Clothoid New Path Response [Fields: type]"""
  ebf4c2301rsp: int = (371, "Clothoid Append Path Response [Fields: Sequence_Number]")
  """Clothoid Append Path Response [Fields: Sequence_Number]"""
  ebf4c2302rsp: int = (372, "Clothoid Activate Clothoid Guidance Response [Fields: Activate]")
  """Clothoid Activate Clothoid Guidance Response [Fields: Activate]"""
  ebf4c8000rsp: int = (373, "Updates the display with FFA status [Fields: Version Swath RequestedSwath TurnProgress Signal SwathIndicators audibleAlert UIMessage ButtonNextSwathEnable ButtonTrueSwathEnable ButtonLeft ButtonRight ButtonSequenceEndOfRow ButtonSequenceStartOfRow ButtonDismiss ButtonAutoTurn ButtonFFAEngage ButtonAcceptLiability ButtonDeclineLiability ButtonTurnStartAuto ButtonTurnStartManual NumberOfEvents SequenceEvents]")
  """Updates the display with FFA status [Fields: Version Swath RequestedSwath TurnProgress Signal SwathIndicators audibleAlert UIMessage ButtonNextSwathEnable ButtonTrueSwathEnable ButtonLeft ButtonRight ButtonSequenceEndOfRow ButtonSequenceStartOfRow ButtonDismiss ButtonAutoTurn ButtonFFAEngage ButtonAcceptLiability ButtonDeclineLiability ButtonTurnStartAuto ButtonTurnStartManual NumberOfEvents SequenceEvents]"""
  ebf4c8001rsp: int = (374, " [Fields: PacketDataLength, PacketData]")
  """ [Fields: PacketDataLength, PacketData]"""
  ebf4c8002rsp: int = (375, "External Device packet response to update the guidance status [Fields: SetStartSwathButtonState StandardButtonState BlockButtonState AlternatingBlockButtonState ContinuousBlockButtonState]")
  """External Device packet response to update the guidance status [Fields: SetStartSwathButtonState StandardButtonState BlockButtonState AlternatingBlockButtonState ContinuousBlockButtonState]"""
  ebf4drsp: int = (376, "GPS simulation response from the Autopilot Navigation Controller. Used for NAV to NAV communication. [Fields: PacketDataLength, PacketData]")
  """GPS simulation response from the Autopilot Navigation Controller. Used for NAV to NAV communication. [Fields: PacketDataLength, PacketData]"""
  ebf4ersp: int = (377, "Piped message response from the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]")
  """Piped message response from the Autopilot Navigation Controller. [Fields: PacketDataLength, PacketData]"""
  ebf4frsp: int = (378, "This is an alias to 0x8f 0xa1. [Fields: PacketDataLength, PacketData]")
  """This is an alias to 0x8f 0xa1. [Fields: PacketDataLength, PacketData]"""
  ebf5014rsp: int = (379, "TAP packet response to the Autosteer Controller [Fields: CommandID, PacketDataLength, PacketData]")
  """TAP packet response to the Autosteer Controller [Fields: CommandID, PacketDataLength, PacketData]"""
  ebf530600rsp: int = (380, "Remote Monitor Control Steering packet response to the Autosteer Controller [Fields: Direction]")
  """Remote Monitor Control Steering packet response to the Autosteer Controller [Fields: Direction]"""
  ebf530601rsp: int = (381, "Remote Monitor Control Speed packet response to the Autosteer Controller [Fields: Direction]")
  """Remote Monitor Control Speed packet response to the Autosteer Controller [Fields: Direction]"""
  ebf570507rsp: int = (382, "Field Computer Ack Current Warning packet response to the Autosteer Controller [Fields: ]")
  """Field Computer Ack Current Warning packet response to the Autosteer Controller [Fields: ]"""
  ebf5c0101rsp: int = (383, "Field Computer Heartbeat packet response from the Autosteer Client [Fields: AutosteerVersion AutosteerState APIVersion SystemState WarningState NoAutoAllowed PositionFixQuality RoadingStatusBits Reserved1 Reserved2]")
  """Field Computer Heartbeat packet response from the Autosteer Client [Fields: AutosteerVersion AutosteerState APIVersion SystemState WarningState NoAutoAllowed PositionFixQuality RoadingStatusBits Reserved1 Reserved2]"""
  ebf5c0106rsp: int = (384, "Field Computer Logging On packet response to the Autosteer Controller [Fields: ]")
  """Field Computer Logging On packet response to the Autosteer Controller [Fields: ]"""
  ebf5c0107rsp: int = (385, "Field Computer Logging Off packet response to the Autosteer Controller [Fields: ]")
  """Field Computer Logging Off packet response to the Autosteer Controller [Fields: ]"""
  ebf5c010brsp: int = (386, "Field Computer Control State packet response to the Autosteer Client [Fields: GuidanceType NoAutoAllowedReason]")
  """Field Computer Control State packet response to the Autosteer Client [Fields: GuidanceType NoAutoAllowedReason]"""
  ebf5c011000rsp: int = (387, "Field Computer Get Nudge packet response to the Autosteer Controller [Fields: NudgeIncrement]")
  """Field Computer Get Nudge packet response to the Autosteer Controller [Fields: NudgeIncrement]"""
  ebf5c011001rsp: int = (388, "Field Computer Set Nudge packet response to the Autosteer Controller [Fields: NudgeIncrement]")
  """Field Computer Set Nudge packet response to the Autosteer Controller [Fields: NudgeIncrement]"""
  ebf5c011002rsp: int = (389, "Field Computer Apply Nudge packet response to the Autosteer Controller [Fields: NudgeDirection]")
  """Field Computer Apply Nudge packet response to the Autosteer Controller [Fields: NudgeDirection]"""
  ebf5c011003rsp: int = (390, "Field Computer Get Total Nudge packet response to the Autosteer Controller [Fields: TotalNudge]")
  """Field Computer Get Total Nudge packet response to the Autosteer Controller [Fields: TotalNudge]"""
  ebf5c011004rsp: int = (391, "Field Computer Set Total Nudge packet response to the Autosteer Controller [Fields: TotalNudge]")
  """Field Computer Set Total Nudge packet response to the Autosteer Controller [Fields: TotalNudge]"""
  ebf5c0111rsp: int = (392, "Field Computer NMEA configuration packet response to the Autosteer Client [Fields: NMEAMask OutputInterval]")
  """Field Computer NMEA configuration packet response to the Autosteer Client [Fields: NMEAMask OutputInterval]"""
  ebf5c0114rsp: int = (393, "Field Computer Adjust GGA position response to the Autosteer Controller [Fields: AdjustPosition]")
  """Field Computer Adjust GGA position response to the Autosteer Controller [Fields: AdjustPosition]"""
  ebf5c0118rsp: int = (394, "Field Computer Pattern Definition packet response to the Autosteer Client [Fields: PatternType SwathNumber NumSwathPoints NumPacketPoints PointIndex FailureCode]")
  """Field Computer Pattern Definition packet response to the Autosteer Client [Fields: PatternType SwathNumber NumSwathPoints NumPacketPoints PointIndex FailureCode]"""
  ebf5c0119rsp: int = (395, "Field Computer Information packet response to the Autosteer Client [Fields: ManufacturerID ProductID1 ProductID2 ProductVersion Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8]")
  """Field Computer Information packet response to the Autosteer Client [Fields: ManufacturerID ProductID1 ProductID2 ProductVersion Reserved1 Reserved2 Reserved3 Reserved4 Reserved5 Reserved6 Reserved7 Reserved8]"""
  ebf6014rsp: int = (396, "TAP packet response to the Inertial Nav feature [Fields: CommandID, PacketDataLength, PacketData]")
  """TAP packet response to the Inertial Nav feature [Fields: CommandID, PacketDataLength, PacketData]"""
  ebf630600rsp: int = (397, "Remote Monitor Control Steering packet response to the Inertial Nav feature [Fields: Direction]")
  """Remote Monitor Control Steering packet response to the Inertial Nav feature [Fields: Direction]"""
  ebf630601rsp: int = (398, "Remote Monitor Control Speed packet response to the Inertial Nav feature [Fields: Direction]")
  """Remote Monitor Control Speed packet response to the Inertial Nav feature [Fields: Direction]"""
  ebf6800rsp: int = (399, "Roll/Pitch corrected Position and Attitude packet from the Inertial Nav feature. [Fields: GPSSecond INSEngineId AntennaId PositionEngine PositionType PositionFlags Latitude Longitude Height EVelocity NVelocity UVelocity Direction IMUStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites HDOP VDOP ESigma NSigma USigma SemiMajorSigma SemiMinorSigma CorrectionAge StationID]")
  """Roll/Pitch corrected Position and Attitude packet from the Inertial Nav feature. [Fields: GPSSecond INSEngineId AntennaId PositionEngine PositionType PositionFlags Latitude Longitude Height EVelocity NVelocity UVelocity Direction IMUStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites HDOP VDOP ESigma NSigma USigma SemiMajorSigma SemiMinorSigma CorrectionAge StationID]"""
  ebf6801rsp: int = (400, "Indicates that a GPS position wasn't generated for the given time period [Fields: GPSSecond INSEngineId AntennaId PositionEngine PositionFlags Direction IMUStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites StationID]")
  """Indicates that a GPS position wasn't generated for the given time period [Fields: GPSSecond INSEngineId AntennaId PositionEngine PositionFlags Direction IMUStatus Yaw Pitch Roll YawRate PitchRate RollRate NumSatellites StationID]"""
  ebf710000rsp: int = (401, "Publish Parameter Block Hardware Information packet response from the Autopilot Navigation Controller [Fields: ControllerSerNum NumDefinedOptions, Options ControllerSimulatingGPS HWType]")
  """Publish Parameter Block Hardware Information packet response from the Autopilot Navigation Controller [Fields: ControllerSerNum NumDefinedOptions, Options ControllerSimulatingGPS HWType]"""
  ebf710100rsp: int = (402, "Publish Parameter Block Software Information packet response from the Autopilot Navigation Controller [Fields: ApplicationId AppCodeVersionMajor AppCodeVersionMinor AppCodeVersionBuildNumber AppCodeVersionBuildType AppTestBuildFlag AppCodeVersionYear AppCodeVersionMonth AppCodeVersionDay ExpireGPSWeek, MonitorId MonCodeVersionMajor MonCodeVersionMinor MonCodeVersionMonth MonCodeVersionDay MonCodeVersionYear]")
  """Publish Parameter Block Software Information packet response from the Autopilot Navigation Controller [Fields: ApplicationId AppCodeVersionMajor AppCodeVersionMinor AppCodeVersionBuildNumber AppCodeVersionBuildType AppTestBuildFlag AppCodeVersionYear AppCodeVersionMonth AppCodeVersionDay ExpireGPSWeek, MonitorId MonCodeVersionMajor MonCodeVersionMinor MonCodeVersionMonth MonCodeVersionDay MonCodeVersionYear]"""
  ebf710200rsp: int = (403, "Publish Parameter Block OPS Config Information packet response from the Autopilot Navigation Controller [Fields: LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset]")
  """Publish Parameter Block OPS Config Information packet response from the Autopilot Navigation Controller [Fields: LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset]"""
  ebf710201rsp: int = (404, "Publish Parameter Block OPS Config Information packet SET confirmation    response from Autopilot [Fields: LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset]")
  """Publish Parameter Block OPS Config Information packet SET confirmation    response from Autopilot [Fields: LookAheadTime SwathChangeoverPoint SteeringAggressiveness NudgeIncrement ImplementDraftIncrement ImplementDraftOffset]"""
  ebf710300rsp: int = (405, "Publish Parameter Block Platform Config Information packet response from the Autopilot Navigation Controller [Fields: VehicleModel VehicleIndex VehicleType VehicleColor, ExtIOFctArray, VdmIOFctArray UseLowSpeedOperation UseVehicleDirectionEstimator DisableEngageButton SuperLowSpeeedAllowed UseSuperLowSpeeed SafetyMinVelocity GyroSteeringSupport UseAutosenseSensor]")
  """Publish Parameter Block Platform Config Information packet response from the Autopilot Navigation Controller [Fields: VehicleModel VehicleIndex VehicleType VehicleColor, ExtIOFctArray, VdmIOFctArray UseLowSpeedOperation UseVehicleDirectionEstimator DisableEngageButton SuperLowSpeeedAllowed UseSuperLowSpeeed SafetyMinVelocity GyroSteeringSupport UseAutosenseSensor]"""
  ebf710400rsp: int = (406, "Publish Parameter Block Safety Config Information packet response from the Autopilot Navigation Controller [Fields: OperatorAliveSwitchSnooze WarningRowEndDistance MaxEngageSpeedForward MaxEngageSpeedReverse MaxOperatingSpeedForward MaxOperatingSpeedReverse MaxSteeringAngleAllowed]")
  """Publish Parameter Block Safety Config Information packet response from the Autopilot Navigation Controller [Fields: OperatorAliveSwitchSnooze WarningRowEndDistance MaxEngageSpeedForward MaxEngageSpeedReverse MaxOperatingSpeedForward MaxOperatingSpeedReverse MaxSteeringAngleAllowed]"""
  ebf710500rsp: int = (407, "Publish Parameter Block Version Information packet response from the Autopilot Navigation Controller [Fields: TsipParamApiVersion, ControllerSerNum AppMajorVersion AppMinorVersion]")
  """Publish Parameter Block Version Information packet response from the Autopilot Navigation Controller [Fields: TsipParamApiVersion, ControllerSerNum AppMajorVersion AppMinorVersion]"""
  ebf710600rsp: int = (408, "Publish Parameter Sensor Hyd State Information packet response from the Autopilot Navigation Controller [Fields: OPSState RemoteEngageState ManualOverrideState MeasuredSteeringAngle SystemVoltage PwmRightSide PwmLeftSide PPSIntCount WheelSpeed GearLeverState NeutralSense MeasuredPumpPressureLeft MeasuredPumpPressureRight EngineSpeed]")
  """Publish Parameter Sensor Hyd State Information packet response from the Autopilot Navigation Controller [Fields: OPSState RemoteEngageState ManualOverrideState MeasuredSteeringAngle SystemVoltage PwmRightSide PwmLeftSide PPSIntCount WheelSpeed GearLeverState NeutralSense MeasuredPumpPressureLeft MeasuredPumpPressureRight EngineSpeed]"""
  ebf710700rsp: int = (409, "Publish Parameter Raw Sensor Status Information packet response from the Autopilot Navigation Controller [Fields: OPS RemoteEngage ManualOverride MeasuredSteeringAngle WheelSpeed GearLever MeasurePumpPressureLeft MeasurePumpPressureRight EngineSpeed OutputBalance SteeringFault]")
  """Publish Parameter Raw Sensor Status Information packet response from the Autopilot Navigation Controller [Fields: OPS RemoteEngage ManualOverride MeasuredSteeringAngle WheelSpeed GearLever MeasurePumpPressureLeft MeasurePumpPressureRight EngineSpeed OutputBalance SteeringFault]"""
  ebf710800rsp: int = (410, "Publish Parameter Block Selected IMU Status Information packet response from the Autopilot Navigation Controller [Fields: Authenticated FirmwareVersionValid VersionMajor VersionMinor SerialNumberValid, SerialNumber IsTemperatureValid Temperature IsRollValid RollEst IsPitchValid PitchEst DataSourceType DataTimestamp Connected]")
  """Publish Parameter Block Selected IMU Status Information packet response from the Autopilot Navigation Controller [Fields: Authenticated FirmwareVersionValid VersionMajor VersionMinor SerialNumberValid, SerialNumber IsTemperatureValid Temperature IsRollValid RollEst IsPitchValid PitchEst DataSourceType DataTimestamp Connected]"""
  ebf710900rsp: int = (411, "Publish Parameter Block CS Information packet response from the Autopilot Navigation Controller [Fields: ValveControllerType CsNum CSValues]")
  """Publish Parameter Block CS Information packet response from the Autopilot Navigation Controller [Fields: ValveControllerType CsNum CSValues]"""
  ebf710a00rsp: int = (412, "Publish Parameter Block Group1 Information packet response from the Autopilot Navigation Controller [Fields: Curvature SteeringAngleFront Frequency Counter]")
  """Publish Parameter Block Group1 Information packet response from the Autopilot Navigation Controller [Fields: Curvature SteeringAngleFront Frequency Counter]"""
  ebf710b00rsp: int = (413, "Publish Parameter Block Group2 Information packet response from the Autopilot Navigation Controller [Fields: RequestReset SteeringInput Readiness Lockout]")
  """Publish Parameter Block Group2 Information packet response from the Autopilot Navigation Controller [Fields: RequestReset SteeringInput Readiness Lockout]"""
  ebf710c00rsp: int = (414, "Publish Parameter Block Group3 Information packet response from the Autopilot Navigation Controller [Fields: JDSecurity JDExitCode]")
  """Publish Parameter Block Group3 Information packet response from the Autopilot Navigation Controller [Fields: JDSecurity JDExitCode]"""
  ebf710d00rsp: int = (415, "Publish Parameter Block GPS Guidance Status Information packet response from the Autopilot Navigation Controller [Fields: AutosteerLockedOut RawXTE SwathOffset ScaledSteeringAngle HeadingError FilteredRoll PathHeading LineAcquisitionState]")
  """Publish Parameter Block GPS Guidance Status Information packet response from the Autopilot Navigation Controller [Fields: AutosteerLockedOut RawXTE SwathOffset ScaledSteeringAngle HeadingError FilteredRoll PathHeading LineAcquisitionState]"""
  ebf710e00rsp: int = (416, "Publish Parameter Block GPS Guidance Diag Information packet response from the Autopilot Navigation Controller [Fields: VehicleDirection FilteredYawRate CommandedSteeringAngle CommandedYawRate CommandedPressureLeft CommandedPressureRight]")
  """Publish Parameter Block GPS Guidance Diag Information packet response from the Autopilot Navigation Controller [Fields: VehicleDirection FilteredYawRate CommandedSteeringAngle CommandedYawRate CommandedPressureLeft CommandedPressureRight]"""
  ebf710f00rsp: int = (417, "Publish Parameter Block Group4 Information packet response from the Autopilot Navigation Controller [Fields: RearSteeringAngle]")
  """Publish Parameter Block Group4 Information packet response from the Autopilot Navigation Controller [Fields: RearSteeringAngle]"""
  ed500rsp: int = (418, "Reports satellite constellation info. Note that multiple packets may be required to describe entire constellation. [Fields: AntennaId NumPackets SequenceId TotalNumSats NumSatsUsedInFix ConstellationFlags NumSatsInPacket SatInfoArray]")
  """Reports satellite constellation info. Note that multiple packets may be required to describe entire constellation. [Fields: AntennaId NumPackets SequenceId TotalNumSats NumSatsUsedInFix ConstellationFlags NumSatsInPacket SatInfoArray]"""
  ed502rsp: int = (419, "Report which satellite system is enabled/disabled [Fields: SatelliteSystemControlFlag]")
  """Report which satellite system is enabled/disabled [Fields: SatelliteSystemControlFlag]"""
  ed6ack: int = (420, "Acknowledges the success or failure of an authenticated command [Fields: DomainId CmdId Result]")
  """Acknowledges the success or failure of an authenticated command [Fields: DomainId CmdId Result]"""
  ed700ack: int = (421, "Lock or Unlock all stinger channels. This packet is for diagnostic purposes only and may change without notice. Command Packet: 0xC7 0x00 [Fields: AcknowledgeChannelLockId]")
  """Lock or Unlock all stinger channels. This packet is for diagnostic purposes only and may change without notice. Command Packet: 0xC7 0x00 [Fields: AcknowledgeChannelLockId]"""
  ed701ack: int = (422, "Acknowledge RF Band and Filter Switches setting command. [Fields: Band_Select Filter_Select]")
  """Acknowledge RF Band and Filter Switches setting command. [Fields: Band_Select Filter_Select]"""
  ed701rsp: int = (423, "Return the RF Band and Filter Switch setting for the signal requested. [Fields: Band_Select Filter_Select]")
  """Return the RF Band and Filter Switch setting for the signal requested. [Fields: Band_Select Filter_Select]"""
  kInvalidServerPacket: int = (-1, "Invalid packet [Fields:]")
  """Invalid packet [Fields:]"""

kNumServerPackets = len(EServerPackets)  # Number of Server Packets


class GroupPacketEncoder(TSIPGroupPacketEncoder):
  def __init__(self, SchemaList, SchemaSize, data=0, size=0):
    super().__init__(SchemaList, SchemaSize, data, size)

class GroupPacketDecoder(TSIPGroupPacketDecoder):
  def __init__(self, SchemaList, SchemaSize, data=0, size=0):
    super().__init__(SchemaList, SchemaSize, data, size)


#----------------------------------------------------------------------
# @name Client Side TSIP Packet Helpers
#
# Encodes client-side packets for the tsip server
class ClientPacketEncoder(GroupPacketEncoder):
  def __init__(self):
    super().__init__(kClientSchemaList, kNumClientPackets)

# Decodes server-side packets for the tsip client
class ServerPacketDecoder(GroupPacketDecoder):
  def __init__(self):
    super().__init__(kServerSchemaList, kNumServerPackets)


#----------------------------------------------------------------------  

#----------------------------------------------------------------------
# @name Server Side TSIP Packet Helpers
#
# Encodes server-side packets for the tsip server
class ServerPacketEncoder(GroupPacketEncoder):
  def __init__(self):
    super().__init__(kServerSchemaList, kNumServerPackets)

# Decodes client-side packets for the tsip client
class ClientPacketDecoder(GroupPacketDecoder):
  def __init__(self):
    super().__init__(kClientSchemaList, kNumClientPackets)


#----------------------------------------------------------------------  

