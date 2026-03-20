

#define NUMFIELDS(_a_) (sizeof(_a_)/sizeof(_a_[0]))
def NUMFIELDS(buff):
  return len(buff)

kCHARSchemaField = CHARSchemaField()
kU8SchemaField = U8SchemaField()
kS8SchemaField = S8SchemaField()
kU16SchemaField = U16SchemaField()
kS16SchemaField = S16SchemaField()
kU32SchemaField = U32SchemaField()
kS32SchemaField = S32SchemaField()
kFLTSchemaField = FLTSchemaField()
kDBLSchemaField = DBLSchemaField()


# DGPS Source info
k8ef9eDGPSSourceInfo = [
  U8SchemaField(), 
  UnusedSchemaField(2)
]

k8ef9eDGPSSourceInfoGroup = GroupSchemaField(k8ef9eDGPSSourceInfo,NUMFIELDS(k8ef9eDGPSSourceInfo))
k00cmdPacketDataData = U8SchemaField()

# This is used so we can get to the raw data
k00cmd = [
  IdSchemaField(0x00), 
  EndTerminatedArraySchemaField(k00cmdPacketDataData)
]

k00cmdEntry = TSIPSchemaEntry(EClientPackets.e00cmd, k00cmd, NUMFIELDS(k00cmd))
k00rspPacketDataData = U8SchemaField()

# This is used so we can get to the raw data
k00rsp = [
  IdSchemaField(0x00), 
  EndTerminatedArraySchemaField(k00rspPacketDataData)
]

k00rspEntry = TSIPSchemaEntry(EServerPackets.e00rsp, k00rsp, NUMFIELDS(k00rsp))
k13rspPacketDataData = U8SchemaField()

# Packet 0x13 is sent to notify the calling software when the receiver cannot parse the data sent in a command packet. The contents of the problem packet are included in the report.
k13rsp = [
  IdSchemaField(0x13), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k13rspPacketDataData)
]

k13rspEntry = TSIPSchemaEntry(EServerPackets.e13rsp, k13rsp, NUMFIELDS(k13rsp))
k1a00cmdRTCMDataData = U8SchemaField()

# Wraps RTCM data for output in a TSIP stream.
k1a00cmd = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x00), 
  EndTerminatedArraySchemaField(k1a00cmdRTCMDataData)
]

k1a00cmdEntry = TSIPSchemaEntry(EClientPackets.e1a00cmd, k1a00cmd, NUMFIELDS(k1a00cmd))
k1a01rspNMEADataChar = CHARSchemaField()

# Wraps NMEA messages for output in a TSIP stream. Command Packet 0x7A 0x07 configures the output of the NMEA wrapped data on a particular port.
k1a01rsp = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ArraySchemaField(k1a01rspNMEADataChar, 2, 0,0, 250)
]

k1a01rspEntry = TSIPSchemaEntry(EServerPackets.e1a01rsp, k1a01rsp, NUMFIELDS(k1a01rsp))
k1a0200cmdDCOLTypesData = U8SchemaField()

# Controls forwarding of DCOL packets to connected port
k1a0200cmd = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ArraySchemaField(k1a0200cmdDCOLTypesData, 3, 0,0, 20)
]

k1a0200cmdEntry = TSIPSchemaEntry(EClientPackets.e1a0200cmd, k1a0200cmd, NUMFIELDS(k1a0200cmd))
k1a0200rspDCOLTypesData = U8SchemaField()

# Indicates current settings for forwarding DCOL packets to connected port
k1a0200rsp = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ArraySchemaField(k1a0200rspDCOLTypesData, 3, 0,0, 20)
]

k1a0200rspEntry = TSIPSchemaEntry(EServerPackets.e1a0200rsp, k1a0200rsp, NUMFIELDS(k1a0200rsp))
k1a0201cmdDCOLMessageData = U8SchemaField()

# TSIP wrapped DCOL message command to device.
k1a0201cmd = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ArraySchemaField(k1a0201cmdDCOLMessageData, 3, 0,0, 250)
]

k1a0201cmdEntry = TSIPSchemaEntry(EClientPackets.e1a0201cmd, k1a0201cmd, NUMFIELDS(k1a0201cmd))
k1a0201rspDCOLMessageData = U8SchemaField()

# TSIP wrapped DCOL message response from device.
k1a0201rsp = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ArraySchemaField(k1a0201rspDCOLMessageData, 3, 0,0, 250)
]

k1a0201rspEntry = TSIPSchemaEntry(EServerPackets.e1a0201rsp, k1a0201rsp, NUMFIELDS(k1a0201rsp))
k1a0202cmdDCOLMessageData = U8SchemaField()

# Wraps DCOL messages for processing in a TSIP stream.
k1a0202cmd = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  ArraySchemaField(k1a0202cmdDCOLMessageData, 3, 0,0, 250)
]

k1a0202cmdEntry = TSIPSchemaEntry(EClientPackets.e1a0202cmd, k1a0202cmd, NUMFIELDS(k1a0202cmd))
k1a0300cmdCanIdsData = U32SchemaField()

# Controls forwarding of CAN messages from connected
k1a0300cmd = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  U8SchemaField(), 
  ArraySchemaField(k1a0300cmdCanIdsData, 5, 0,0, 50)
]

k1a0300cmdEntry = TSIPSchemaEntry(EClientPackets.e1a0300cmd, k1a0300cmd, NUMFIELDS(k1a0300cmd))
k1a0300rspCanIdsData = U32SchemaField()

# TSIP wrapped CAN message
k1a0300rsp = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  U8SchemaField(), 
  ArraySchemaField(k1a0300rspCanIdsData, 5, 0,0, 50)
]

k1a0300rspEntry = TSIPSchemaEntry(EServerPackets.e1a0300rsp, k1a0300rsp, NUMFIELDS(k1a0300rsp))
k1a0301cmdCanMsgData = U8SchemaField()

# TSIP wrapped CAN message to forward to CAN device
k1a0301cmd = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  U32SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k1a0301cmdCanMsgData, 6, 0,0, 8)
]

k1a0301cmdEntry = TSIPSchemaEntry(EClientPackets.e1a0301cmd, k1a0301cmd, NUMFIELDS(k1a0301cmd))
k1a0301rspCanMsgData = U8SchemaField()

# TSIP wrapped CAN message forwarded from device
k1a0301rsp = [
  IdSchemaField(0x1a), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x01), 
  UnusedSchemaField(3), 
  U32SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k1a0301rspCanMsgData, 5, 0,0, 8)
]

k1a0301rspEntry = TSIPSchemaEntry(EServerPackets.e1a0301rsp, k1a0301rsp, NUMFIELDS(k1a0301rsp))

# Clears all battery-backed data and performs a software reset to initiate a cold start of the receiver.
k1e4bcmd = [
  IdSchemaField(0x1e), 
  SubIdSchemaField(0x4b)
]

k1e4bcmdEntry = TSIPSchemaEntry(EClientPackets.e1e4bcmd, k1e4bcmd, NUMFIELDS(k1e4bcmd))

# Requests the firmware information from the receiver. Responds with the 0x45 packet.
k1freq = [
  IdSchemaField(0x1f)
]

k1freqEntry = TSIPSchemaEntry(EClientPackets.e1freq, k1freq, NUMFIELDS(k1freq))

# Requests the firmware information from the receiver. Responds with the 0x45 packet.
k1freqv1 = [
  IdSchemaField(0x1f), 
  U8SchemaField(), 
  U8SchemaField()
]

k1freqv1Entry = TSIPSchemaEntry(EClientPackets.e1freqv1, k1freqv1, NUMFIELDS(k1freqv1))

# Requests almanac data for one satellite from the receiver
k20req = [
  IdSchemaField(0x20), 
  U8SchemaField()
]

k20reqEntry = TSIPSchemaEntry(EClientPackets.e20req, k20req, NUMFIELDS(k20req))

# Requests current GPS time from the receiver. Report packet 0x41 is sent in response.
k21req = [
  IdSchemaField(0x21)
]

k21reqEntry = TSIPSchemaEntry(EClientPackets.e21req, k21req, NUMFIELDS(k21req))

# Configures the receiver to operate in a specific position fix mode and stores the new mode setting in battery-backed memory.
k22cmd = [
  IdSchemaField(0x22), 
  U8SchemaField()
]

k22cmdEntry = TSIPSchemaEntry(EClientPackets.e22cmd, k22cmd, NUMFIELDS(k22cmd))

# Initiates a software reset for the receiver, causing the receiver to perform the equivalent of powering off and then on. The receiver performs a self-test during the reset routine. Command Packet 0x25 contains no data bytes.
k25cmd = [
  IdSchemaField(0x25)
]

k25cmdEntry = TSIPSchemaEntry(EClientPackets.e25cmd, k25cmd, NUMFIELDS(k25cmd))

# Requests health and status information from the receiver. Report packets 0x46 and 0x4B are sent in response.
k26req = [
  IdSchemaField(0x26)
]

k26reqEntry = TSIPSchemaEntry(EClientPackets.e26req, k26req, NUMFIELDS(k26req))

# Requests signal levels for all satellites currently being tracked. Report packet 0x47 is sent in response.
k27req = [
  IdSchemaField(0x27)
]

k27reqEntry = TSIPSchemaEntry(EClientPackets.e27req, k27req, NUMFIELDS(k27req))

# Request the current operating parameter values of the receiver, which responds with Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory.
k2creq = [
  IdSchemaField(0x2c)
]

k2creqEntry = TSIPSchemaEntry(EClientPackets.e2creq, k2creq, NUMFIELDS(k2creq))

# Sets the operating parameter values of a receiver or requests the current parameter values, and the receiver responds by sending the parameter values in Report Packet 0x4C. The receiver stores the operating parameters in battery-backed memory.
k2ccmd = [
  IdSchemaField(0x2c), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k2ccmdEntry = TSIPSchemaEntry(EClientPackets.e2ccmd, k2ccmd, NUMFIELDS(k2ccmd))

# Requests analog to digital readings from receiver
k33req = [
  IdSchemaField(0x33)
]

k33reqEntry = TSIPSchemaEntry(EClientPackets.e33req, k33req, NUMFIELDS(k33req))

# Requests the current I/O option flags. The receiver responds by sending Report Packet 0x55.
k35req = [
  IdSchemaField(0x35)
]

k35reqEntry = TSIPSchemaEntry(EClientPackets.e35req, k35req, NUMFIELDS(k35req))

# Sets the current I/O option flags. The receiver records the I/O option flags settings in battery-backed memory and sends Report Packet 0x55 in response.
k35cmd = [
  IdSchemaField(0x35), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k35cmdEntry = TSIPSchemaEntry(EClientPackets.e35cmd, k35cmd, NUMFIELDS(k35cmd))

# Command Packet 0x38 downloads satellite data from one receiver, and uploads the data to another receiver. The receiver acknowledges a download operation by sending the requested data in Report Packet 0x58. The process of downloading satellite data from one receiver and uploading it to another decreases the amount of time required for the receiver to initialize from a cold start (battery-backed memory cleared). Note that the receiver can initialize itself without uploading data, it merely takes longer. To download data from one receiver, use only bytes 0&#8211;2. To upload the data to another receiver, use all bytes.
k38cmd = [
  IdSchemaField(0x38), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k38cmdEntry = TSIPSchemaEntry(EClientPackets.e38cmd, k38cmd, NUMFIELDS(k38cmd))

# Command Packet 0x3B requests the current status of satellite ephemeris data. The receiver acknowledges with Report Packet 0x5B when data is available.
k3breq = [
  IdSchemaField(0x3b), 
  U8SchemaField()
]

k3breqEntry = TSIPSchemaEntry(EClientPackets.e3breq, k3breq, NUMFIELDS(k3breq))

# Requests the current satellite tracking status. The receiver acknowledges with Report Packet 0x5C when data is available.
k3creq = [
  IdSchemaField(0x3c), 
  U8SchemaField()
]

k3creqEntry = TSIPSchemaEntry(EClientPackets.e3creq, k3creq, NUMFIELDS(k3creq))

# Controls output of Engineering Diagnostics
k3f02cmd = [
  IdSchemaField(0x3f), 
  SubIdSchemaField(0x02), 
  U8SchemaField()
]

k3f02cmdEntry = TSIPSchemaEntry(EClientPackets.e3f02cmd, k3f02cmd, NUMFIELDS(k3f02cmd))

# Gets the mask controlling diagnostic types output
k3f2200req = [
  IdSchemaField(0x3f), 
  SubIdSchemaField(0x22), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k3f2200reqEntry = TSIPSchemaEntry(EClientPackets.e3f2200req, k3f2200req, NUMFIELDS(k3f2200req))

# Sets the mask controlling diagnostic types output
k3f2200cmd = [
  IdSchemaField(0x3f), 
  SubIdSchemaField(0x22), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k3f2200cmdEntry = TSIPSchemaEntry(EClientPackets.e3f2200cmd, k3f2200cmd, NUMFIELDS(k3f2200cmd))

# reports the almanac data for a single satellite
k40rsp = [
  IdSchemaField(0x40), 
  U8SchemaField(), 
  FLTSchemaField(), 
  S16SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k40rspEntry = TSIPSchemaEntry(EServerPackets.e40rsp, k40rsp, NUMFIELDS(k40rsp))

# Reports the current GPS time of week and the week number.
k41rsp = [
  IdSchemaField(0x41), 
  FLTSchemaField(), 
  S16SchemaField(), 
  FLTSchemaField()
]

k41rspEntry = TSIPSchemaEntry(EServerPackets.e41rsp, k41rsp, NUMFIELDS(k41rsp))

# Reports the current GPS position fix in XYZ ECEF coordinate components. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm.
k42rsp = [
  IdSchemaField(0x42), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField()
]

k42rspEntry = TSIPSchemaEntry(EServerPackets.e42rsp, k42rsp, NUMFIELDS(k42rsp))

# Reports the current GPS velocity fix in XYZ ECEF coordinate. The I/O velocity option must be set to XYZ ECEF for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm.
k43rsp = [
  IdSchemaField(0x43), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField()
]

k43rspEntry = TSIPSchemaEntry(EServerPackets.e43rsp, k43rsp, NUMFIELDS(k43rsp))

# Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F.
k45rsp = [
  IdSchemaField(0x45), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k45rspEntry = TSIPSchemaEntry(EServerPackets.e45rsp, k45rsp, NUMFIELDS(k45rsp))
k45rspv1BCDSerialNumberBCDData = U8SchemaField()

# Provides information about the version of firmware in the Navigation and Signal Processors, and can provide information about the receiver configuration. The receiver sends this packet containing the software versions only after a power-on or reset and in response to Command Packet 0x1F.
k45rspv1 = [
  IdSchemaField(0x45), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FixedArraySchemaField(k45rspv1BCDSerialNumberBCDData, 4), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1), 
  UnusedSchemaField(64), 
  ChecksumSchemaField()
]

k45rspv1Entry = TSIPSchemaEntry(EServerPackets.e45rspv1, k45rspv1, NUMFIELDS(k45rspv1))

# Reports info about the satellite tracking status and operational health of the receiver.
k46rsp = [
  IdSchemaField(0x46), 
  U8SchemaField(), 
  U8SchemaField()
]

k46rspEntry = TSIPSchemaEntry(EServerPackets.e46rsp, k46rsp, NUMFIELDS(k46rsp))

# Signal level info
k47rspSignalLevelsInfoArraySignalLevelInfo = [
  U8SchemaField(), 
  FLTSchemaField()
]

k47rspSignalLevelsInfoArraySignalLevelInfoGroup = GroupSchemaField(k47rspSignalLevelsInfoArraySignalLevelInfo,NUMFIELDS(k47rspSignalLevelsInfoArraySignalLevelInfo))

# Reports signal levels for all satellites currently being tracked in response to packet 0x27.
k47rsp = [
  IdSchemaField(0x47), 
  U8SchemaField(), 
  ArraySchemaField(k47rspSignalLevelsInfoArraySignalLevelInfoGroup, 1, 0,0, 12)
]

k47rspEntry = TSIPSchemaEntry(EServerPackets.e47rsp, k47rsp, NUMFIELDS(k47rsp))

# GPS system message
k48rsp = [
  IdSchemaField(0x48), 
  StringSchemaField(22)
]

k48rspEntry = TSIPSchemaEntry(EServerPackets.e48rsp, k48rsp, NUMFIELDS(k48rsp))

# Provides the single precision lls fix values stored in the receiver
k4arsp = [
  IdSchemaField(0x4a), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField()
]

k4arspEntry = TSIPSchemaEntry(EServerPackets.e4arsp, k4arsp, NUMFIELDS(k4arsp))

# Provides the single precision lls fix values stored in the receiver
k4arspv1 = [
  IdSchemaField(0x4a), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k4arspv1Entry = TSIPSchemaEntry(EServerPackets.e4arspv1, k4arspv1, NUMFIELDS(k4arspv1))

# Provides the single precision lls fix values stored in the receiver
k4arspv2 = [
  IdSchemaField(0x4a), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField()
]

k4arspv2Entry = TSIPSchemaEntry(EServerPackets.e4arspv2, k4arspv2, NUMFIELDS(k4arspv2))

# Reports receiver's machine ID and additional status info in response to packet 0x26.
k4brsp = [
  IdSchemaField(0x4b), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k4brspEntry = TSIPSchemaEntry(EServerPackets.e4brsp, k4brsp, NUMFIELDS(k4brsp))

# Provides the operating parameter values of a receiver or requests the current parameter values stored in the receiver
k4crsp = [
  IdSchemaField(0x4c), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k4crspEntry = TSIPSchemaEntry(EServerPackets.e4crsp, k4crsp, NUMFIELDS(k4crsp))

# UTC Parameters
k4frsp = [
  IdSchemaField(0x4f), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  S16SchemaField(), 
  FLTSchemaField(), 
  S16SchemaField(), 
  S16SchemaField(), 
  S16SchemaField(), 
  S16SchemaField()
]

k4frspEntry = TSIPSchemaEntry(EServerPackets.e4frsp, k4frsp, NUMFIELDS(k4frsp))

# Analog to digital readings from receiver
k53rsp = [
  IdSchemaField(0x53), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k53rspEntry = TSIPSchemaEntry(EServerPackets.e53rsp, k53rsp, NUMFIELDS(k53rsp))

# Reports current I/O options in response to Command Packet 0x35.
k55rsp = [
  IdSchemaField(0x55), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k55rspEntry = TSIPSchemaEntry(EServerPackets.e55rsp, k55rsp, NUMFIELDS(k55rsp))
k58rspSVDatabytes = U8SchemaField()

# Report Packet 0x58 provides GPS data (almanac, ephemeris, etc.). The receiver sends this packet on request or in response to Command Packet 0x38 (acknowledging the loading of data). To get ionosphere or ephemeris, this report packet must be used
k58rsp = [
  IdSchemaField(0x58), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k58rspSVDatabytes, 4, 0,0, 200)
]

k58rspEntry = TSIPSchemaEntry(EServerPackets.e58rsp, k58rsp, NUMFIELDS(k58rsp))

# Report data specific to the almanc response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
k5822rsp = [
  IdSchemaField(0x58), 
  SubIdSchemaField(0x2), 
  SubIdSchemaField(0x2), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U16SchemaField()
]

k5822rspEntry = TSIPSchemaEntry(EServerPackets.e5822rsp, k5822rsp, NUMFIELDS(k5822rsp))

# Report data specific to the almanc health response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
k5823rsp = [
  IdSchemaField(0x58), 
  SubIdSchemaField(0x2), 
  SubIdSchemaField(0x3), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField()
]

k5823rspEntry = TSIPSchemaEntry(EServerPackets.e5823rsp, k5823rsp, NUMFIELDS(k5823rsp))

# Report data specific to the ionosphere data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
k5824rsp = [
  IdSchemaField(0x58), 
  SubIdSchemaField(0x2), 
  SubIdSchemaField(0x4), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k5824rspEntry = TSIPSchemaEntry(EServerPackets.e5824rsp, k5824rsp, NUMFIELDS(k5824rsp))

# Report data specific to the UTC data response. This data will arrive in response to command packet 0x38 For all following fields, please see their corresponding reference in ICD-GPS-2000
k5825rsp = [
  IdSchemaField(0x58), 
  SubIdSchemaField(0x2), 
  SubIdSchemaField(0x5), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(13), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField()
]

k5825rspEntry = TSIPSchemaEntry(EServerPackets.e5825rsp, k5825rsp, NUMFIELDS(k5825rsp))

# Report data specific to the Ephemeris response. This data can arrive in response to command packet 0x38 OR via configuration in command packet 0x7C 0x01. For all following fields, please see their corresponding reference in ICD-GPS-2000
k5826rsp = [
  IdSchemaField(0x58), 
  SubIdSchemaField(0x2), 
  SubIdSchemaField(0x6), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

k5826rspEntry = TSIPSchemaEntry(EServerPackets.e5826rsp, k5826rsp, NUMFIELDS(k5826rsp))

# Reports ephemeris status for a specified satellite in response to Command Packet 0x3B.
k5brsp = [
  IdSchemaField(0x5b), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField()
]

k5brspEntry = TSIPSchemaEntry(EServerPackets.e5brsp, k5brsp, NUMFIELDS(k5brsp))

# Reports tracking status for a specified satellite in response to Command Packet 0x3C.
k5crsp = [
  IdSchemaField(0x5c), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k5crspEntry = TSIPSchemaEntry(EServerPackets.e5crsp, k5crsp, NUMFIELDS(k5crsp))
k5f01rspDiagMsgChar = CHARSchemaField()

# Diagnostic message output from the receiver
k5f01rsp = [
  IdSchemaField(0x5f), 
  SubIdSchemaField(0x01), 
  EndTerminatedArraySchemaField(k5f01rspDiagMsgChar)
]

k5f01rspEntry = TSIPSchemaEntry(EServerPackets.e5f01rsp, k5f01rsp, NUMFIELDS(k5f01rsp))

# State of TSIP diagnostics output
k5f02rsp = [
  IdSchemaField(0x5f), 
  SubIdSchemaField(0x02), 
  U8SchemaField()
]

k5f02rspEntry = TSIPSchemaEntry(EServerPackets.e5f02rsp, k5f02rsp, NUMFIELDS(k5f02rsp))
k5f10rspDiagDataData = U8SchemaField()

# Diagnostic data output from the receiver
k5f10rsp = [
  IdSchemaField(0x5f), 
  SubIdSchemaField(0x10), 
  EndTerminatedArraySchemaField(k5f10rspDiagDataData)
]

k5f10rspEntry = TSIPSchemaEntry(EServerPackets.e5f10rsp, k5f10rsp, NUMFIELDS(k5f10rsp))

# Retrieve the mask used to output Diagnostic data from the receiver
k5f2200rsp = [
  IdSchemaField(0x5f), 
  SubIdSchemaField(0x22), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k5f2200rspEntry = TSIPSchemaEntry(EServerPackets.e5f2200rsp, k5f2200rsp, NUMFIELDS(k5f2200rsp))
k5f2201rspMsgMsg = CHARSchemaField()

# Diagnostic data output from the receiver
k5f2201rsp = [
  IdSchemaField(0x5f), 
  SubIdSchemaField(0x22), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(2), 
  DBLSchemaField(), 
  EndTerminatedArraySchemaField(k5f2201rspMsgMsg), 
  ChecksumSchemaField()
]

k5f2201rspEntry = TSIPSchemaEntry(EServerPackets.e5f2201rsp, k5f2201rsp, NUMFIELDS(k5f2201rsp))

# Requests the differential GPS position fix mode. Report packet 0x82 is sent in response
k62req = [
  IdSchemaField(0x62)
]

k62reqEntry = TSIPSchemaEntry(EClientPackets.e62req, k62req, NUMFIELDS(k62req))

# Sets the differential GPS position fix mode. Report packet 0x82 is sent in response
k62cmd = [
  IdSchemaField(0x62), 
  U8SchemaField()
]

k62cmdEntry = TSIPSchemaEntry(EClientPackets.e62cmd, k62cmd, NUMFIELDS(k62cmd))

# Requests DGPS corrections for given SVID
k65req = [
  IdSchemaField(0x65), 
  U8SchemaField()
]

k65reqEntry = TSIPSchemaEntry(EClientPackets.e65req, k65req, NUMFIELDS(k65req))

# Requests the status of SecureRTK and the 5 rover keys.
k690000req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k690000reqEntry = TSIPSchemaEntry(EClientPackets.e690000req, k690000req, NUMFIELDS(k690000req))

# Rover Key Data
k690001req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k690001reqEntry = TSIPSchemaEntry(EClientPackets.e690001req, k690001req, NUMFIELDS(k690001req))

# Set Rover Key Data
k690002cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  StringSchemaField(17), 
  StringSchemaField(16), 
  ChecksumSchemaField()
]

k690002cmdEntry = TSIPSchemaEntry(EClientPackets.e690002cmd, k690002cmd, NUMFIELDS(k690002cmd))

# Delete Rover Key Data
k690003cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k690003cmdEntry = TSIPSchemaEntry(EClientPackets.e690003cmd, k690003cmd, NUMFIELDS(k690003cmd))

# Requests one of several RTK stats reports. A variant of report packet 0x89 0x33 is sent in response, with the second report packet byte indicating the type of stats.
k6932req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x32), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k6932reqEntry = TSIPSchemaEntry(EClientPackets.e6932req, k6932req, NUMFIELDS(k6932req))

# Requests the RTK configuration
k6940req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x40), 
  ChecksumSchemaField()
]

k6940reqEntry = TSIPSchemaEntry(EClientPackets.e6940req, k6940req, NUMFIELDS(k6940req))

# Sets the RTK configuration
k6940cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x40), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(30), 
  ChecksumSchemaField()
]

k6940cmdEntry = TSIPSchemaEntry(EClientPackets.e6940cmd, k6940cmd, NUMFIELDS(k6940cmd))

# Requests RTK solution info. Report packet 0x89 0x41 is sent in response.
k6941req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x41), 
  ChecksumSchemaField()
]

k6941reqEntry = TSIPSchemaEntry(EClientPackets.e6941req, k6941req, NUMFIELDS(k6941req))

# Requests the RTK auxilliary settings. Report packet 0x89 0x50 is sent in response.
k6950req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x50), 
  ChecksumSchemaField()
]

k6950reqEntry = TSIPSchemaEntry(EClientPackets.e6950req, k6950req, NUMFIELDS(k6950req))

# Updates RTK auxilliary settings. Report packet 0x89 0x50 is sent in response.
k6950cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x50), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k6950cmdEntry = TSIPSchemaEntry(EClientPackets.e6950cmd, k6950cmd, NUMFIELDS(k6950cmd))

# Requests the RTK auxilliary status. Report packet 0x89 0x51 is sent in response.
k6951req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x51), 
  ChecksumSchemaField()
]

k6951reqEntry = TSIPSchemaEntry(EClientPackets.e6951req, k6951req, NUMFIELDS(k6951req))

# Requests RTK base info. Report packet 0x89 0x60 is sent in response.
k6960req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x60), 
  ChecksumSchemaField()
]

k6960reqEntry = TSIPSchemaEntry(EClientPackets.e6960req, k6960req, NUMFIELDS(k6960req))

# Requests CMR info. Report packet 0x89 0x61 is sent in response.
k6961req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x61), 
  ChecksumSchemaField()
]

k6961reqEntry = TSIPSchemaEntry(EClientPackets.e6961req, k6961req, NUMFIELDS(k6961req))

# Requests Ionospheric disturbance info. Report packet 0x89 0x62 is sent in response.
k6962req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x62), 
  ChecksumSchemaField()
]

k6962reqEntry = TSIPSchemaEntry(EClientPackets.e6962req, k6962req, NUMFIELDS(k6962req))

# Requests RTK radio status. Report packet 0x89 0x70 0x00 is sent in response.
k697000req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k697000reqEntry = TSIPSchemaEntry(EClientPackets.e697000req, k697000req, NUMFIELDS(k697000req))

# Requests RTK radio identity. Report packet 0x89 0x70 0x01 is sent in response.
k697001req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k697001reqEntry = TSIPSchemaEntry(EClientPackets.e697001req, k697001req, NUMFIELDS(k697001req))

# Requests RTK radio capabilities. Report packet 0x89 0x70 0x02 is sent in response.
k697002req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k697002reqEntry = TSIPSchemaEntry(EClientPackets.e697002req, k697002req, NUMFIELDS(k697002req))

# Requests RTK radio country info. Report packet 0x89 0x70 0x03 is sent in response.
k697003req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k697003reqEntry = TSIPSchemaEntry(EClientPackets.e697003req, k697003req, NUMFIELDS(k697003req))

# Requests config specific to 900MHz RTK radio. Report packet 0x89 0x70 0x04 is sent in response.
k697004req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x04), 
  ChecksumSchemaField()
]

k697004reqEntry = TSIPSchemaEntry(EClientPackets.e697004req, k697004req, NUMFIELDS(k697004req))

# Requests config specific to 450MHz RTK radio. Report packet 0x89 0x70 0x05 is sent in response.
k697005req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x05), 
  ChecksumSchemaField()
]

k697005reqEntry = TSIPSchemaEntry(EClientPackets.e697005req, k697005req, NUMFIELDS(k697005req))

# Sets RTK radio country code. Ack packet 0x89 0x70 0x06 is sent in response.
k697006cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k697006cmdEntry = TSIPSchemaEntry(EClientPackets.e697006cmd, k697006cmd, NUMFIELDS(k697006cmd))

# Sets 900MHz RTK radio network ID. Ack packet 0x89 0x70 0x07 is sent in response.
k697007cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k697007cmdEntry = TSIPSchemaEntry(EClientPackets.e697007cmd, k697007cmd, NUMFIELDS(k697007cmd))

# Sets 450MHz RTK radio channel ID. Ack packet 0x89 0x70 0x08 is sent in response.
k697008cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k697008cmdEntry = TSIPSchemaEntry(EClientPackets.e697008cmd, k697008cmd, NUMFIELDS(k697008cmd))

# Sets 450MHz RTK radio channel frequency. Ack packet 0x89 0x70 0x09 is sent in response.
k697009cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k697009cmdEntry = TSIPSchemaEntry(EClientPackets.e697009cmd, k697009cmd, NUMFIELDS(k697009cmd))

# Sets 450MHz RTK radio mode. Ack packet 0x89 0x70 0x0a is sent in response.
k69700acmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x0a), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k69700acmdEntry = TSIPSchemaEntry(EClientPackets.e69700acmd, k69700acmd, NUMFIELDS(k69700acmd))

# Restart connected RTK radio and re-establish communication. Ack packet 0x89 0x70 0x0b is sent in response.
k69700bcmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x0b), 
  ChecksumSchemaField()
]

k69700bcmdEntry = TSIPSchemaEntry(EClientPackets.e69700bcmd, k69700bcmd, NUMFIELDS(k69700bcmd))

# Requests Fallback RTX: X, Y, and Z offsets for the designated source. Response packet is 0x89 0x71 0x00. No longer supported, do not use.
k697100req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k697100reqEntry = TSIPSchemaEntry(EClientPackets.e697100req, k697100req, NUMFIELDS(k697100req))

# Set the X, Y, and Z user offsets. ACK packet is 0x89 0x71 0x01. No longer supported, do not use.
k697100cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x00), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k697100cmdEntry = TSIPSchemaEntry(EClientPackets.e697100cmd, k697100cmd, NUMFIELDS(k697100cmd))

# Requests the Fallback RTX configuration mode and the offset source. Response packet is 0x89 0x71 0x01. No longer supported, do not use.
k697101req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k697101reqEntry = TSIPSchemaEntry(EClientPackets.e697101req, k697101req, NUMFIELDS(k697101req))

# Sets Fallback RTX mode and offset source. ACK packet is 0x89 0x71 0x03. No longer supported, do not use.
k697101cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k697101cmdEntry = TSIPSchemaEntry(EClientPackets.e697101cmd, k697101cmd, NUMFIELDS(k697101cmd))

# Requests xFill Premium configuration. Response packet is 0x89 0x71 0x03.
k697103req = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k697103reqEntry = TSIPSchemaEntry(EClientPackets.e697103req, k697103req, NUMFIELDS(k697103req))

# Sets xFill Premium Configuration. ACK packet is 0x89 0x71 0x03.
k697103cmd = [
  IdSchemaField(0x69), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k697103cmdEntry = TSIPSchemaEntry(EClientPackets.e697103cmd, k697103cmd, NUMFIELDS(k697103cmd))

# Requests current differential corrections output control settings.
k6a01req = [
  IdSchemaField(0x6a), 
  SubIdSchemaField(0x01)
]

k6a01reqEntry = TSIPSchemaEntry(EClientPackets.e6a01req, k6a01req, NUMFIELDS(k6a01req))

# Controls whether or not the receiver will output differential correction information.
k6a01cmd = [
  IdSchemaField(0x6a), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k6a01cmdEntry = TSIPSchemaEntry(EClientPackets.e6a01cmd, k6a01cmd, NUMFIELDS(k6a01cmd))

# Indicates whether or not the receiver will output differential correction information.
k6a01rsp = [
  IdSchemaField(0x6a), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k6a01rspEntry = TSIPSchemaEntry(EServerPackets.e6a01rsp, k6a01rsp, NUMFIELDS(k6a01rsp))

# Requests current state of automatic position sigma reporting
k6b00req = [
  IdSchemaField(0x6b), 
  SubIdSchemaField(0x00)
]

k6b00reqEntry = TSIPSchemaEntry(EClientPackets.e6b00req, k6b00req, NUMFIELDS(k6b00req))

# Controls automatic reporting of position sigma
k6b00cmd = [
  IdSchemaField(0x6b), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k6b00cmdEntry = TSIPSchemaEntry(EClientPackets.e6b00cmd, k6b00cmd, NUMFIELDS(k6b00cmd))

# Requests a single position sigma (error) information report, automatic reporting can be set up with command 0x6B 0x00
k6b02req = [
  IdSchemaField(0x6b), 
  SubIdSchemaField(0x02)
]

k6b02reqEntry = TSIPSchemaEntry(EClientPackets.e6b02req, k6b02req, NUMFIELDS(k6b02req))
k6drspSatsInViewSat = U8SchemaField()

# Reports the list of satelliites used for position fixes by the receiver.
k6drsp = [
  IdSchemaField(0x6d), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  ArraySchemaField(k6drspSatsInViewSat, 1, 0xf0,4, 16)
]

k6drspEntry = TSIPSchemaEntry(EServerPackets.e6drsp, k6drsp, NUMFIELDS(k6drsp))

# 
k6e03cmd = [
  IdSchemaField(0x6e), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField()
]

k6e03cmdEntry = TSIPSchemaEntry(EClientPackets.e6e03cmd, k6e03cmd, NUMFIELDS(k6e03cmd))

# Complete measurement report for the L1 GPS frequency
k6f01rsp = [
  IdSchemaField(0x6f), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k6f01rspEntry = TSIPSchemaEntry(EServerPackets.e6f01rsp, k6f01rsp, NUMFIELDS(k6f01rsp))

# Complete measurement report for the L2 GPS frequency
k6f10rsp = [
  IdSchemaField(0x6f), 
  SubIdSchemaField(0x10), 
  ChecksumSchemaField()
]

k6f10rspEntry = TSIPSchemaEntry(EServerPackets.e6f10rsp, k6f10rsp, NUMFIELDS(k6f10rsp))

# epoch header for the GNSS T01 type 27 style packet
k6f20rsp = [
  IdSchemaField(0x6f), 
  SubIdSchemaField(0x20), 
  U16SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k6f20rspEntry = TSIPSchemaEntry(EServerPackets.e6f20rsp, k6f20rsp, NUMFIELDS(k6f20rsp))
k6f21rspPayloadData = U8SchemaField()

# These are the measurement blocks for the GNSS T01 type 27 style packet. Each packet contains up to 6 SVs with each of their submeas (l1, l2, etc.)
k6f21rsp = [
  IdSchemaField(0x6f), 
  SubIdSchemaField(0x21), 
  S16SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k6f21rspPayloadData)
]

k6f21rspEntry = TSIPSchemaEntry(EServerPackets.e6f21rsp, k6f21rsp, NUMFIELDS(k6f21rsp))

# Enables or disables the P/V Filter, Static Filter, and/or Altitude Filter.
k70cmd = [
  IdSchemaField(0x70), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k70cmdEntry = TSIPSchemaEntry(EClientPackets.e70cmd, k70cmd, NUMFIELDS(k70cmd))

# Reports the state of the P/V Filter, Static Filter, and/or Altitude Filter in response to Command Packet 0x70.
k70rsp = [
  IdSchemaField(0x70), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k70rspEntry = TSIPSchemaEntry(EServerPackets.e70rsp, k70rsp, NUMFIELDS(k70rsp))

# Requests the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode. The receiver acknowledges with Report Packet 0x78.
k77req = [
  IdSchemaField(0x77)
]

k77reqEntry = TSIPSchemaEntry(EClientPackets.e77req, k77req, NUMFIELDS(k77req))

# Sets the maximum time interval in seconds to propagate RTCM pseudorange corrections (PRC) if no corrections are received while the receiver is operating in DGPS mode.
k77cmd = [
  IdSchemaField(0x77), 
  U16SchemaField()
]

k77cmdEntry = TSIPSchemaEntry(EClientPackets.e77cmd, k77cmd, NUMFIELDS(k77cmd))

# Reports the amount of time in seconds that RTCM pseudorange corrections can be propagated in DGPS mode before they are no longer used.
k78rsp = [
  IdSchemaField(0x78), 
  U16SchemaField()
]

k78rspEntry = TSIPSchemaEntry(EServerPackets.e78rsp, k78rsp, NUMFIELDS(k78rsp))

# Requests the data reporting options for the NMEA output on the specified port. The receiver responds with Report Packet 0x7B 0x07.
k7a07req = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x07), 
  U8SchemaField()
]

k7a07reqEntry = TSIPSchemaEntry(EClientPackets.e7a07req, k7a07req, NUMFIELDS(k7a07req))

# Sets the data reporting options for the NMEA output on the specified port.
k7a07cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(2)
]

k7a07cmdEntry = TSIPSchemaEntry(EClientPackets.e7a07cmd, k7a07cmd, NUMFIELDS(k7a07cmd))

# Requests the data reporting options for NMEA on the specified receiver port. The receiver responds with Report Packet 0x7B 0x08.
k7a08req = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x08), 
  U8SchemaField()
]

k7a08reqEntry = TSIPSchemaEntry(EClientPackets.e7a08req, k7a08req, NUMFIELDS(k7a08req))

# Each Ag Receivers supports a varying number of serial ports that can transmit NMEA messages. This command configures various parameters of the NMEA for the specified serial port (if supported) on the receiver. This command supersedes other NMEA configuration commands and is designed to be used stand-alone (and not in conjunction with other NMEA Configuration command packets). The receiver acknowledges with 0x7B 0x08.
k7a08cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(40)
]

k7a08cmdEntry = TSIPSchemaEntry(EClientPackets.e7a08cmd, k7a08cmd, NUMFIELDS(k7a08cmd))

# Requests the NMEA message transmission interval or a combination of the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response.
k7a80req = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x80)
]

k7a80reqEntry = TSIPSchemaEntry(EClientPackets.e7a80req, k7a80req, NUMFIELDS(k7a80req))

# Sets the NMEA message transmission interval and the message mask for the current port. Report Packet 0x7B 0x80 is sent in response.
k7a80cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x80), 
  U8SchemaField(), 
  U32SchemaField()
]

k7a80cmdEntry = TSIPSchemaEntry(EClientPackets.e7a80cmd, k7a80cmd, NUMFIELDS(k7a80cmd))

# Requests the data reporting options for the NMEA GGA, GGL, VTG, and RMC message sentences for the current port. Report Packet 0x7B 0x86 is sent in response.
k7a86req = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x86), 
  U8SchemaField()
]

k7a86reqEntry = TSIPSchemaEntry(EClientPackets.e7a86req, k7a86req, NUMFIELDS(k7a86req))

# Sets the GGA options and precision for the current port.
k7a8600cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField()
]

k7a8600cmdEntry = TSIPSchemaEntry(EClientPackets.e7a8600cmd, k7a8600cmd, NUMFIELDS(k7a8600cmd))

# Sets the VTG options for the current port.
k7a8602cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x02), 
  U8SchemaField()
]

k7a8602cmdEntry = TSIPSchemaEntry(EClientPackets.e7a8602cmd, k7a8602cmd, NUMFIELDS(k7a8602cmd))

# Sets the VTG speed precision for the current port.
k7a8603cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x03), 
  U8SchemaField()
]

k7a8603cmdEntry = TSIPSchemaEntry(EClientPackets.e7a8603cmd, k7a8603cmd, NUMFIELDS(k7a8603cmd))

# Sets the RMC options and precision for the current port.
k7a8604cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k7a8604cmdEntry = TSIPSchemaEntry(EClientPackets.e7a8604cmd, k7a8604cmd, NUMFIELDS(k7a8604cmd))

# Sets the VTG Heading Precision for the current port.
k7a8605cmd = [
  IdSchemaField(0x7a), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x05), 
  U8SchemaField()
]

k7a8605cmdEntry = TSIPSchemaEntry(EClientPackets.e7a8605cmd, k7a8605cmd, NUMFIELDS(k7a8605cmd))

# Reports the data reporting options for the NMEA output on the specified port.
k7b07rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(2)
]

k7b07rspEntry = TSIPSchemaEntry(EServerPackets.e7b07rsp, k7b07rsp, NUMFIELDS(k7b07rsp))

# Acknowledges command to set NMEA Extended Port Configuration Options
k7b08ack = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k7b08ackEntry = TSIPSchemaEntry(EServerPackets.e7b08ack, k7b08ack, NUMFIELDS(k7b08ack))

# Reports the data reporting options for the NMEA extended output for a specified port.
k7b08rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(40)
]

k7b08rspEntry = TSIPSchemaEntry(EServerPackets.e7b08rsp, k7b08rsp, NUMFIELDS(k7b08rsp))

# Reports the NMEA message output interval and the message mask for the current port.
k7b80rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x80), 
  U8SchemaField(), 
  U32SchemaField()
]

k7b80rspEntry = TSIPSchemaEntry(EServerPackets.e7b80rsp, k7b80rsp, NUMFIELDS(k7b80rsp))

# Reports the GGA option settings for the current port.
k7b8600rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField()
]

k7b8600rspEntry = TSIPSchemaEntry(EServerPackets.e7b8600rsp, k7b8600rsp, NUMFIELDS(k7b8600rsp))

# Reports the VTG options for the current port.
k7b8602rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x02), 
  U8SchemaField()
]

k7b8602rspEntry = TSIPSchemaEntry(EServerPackets.e7b8602rsp, k7b8602rsp, NUMFIELDS(k7b8602rsp))

# Reports the VTG options for the current port.
k7b8603rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x03), 
  U8SchemaField()
]

k7b8603rspEntry = TSIPSchemaEntry(EServerPackets.e7b8603rsp, k7b8603rsp, NUMFIELDS(k7b8603rsp))

# Reports the VTG options for the current port.
k7b8605rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x05), 
  U8SchemaField()
]

k7b8605rspEntry = TSIPSchemaEntry(EServerPackets.e7b8605rsp, k7b8605rsp, NUMFIELDS(k7b8605rsp))

# Reports the RMC options and precision for the current port.
k7b860604rsp = [
  IdSchemaField(0x7b), 
  SubIdSchemaField(0x86), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k7b860604rspEntry = TSIPSchemaEntry(EServerPackets.e7b860604rsp, k7b860604rsp, NUMFIELDS(k7b860604rsp))

# Requests the rate for computing position fixes. Report Packet 0x7D 0x00 is sent in response.
k7c00req = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x00)
]

k7c00reqEntry = TSIPSchemaEntry(EClientPackets.e7c00req, k7c00req, NUMFIELDS(k7c00req))

# Sets the rate for computing position fixes.
k7c00cmd = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x00), 
  U8SchemaField()
]

k7c00cmdEntry = TSIPSchemaEntry(EClientPackets.e7c00cmd, k7c00cmd, NUMFIELDS(k7c00cmd))

# Requests the position fix rate I/O option bytes. Report Packet 0x7D 0x01 is sent in response.
k7c01req = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x01)
]

k7c01reqEntry = TSIPSchemaEntry(EClientPackets.e7c01req, k7c01req, NUMFIELDS(k7c01req))

# Sets the position fix rate I/O options bytes.
k7c01cmd = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField()
]

k7c01cmdEntry = TSIPSchemaEntry(EClientPackets.e7c01cmd, k7c01cmd, NUMFIELDS(k7c01cmd))

# Requests the position fix output interval and offset that are used to deterimne output rate in relation to fix rate. Report Packet 0x7D 0x02 is sent in response.
k7c02req = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x02)
]

k7c02reqEntry = TSIPSchemaEntry(EClientPackets.e7c02req, k7c02req, NUMFIELDS(k7c02req))

# Sets the position fix output interval and offset that are used to deterimne output rate in relation to fix rate.
k7c02cmd = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  U16SchemaField()
]

k7c02cmdEntry = TSIPSchemaEntry(EClientPackets.e7c02cmd, k7c02cmd, NUMFIELDS(k7c02cmd))

# Requests the message interval for the specified port and protocol.
k7c09req = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k7c09reqEntry = TSIPSchemaEntry(EClientPackets.e7c09req, k7c09req, NUMFIELDS(k7c09req))

# Sets the message interval for the specifed port and protocol.
k7c09cmd = [
  IdSchemaField(0x7c), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k7c09cmdEntry = TSIPSchemaEntry(EClientPackets.e7c09cmd, k7c09cmd, NUMFIELDS(k7c09cmd))

# Reports the number of position fixes per second.
k7d00rsp = [
  IdSchemaField(0x7d), 
  SubIdSchemaField(0x00), 
  U8SchemaField()
]

k7d00rspEntry = TSIPSchemaEntry(EServerPackets.e7d00rsp, k7d00rsp, NUMFIELDS(k7d00rsp))

# Reports the position fix rate I/O options bytes.
k7d01rsp = [
  IdSchemaField(0x7d), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField()
]

k7d01rspEntry = TSIPSchemaEntry(EServerPackets.e7d01rsp, k7d01rsp, NUMFIELDS(k7d01rsp))

# Reports the position fix output interval and offset that are used to deterimne output rate in relation to fix rate.
k7d02rsp = [
  IdSchemaField(0x7d), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  U16SchemaField()
]

k7d02rspEntry = TSIPSchemaEntry(EServerPackets.e7d02rsp, k7d02rsp, NUMFIELDS(k7d02rsp))

# Reports the message interval for the specifed port and protocol.
k7d09rsp = [
  IdSchemaField(0x7d), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k7d09rspEntry = TSIPSchemaEntry(EServerPackets.e7d09rsp, k7d09rsp, NUMFIELDS(k7d09rsp))

# Reports the differential position fix mode of the receiver.
k82rsp = [
  IdSchemaField(0x82), 
  U8SchemaField()
]

k82rspEntry = TSIPSchemaEntry(EServerPackets.e82rsp, k82rsp, NUMFIELDS(k82rsp))

# Reports the differential position fix mode of the receiver.
k82rspv1 = [
  IdSchemaField(0x82), 
  U8SchemaField(), 
  U8SchemaField(), 
  S16SchemaField()
]

k82rspv1Entry = TSIPSchemaEntry(EServerPackets.e82rspv1, k82rspv1, NUMFIELDS(k82rspv1))

# Reports the current GPS position fix in XYZ ECEF coordinate components. The I/O position option must be set to XYZ ECEF and double-precision must be selected for this packet to be generated. Note also that this packet assumes double-precision time of fix, since 5Hz and faster fix rates are now the norm.
k83rsp = [
  IdSchemaField(0x83), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

k83rspEntry = TSIPSchemaEntry(EServerPackets.e83rsp, k83rsp, NUMFIELDS(k83rsp))

# Overall Secure RTK Status
k890000rspOverallSystemStatus = [
  U8SchemaField(), 
  U16SchemaField()
]

k890000rspOverallSystemStatusGroup = GroupSchemaField(k890000rspOverallSystemStatus,NUMFIELDS(k890000rspOverallSystemStatus))

# Key Slot Information
k890000rspIndividualKeysStatusKeyStatus = [
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField()
]

k890000rspIndividualKeysStatusKeyStatusGroup = GroupSchemaField(k890000rspIndividualKeysStatusKeyStatus,NUMFIELDS(k890000rspIndividualKeysStatusKeyStatus))

# Status of SecureRTK and the 5 rover keys.
k890000rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k890000rspOverallSystemStatus,NUMFIELDS(k890000rspOverallSystemStatus)), 
  FixedArraySchemaField(k890000rspIndividualKeysStatusKeyStatusGroup, 5), 
  ChecksumSchemaField()
]

k890000rspEntry = TSIPSchemaEntry(EServerPackets.e890000rsp, k890000rsp, NUMFIELDS(k890000rsp))

# Rover Key Data
k890001rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  StringSchemaField(17), 
  StringSchemaField(16), 
  ChecksumSchemaField()
]

k890001rspEntry = TSIPSchemaEntry(EServerPackets.e890001rsp, k890001rsp, NUMFIELDS(k890001rsp))

# Set Rover Key Data Response
k890002rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  ChecksumSchemaField()
]

k890002rspEntry = TSIPSchemaEntry(EServerPackets.e890002rsp, k890002rsp, NUMFIELDS(k890002rsp))

# Delete Rover Key Data Response
k890003rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k890003rspEntry = TSIPSchemaEntry(EServerPackets.e890003rsp, k890003rsp, NUMFIELDS(k890003rsp))
k893308rspStationIdsStationId = U8SchemaField()
k893308rspLinkQualityLinkQuality = U8SchemaField()
k893308rspLastCMRTimeLastCMRTime = U32SchemaField()

# Provides CMR reception statistics for all the available base stations
k893308rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x33), 
  SubIdSchemaField(0x08), 
  UnusedSchemaField(1), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k893308rspStationIdsStationId, 4, 0,0, 6), 
  ArraySchemaField(k893308rspLinkQualityLinkQuality, 4, 0,0, 6), 
  ArraySchemaField(k893308rspLastCMRTimeLastCMRTime, 4, 0,0, 6), 
  ChecksumSchemaField()
]

k893308rspEntry = TSIPSchemaEntry(EServerPackets.e893308rsp, k893308rsp, NUMFIELDS(k893308rsp))

# Sets the RTK configuration
k8940rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x40), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(30), 
  ChecksumSchemaField()
]

k8940rspEntry = TSIPSchemaEntry(EServerPackets.e8940rsp, k8940rsp, NUMFIELDS(k8940rsp))

# Provides RTK Solution Info
k8941rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x41), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8941rspEntry = TSIPSchemaEntry(EServerPackets.e8941rsp, k8941rsp, NUMFIELDS(k8941rsp))

# Provides RTK Aux Settings
k8950rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x50), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8950rspEntry = TSIPSchemaEntry(EServerPackets.e8950rsp, k8950rsp, NUMFIELDS(k8950rsp))

# Provides RTK Aux Status
k8951rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x51), 
  U8SchemaField(), 
  S16SchemaField(), 
  S16SchemaField(), 
  UnusedSchemaField(22), 
  ChecksumSchemaField()
]

k8951rspEntry = TSIPSchemaEntry(EServerPackets.e8951rsp, k8951rsp, NUMFIELDS(k8951rsp))

# 
k8960rspBaseVector = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

k8960rspBaseVectorGroup = GroupSchemaField(k8960rspBaseVector,NUMFIELDS(k8960rspBaseVector))

# Provides RTK Base Info
k8960rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x60), 
  U16SchemaField(), 
  StringSchemaField(9), 
  U32SchemaField(), 
  DBLSchemaField(), 
  GroupSchemaField(k8960rspBaseVector,NUMFIELDS(k8960rspBaseVector)), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8960rspEntry = TSIPSchemaEntry(EServerPackets.e8960rsp, k8960rsp, NUMFIELDS(k8960rsp))

# 
k8961rspBasePosition = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

k8961rspBasePositionGroup = GroupSchemaField(k8961rspBasePosition,NUMFIELDS(k8961rspBasePosition))

# Provides CMR Info
k8961rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x61), 
  U16SchemaField(), 
  U32SchemaField(), 
  GroupSchemaField(k8961rspBasePosition,NUMFIELDS(k8961rspBasePosition)), 
  UnusedSchemaField(10), 
  ChecksumSchemaField()
]

k8961rspEntry = TSIPSchemaEntry(EServerPackets.e8961rsp, k8961rsp, NUMFIELDS(k8961rsp))

# Provides information on the overall disturbance level of the ionosphere
k8962rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x62), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(65), 
  ChecksumSchemaField()
]

k8962rspEntry = TSIPSchemaEntry(EServerPackets.e8962rsp, k8962rsp, NUMFIELDS(k8962rsp))

# Provides status of managed RTK radio (if any)
k897000rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k897000rspEntry = TSIPSchemaEntry(EServerPackets.e897000rsp, k897000rsp, NUMFIELDS(k897000rsp))

# Provides identity of managed RTK radio (if any)
k897001rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x01), 
  StringSchemaField(21), 
  StringSchemaField(21), 
  StringSchemaField(21), 
  StringSchemaField(31), 
  ChecksumSchemaField()
]

k897001rspEntry = TSIPSchemaEntry(EServerPackets.e897001rsp, k897001rsp, NUMFIELDS(k897001rsp))
k897002rspSupportedModesMode = U8SchemaField()
k897002rspSupportedCountriesCountryCode = U8SchemaField()

# Provides capabilities of managed RTK radio (if any)
k897002rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k897002rspSupportedModesMode, 4, 0,0, 64), 
  S8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k897002rspSupportedCountriesCountryCode, 7, 0,0, 10), 
  ChecksumSchemaField()
]

k897002rspEntry = TSIPSchemaEntry(EServerPackets.e897002rsp, k897002rsp, NUMFIELDS(k897002rsp))

# Provides country info for managed RTK radio (if any)
k897003rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x03), 
  S8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897003rspEntry = TSIPSchemaEntry(EServerPackets.e897003rsp, k897003rsp, NUMFIELDS(k897003rsp))

# Provides config specific to 900MHz RTK radio (if any)
k897004rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897004rspEntry = TSIPSchemaEntry(EServerPackets.e897004rsp, k897004rsp, NUMFIELDS(k897004rsp))

# Describes allowed freq range and spacing
k897005rspBanding = [
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField()
]

k897005rspBandingGroup = GroupSchemaField(k897005rspBanding,NUMFIELDS(k897005rspBanding))

# Info for a single channel
k897005rspChannelArrayChannelInfo = [
  U8SchemaField(), 
  U32SchemaField()
]

k897005rspChannelArrayChannelInfoGroup = GroupSchemaField(k897005rspChannelArrayChannelInfo,NUMFIELDS(k897005rspChannelArrayChannelInfo))

# Provides config specific to 450MHz RTK radio (if any)
k897005rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k897005rspChannelArrayChannelInfoGroup, 4, 0,0, 20), 
  U8SchemaField(), 
  GroupSchemaField(k897005rspBanding,NUMFIELDS(k897005rspBanding)), 
  ChecksumSchemaField()
]

k897005rspEntry = TSIPSchemaEntry(EServerPackets.e897005rsp, k897005rsp, NUMFIELDS(k897005rsp))

# Acknowledges command to set country code
k897006ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897006ackEntry = TSIPSchemaEntry(EServerPackets.e897006ack, k897006ack, NUMFIELDS(k897006ack))

# Acknowledges command to set 900MHz network ID
k897007ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897007ackEntry = TSIPSchemaEntry(EServerPackets.e897007ack, k897007ack, NUMFIELDS(k897007ack))

# Acknowledges command to set 450MHz channel ID
k897008ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897008ackEntry = TSIPSchemaEntry(EServerPackets.e897008ack, k897008ack, NUMFIELDS(k897008ack))

# Acknowledges command to set 450MHz channel frequency
k897009ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897009ackEntry = TSIPSchemaEntry(EServerPackets.e897009ack, k897009ack, NUMFIELDS(k897009ack))

# Acknowledges command to set 450MHz mode
k89700aack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x0a), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k89700aackEntry = TSIPSchemaEntry(EServerPackets.e89700aack, k89700aack, NUMFIELDS(k89700aack))

# Acknowledges command to restart RTK radio
k89700back = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x0b), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k89700backEntry = TSIPSchemaEntry(EServerPackets.e89700back, k89700back, NUMFIELDS(k89700back))

# Acknowledges command to set RTK radio channel bandwidth
k89700cack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x0c), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k89700cackEntry = TSIPSchemaEntry(EServerPackets.e89700cack, k89700cack, NUMFIELDS(k89700cack))

# Provides RTK radio channel bandwidth info
k89700drsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x70), 
  SubIdSchemaField(0x0d), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k89700drspEntry = TSIPSchemaEntry(EServerPackets.e89700drsp, k89700drsp, NUMFIELDS(k89700drsp))

# For the designated source, retrieve the X, Y, and Z offset values in Fallback RTX. Request packet is 0x69 0x71 0x0. No longer supported, do not use. Packet will always return manual source, and an invalid offset with all zeros
k897100rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k897100rspEntry = TSIPSchemaEntry(EServerPackets.e897100rsp, k897100rsp, NUMFIELDS(k897100rsp))

# Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Result will always be failure.
k897100ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897100ackEntry = TSIPSchemaEntry(EServerPackets.e897100ack, k897100ack, NUMFIELDS(k897100ack))

# Reports Fallback RTX mode. Request packet is 0x69 0x71 0x02. No longer supported, do not use. It will always return UnknownMode and manual status.
k897101rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  ChecksumSchemaField()
]

k897101rspEntry = TSIPSchemaEntry(EServerPackets.e897101rsp, k897101rsp, NUMFIELDS(k897101rsp))

# Acknowledge the command 0x69 0x71 0x01. No longer supported, do not use. Will always return failure.
k897101ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897101ackEntry = TSIPSchemaEntry(EServerPackets.e897101ack, k897101ack, NUMFIELDS(k897101ack))

# Reports xFill Premium Status. Request packet is 0x69 0x71 0x03.
k897103rsp = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  S16SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  UnusedSchemaField(14), 
  ChecksumSchemaField()
]

k897103rspEntry = TSIPSchemaEntry(EServerPackets.e897103rsp, k897103rsp, NUMFIELDS(k897103rsp))

# Acknowledges command to set xFill Premium Configuration. Ack is sent in response to 0x69 0x71 0x03
k897103ack = [
  IdSchemaField(0x89), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k897103ackEntry = TSIPSchemaEntry(EServerPackets.e897103ack, k897103ack, NUMFIELDS(k897103ack))

# Indicates current state of automatic position sigma reporting
k8b00rsp = [
  IdSchemaField(0x8b), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8b00rspEntry = TSIPSchemaEntry(EServerPackets.e8b00rsp, k8b00rsp, NUMFIELDS(k8b00rsp))

# Single position sigma (error) information report
k8b02rsp = [
  IdSchemaField(0x8b), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(6), 
  ChecksumSchemaField()
]

k8b02rspEntry = TSIPSchemaEntry(EServerPackets.e8b02rsp, k8b02rsp, NUMFIELDS(k8b02rsp))

# Requests a report containing the current receiver configuration parameter settings and software version number. Report Packet 0x8F 0x7B is sent in response.
k8e7breq = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x7b), 
  ChecksumSchemaField()
]

k8e7breqEntry = TSIPSchemaEntry(EClientPackets.e8e7breq, k8e7breq, NUMFIELDS(k8e7breq))

# 
k8e7ccmdConfigBlockV3FixedDefBoilerPlate = [
  StringSchemaField(22), 
  StringSchemaField(10), 
  StringSchemaField(17), 
  StringSchemaField(6), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField()
]

k8e7ccmdConfigBlockV3FixedDefBoilerPlateGroup = GroupSchemaField(k8e7ccmdConfigBlockV3FixedDefBoilerPlate,NUMFIELDS(k8e7ccmdConfigBlockV3FixedDefBoilerPlate))

# 
k8e7ccmdConfigBlockV3FixedDefRxDef = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8e7ccmdConfigBlockV3FixedDefRxDefGroup = GroupSchemaField(k8e7ccmdConfigBlockV3FixedDefRxDef,NUMFIELDS(k8e7ccmdConfigBlockV3FixedDefRxDef))

# 
k8e7ccmdConfigBlockV3FixedDef = [
  GroupSchemaField(k8e7ccmdConfigBlockV3FixedDefBoilerPlate,NUMFIELDS(k8e7ccmdConfigBlockV3FixedDefBoilerPlate)), 
  GroupSchemaField(k8e7ccmdConfigBlockV3FixedDefRxDef,NUMFIELDS(k8e7ccmdConfigBlockV3FixedDefRxDef)), 
  UnusedSchemaField(27)
]

k8e7ccmdConfigBlockV3FixedDefGroup = GroupSchemaField(k8e7ccmdConfigBlockV3FixedDef,NUMFIELDS(k8e7ccmdConfigBlockV3FixedDef))

# 
k8e7ccmdConfigBlockV3UserDefPortConfigPortConfig = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8e7ccmdConfigBlockV3UserDefPortConfigPortConfigGroup = GroupSchemaField(k8e7ccmdConfigBlockV3UserDefPortConfigPortConfig,NUMFIELDS(k8e7ccmdConfigBlockV3UserDefPortConfigPortConfig))

# 
k8e7ccmdConfigBlockV3UserDef = [
  FixedArraySchemaField(k8e7ccmdConfigBlockV3UserDefPortConfigPortConfigGroup, 3), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(29)
]

k8e7ccmdConfigBlockV3UserDefGroup = GroupSchemaField(k8e7ccmdConfigBlockV3UserDef,NUMFIELDS(k8e7ccmdConfigBlockV3UserDef))

# 
k8e7ccmdConfigBlockV3 = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k8e7ccmdConfigBlockV3FixedDef,NUMFIELDS(k8e7ccmdConfigBlockV3FixedDef)), 
  GroupSchemaField(k8e7ccmdConfigBlockV3UserDef,NUMFIELDS(k8e7ccmdConfigBlockV3UserDef)), 
  U16SchemaField(), 
  U16SchemaField()
]

k8e7ccmdConfigBlockV3Group = GroupSchemaField(k8e7ccmdConfigBlockV3,NUMFIELDS(k8e7ccmdConfigBlockV3))

# Used to set the receiver configuration parameters stored in battery-backed RAM (Random Access Memory). Report Packet 0x8F 0x7C is sent in response.
k8e7ccmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x7c), 
  U8SchemaField(), 
  StringSchemaField(20), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k8e7ccmdConfigBlockV3,NUMFIELDS(k8e7ccmdConfigBlockV3)), 
  ChecksumSchemaField()
]

k8e7ccmdEntry = TSIPSchemaEntry(EClientPackets.e8e7ccmd, k8e7ccmd, NUMFIELDS(k8e7ccmd))

# Request DGPS Receiver ROM Configuration Block Report
k8e7freq = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x7f), 
  ChecksumSchemaField()
]

k8e7freqEntry = TSIPSchemaEntry(EClientPackets.e8e7freq, k8e7freq, NUMFIELDS(k8e7freq))

# requests the current status of the DGPS service provider. Report packet 0x8f 0x80 is sent in response.
k8e80req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x80), 
  U8SchemaField(), 
  U16SchemaField(), 
  ChecksumSchemaField()
]

k8e80reqEntry = TSIPSchemaEntry(EClientPackets.e8e80req, k8e80req, NUMFIELDS(k8e80req))

# Get spot station info
k8e81req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x81), 
  ChecksumSchemaField()
]

k8e81reqEntry = TSIPSchemaEntry(EClientPackets.e8e81req, k8e81req, NUMFIELDS(k8e81req))

# Starts or stops the satellite FFT (Fast Fourier Transform) diagnostics and sets the FFT diagnostic options. Acknowledged with Report Packet 0x8F 0x84.
k8e84cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x84), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8e84cmdEntry = TSIPSchemaEntry(EClientPackets.e8e84cmd, k8e84cmd, NUMFIELDS(k8e84cmd))

# requests the tracking status for the source of DGPS corrections (either beacon or satellite). Report packet 0x8f 0x85 is sent in response.
k8e85req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x85), 
  ChecksumSchemaField()
]

k8e85reqEntry = TSIPSchemaEntry(EClientPackets.e8e85req, k8e85req, NUMFIELDS(k8e85req))

# Requests current 
k8e88req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x88), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8e88reqEntry = TSIPSchemaEntry(EClientPackets.e8e88req, k8e88req, NUMFIELDS(k8e88req))

# Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response.
k8e88cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x88), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8e88cmdEntry = TSIPSchemaEntry(EClientPackets.e8e88cmd, k8e88cmd, NUMFIELDS(k8e88cmd))

# Requests current DGPS source and related settings. Report packet 0x8F 0x89 is sent in response.
k8e89req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x89), 
  ChecksumSchemaField()
]

k8e89reqEntry = TSIPSchemaEntry(EClientPackets.e8e89req, k8e89req, NUMFIELDS(k8e89req))

# Controls DGPS source and related settings. Acknowledgement packet 0x8F 0x89 is sent in response.
k8e89cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x89), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8e89cmdEntry = TSIPSchemaEntry(EClientPackets.e8e89cmd, k8e89cmd, NUMFIELDS(k8e89cmd))

# Requests service provider activation information. Report Packet 0x8F 0x8B is sent in response.
k8e8breq = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8b), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8e8breqEntry = TSIPSchemaEntry(EClientPackets.e8e8breq, k8e8breq, NUMFIELDS(k8e8breq))

# The key press command packet simulates sending a key press to the display. Whenever the end user application wants to move around the remote display (i.e. in response to a key press on its own terminal, touch screen, etc.), this packet is sent to the receiver to indicate that the receiver should process the specified key press action. The receiver will acknowledge the key press command by sending Report Packet 0x8F 0x8C.
k8e8c00cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8e8c00cmdEntry = TSIPSchemaEntry(EClientPackets.e8e8c00cmd, k8e8c00cmd, NUMFIELDS(k8e8c00cmd))

# Requests the remote display screen contents once. The receiver will respond by sending Report Packet 0x8F 0x8C 0x01. If automatic reporting of the screen contents is configured, this packet must be sent once per minute to maintain that configuration (version 1.40 and later). This provides a timeout mechanism if the receiver is disconnected from the user terminal so the automatic reporting does not continue indefinitely if not needed.
k8e8c01req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8e8c01reqEntry = TSIPSchemaEntry(EClientPackets.e8e8c01req, k8e8c01req, NUMFIELDS(k8e8c01req))

# Requests the remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x03
k8e8c03req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k8e8c03reqEntry = TSIPSchemaEntry(EClientPackets.e8e8c03req, k8e8c03req, NUMFIELDS(k8e8c03req))

# Sets the remote display configuration
k8e8c03cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8e8c03cmdEntry = TSIPSchemaEntry(EClientPackets.e8e8c03cmd, k8e8c03cmd, NUMFIELDS(k8e8c03cmd))

# Requests the extended remote display configuration. The receiver will respond by sending Report Packet 0x8F 0x8C 0x04
k8e8c04req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x04), 
  ChecksumSchemaField()
]

k8e8c04reqEntry = TSIPSchemaEntry(EClientPackets.e8e8c04req, k8e8c04req, NUMFIELDS(k8e8c04req))

# Sets the extended remote display configuration
k8e8c04cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8e8c04cmdEntry = TSIPSchemaEntry(EClientPackets.e8e8c04cmd, k8e8c04cmd, NUMFIELDS(k8e8c04cmd))

# Indicates that one of the event lines into the remote display has changed state.
k8e8c05cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8e8c05cmdEntry = TSIPSchemaEntry(EClientPackets.e8e8c05cmd, k8e8c05cmd, NUMFIELDS(k8e8c05cmd))

# Requests a report containing the receiver's Machine ID and Product ID used to uniquely identify the receiver architecture. Report Packet 0x8F 0x8F is sent in response.
k8e8freq = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x8f), 
  ChecksumSchemaField()
]

k8e8freqEntry = TSIPSchemaEntry(EClientPackets.e8e8freq, k8e8freq, NUMFIELDS(k8e8freq))

# Request the Guidance Configuration Information
k8e91req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x91), 
  ChecksumSchemaField()
]

k8e91reqEntry = TSIPSchemaEntry(EClientPackets.e8e91req, k8e91req, NUMFIELDS(k8e91req))

# Set the guidance configuration information
k8e91cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x91), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8e91cmdEntry = TSIPSchemaEntry(EClientPackets.e8e91cmd, k8e91cmd, NUMFIELDS(k8e91cmd))
k8e931500reqPathChar = CHARSchemaField()

# Requests a list of files found in the specified directory. A File Transfer Listing Reponse packet is sent for each file in the directory (empty directory will produce no response).
k8e931500req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x00), 
  EndTerminatedArraySchemaField(k8e931500reqPathChar), 
  ChecksumSchemaField()
]

k8e931500reqEntry = TSIPSchemaEntry(EClientPackets.e8e931500req, k8e931500req, NUMFIELDS(k8e931500req))
k8e93150101reqFilenameChar = CHARSchemaField()

# Requests that file be opened for reading. File Transfer Get - Open Response is sent with info needed for the transfer.
k8e93150101req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  EndTerminatedArraySchemaField(k8e93150101reqFilenameChar), 
  ChecksumSchemaField()
]

k8e93150101reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150101req, k8e93150101req, NUMFIELDS(k8e93150101req))

# Requests to read block of data from open file. If successful File Transfer Get - Data Block Response is sent with the data, otherwise File Transfer Get - Close Response or File Transfer Get - Error Response is sent.
k8e93150102req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8e93150102reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150102req, k8e93150102req, NUMFIELDS(k8e93150102req))

# Requests to close previously opened file. If successful File Transfer Get - Close Response is sent, otherwise File Transfer Get - Error Response is sent.
k8e93150103req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x03), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k8e93150103reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150103req, k8e93150103req, NUMFIELDS(k8e93150103req))
k8e93150104reqFilenameChar = CHARSchemaField()

# Requests an Hash of the specified file in the fusion file system. The receiver will respond with an Hash response packet (8f930104...)
k8e93150104req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  EndTerminatedArraySchemaField(k8e93150104reqFilenameChar), 
  ChecksumSchemaField()
]

k8e93150104reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150104req, k8e93150104req, NUMFIELDS(k8e93150104req))
k8e93150201reqFilenameChar = CHARSchemaField()

# Requests that file be opened for writing. File Transfer Put - Open Response is sent with info needed for the transfer.
k8e93150201req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  EndTerminatedArraySchemaField(k8e93150201reqFilenameChar), 
  ChecksumSchemaField()
]

k8e93150201reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150201req, k8e93150201req, NUMFIELDS(k8e93150201req))
k8e93150202reqDataBlockData = U8SchemaField()

# Requests to write block of data to open file. If successful File Transfer Put - Data Block Response is sent with the data, otherwise File Transfer Put - Close Response or File Transfer Put - Error Response is sent.
k8e93150202req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k8e93150202reqDataBlockData), 
  ChecksumSchemaField()
]

k8e93150202reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150202req, k8e93150202req, NUMFIELDS(k8e93150202req))

# Requests to close previously opened file. If successful File Transfer Put - Close Response is sent, otherwise File Transfer Put - Error Response is sent.
k8e93150203req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x03), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k8e93150203reqEntry = TSIPSchemaEntry(EClientPackets.e8e93150203req, k8e93150203req, NUMFIELDS(k8e93150203req))
k8e931503reqFilenameChar = CHARSchemaField()

# Requests delete of specified file. File Transfer Delete Response is sent to indicate status.
k8e931503req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x03), 
  EndTerminatedArraySchemaField(k8e931503reqFilenameChar), 
  ChecksumSchemaField()
]

k8e931503reqEntry = TSIPSchemaEntry(EClientPackets.e8e931503req, k8e931503req, NUMFIELDS(k8e931503req))

# Requests a report containing differential correction information. Report Packet 0x8F 0x9A is sent in response.
k8e9areq = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9a), 
  ChecksumSchemaField()
]

k8e9areqEntry = TSIPSchemaEntry(EClientPackets.e8e9areq, k8e9areq, NUMFIELDS(k8e9areq))

# Requests a report containing DGPS source priorities. Report Packet 0x8F 0x9E is sent in response.
k8e9ereq = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9e), 
  ChecksumSchemaField()
]

k8e9ereqEntry = TSIPSchemaEntry(EClientPackets.e8e9ereq, k8e9ereq, NUMFIELDS(k8e9ereq))
k8e9ecmdSourceInfoArrayGroup = GroupSchemaField(k8ef9eDGPSSourceInfo,NUMFIELDS(k8ef9eDGPSSourceInfo))

# Sets the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be set. The resulting receiver configuration is returned in the response packet 0x8F 0x9E.
k8e9ecmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9e), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ArraySchemaField(k8e9ecmdSourceInfoArrayGroup, 2, 0,0, 4), 
  ChecksumSchemaField()
]

k8e9ecmdEntry = TSIPSchemaEntry(EClientPackets.e8e9ecmd, k8e9ecmd, NUMFIELDS(k8e9ecmd))

# Request information on the CAN bus configuration
k8e9f00req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8e9f00reqEntry = TSIPSchemaEntry(EClientPackets.e8e9f00req, k8e9f00req, NUMFIELDS(k8e9f00req))

# CAN Channel Config
k8e9f00cmdChannelCfgCANChannelCfg = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4)
]

k8e9f00cmdChannelCfgCANChannelCfgGroup = GroupSchemaField(k8e9f00cmdChannelCfgCANChannelCfg,NUMFIELDS(k8e9f00cmdChannelCfgCANChannelCfg))

# Sets the CAN bus configuration for specified channels
k8e9f00cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(2), 
  U8SchemaField(), 
  ArraySchemaField(k8e9f00cmdChannelCfgCANChannelCfgGroup, 4, 0,0, 16), 
  ChecksumSchemaField()
]

k8e9f00cmdEntry = TSIPSchemaEntry(EClientPackets.e8e9f00cmd, k8e9f00cmd, NUMFIELDS(k8e9f00cmd))

# Request information on the CAN bus status
k8e9f01req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8e9f01reqEntry = TSIPSchemaEntry(EClientPackets.e8e9f01req, k8e9f01req, NUMFIELDS(k8e9f01req))

# Request current J1939 message configuration for channel
k8e9f02req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8e9f02reqEntry = TSIPSchemaEntry(EClientPackets.e8e9f02req, k8e9f02req, NUMFIELDS(k8e9f02req))

# J1939 message configuration
k8e9f02cmdMsgCfgArrayMsgCfg = [
  U8SchemaField(), 
  U16SchemaField()
]

k8e9f02cmdMsgCfgArrayMsgCfgGroup = GroupSchemaField(k8e9f02cmdMsgCfgArrayMsgCfg,NUMFIELDS(k8e9f02cmdMsgCfgArrayMsgCfg))

# Configures one or more J1939 messages for channel
k8e9f02cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8e9f02cmdMsgCfgArrayMsgCfgGroup, 4, 0,0, 10), 
  ChecksumSchemaField()
]

k8e9f02cmdEntry = TSIPSchemaEntry(EClientPackets.e8e9f02cmd, k8e9f02cmd, NUMFIELDS(k8e9f02cmd))

# Request current NMEA2K message configuration for channel
k8e9f03req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8e9f03reqEntry = TSIPSchemaEntry(EClientPackets.e8e9f03req, k8e9f03req, NUMFIELDS(k8e9f03req))

# NMEA2K message configuration
k8e9f03cmdMsgCfgArrayMsgCfg = [
  U8SchemaField(), 
  U16SchemaField()
]

k8e9f03cmdMsgCfgArrayMsgCfgGroup = GroupSchemaField(k8e9f03cmdMsgCfgArrayMsgCfg,NUMFIELDS(k8e9f03cmdMsgCfgArrayMsgCfg))

# Configures one or more NMEA2K messages for channel
k8e9f03cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8e9f03cmdMsgCfgArrayMsgCfgGroup, 4, 0,0, 25), 
  ChecksumSchemaField()
]

k8e9f03cmdEntry = TSIPSchemaEntry(EClientPackets.e8e9f03cmd, k8e9f03cmd, NUMFIELDS(k8e9f03cmd))

# Request current ISO message configuration for channel
k8e9f04req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8e9f04reqEntry = TSIPSchemaEntry(EClientPackets.e8e9f04req, k8e9f04req, NUMFIELDS(k8e9f04req))

# ISO message configuration
k8e9f04cmdMsgCfgArrayMsgCfg = [
  U8SchemaField(), 
  U16SchemaField()
]

k8e9f04cmdMsgCfgArrayMsgCfgGroup = GroupSchemaField(k8e9f04cmdMsgCfgArrayMsgCfg,NUMFIELDS(k8e9f04cmdMsgCfgArrayMsgCfg))

# Configures one or more ISO messages for channel
k8e9f04cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8e9f04cmdMsgCfgArrayMsgCfgGroup, 4, 0,0, 10), 
  ChecksumSchemaField()
]

k8e9f04cmdEntry = TSIPSchemaEntry(EClientPackets.e8e9f04cmd, k8e9f04cmd, NUMFIELDS(k8e9f04cmd))

# Request an option upgrade via a supplied password. The receiver respond by sending Response Packet 0x8F 0xA0.
k8ea0cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa0), 
  StringSchemaField(22), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea0cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea0cmd, k8ea0cmd, NUMFIELDS(k8ea0cmd))
k8ea1cmdPacketDataData = U8SchemaField()

# This is an alias to 0x8e 0xa1.
k8ea1cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa1), 
  EndTerminatedArraySchemaField(k8ea1cmdPacketDataData), 
  ChecksumSchemaField()
]

k8ea1cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea1cmd, k8ea1cmd, NUMFIELDS(k8ea1cmd))

# Requests a Position Solution Status 0x8F 0xA2 report.
k8ea2req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa2), 
  ChecksumSchemaField()
]

k8ea2reqEntry = TSIPSchemaEntry(EClientPackets.e8ea2req, k8ea2req, NUMFIELDS(k8ea2req))

# Requests specific information about the Omnistar XP/HP process
k8ea3req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa3), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea3reqEntry = TSIPSchemaEntry(EClientPackets.e8ea3req, k8ea3req, NUMFIELDS(k8ea3req))

# Sets Auto-Seed information held by the receiver. If the Auto-Seed functionality is turned on in the receiver, these values will be used at startup when the receiver is rebooted.
k8ea304cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8ea304cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea304cmd, k8ea304cmd, NUMFIELDS(k8ea304cmd))

# Sets various control parameters of the Omnistar XP/HP processor
k8ea305cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x05), 
  U16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8ea305cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea305cmd, k8ea305cmd, NUMFIELDS(k8ea305cmd))

# Sets up the debugging output of the XP/HP processor
k8ea306cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(18), 
  ChecksumSchemaField()
]

k8ea306cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea306cmd, k8ea306cmd, NUMFIELDS(k8ea306cmd))

# Resets the XP/HP engine
k8ea307cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x07), 
  ChecksumSchemaField()
]

k8ea307cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea307cmd, k8ea307cmd, NUMFIELDS(k8ea307cmd))

# Requests Filter configuration. Report Packet 0x8F 0xA4 is sent in response.
k8ea4req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa4), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea4reqEntry = TSIPSchemaEntry(EClientPackets.e8ea4req, k8ea4req, NUMFIELDS(k8ea4req))

# Sets Quadratic Bias Filter configuration. Report Packet 0x8F 0xA4 0x05 is sent in response.
k8ea405cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa4), 
  SubIdSchemaField(0x05), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8ea405cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea405cmd, k8ea405cmd, NUMFIELDS(k8ea405cmd))

# Sets Kalman Filter configuration. Report Packet 0x8F 0xA4 0x06 is sent in response.
k8ea406cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa4), 
  SubIdSchemaField(0x06), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea406cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea406cmd, k8ea406cmd, NUMFIELDS(k8ea406cmd))

# Command to enable or disable Field Level Smoothing. Response (ACK) Packet is 0x8f 0xa4 0x07
k8ea407cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa4), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea407cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea407cmd, k8ea407cmd, NUMFIELDS(k8ea407cmd))

# Requests and sets the current SBAS settings. The command and report packets can each contain a variable number of SBAS SV entries.
k8ea500req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea500reqEntry = TSIPSchemaEntry(EClientPackets.e8ea500req, k8ea500req, NUMFIELDS(k8ea500req))

# Information for a particular SBAS satellite
k8ea500cmdSBASInfoArraySBASInfo = [
  U8SchemaField(), 
  U8SchemaField()
]

k8ea500cmdSBASInfoArraySBASInfoGroup = GroupSchemaField(k8ea500cmdSBASInfoArraySBASInfo,NUMFIELDS(k8ea500cmdSBASInfoArraySBASInfo))

# Sets the current SBAS settings. This packet can contain a variable number of SBAS SV entries. SV entries not listed in the command packet will not be updated.
k8ea500cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ArraySchemaField(k8ea500cmdSBASInfoArraySBASInfoGroup, 3, 0,0, 39), 
  ChecksumSchemaField()
]

k8ea500cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea500cmd, k8ea500cmd, NUMFIELDS(k8ea500cmd))

# Requests the current 'Use SBAS+' settings. Response packet is 0x8F 0xA5 0x01
k8ea501req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8ea501reqEntry = TSIPSchemaEntry(EClientPackets.e8ea501req, k8ea501req, NUMFIELDS(k8ea501req))

# Sets the 'Use SBAS+' configuration settings. SBAS+ mode uses as much SBAS correction information as possible and as many satellites as possible to improve yield and accuracy when positioning in SBAS mode. Response packet is 0x8F 0xA5 0x01
k8ea501cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea501cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea501cmd, k8ea501cmd, NUMFIELDS(k8ea501cmd))

# Resets the receiver's SBAS constellation tracking scheme to the defaults.
k8ea502cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(39), 
  ChecksumSchemaField()
]

k8ea502cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea502cmd, k8ea502cmd, NUMFIELDS(k8ea502cmd))

# Sets the state of a Output pin.
k8ea601cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(12), 
  ChecksumSchemaField()
]

k8ea601cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea601cmd, k8ea601cmd, NUMFIELDS(k8ea601cmd))

# Request the state of an external input pin.
k8ea602req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8ea602reqEntry = TSIPSchemaEntry(EClientPackets.e8ea602req, k8ea602req, NUMFIELDS(k8ea602req))

# Requests the manufacturing information of the unit.
k8ea608req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x08), 
  UnusedSchemaField(14), 
  ChecksumSchemaField()
]

k8ea608reqEntry = TSIPSchemaEntry(EClientPackets.e8ea608req, k8ea608req, NUMFIELDS(k8ea608req))

# Requests Omnistar Id from the unit.
k8ea617req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x17), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea617reqEntry = TSIPSchemaEntry(EClientPackets.e8ea617req, k8ea617req, NUMFIELDS(k8ea617req))

# Requests MAC addresses from the unit.
k8ea622req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x22), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea622reqEntry = TSIPSchemaEntry(EClientPackets.e8ea622req, k8ea622req, NUMFIELDS(k8ea622req))

# Requests the alternate unique ID from the unit.
k8ea623req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x23), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea623reqEntry = TSIPSchemaEntry(EClientPackets.e8ea623req, k8ea623req, NUMFIELDS(k8ea623req))

# Requests unit's extended manufacturing information.
k8ea624req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x24), 
  UnusedSchemaField(14), 
  ChecksumSchemaField()
]

k8ea624reqEntry = TSIPSchemaEntry(EClientPackets.e8ea624req, k8ea624req, NUMFIELDS(k8ea624req))

# Sets unit's extended manufacturing information.
k8ea625cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x25), 
  StringSchemaField(16), 
  StringSchemaField(20), 
  UnusedSchemaField(60), 
  ChecksumSchemaField()
]

k8ea625cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea625cmd, k8ea625cmd, NUMFIELDS(k8ea625cmd))

# Requests unit's product information.
k8ea626req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x26), 
  UnusedSchemaField(14), 
  ChecksumSchemaField()
]

k8ea626reqEntry = TSIPSchemaEntry(EClientPackets.e8ea626req, k8ea626req, NUMFIELDS(k8ea626req))

# Sets unit's product information.
k8ea627cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x27), 
  StringSchemaField(20), 
  StringSchemaField(18), 
  StringSchemaField(6), 
  UnusedSchemaField(60), 
  ChecksumSchemaField()
]

k8ea627cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea627cmd, k8ea627cmd, NUMFIELDS(k8ea627cmd))

# Put the receiver into manufacturing test mode.
k8ea628cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x28), 
  StringSchemaField(32), 
  ChecksumSchemaField()
]

k8ea628cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea628cmd, k8ea628cmd, NUMFIELDS(k8ea628cmd))

# Request the firmware signature at the given offset.
k8ea629req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x29), 
  U32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea629reqEntry = TSIPSchemaEntry(EClientPackets.e8ea629req, k8ea629req, NUMFIELDS(k8ea629req))

# Requests the peak FFT frequency from the RF spectrum analyzer for GNSS bands. Intended for factory test use only.
k8ea630req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x30), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea630reqEntry = TSIPSchemaEntry(EClientPackets.e8ea630req, k8ea630req, NUMFIELDS(k8ea630req))

# Requests metadata about the MSS tracking, including the peak value of the FFT, min/max signal level and gain in db/% 
k8ea631req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x31), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea631reqEntry = TSIPSchemaEntry(EClientPackets.e8ea631req, k8ea631req, NUMFIELDS(k8ea631req))

# Requests a register read operation to a specific polaris device
k8ea632req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x32), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea632reqEntry = TSIPSchemaEntry(EClientPackets.e8ea632req, k8ea632req, NUMFIELDS(k8ea632req))

# Writes a value to a specific polaris device's register
k8ea632cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x32), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea632cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea632cmd, k8ea632cmd, NUMFIELDS(k8ea632cmd))

# Requests a ADC read of the RSSI on a specific polaris device
k8ea633req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x33), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea633reqEntry = TSIPSchemaEntry(EClientPackets.e8ea633req, k8ea633req, NUMFIELDS(k8ea633req))

# Requests the receiver to perform the Polaris full AGC test. The receiver will acknowledge the request, and then send the 0x8f 0xa6 0x34 response when the test completes.
k8ea634req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x34), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea634reqEntry = TSIPSchemaEntry(EClientPackets.e8ea634req, k8ea634req, NUMFIELDS(k8ea634req))

# Enables the PLT (Production Line Test) Mode for WiFi testing.
k8ea640cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x40), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea640cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea640cmd, k8ea640cmd, NUMFIELDS(k8ea640cmd))

# Disables the PLT (Production Line Test) Mode for WiFi testing.
k8ea641cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x41), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea641cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea641cmd, k8ea641cmd, NUMFIELDS(k8ea641cmd))

# Configures the device to operate in a specific WiFi band and channel.
k8ea642cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x42), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea642cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea642cmd, k8ea642cmd, NUMFIELDS(k8ea642cmd))

# Sets the transmission power of the WL18xx device.
k8ea643cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x43), 
  U8SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  S8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea643cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea643cmd, k8ea643cmd, NUMFIELDS(k8ea643cmd))
k8ea644cmdSourceMACSourceMACHex = U8SchemaField()
k8ea644cmdDestMACDestMACHex = U8SchemaField()

# Enables TX test using the start_tx command.
k8ea644cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x44), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FixedArraySchemaField(k8ea644cmdSourceMACSourceMACHex, 6), 
  FixedArraySchemaField(k8ea644cmdDestMACDestMACHex, 6), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea644cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea644cmd, k8ea644cmd, NUMFIELDS(k8ea644cmd))

# Disables TX test using the stop_tx command.
k8ea645cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x45), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea645cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea645cmd, k8ea645cmd, NUMFIELDS(k8ea645cmd))
k8ea646cmdSourceMACSourceMACHex = U8SchemaField()
k8ea646cmdDestMACDestMACHex = U8SchemaField()

# Starts calculations of RX statistics.
k8ea646cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x46), 
  U8SchemaField(), 
  FixedArraySchemaField(k8ea646cmdSourceMACSourceMACHex, 6), 
  FixedArraySchemaField(k8ea646cmdDestMACDestMACHex, 6), 
  ChecksumSchemaField()
]

k8ea646cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea646cmd, k8ea646cmd, NUMFIELDS(k8ea646cmd))

# Requests the RX statistics.
k8ea647req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x47), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea647reqEntry = TSIPSchemaEntry(EClientPackets.e8ea647req, k8ea647req, NUMFIELDS(k8ea647req))

# Stops calculations of the RX statistics.
k8ea648cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x48), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea648cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea648cmd, k8ea648cmd, NUMFIELDS(k8ea648cmd))

# Sets up default automatic reports for a selected antenna. This will output the position used internally by the receiver.
k8ea70000cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea70000cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea70000cmd, k8ea70000cmd, NUMFIELDS(k8ea70000cmd))
k8ea70001cmdPositionEngArrayPositionEng = U8SchemaField()

# Sets up automatic reports for a selected antenna based on the position engine used to generate the solution. Only positions of from the specified engines will be output
k8ea70001cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8ea70001cmdPositionEngArrayPositionEng, 7, 0,0, 12), 
  ChecksumSchemaField()
]

k8ea70001cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea70001cmd, k8ea70001cmd, NUMFIELDS(k8ea70001cmd))
k8ea70002cmdPositionTypeArrayPositionType = U8SchemaField()

# Sets up automatic reports for a selected antenna based on the position type produced. Only positions of those types will be output.
k8ea70002cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8ea70002cmdPositionTypeArrayPositionType, 7, 0,0, 12), 
  ChecksumSchemaField()
]

k8ea70002cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea70002cmd, k8ea70002cmd, NUMFIELDS(k8ea70002cmd))

# Sets up automatic reports for a selected antenna based on the position flags assigned. Only positions with the given flags will be output.
k8ea70003cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea70003cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea70003cmd, k8ea70003cmd, NUMFIELDS(k8ea70003cmd))

# Requests the last position from for a specified antenna. If the last position wasn't valid, a no position is output instead
k8ea70100req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea70100reqEntry = TSIPSchemaEntry(EClientPackets.e8ea70100req, k8ea70100req, NUMFIELDS(k8ea70100req))

# Requests the last position from the given engine on the specified antenna. If the last position wasn't valid, a no position is output instead
k8ea70101req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea70101reqEntry = TSIPSchemaEntry(EClientPackets.e8ea70101req, k8ea70101req, NUMFIELDS(k8ea70101req))

# Requests the last position of the given type from the specified antenna. If the last position wasn't valid, a no position is output instead
k8ea70102req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea70102reqEntry = TSIPSchemaEntry(EClientPackets.e8ea70102req, k8ea70102req, NUMFIELDS(k8ea70102req))

# Requests the last position matching the provided flags from the specified antenna. If the last position wasn't valid, a no position is output instead
k8ea70103req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea70103reqEntry = TSIPSchemaEntry(EClientPackets.e8ea70103req, k8ea70103req, NUMFIELDS(k8ea70103req))

# Request the VRS Radio Status
k8ea800req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea800reqEntry = TSIPSchemaEntry(EClientPackets.e8ea800req, k8ea800req, NUMFIELDS(k8ea800req))
k8ea801cmdIPAddressChar = CHARSchemaField()
k8ea801cmdMountPointChar = CHARSchemaField()
k8ea801cmdUserNameChar = CHARSchemaField()
k8ea801cmdPasswordChar = CHARSchemaField()

# Set the NTRIP parameters for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
k8ea801cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x01), 
  U16SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea801cmdIPAddressChar, 4, 0,0, 60), 
  U8SchemaField(), 
  ArraySchemaField(k8ea801cmdMountPointChar, 6, 0,0, 60), 
  U8SchemaField(), 
  ArraySchemaField(k8ea801cmdUserNameChar, 8, 0,0, 60), 
  U8SchemaField(), 
  ArraySchemaField(k8ea801cmdPasswordChar, 10, 0,0, 60), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  ChecksumSchemaField()
]

k8ea801cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea801cmd, k8ea801cmd, NUMFIELDS(k8ea801cmd))

# Request the NTRIP parameters for the VRS Radio
k8ea801req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x01), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea801reqEntry = TSIPSchemaEntry(EClientPackets.e8ea801req, k8ea801req, NUMFIELDS(k8ea801req))
k8ea802cmdUserNameChar = CHARSchemaField()

# Set the GPRS Username for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
k8ea802cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x02), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8ea802cmdUserNameChar, 4, 0,0, 60), 
  ChecksumSchemaField()
]

k8ea802cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea802cmd, k8ea802cmd, NUMFIELDS(k8ea802cmd))

# Request the GPRS Username for the VRS Radio
k8ea802req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x02), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8ea802reqEntry = TSIPSchemaEntry(EClientPackets.e8ea802req, k8ea802req, NUMFIELDS(k8ea802req))
k8ea803cmdPasswordChar = CHARSchemaField()

# Set the GPRS Password for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
k8ea803cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x03), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8ea803cmdPasswordChar, 4, 0,0, 60), 
  ChecksumSchemaField()
]

k8ea803cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea803cmd, k8ea803cmd, NUMFIELDS(k8ea803cmd))

# Request the GPRS Password for the VRS Radio
k8ea803req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x03), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8ea803reqEntry = TSIPSchemaEntry(EClientPackets.e8ea803req, k8ea803req, NUMFIELDS(k8ea803req))
k8ea804cmdInitStringChar = CHARSchemaField()

# Set the GPRS InitString for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
k8ea804cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x04), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8ea804cmdInitStringChar, 4, 0,0, 60), 
  ChecksumSchemaField()
]

k8ea804cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea804cmd, k8ea804cmd, NUMFIELDS(k8ea804cmd))

# Request the GPRS InitString for the VRS Radio
k8ea804req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x04), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8ea804reqEntry = TSIPSchemaEntry(EClientPackets.e8ea804req, k8ea804req, NUMFIELDS(k8ea804req))
k8ea805cmdCPINChar = CHARSchemaField()

# Set the GPRS CPIN for the VRS Radio. All strings are not null terminated, and the stringLength value is the number of actual characters
k8ea805cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x05), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8ea805cmdCPINChar, 4, 0,0, 60), 
  ChecksumSchemaField()
]

k8ea805cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea805cmd, k8ea805cmd, NUMFIELDS(k8ea805cmd))

# Configure the VRS Radio
k8ea806cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(6), 
  ChecksumSchemaField()
]

k8ea806cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea806cmd, k8ea806cmd, NUMFIELDS(k8ea806cmd))

# Request the VRS Radio Config
k8ea806req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x06), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8ea806reqEntry = TSIPSchemaEntry(EClientPackets.e8ea806req, k8ea806req, NUMFIELDS(k8ea806req))

# Requests the various firmware and hardware version information
k8ea900req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8ea900reqEntry = TSIPSchemaEntry(EClientPackets.e8ea900req, k8ea900req, NUMFIELDS(k8ea900req))
k8ea90100cmdFilenameChar = CHARSchemaField()

# Requests that the receiver begin upgrading with the provided file. The upgrading performed by the receiver will depend on the hardware, but it is expected to begin upgrading if possible. The receiver will respond with information regarding whether the request was carried out.
k8ea90100cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea90100cmdFilenameChar, 5, 0,0, 250), 
  ChecksumSchemaField()
]

k8ea90100cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90100cmd, k8ea90100cmd, NUMFIELDS(k8ea90100cmd))
k8ea90101cmdprefixChar = CHARSchemaField()

# Allows the user to start and stop logging, and provide the location to log to.
k8ea90101cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea90101cmdprefixChar, 5, 0,0, 240), 
  ChecksumSchemaField()
]

k8ea90101cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90101cmd, k8ea90101cmd, NUMFIELDS(k8ea90101cmd))

# Requests the current status of the logging control
k8ea90101req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8ea90101reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90101req, k8ea90101req, NUMFIELDS(k8ea90101req))
k8ea90102cmdFilenameChar = CHARSchemaField()

# Requests a particular log be dumped to specified path.
k8ea90102cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea90102cmdFilenameChar, 5, 0,0, 250), 
  ChecksumSchemaField()
]

k8ea90102cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90102cmd, k8ea90102cmd, NUMFIELDS(k8ea90102cmd))
k8ea90103cmdDataData = U8SchemaField()

# Sends a variable length data packet (ping), that will be returned by the receiver (pong). This allows a type of serial communication test to occur.
k8ea90103cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ArraySchemaField(k8ea90103cmdDataData, 4, 0,0, 250), 
  ChecksumSchemaField()
]

k8ea90103cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90103cmd, k8ea90103cmd, NUMFIELDS(k8ea90103cmd))

# Request the IP Address and port number for the VRS Daemon
k8ea90104req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea90104reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90104req, k8ea90104req, NUMFIELDS(k8ea90104req))

# Set the IP Address and port number for the VRS Daemon
k8ea90104cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  StringSchemaField(20), 
  U16SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea90104cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90104cmd, k8ea90104cmd, NUMFIELDS(k8ea90104cmd))
k8ea90105cmdFilenameChar = CHARSchemaField()

# Requests that the receiver install licenses with a given file
k8ea90105cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  ArraySchemaField(k8ea90105cmdFilenameChar, 4, 0,0, 250), 
  ChecksumSchemaField()
]

k8ea90105cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90105cmd, k8ea90105cmd, NUMFIELDS(k8ea90105cmd))

# Request the current state of the receiver automatic reboot capability
k8ea90106req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x06), 
  ChecksumSchemaField()
]

k8ea90106reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90106req, k8ea90106req, NUMFIELDS(k8ea90106req))

# Control the frequency at which the receiver will automatically reboot
k8ea90106cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90106cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90106cmd, k8ea90106cmd, NUMFIELDS(k8ea90106cmd))

# Request the IP Address and port number for the CLAAS RTK NET modem
k8ea90107req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x07), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea90107reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90107req, k8ea90107req, NUMFIELDS(k8ea90107req))

# Set the IP Address and port number for the CLAAS RTK NET modem
k8ea90107cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x07), 
  StringSchemaField(20), 
  U16SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea90107cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90107cmd, k8ea90107cmd, NUMFIELDS(k8ea90107cmd))

# Request the TNFS Host Address
k8ea90108req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x08), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea90108reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90108req, k8ea90108req, NUMFIELDS(k8ea90108req))

# Set the IP Address for the TNFS Host Address
k8ea90108cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x08), 
  StringSchemaField(20), 
  UnusedSchemaField(7), 
  ChecksumSchemaField()
]

k8ea90108cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90108cmd, k8ea90108cmd, NUMFIELDS(k8ea90108cmd))

# Requests the upgrade/downgrade version floor of the receiver
k8ea90130req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x30), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea90130reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90130req, k8ea90130req, NUMFIELDS(k8ea90130req))

# Checks if an upgrade/downgrade to the given version is allowed
k8ea90131req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x31), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea90131reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90131req, k8ea90131req, NUMFIELDS(k8ea90131req))

# Request the mux settings of the digital output of a particular port.
k8ea90200req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90200reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90200req, k8ea90200req, NUMFIELDS(k8ea90200req))

# Sets the mux behaviour of the digital output for a particular port.
k8ea90200cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea90200cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90200cmd, k8ea90200cmd, NUMFIELDS(k8ea90200cmd))

# Request the settings of the digital input of a particular port.
k8ea90201req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90201reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90201req, k8ea90201req, NUMFIELDS(k8ea90201req))

# Sets the behaviour of the digital input for a particular port.
k8ea90201cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90201cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90201cmd, k8ea90201cmd, NUMFIELDS(k8ea90201cmd))

# Request the settings of the Pollux FPGA GPO.
k8ea90202req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8ea90202reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90202req, k8ea90202req, NUMFIELDS(k8ea90202req))

# Sets the behaviour of the GPO for the Pollux FPGA.
k8ea90202cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90202cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90202cmd, k8ea90202cmd, NUMFIELDS(k8ea90202cmd))

# Requests information about connected Antennas.
k8ea90300req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea90300reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90300req, k8ea90300req, NUMFIELDS(k8ea90300req))

# Commands the power state of an antenna. The command is acknowledged with the Antenna info packet.
k8ea90301cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90301cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90301cmd, k8ea90301cmd, NUMFIELDS(k8ea90301cmd))

# Requests information on the Radar setup
k8ea90400req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x04), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea90400reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90400req, k8ea90400req, NUMFIELDS(k8ea90400req))

# Configures the Radar setup
k8ea90400cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x04), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea90400cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90400cmd, k8ea90400cmd, NUMFIELDS(k8ea90400cmd))
k8ea905cmdLogMessageChar = CHARSchemaField()

# Place a string command into the receiver program log. Responds with a simple ack.
k8ea905cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x05), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea905cmdLogMessageChar, 5, 0,0, 240), 
  ChecksumSchemaField()
]

k8ea905cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea905cmd, k8ea905cmd, NUMFIELDS(k8ea905cmd))

# Requests the reading of the given ADC Channel
k8ea90600req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90600reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90600req, k8ea90600req, NUMFIELDS(k8ea90600req))

# Requests the settings of the Module-A Digital Pin Muxing.
k8ea90700req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90700reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90700req, k8ea90700req, NUMFIELDS(k8ea90700req))

# Sets the Module-A Digital Pin Muxing.
k8ea90700cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea90700cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90700cmd, k8ea90700cmd, NUMFIELDS(k8ea90700cmd))

# Requests the settings of the pwmon control point.
k8ea90701req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90701reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90701req, k8ea90701req, NUMFIELDS(k8ea90701req))

# Sets the Module-A power monitor options.
k8ea90701cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90701cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90701cmd, k8ea90701cmd, NUMFIELDS(k8ea90701cmd))

# Requests the settings Video Input Mux.
k8ea90703req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90703reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90703req, k8ea90703req, NUMFIELDS(k8ea90703req))

# Sets the Module-A Video Mux options.
k8ea90703cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea90703cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90703cmd, k8ea90703cmd, NUMFIELDS(k8ea90703cmd))

# Requests Module-A auto shutdown timer settings.
k8ea90704req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x04), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea90704reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90704req, k8ea90704req, NUMFIELDS(k8ea90704req))

# Sets Module-A auto shutdown timer delay.
k8ea90704cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea90704cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90704cmd, k8ea90704cmd, NUMFIELDS(k8ea90704cmd))

# Gets the network interface configuration info.
k8ea90705req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90705reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90705req, k8ea90705req, NUMFIELDS(k8ea90705req))

# Sets the Module A's network interface to a specific setting.
k8ea90705cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea90705cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90705cmd, k8ea90705cmd, NUMFIELDS(k8ea90705cmd))

# Requests Module-A hardware configuration
k8ea90706req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x06), 
  ChecksumSchemaField()
]

k8ea90706reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90706req, k8ea90706req, NUMFIELDS(k8ea90706req))

# Requests the socket uart device details configured for Port-D on the Module-A
k8ea90707req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x07), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea90707reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90707req, k8ea90707req, NUMFIELDS(k8ea90707req))

# Sets the socket uart device to be used for Port-D on the Module-A.  The device must be a TBIP device that supports the socket-uart protocol.
k8ea90707cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x07), 
  U32SchemaField(), 
  StringSchemaField(32), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea90707cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90707cmd, k8ea90707cmd, NUMFIELDS(k8ea90707cmd))

# Retrieves the current counters statistics for a port on the switch
k8ea90708req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea90708reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90708req, k8ea90708req, NUMFIELDS(k8ea90708req))

# Requests the current state of RTK correction rebroadcasting
k8ea90800req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x08), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea90800reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90800req, k8ea90800req, NUMFIELDS(k8ea90800req))

# Sets the state of RTK correction rebroadcasting
k8ea90800cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x08), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8ea90800cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea90800cmd, k8ea90800cmd, NUMFIELDS(k8ea90800cmd))

# Request the status of the Receiver LEDs (if supported). This request invokes a response TSIP packet: 0x8F 0xA9 0x08 0x00.
k8ea909req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea909reqEntry = TSIPSchemaEntry(EClientPackets.e8ea909req, k8ea909req, NUMFIELDS(k8ea909req))

# Sets the behaviour of Receiver LEDs. This command is acknowledged with TSIP Packet 0x8F 0xA9 0xA8 0x00.
k8ea909cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8ea909cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea909cmd, k8ea909cmd, NUMFIELDS(k8ea909cmd))

# Requests all the enabled features in the Feature Manager
k8ea90a00req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x0a), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90a00reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90a00req, k8ea90a00req, NUMFIELDS(k8ea90a00req))

# Requests the license status from the Feature Manager
k8ea90a01req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x0a), 
  SubIdSchemaField(0x01), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea90a01reqEntry = TSIPSchemaEntry(EClientPackets.e8ea90a01req, k8ea90a01req, NUMFIELDS(k8ea90a01req))

# Requests the status of receiver unlocks
k8ea910req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x10), 
  ChecksumSchemaField()
]

k8ea910reqEntry = TSIPSchemaEntry(EClientPackets.e8ea910req, k8ea910req, NUMFIELDS(k8ea910req))

# Product Information Request
k8ea911req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x11), 
  ChecksumSchemaField()
]

k8ea911reqEntry = TSIPSchemaEntry(EClientPackets.e8ea911req, k8ea911req, NUMFIELDS(k8ea911req))

# Boot Count Information Request
k8ea912req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x12), 
  ChecksumSchemaField()
]

k8ea912reqEntry = TSIPSchemaEntry(EClientPackets.e8ea912req, k8ea912req, NUMFIELDS(k8ea912req))

# Geoidal Separation Information Request
k8ea913req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x13), 
  ChecksumSchemaField()
]

k8ea913reqEntry = TSIPSchemaEntry(EClientPackets.e8ea913req, k8ea913req, NUMFIELDS(k8ea913req))
k8ea91500cmdclientFileIdbyte = U8SchemaField()

# Initiates transfer operation (get or put) for the given file type.
k8ea91500cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea91500cmdclientFileIdbyte, 7, 0,0, 128), 
  ChecksumSchemaField()
]

k8ea91500cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91500cmd, k8ea91500cmd, NUMFIELDS(k8ea91500cmd))

# Request to get a block from a system file
k8ea91501cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k8ea91501cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91501cmd, k8ea91501cmd, NUMFIELDS(k8ea91501cmd))
k8ea91502cmdblockDatabyte = U8SchemaField()

# Request to put block to a system file
k8ea91502cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8ea91502cmdblockDatabyte, 6, 0,0, 256), 
  ChecksumSchemaField()
]

k8ea91502cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91502cmd, k8ea91502cmd, NUMFIELDS(k8ea91502cmd))

# Closes the open stream identified by fileId
k8ea91503cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x03), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k8ea91503cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91503cmd, k8ea91503cmd, NUMFIELDS(k8ea91503cmd))

# Requests deletion of the specified system file
k8ea91504cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea91504cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91504cmd, k8ea91504cmd, NUMFIELDS(k8ea91504cmd))

# Get the mode of the GP uart mux
k8ea9160000req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea9160000reqEntry = TSIPSchemaEntry(EClientPackets.e8ea9160000req, k8ea9160000req, NUMFIELDS(k8ea9160000req))

# Change internal routing of the General Purpose UART port in Fusion
k8ea9160000cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea9160000cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea9160000cmd, k8ea9160000cmd, NUMFIELDS(k8ea9160000cmd))

# Get the mux mode of the TX UART port in Fusion
k8ea9160001req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8ea9160001reqEntry = TSIPSchemaEntry(EClientPackets.e8ea9160001req, k8ea9160001req, NUMFIELDS(k8ea9160001req))

# Change internal routing of the TX UART port in Fusion
k8ea9160001cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea9160001cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea9160001cmd, k8ea9160001cmd, NUMFIELDS(k8ea9160001cmd))

# Request the mux mode of the Radio port uart in Fusion
k8ea9160002req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8ea9160002reqEntry = TSIPSchemaEntry(EClientPackets.e8ea9160002req, k8ea9160002req, NUMFIELDS(k8ea9160002req))

# Change internal routing of the Radio port uart in Fusion
k8ea9160002cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea9160002cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea9160002cmd, k8ea9160002cmd, NUMFIELDS(k8ea9160002cmd))

# Request the mode of the internal AP virtual uart in Fusion
k8ea9160100req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea9160100reqEntry = TSIPSchemaEntry(EClientPackets.e8ea9160100req, k8ea9160100req, NUMFIELDS(k8ea9160100req))

# Sets the mode of the internal AP virtual uart in Fusion
k8ea9160100cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8ea9160100cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea9160100cmd, k8ea9160100cmd, NUMFIELDS(k8ea9160100cmd))

# Request Bluetooth state (enabled or disabled)
k8ea91602req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8ea91602reqEntry = TSIPSchemaEntry(EClientPackets.e8ea91602req, k8ea91602req, NUMFIELDS(k8ea91602req))

# Enable/disable Bluetooth
k8ea91602cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ea91602cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91602cmd, k8ea91602cmd, NUMFIELDS(k8ea91602cmd))

# Clear All Licenses installed via user entry and factory installation
k8ea91603cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k8ea91603cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91603cmd, k8ea91603cmd, NUMFIELDS(k8ea91603cmd))

# Remove / Restore Manufacturing Licenses
k8ea91604cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8ea91604cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91604cmd, k8ea91604cmd, NUMFIELDS(k8ea91604cmd))
k8ea91605cmdFragmentChar = CHARSchemaField()

# Remove Licenses By Fragment command
k8ea91605cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  ArraySchemaField(k8ea91605cmdFragmentChar, 4, 0,0, 200), 
  ChecksumSchemaField()
]

k8ea91605cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91605cmd, k8ea91605cmd, NUMFIELDS(k8ea91605cmd))

# Requests UDS diagnostic status
k8ea91606req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x06), 
  ChecksumSchemaField()
]

k8ea91606reqEntry = TSIPSchemaEntry(EClientPackets.e8ea91606req, k8ea91606req, NUMFIELDS(k8ea91606req))

# Request the IMU settings. Expects response of 0x8f 0xa9 0x17 0x00.
k8ea91700req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ea91700reqEntry = TSIPSchemaEntry(EClientPackets.e8ea91700req, k8ea91700req, NUMFIELDS(k8ea91700req))

# Send IMU settings to configure pitch and roll corrected positions. Expects response of 0x8f 0xa9 0x17 0x00.
k8ea91700cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(12), 
  ChecksumSchemaField()
]

k8ea91700cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91700cmd, k8ea91700cmd, NUMFIELDS(k8ea91700cmd))

# Enable Fusion position correction based on IMU values.
k8ea91701cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8ea91701cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91701cmd, k8ea91701cmd, NUMFIELDS(k8ea91701cmd))

# Query if IMU-Corrected positions and streaming are enabled.
k8ea91701req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8ea91701reqEntry = TSIPSchemaEntry(EClientPackets.e8ea91701req, k8ea91701req, NUMFIELDS(k8ea91701req))

# Get the position details in case streaming is off; IMU-corrected if enabled.
k8ea91702req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8ea91702reqEntry = TSIPSchemaEntry(EClientPackets.e8ea91702req, k8ea91702req, NUMFIELDS(k8ea91702req))

# Request the IMU settings Block 2. Expects response of 0x8f 0xa9 0x17 0x03.
k8ea91703req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k8ea91703reqEntry = TSIPSchemaEntry(EClientPackets.e8ea91703req, k8ea91703req, NUMFIELDS(k8ea91703req))

# Send IMU settings to configure extra settings related to the Fusion IMU supported features. Expects response of 0x8f 0xa9 0x17 0x03.
k8ea91703cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(80), 
  ChecksumSchemaField()
]

k8ea91703cmdEntry = TSIPSchemaEntry(EClientPackets.e8ea91703cmd, k8ea91703cmd, NUMFIELDS(k8ea91703cmd))

# Requests the cryptochip configuration CRC value
k8ea918req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x18), 
  ChecksumSchemaField()
]

k8ea918reqEntry = TSIPSchemaEntry(EClientPackets.e8ea918req, k8ea918req, NUMFIELDS(k8ea918req))

# New 27 character passcode upgrade request packet
k8ea9a5req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0xa5), 
  StringSchemaField(65), 
  ChecksumSchemaField()
]

k8ea9a5reqEntry = TSIPSchemaEntry(EClientPackets.e8ea9a5req, k8ea9a5req, NUMFIELDS(k8ea9a5req))

# Requests type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response.
k8eaa00req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xaa), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eaa00reqEntry = TSIPSchemaEntry(EClientPackets.e8eaa00req, k8eaa00req, NUMFIELDS(k8eaa00req))

# Command to set type of specified antenna. Packet 0x8f 0xaa 0x00 is sent in response.
k8eaa00cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xaa), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8eaa00cmdEntry = TSIPSchemaEntry(EClientPackets.e8eaa00cmd, k8eaa00cmd, NUMFIELDS(k8eaa00cmd))

# Checks the RTX subscription on the receiver and shows which connections are available
k8eab00req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8eab00reqEntry = TSIPSchemaEntry(EClientPackets.e8eab00req, k8eab00req, NUMFIELDS(k8eab00req))

# Requests the Centerpoint RTX fast Network Info from the receiver. Packet 0x8f 0xab 0x01 is sent in response.
k8eab01req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8eab01reqEntry = TSIPSchemaEntry(EClientPackets.e8eab01req, k8eab01req, NUMFIELDS(k8eab01req))

# Cancels RTX std FastRestart. The command is acknowledged with packet 0x8f 0xab 0x02.
k8eab02cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8eab02cmdEntry = TSIPSchemaEntry(EClientPackets.e8eab02cmd, k8eab02cmd, NUMFIELDS(k8eab02cmd))

# Requests CenterPoint RTX status. The command is acknowledged with packet 0x8f 0xab 0x03.
k8eab03req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k8eab03reqEntry = TSIPSchemaEntry(EClientPackets.e8eab03req, k8eab03req, NUMFIELDS(k8eab03req))

# Allows TSIP to confirm whether vehicle has moved post reboot on FastRestart enabled Ag receivers. The command is acknowledged with packet 0x8f 0xab 0x04.
k8eab04cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eab04cmdEntry = TSIPSchemaEntry(EClientPackets.e8eab04cmd, k8eab04cmd, NUMFIELDS(k8eab04cmd))

# Custom RTX offset
k8eab05cmdRTXOffset = [
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k8eab05cmdRTXOffsetGroup = GroupSchemaField(k8eab05cmdRTXOffset,NUMFIELDS(k8eab05cmdRTXOffset))

# Allows the RTX output settings to be selected using TSIP. The command is acknowledged with packet 0x8f 0xab 0x05.
k8eab05cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  GroupSchemaField(k8eab05cmdRTXOffset,NUMFIELDS(k8eab05cmdRTXOffset)), 
  UnusedSchemaField(51), 
  ChecksumSchemaField()
]

k8eab05cmdEntry = TSIPSchemaEntry(EClientPackets.e8eab05cmd, k8eab05cmd, NUMFIELDS(k8eab05cmd))

# Requests the current RTX output settings using TSIP. The request is acknowledged with packet 0x8f 0xab 0x05.
k8eab05req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x05), 
  ChecksumSchemaField()
]

k8eab05reqEntry = TSIPSchemaEntry(EClientPackets.e8eab05req, k8eab05req, NUMFIELDS(k8eab05req))

# If RTK is unlocked, function automatically determines what Centerpoint RTX (FAST/STD) to be used based on what Centerpoint license is available. If RTK and/or RTX unlock(s) are not found, convergence is autoamtically set to SBAS. The request is acknowledged with packet 0x8f 0xab 0x06.
k8eab06cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x06), 
  ChecksumSchemaField()
]

k8eab06cmdEntry = TSIPSchemaEntry(EClientPackets.e8eab06cmd, k8eab06cmd, NUMFIELDS(k8eab06cmd))

# Request the current configuration and mode of the MSS Mode Switch
k8eab07req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x07), 
  ChecksumSchemaField()
]

k8eab07reqEntry = TSIPSchemaEntry(EClientPackets.e8eab07req, k8eab07req, NUMFIELDS(k8eab07req))

# Control the MSS Mode Switch
k8eab07cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eab07cmdEntry = TSIPSchemaEntry(EClientPackets.e8eab07cmd, k8eab07cmd, NUMFIELDS(k8eab07cmd))

# Requests the realtime RTK/RTX Custom Offsets using TSIP. The request is acknowledged with packet 0x8f 0xab 0x08.
k8eab08req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eab08reqEntry = TSIPSchemaEntry(EClientPackets.e8eab08req, k8eab08req, NUMFIELDS(k8eab08req))

# Sets the configuration for genral parameters of the boom height system
k8eac0000cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  S8SchemaField(), 
  S8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8eac0000cmdEntry = TSIPSchemaEntry(EClientPackets.e8eac0000cmd, k8eac0000cmd, NUMFIELDS(k8eac0000cmd))

# 
k8eac0001cmdsensorsArraysensors = [
  StringSchemaField(11), 
  U8SchemaField(), 
  S8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

k8eac0001cmdsensorsArraysensorsGroup = GroupSchemaField(k8eac0001cmdsensorsArraysensors,NUMFIELDS(k8eac0001cmdsensorsArraysensors))

# Sets the configuration for sensor parameters of the boom height system
k8eac0001cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8eac0001cmdsensorsArraysensorsGroup, 5, 0,0, 5), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8eac0001cmdEntry = TSIPSchemaEntry(EClientPackets.e8eac0001cmd, k8eac0001cmd, NUMFIELDS(k8eac0001cmd))

# 
k8eac0002cmdactuatorsArrayactuators = [
  StringSchemaField(11), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField()
]

k8eac0002cmdactuatorsArrayactuatorsGroup = GroupSchemaField(k8eac0002cmdactuatorsArrayactuators,NUMFIELDS(k8eac0002cmdactuatorsArrayactuators))

# Sets the configuration for actuator parameters of the boom height system
k8eac0002cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8eac0002cmdactuatorsArrayactuatorsGroup, 5, 0,0, 3), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8eac0002cmdEntry = TSIPSchemaEntry(EClientPackets.e8eac0002cmd, k8eac0002cmd, NUMFIELDS(k8eac0002cmd))

# Requests the configuration for genral parameters
k8eac0100req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8eac0100reqEntry = TSIPSchemaEntry(EClientPackets.e8eac0100req, k8eac0100req, NUMFIELDS(k8eac0100req))

# Requests the configuration for sensor parameters
k8eac0101req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8eac0101reqEntry = TSIPSchemaEntry(EClientPackets.e8eac0101req, k8eac0101req, NUMFIELDS(k8eac0101req))

# Requests the configuration for actuator parameters
k8eac0102req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8eac0102reqEntry = TSIPSchemaEntry(EClientPackets.e8eac0102req, k8eac0102req, NUMFIELDS(k8eac0102req))

# Commands to initiate actuator calibration modes
k8eac02cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eac02cmdEntry = TSIPSchemaEntry(EClientPackets.e8eac02cmd, k8eac02cmd, NUMFIELDS(k8eac02cmd))

# Request for actuator status
k8eac03req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eac03reqEntry = TSIPSchemaEntry(EClientPackets.e8eac03req, k8eac03req, NUMFIELDS(k8eac03req))

# 
k8eac04cmdManualZoneArrayZoneMan = [
  U8SchemaField(), 
  FLTSchemaField()
]

k8eac04cmdManualZoneArrayZoneManGroup = GroupSchemaField(k8eac04cmdManualZoneArrayZoneMan,NUMFIELDS(k8eac04cmdManualZoneArrayZoneMan))

# Sets the Boom Height control state system including various parameters. This is typically sent periodically at 5Hz
k8eac04cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  FLTSchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8eac04cmdManualZoneArrayZoneManGroup, 8, 0,0, 3), 
  ChecksumSchemaField()
]

k8eac04cmdEntry = TSIPSchemaEntry(EClientPackets.e8eac04cmd, k8eac04cmd, NUMFIELDS(k8eac04cmd))

# Commands to commit system actions
k8eac05cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eac05cmdEntry = TSIPSchemaEntry(EClientPackets.e8eac05cmd, k8eac05cmd, NUMFIELDS(k8eac05cmd))

# Requests alert statuses
k8eac06req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eac06reqEntry = TSIPSchemaEntry(EClientPackets.e8eac06req, k8eac06req, NUMFIELDS(k8eac06req))

# Request list of attached devices
k8eac07req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8eac07reqEntry = TSIPSchemaEntry(EClientPackets.e8eac07req, k8eac07req, NUMFIELDS(k8eac07req))

# Retrieve Centerpoint or Rangepoint RTX Passcodes on the receiver if a subscription is available. Response Packet: 0x8f 0xad 0x00
k8ead00req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8ead00reqEntry = TSIPSchemaEntry(EClientPackets.e8ead00req, k8ead00req, NUMFIELDS(k8ead00req))

# Command to erase/clear Centerpoint/Rangepoint RTX Passcodes installed in the receiver. ACK Packet is 0x8f 0xad 0x01
k8ead01cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ead01cmdEntry = TSIPSchemaEntry(EClientPackets.e8ead01cmd, k8ead01cmd, NUMFIELDS(k8ead01cmd))

# Retrieve RTX Position Allowed Status on the receiver. Response Packet: 0x8f 0xad 0x02
k8ead02req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8ead02reqEntry = TSIPSchemaEntry(EClientPackets.e8ead02req, k8ead02req, NUMFIELDS(k8ead02req))

# Command to set or clear the RTX position allowed flag status. Response Packet: 0x8f 0xad 0x02
k8ead03cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8ead03cmdEntry = TSIPSchemaEntry(EClientPackets.e8ead03cmd, k8ead03cmd, NUMFIELDS(k8ead03cmd))

# Requests the Bluetooth pairing information from the receiver
k8eae00req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8eae00reqEntry = TSIPSchemaEntry(EClientPackets.e8eae00req, k8eae00req, NUMFIELDS(k8eae00req))

# Commands the power state of the Bluetooth module
k8eae01cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8eae01cmdEntry = TSIPSchemaEntry(EClientPackets.e8eae01cmd, k8eae01cmd, NUMFIELDS(k8eae01cmd))

# Commands the Bluetooth pairing state of the receiver
k8eae02cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8eae02cmdEntry = TSIPSchemaEntry(EClientPackets.e8eae02cmd, k8eae02cmd, NUMFIELDS(k8eae02cmd))

# Commands the receiver to unpair all Bluetooth devices
k8eae03cmd = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x03), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8eae03cmdEntry = TSIPSchemaEntry(EClientPackets.e8eae03cmd, k8eae03cmd, NUMFIELDS(k8eae03cmd))

# Request the NAV to report pairing state changes
k8eae04req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x04), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8eae04reqEntry = TSIPSchemaEntry(EClientPackets.e8eae04req, k8eae04req, NUMFIELDS(k8eae04req))

# Request notifications for Bluetooth device pairing and connection events
k8eae05req = [
  IdSchemaField(0x8e), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x05), 
  U32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8eae05reqEntry = TSIPSchemaEntry(EClientPackets.e8eae05req, k8eae05req, NUMFIELDS(k8eae05req))

# Generic acknowledgement of packet receipt.
k8frsp = [
  IdSchemaField(0x8f), 
  ChecksumSchemaField()
]

k8frspEntry = TSIPSchemaEntry(EServerPackets.e8frsp, k8frsp, NUMFIELDS(k8frsp))
k8f77rspSampleData = U8SchemaField()

# Sample data for the fft report
k8f77rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x77), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k8f77rspSampleData), 
  ChecksumSchemaField()
]

k8f77rspEntry = TSIPSchemaEntry(EServerPackets.e8f77rsp, k8f77rsp, NUMFIELDS(k8f77rsp))
k8f770rspSampleData = U8SchemaField()

# Report Packet 0x8F 0x77 is generated after Command Packet 0x8E 0x75 is acknowledged with Report Packet 0x8F 0x75. The receiver performs a 1024-point Fast Fourier Transform (FFT) by the number of times specified by the Number of Integrations parameter in Command Packet 0x8E 0x75. Once the FFT report is completed, the receiver begins the next FFT. The FFT reports are generated and sent continuously until the FFT Stop Command (Command Packet 0x8E 0x76) is issued. Because the amount of data contained in the FFT report exceeds 123 bytes, the report is divided into multiple packets (pages). Even if all data bytes are DLEs (which would transmit 2 TSIP bytes for each data byte), the message structure does not overflow the 255 byte TSIP buffer length.
k8f770rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x77), 
  SubIdSchemaField(0x0), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  FLTSchemaField(), 
  FixedArraySchemaField(k8f770rspSampleData, 99), 
  ChecksumSchemaField()
]

k8f770rspEntry = TSIPSchemaEntry(EServerPackets.e8f770rsp, k8f770rsp, NUMFIELDS(k8f770rsp))

# 
k8f7brspConfigBlockV3FixedDefBoilerPlate = [
  StringSchemaField(22), 
  StringSchemaField(10), 
  StringSchemaField(17), 
  StringSchemaField(6), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField()
]

k8f7brspConfigBlockV3FixedDefBoilerPlateGroup = GroupSchemaField(k8f7brspConfigBlockV3FixedDefBoilerPlate,NUMFIELDS(k8f7brspConfigBlockV3FixedDefBoilerPlate))

# 
k8f7brspConfigBlockV3FixedDefRxDef = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8f7brspConfigBlockV3FixedDefRxDefGroup = GroupSchemaField(k8f7brspConfigBlockV3FixedDefRxDef,NUMFIELDS(k8f7brspConfigBlockV3FixedDefRxDef))

# 
k8f7brspConfigBlockV3FixedDef = [
  GroupSchemaField(k8f7brspConfigBlockV3FixedDefBoilerPlate,NUMFIELDS(k8f7brspConfigBlockV3FixedDefBoilerPlate)), 
  GroupSchemaField(k8f7brspConfigBlockV3FixedDefRxDef,NUMFIELDS(k8f7brspConfigBlockV3FixedDefRxDef)), 
  UnusedSchemaField(27)
]

k8f7brspConfigBlockV3FixedDefGroup = GroupSchemaField(k8f7brspConfigBlockV3FixedDef,NUMFIELDS(k8f7brspConfigBlockV3FixedDef))

# 
k8f7brspConfigBlockV3UserDefPortConfigPortConfig = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8f7brspConfigBlockV3UserDefPortConfigPortConfigGroup = GroupSchemaField(k8f7brspConfigBlockV3UserDefPortConfigPortConfig,NUMFIELDS(k8f7brspConfigBlockV3UserDefPortConfigPortConfig))

# 
k8f7brspConfigBlockV3UserDef = [
  FixedArraySchemaField(k8f7brspConfigBlockV3UserDefPortConfigPortConfigGroup, 3), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(29)
]

k8f7brspConfigBlockV3UserDefGroup = GroupSchemaField(k8f7brspConfigBlockV3UserDef,NUMFIELDS(k8f7brspConfigBlockV3UserDef))

# 
k8f7brspConfigBlockV3 = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k8f7brspConfigBlockV3FixedDef,NUMFIELDS(k8f7brspConfigBlockV3FixedDef)), 
  GroupSchemaField(k8f7brspConfigBlockV3UserDef,NUMFIELDS(k8f7brspConfigBlockV3UserDef)), 
  U16SchemaField(), 
  U16SchemaField()
]

k8f7brspConfigBlockV3Group = GroupSchemaField(k8f7brspConfigBlockV3,NUMFIELDS(k8f7brspConfigBlockV3))

# The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C.
k8f7brsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x7b), 
  U8SchemaField(), 
  StringSchemaField(20), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k8f7brspConfigBlockV3,NUMFIELDS(k8f7brspConfigBlockV3)), 
  ChecksumSchemaField()
]

k8f7brspEntry = TSIPSchemaEntry(EServerPackets.e8f7brsp, k8f7brsp, NUMFIELDS(k8f7brsp))

# sent to acknowledge Command Packet 0x8E 0x7C
k8f7cack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x7c), 
  ChecksumSchemaField()
]

k8f7cackEntry = TSIPSchemaEntry(EServerPackets.e8f7cack, k8f7cack, NUMFIELDS(k8f7cack))

# 
k8f7frspConfigBlockV3FixedDefBoilerPlate = [
  StringSchemaField(22), 
  StringSchemaField(10), 
  StringSchemaField(17), 
  StringSchemaField(6), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField()
]

k8f7frspConfigBlockV3FixedDefBoilerPlateGroup = GroupSchemaField(k8f7frspConfigBlockV3FixedDefBoilerPlate,NUMFIELDS(k8f7frspConfigBlockV3FixedDefBoilerPlate))

# 
k8f7frspConfigBlockV3FixedDefRxDef = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8f7frspConfigBlockV3FixedDefRxDefGroup = GroupSchemaField(k8f7frspConfigBlockV3FixedDefRxDef,NUMFIELDS(k8f7frspConfigBlockV3FixedDefRxDef))

# 
k8f7frspConfigBlockV3FixedDef = [
  GroupSchemaField(k8f7frspConfigBlockV3FixedDefBoilerPlate,NUMFIELDS(k8f7frspConfigBlockV3FixedDefBoilerPlate)), 
  GroupSchemaField(k8f7frspConfigBlockV3FixedDefRxDef,NUMFIELDS(k8f7frspConfigBlockV3FixedDefRxDef)), 
  UnusedSchemaField(27)
]

k8f7frspConfigBlockV3FixedDefGroup = GroupSchemaField(k8f7frspConfigBlockV3FixedDef,NUMFIELDS(k8f7frspConfigBlockV3FixedDef))

# 
k8f7frspConfigBlockV3UserDefPortConfigPortConfig = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8f7frspConfigBlockV3UserDefPortConfigPortConfigGroup = GroupSchemaField(k8f7frspConfigBlockV3UserDefPortConfigPortConfig,NUMFIELDS(k8f7frspConfigBlockV3UserDefPortConfigPortConfig))

# 
k8f7frspConfigBlockV3UserDef = [
  FixedArraySchemaField(k8f7frspConfigBlockV3UserDefPortConfigPortConfigGroup, 3), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(29)
]

k8f7frspConfigBlockV3UserDefGroup = GroupSchemaField(k8f7frspConfigBlockV3UserDef,NUMFIELDS(k8f7frspConfigBlockV3UserDef))

# 
k8f7frspConfigBlockV3 = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k8f7frspConfigBlockV3FixedDef,NUMFIELDS(k8f7frspConfigBlockV3FixedDef)), 
  GroupSchemaField(k8f7frspConfigBlockV3UserDef,NUMFIELDS(k8f7frspConfigBlockV3UserDef)), 
  U16SchemaField(), 
  U16SchemaField()
]

k8f7frspConfigBlockV3Group = GroupSchemaField(k8f7frspConfigBlockV3,NUMFIELDS(k8f7frspConfigBlockV3))

# The report contains current receiver configuration parameter settings and a software version report. The actual receiver configuration parameters are set using Command Packet 0x8E 0x7C.
k8f7frsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x7f), 
  U8SchemaField(), 
  StringSchemaField(20), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  GroupSchemaField(k8f7frspConfigBlockV3,NUMFIELDS(k8f7frspConfigBlockV3)), 
  ChecksumSchemaField()
]

k8f7frspEntry = TSIPSchemaEntry(EServerPackets.e8f7frsp, k8f7frsp, NUMFIELDS(k8f7frsp))

# This packet is used to obtain information about the current DGPS service provider. Due to operational differences among the service providers, the decoder state and access information is interpreted slightly differently for each service provider. Racal Service - At all times, the user access information accurately reflects the current access state, where &#8220;Access information available&#8221; indicates that no access information has been received yet. The initial confirmation of user access typically occurs after decoder initialization is complete. Omnistar Service - Once the initialization sequence is complete, the user access information is valid. Before initialization is completed, the access may not accurately reflect the final access state. To help determine whether the user access will become enabled when initialization is complete, the user may wish to look at the activation stop date provided by Report Packet 0x8F 0x8B. If the activation stop date is a future date, user access will become enabled when initialization is completed.
k8f80rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x80), 
  U8SchemaField(), 
  S32SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8f80rspEntry = TSIPSchemaEntry(EServerPackets.e8f80rsp, k8f80rsp, NUMFIELDS(k8f80rsp))

# Acknowledges the start and stop of satellite FFT diagnostics.
k8f84ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x84), 
  ChecksumSchemaField()
]

k8f84ackEntry = TSIPSchemaEntry(EServerPackets.e8f84ack, k8f84ack, NUMFIELDS(k8f84ack))

# Channel data
k8f85rspChannelDataArrayChannelDataBlock = [
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(4)
]

k8f85rspChannelDataArrayChannelDataBlockGroup = GroupSchemaField(k8f85rspChannelDataArrayChannelDataBlock,NUMFIELDS(k8f85rspChannelDataArrayChannelDataBlock))

# This packet is used to convey the DGPS tracking status for either beacon or satellite differential signals. Some fields have duplicate meanings depending on the Acquisition Mode (beacon or satellite). In addition, channels with Acquisition Mode 255 (Unused), should be ignored. For backwards compatibility, a minimum of two channels of data is always reported, but in a dual DSP receiver such as NH134, three channels of data may be reported. In this case, the channel block (bytes 3&#8211;32) will be repeated a third time for the third channel data. The value in byte 2 indicates how many blocks of channel data are provided in the packet with a minimum of 2 data blocks. If byte 2 is set to zero (backwards compatibility), 2 channels of data will be sent.
k8f85rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x85), 
  UnusedSchemaField(1), 
  U8SchemaField(), 
  ArraySchemaField(k8f85rspChannelDataArrayChannelDataBlockGroup, 3, 0,0, 3), 
  ChecksumSchemaField()
]

k8f85rspEntry = TSIPSchemaEntry(EServerPackets.e8f85rsp, k8f85rsp, NUMFIELDS(k8f85rsp))

# Indicates current DGPS source and related settings.
k8f89rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x89), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8f89rspEntry = TSIPSchemaEntry(EServerPackets.e8f89rsp, k8f89rsp, NUMFIELDS(k8f89rsp))

# Acknowledges DGPS source control command.
k8f89ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x89), 
  ChecksumSchemaField()
]

k8f89ackEntry = TSIPSchemaEntry(EServerPackets.e8f89ack, k8f89ack, NUMFIELDS(k8f89ack))
k8f8brspActivationCodeData = U8SchemaField()

# Brief information about service provider activation.
k8f8brsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8b), 
  U8SchemaField(), 
  FixedArraySchemaField(k8f8brspActivationCodeData, 24), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S32SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8f8brspEntry = TSIPSchemaEntry(EServerPackets.e8f8brsp, k8f8brsp, NUMFIELDS(k8f8brsp))

# Acknowledges when the remote display is enabled or disabled, or when a key press message is received.
k8f8cack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8c), 
  ChecksumSchemaField()
]

k8f8cackEntry = TSIPSchemaEntry(EServerPackets.e8f8cack, k8f8cack, NUMFIELDS(k8f8cack))

# Reports the data currently appearing on the display in ASCII format (except for a few special characters) and the cursor position and mode. This packet can be requested for a single output using Command Packet 0x8E 0x8C 0x01 or it can be configured to be output automatically whenever the screen contents changes using Command Packet 0x8E 0x8C 0x03.
k8f8c01rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  StringSchemaField(17), 
  UnusedSchemaField(5), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8f8c01rspEntry = TSIPSchemaEntry(EServerPackets.e8f8c01rsp, k8f8c01rsp, NUMFIELDS(k8f8c01rsp))

# Sent by the receiver to control the state of a remote output line, i.e. an alarm. It is sent automatically if the receiver has been configured to drive output lines. For example, the PSO interface allows the user to set criteria for tripping an audible alarm. To control the output line to this alarm remotely (i.e. the output line is not directly connected to the receiver), this packet is sent.
k8f8c02rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8f8c02rspEntry = TSIPSchemaEntry(EServerPackets.e8f8c02rsp, k8f8c02rsp, NUMFIELDS(k8f8c02rsp))

# Shows the receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03.
k8f8c03rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8f8c03rspEntry = TSIPSchemaEntry(EServerPackets.e8f8c03rsp, k8f8c03rsp, NUMFIELDS(k8f8c03rsp))

# Shows the extended receiver configuration to display data on its own display or a remote display (i.e. a PC) connected to a serial port. This packet includes a text description of what kind of receiver it is, i.e. Ag132, Ag124, etc. It is sent in response to a configuration request via Command Packet 0x8E 0x8C 0x03.
k8f8c04rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8c), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  StringSchemaField(6), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8f8c04rspEntry = TSIPSchemaEntry(EServerPackets.e8f8c04rsp, k8f8c04rsp, NUMFIELDS(k8f8c04rsp))

# Report Packet 0x8F 0x8F is sent when the receiver is powered on and can be sent in response to Command Packet 0x8E 0x8F. The packet indicates the type of receiver and why the receiver restarted if an error caused the receiver to reset.
k8f8frsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x8f), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(7), 
  ChecksumSchemaField()
]

k8f8frspEntry = TSIPSchemaEntry(EServerPackets.e8f8frsp, k8f8frsp, NUMFIELDS(k8f8frsp))

# Return the guidance configuration information
k8f91rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x91), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8f91rspEntry = TSIPSchemaEntry(EServerPackets.e8f91rsp, k8f91rsp, NUMFIELDS(k8f91rsp))

# Return Guidance Configuration Information
k8f91ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x91), 
  ChecksumSchemaField()
]

k8f91ackEntry = TSIPSchemaEntry(EServerPackets.e8f91ack, k8f91ack, NUMFIELDS(k8f91ack))
k8f9306rspDebugMsgChar = CHARSchemaField()

# Debugging message output from the receiver
k8f9306rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x06), 
  U16SchemaField(), 
  ArraySchemaField(k8f9306rspDebugMsgChar, 3, 0,0, 252), 
  ChecksumSchemaField()
]

k8f9306rspEntry = TSIPSchemaEntry(EServerPackets.e8f9306rsp, k8f9306rsp, NUMFIELDS(k8f9306rsp))
k8f931500rspFilenameChar = CHARSchemaField()

# Sent in response to a File Transfer Listing Request, one for each entry in the directory requested.
k8f931500rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k8f931500rspFilenameChar), 
  ChecksumSchemaField()
]

k8f931500rspEntry = TSIPSchemaEntry(EServerPackets.e8f931500rsp, k8f931500rsp, NUMFIELDS(k8f931500rsp))
k8f93150100rspFilenameChar = CHARSchemaField()

# Info for transfer sent in response to File Transfer Get - Open Request.
k8f93150100rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  U32SchemaField(), 
  EndTerminatedArraySchemaField(k8f93150100rspFilenameChar), 
  ChecksumSchemaField()
]

k8f93150100rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150100rsp, k8f93150100rsp, NUMFIELDS(k8f93150100rsp))
k8f93150101rspDataBlockData = U8SchemaField()

# Block of file data sent in response to File Transfer Get - Data Block Request.
k8f93150101rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k8f93150101rspDataBlockData), 
  ChecksumSchemaField()
]

k8f93150101rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150101rsp, k8f93150101rsp, NUMFIELDS(k8f93150101rsp))

# Confirms that requested file has been closed, sent in response to File Transfer Get - Close Request.
k8f93150102rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k8f93150102rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150102rsp, k8f93150102rsp, NUMFIELDS(k8f93150102rsp))

# Indicates error that caused request to fail.
k8f93150103rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x03), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8f93150103rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150103rsp, k8f93150103rsp, NUMFIELDS(k8f93150103rsp))
k8f93150104rspHashByte = U8SchemaField()
k8f93150104rspFilenameChar = CHARSchemaField()

# Hash of the requested file in the fusion file system.
k8f93150104rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8f93150104rspHashByte, 8, 0,0, 128), 
  EndTerminatedArraySchemaField(k8f93150104rspFilenameChar), 
  ChecksumSchemaField()
]

k8f93150104rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150104rsp, k8f93150104rsp, NUMFIELDS(k8f93150104rsp))
k8f93150200rspFilenameChar = CHARSchemaField()

# Info for transfer sent in response to File Transfer Put - Open Request.
k8f93150200rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  U32SchemaField(), 
  EndTerminatedArraySchemaField(k8f93150200rspFilenameChar), 
  ChecksumSchemaField()
]

k8f93150200rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150200rsp, k8f93150200rsp, NUMFIELDS(k8f93150200rsp))

# Indicates successful file write in response to File Transfer Put - Data Block Request.
k8f93150201rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8f93150201rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150201rsp, k8f93150201rsp, NUMFIELDS(k8f93150201rsp))

# Confirms that requested file has been closed, sent in response to File Transfer Put - Close Request.
k8f93150202rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  ChecksumSchemaField()
]

k8f93150202rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150202rsp, k8f93150202rsp, NUMFIELDS(k8f93150202rsp))

# Indicates error that caused request to fail.
k8f93150203rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x03), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8f93150203rspEntry = TSIPSchemaEntry(EServerPackets.e8f93150203rsp, k8f93150203rsp, NUMFIELDS(k8f93150203rsp))
k8f931503rspFilenameChar = CHARSchemaField()

# Indicates status of file delete, sent in response to File Transfer Delete Request.
k8f931503rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x93), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(k8f931503rspFilenameChar), 
  ChecksumSchemaField()
]

k8f931503rspEntry = TSIPSchemaEntry(EServerPackets.e8f931503rsp, k8f931503rsp, NUMFIELDS(k8f931503rsp))

# Report Packet 0x8F 0x9A contains information about the last differential correction set that was received and used by the receiver.
k8f9arsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9a), 
  U16SchemaField(), 
  S16SchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8f9arspEntry = TSIPSchemaEntry(EServerPackets.e8f9arsp, k8f9arsp, NUMFIELDS(k8f9arsp))
k8f9erspSourceInfoArrayGroup = GroupSchemaField(k8ef9eDGPSSourceInfo,NUMFIELDS(k8ef9eDGPSSourceInfo))

# Reports the priorities of the DGPS sources that are in use by the receiver. Up to four different DGPS sources can be reported.
k8f9ersp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9e), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ArraySchemaField(k8f9erspSourceInfoArrayGroup, 2, 0,0, 4), 
  ChecksumSchemaField()
]

k8f9erspEntry = TSIPSchemaEntry(EServerPackets.e8f9ersp, k8f9ersp, NUMFIELDS(k8f9ersp))

# CAN Channel Config
k8f9f00rspChannelCfgCANChannelCfg = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4)
]

k8f9f00rspChannelCfgCANChannelCfgGroup = GroupSchemaField(k8f9f00rspChannelCfgCANChannelCfg,NUMFIELDS(k8f9f00rspChannelCfgCANChannelCfg))

# Sets the CAN bus configuration for specified channels
k8f9f00rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(2), 
  U8SchemaField(), 
  ArraySchemaField(k8f9f00rspChannelCfgCANChannelCfgGroup, 4, 0,0, 16), 
  ChecksumSchemaField()
]

k8f9f00rspEntry = TSIPSchemaEntry(EServerPackets.e8f9f00rsp, k8f9f00rsp, NUMFIELDS(k8f9f00rsp))

# Acknowledgement that the CAN configuration was received
k8f9f00ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x00), 
  ChecksumSchemaField()
]

k8f9f00ackEntry = TSIPSchemaEntry(EServerPackets.e8f9f00ack, k8f9f00ack, NUMFIELDS(k8f9f00ack))

# CAN Channel Config
k8f9f01rspChannelCfgCANChannelCfg = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3)
]

k8f9f01rspChannelCfgCANChannelCfgGroup = GroupSchemaField(k8f9f01rspChannelCfgCANChannelCfg,NUMFIELDS(k8f9f01rspChannelCfgCANChannelCfg))

# Provides the current CAN status for the channel
k8f9f01rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x01), 
  UnusedSchemaField(2), 
  U8SchemaField(), 
  ArraySchemaField(k8f9f01rspChannelCfgCANChannelCfgGroup, 4, 0,0, 16), 
  ChecksumSchemaField()
]

k8f9f01rspEntry = TSIPSchemaEntry(EServerPackets.e8f9f01rsp, k8f9f01rsp, NUMFIELDS(k8f9f01rsp))

# J1939 message configuration
k8f9f02rspMsgCfgArrayMsgCfg = [
  U8SchemaField(), 
  U16SchemaField()
]

k8f9f02rspMsgCfgArrayMsgCfgGroup = GroupSchemaField(k8f9f02rspMsgCfgArrayMsgCfg,NUMFIELDS(k8f9f02rspMsgCfgArrayMsgCfg))

# Provides current J1939 message configuration for channel
k8f9f02rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8f9f02rspMsgCfgArrayMsgCfgGroup, 4, 0,0, 10), 
  ChecksumSchemaField()
]

k8f9f02rspEntry = TSIPSchemaEntry(EServerPackets.e8f9f02rsp, k8f9f02rsp, NUMFIELDS(k8f9f02rsp))

# Acknowledgement that J1939 message configuration was received
k8f9f02ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8f9f02ackEntry = TSIPSchemaEntry(EServerPackets.e8f9f02ack, k8f9f02ack, NUMFIELDS(k8f9f02ack))

# NMEA2K message configuration
k8f9f03rspMsgCfgArrayMsgCfg = [
  U8SchemaField(), 
  U16SchemaField()
]

k8f9f03rspMsgCfgArrayMsgCfgGroup = GroupSchemaField(k8f9f03rspMsgCfgArrayMsgCfg,NUMFIELDS(k8f9f03rspMsgCfgArrayMsgCfg))

# Provides current NMEA2K message configuration for channel
k8f9f03rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8f9f03rspMsgCfgArrayMsgCfgGroup, 4, 0,0, 25), 
  ChecksumSchemaField()
]

k8f9f03rspEntry = TSIPSchemaEntry(EServerPackets.e8f9f03rsp, k8f9f03rsp, NUMFIELDS(k8f9f03rsp))

# Acknowledgement that NMEA2K message configuration was received
k8f9f03ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x03), 
  ChecksumSchemaField()
]

k8f9f03ackEntry = TSIPSchemaEntry(EServerPackets.e8f9f03ack, k8f9f03ack, NUMFIELDS(k8f9f03ack))

# ISO message configuration
k8f9f04rspMsgCfgArrayMsgCfg = [
  U8SchemaField(), 
  U16SchemaField()
]

k8f9f04rspMsgCfgArrayMsgCfgGroup = GroupSchemaField(k8f9f04rspMsgCfgArrayMsgCfg,NUMFIELDS(k8f9f04rspMsgCfgArrayMsgCfg))

# Provides current ISO message configuration for channel
k8f9f04rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8f9f04rspMsgCfgArrayMsgCfgGroup, 4, 0,0, 10), 
  ChecksumSchemaField()
]

k8f9f04rspEntry = TSIPSchemaEntry(EServerPackets.e8f9f04rsp, k8f9f04rsp, NUMFIELDS(k8f9f04rsp))

# Acknowledgement that ISO message configuration was received
k8f9f04ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0x9f), 
  SubIdSchemaField(0x04), 
  ChecksumSchemaField()
]

k8f9f04ackEntry = TSIPSchemaEntry(EServerPackets.e8f9f04ack, k8f9f04ack, NUMFIELDS(k8f9f04ack))

# 
k8fa0rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa0), 
  U8SchemaField(), 
  StringSchemaField(33), 
  ChecksumSchemaField()
]

k8fa0rspEntry = TSIPSchemaEntry(EServerPackets.e8fa0rsp, k8fa0rsp, NUMFIELDS(k8fa0rsp))
k8fa1rspPacketDataData = U8SchemaField()

# This is an alias to 0x8f 0xa1.
k8fa1rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa1), 
  EndTerminatedArraySchemaField(k8fa1rspPacketDataData), 
  ChecksumSchemaField()
]

k8fa1rspEntry = TSIPSchemaEntry(EServerPackets.e8fa1rsp, k8fa1rsp, NUMFIELDS(k8fa1rsp))

# Reports additional information about the current generated position solution. It is sent once in response to a query packet Command Packet 0x8E 0xA2, or automatically if configured using Command Packet 0x6A 0x01.
k8fa2rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa2), 
  U8SchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(9), 
  ChecksumSchemaField()
]

k8fa2rspEntry = TSIPSchemaEntry(EServerPackets.e8fa2rsp, k8fa2rsp, NUMFIELDS(k8fa2rsp))

# The version of the Omnistar XP/HP engine
k8fa300rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x00), 
  StringSchemaField(33), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fa300rspEntry = TSIPSchemaEntry(EServerPackets.e8fa300rsp, k8fa300rsp, NUMFIELDS(k8fa300rsp))

# The subscription information for the Omnistar XP/HP service
k8fa301rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  S32SchemaField(), 
  S32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa301rspEntry = TSIPSchemaEntry(EServerPackets.e8fa301rsp, k8fa301rsp, NUMFIELDS(k8fa301rsp))
k8fa302rspStationIdsStationId = S32SchemaField()

# Status information on the current state of the Omnistar XP/HP engine
k8fa302rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S32SchemaField(), 
  UnusedSchemaField(10), 
  U8SchemaField(), 
  ArraySchemaField(k8fa302rspStationIdsStationId, 11, 0,0, 12), 
  ChecksumSchemaField()
]

k8fa302rspEntry = TSIPSchemaEntry(EServerPackets.e8fa302rsp, k8fa302rsp, NUMFIELDS(k8fa302rsp))

# Base station information
k8fa303rspStationInfoArrayStationInfo = [
  S32SchemaField(), 
  StringSchemaField(13)
]

k8fa303rspStationInfoArrayStationInfoGroup = GroupSchemaField(k8fa303rspStationInfoArrayStationInfo,NUMFIELDS(k8fa303rspStationInfoArrayStationInfo))

# The base stations currently used by the Omnistar XP/HP engine
k8fa303rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ArraySchemaField(k8fa303rspStationInfoArrayStationInfoGroup, 3, 0,0, 7), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fa303rspEntry = TSIPSchemaEntry(EServerPackets.e8fa303rsp, k8fa303rsp, NUMFIELDS(k8fa303rsp))

# Provides information about the current Auto-Seed information held by the receiver. If Auto-Seed functionality is on in the receiver, these values would be used at startup if the receiver was rebooted at this point in time.
k8fa304rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fa304rspEntry = TSIPSchemaEntry(EServerPackets.e8fa304rsp, k8fa304rsp, NUMFIELDS(k8fa304rsp))

# Provides infomration about the control parameters of the Omnistar XP/HP processor
k8fa305rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x05), 
  U16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8fa305rspEntry = TSIPSchemaEntry(EServerPackets.e8fa305rsp, k8fa305rsp, NUMFIELDS(k8fa305rsp))

# Provides information about the debugging output of the XP/HP processor
k8fa306rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(18), 
  ChecksumSchemaField()
]

k8fa306rspEntry = TSIPSchemaEntry(EServerPackets.e8fa306rsp, k8fa306rsp, NUMFIELDS(k8fa306rsp))

# Acknowledgment that the XP/HP engine was reset
k8fa307ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa3), 
  SubIdSchemaField(0x07), 
  ChecksumSchemaField()
]

k8fa307ackEntry = TSIPSchemaEntry(EServerPackets.e8fa307ack, k8fa307ack, NUMFIELDS(k8fa307ack))

# Reports Quadratic Bias Filter configuration in response to packet 0x8E 0xA4 0x05.
k8fa405rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa4), 
  SubIdSchemaField(0x05), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1), 
  ChecksumSchemaField()
]

k8fa405rspEntry = TSIPSchemaEntry(EServerPackets.e8fa405rsp, k8fa405rsp, NUMFIELDS(k8fa405rsp))

# Reports Kalman Filter configuration in response to packet 0x8E 0xA4 0x06.
k8fa406rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa4), 
  SubIdSchemaField(0x06), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa406rspEntry = TSIPSchemaEntry(EServerPackets.e8fa406rsp, k8fa406rsp, NUMFIELDS(k8fa406rsp))

# Reports the current status of Field Level Smoothing. Request Packet: 0x8e 0xa4 0x07
k8fa407rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa4), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa407rspEntry = TSIPSchemaEntry(EServerPackets.e8fa407rsp, k8fa407rsp, NUMFIELDS(k8fa407rsp))

# Information for a particular SBAS satellite
k8fa500rspSBASInfoArraySBASInfo = [
  U8SchemaField(), 
  U8SchemaField()
]

k8fa500rspSBASInfoArraySBASInfoGroup = GroupSchemaField(k8fa500rspSBASInfoArraySBASInfo,NUMFIELDS(k8fa500rspSBASInfoArraySBASInfo))

# Reports the current SBAS settings. This packet can contain a variable number of SBAS SV entries. The request or command packet used to trigger the report will determine the number of entries. A 0x8EA500 request will generate a report for all SVs. A 0x8EA500 command will generate a report for those SVs listed in the command.
k8fa500rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ArraySchemaField(k8fa500rspSBASInfoArraySBASInfoGroup, 3, 0,0, 39), 
  ChecksumSchemaField()
]

k8fa500rspEntry = TSIPSchemaEntry(EServerPackets.e8fa500rsp, k8fa500rsp, NUMFIELDS(k8fa500rsp))

# Reports the current SBAS+ settings. Request packet is 0x8E 0xA5 0x01
k8fa501rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa501rspEntry = TSIPSchemaEntry(EServerPackets.e8fa501rsp, k8fa501rsp, NUMFIELDS(k8fa501rsp))

# Acks SBAS Default Constellation Reset Command 
k8fa502ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa5), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8fa502ackEntry = TSIPSchemaEntry(EServerPackets.e8fa502ack, k8fa502ack, NUMFIELDS(k8fa502ack))

# Acknowledges the Set External Output Pin state cmd.
k8fa601ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8fa601ackEntry = TSIPSchemaEntry(EServerPackets.e8fa601ack, k8fa601ack, NUMFIELDS(k8fa601ack))
k8fa602rspExternalInputsInputPinState = U8SchemaField()

# Responds with the state of the external input pins.
k8fa602rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  FixedArraySchemaField(k8fa602rspExternalInputsInputPinState, 17), 
  ChecksumSchemaField()
]

k8fa602rspEntry = TSIPSchemaEntry(EServerPackets.e8fa602rsp, k8fa602rsp, NUMFIELDS(k8fa602rsp))

# Provides the manufacturing information of the unit.
k8fa608rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  StringSchemaField(16), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa608rspEntry = TSIPSchemaEntry(EServerPackets.e8fa608rsp, k8fa608rsp, NUMFIELDS(k8fa608rsp))

# Provides the Omnistar Id for the unit.
k8fa617rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x17), 
  U8SchemaField(), 
  StringSchemaField(20), 
  ChecksumSchemaField()
]

k8fa617rspEntry = TSIPSchemaEntry(EServerPackets.e8fa617rsp, k8fa617rsp, NUMFIELDS(k8fa617rsp))
k8fa622rspMac1AddrMac1Hex = U8SchemaField()
k8fa622rspMac2AddrMac2Hex = U8SchemaField()
k8fa622rspMac3AddrMac3Hex = U8SchemaField()
k8fa622rspMac4AddrMac4Hex = U8SchemaField()

# Provides MAC addresses (4 max) for the unit.
k8fa622rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x22), 
  U8SchemaField(), 
  U8SchemaField(), 
  FixedArraySchemaField(k8fa622rspMac1AddrMac1Hex, 6), 
  U8SchemaField(), 
  FixedArraySchemaField(k8fa622rspMac2AddrMac2Hex, 6), 
  U8SchemaField(), 
  FixedArraySchemaField(k8fa622rspMac3AddrMac3Hex, 6), 
  U8SchemaField(), 
  FixedArraySchemaField(k8fa622rspMac4AddrMac4Hex, 6), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fa622rspEntry = TSIPSchemaEntry(EServerPackets.e8fa622rsp, k8fa622rsp, NUMFIELDS(k8fa622rsp))
k8fa623rspAltUniqueIdFieldAltUniqueId = U8SchemaField()

# Provides the alternate unique ID for the unit.
k8fa623rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x23), 
  U8SchemaField(), 
  FixedArraySchemaField(k8fa623rspAltUniqueIdFieldAltUniqueId, 20), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8fa623rspEntry = TSIPSchemaEntry(EServerPackets.e8fa623rsp, k8fa623rsp, NUMFIELDS(k8fa623rsp))

# Provides unit's extended manufacturing information.
k8fa624rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x24), 
  StringSchemaField(16), 
  StringSchemaField(20), 
  UnusedSchemaField(60), 
  ChecksumSchemaField()
]

k8fa624rspEntry = TSIPSchemaEntry(EServerPackets.e8fa624rsp, k8fa624rsp, NUMFIELDS(k8fa624rsp))

# Acks extended manufacturing information cmd.
k8fa625ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x25), 
  ChecksumSchemaField()
]

k8fa625ackEntry = TSIPSchemaEntry(EServerPackets.e8fa625ack, k8fa625ack, NUMFIELDS(k8fa625ack))

# Provides unit's product information.
k8fa626rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x26), 
  StringSchemaField(20), 
  StringSchemaField(18), 
  StringSchemaField(6), 
  UnusedSchemaField(60), 
  ChecksumSchemaField()
]

k8fa626rspEntry = TSIPSchemaEntry(EServerPackets.e8fa626rsp, k8fa626rsp, NUMFIELDS(k8fa626rsp))

# Acks product information cmd.
k8fa627ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x27), 
  ChecksumSchemaField()
]

k8fa627ackEntry = TSIPSchemaEntry(EServerPackets.e8fa627ack, k8fa627ack, NUMFIELDS(k8fa627ack))

# If received,receiver is now in manufacturing test mode.
k8fa628ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x28), 
  U8SchemaField(), 
  UnusedSchemaField(13), 
  ChecksumSchemaField()
]

k8fa628ackEntry = TSIPSchemaEntry(EServerPackets.e8fa628ack, k8fa628ack, NUMFIELDS(k8fa628ack))
k8fa629rspsignatureSignatureByte = U8SchemaField()

# Responds with the signature at the given offset
k8fa629rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x29), 
  U32SchemaField(), 
  FixedArraySchemaField(k8fa629rspsignatureSignatureByte, 32), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa629rspEntry = TSIPSchemaEntry(EServerPackets.e8fa629rsp, k8fa629rsp, NUMFIELDS(k8fa629rsp))

# Response containing the peak FFT frequency and SNR from the RF spectrum analyzer for GNSS bands. Intended for factory test use only.
k8fa630rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x30), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(64), 
  ChecksumSchemaField()
]

k8fa630rspEntry = TSIPSchemaEntry(EServerPackets.e8fa630rsp, k8fa630rsp, NUMFIELDS(k8fa630rsp))

# Response containing metadata about the condition of MSS tracking
k8fa631rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x31), 
  U8SchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(64), 
  ChecksumSchemaField()
]

k8fa631rspEntry = TSIPSchemaEntry(EServerPackets.e8fa631rsp, k8fa631rsp, NUMFIELDS(k8fa631rsp))

# Result of a register read operation to a specific polaris device
k8fa632rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x32), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa632rspEntry = TSIPSchemaEntry(EServerPackets.e8fa632rsp, k8fa632rsp, NUMFIELDS(k8fa632rsp))

# Requests a register read operation to a specific polaris device
k8fa632ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x32), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa632ackEntry = TSIPSchemaEntry(EServerPackets.e8fa632ack, k8fa632ack, NUMFIELDS(k8fa632ack))

# Result of a RSSI ADC value read operation to a specific polaris device
k8fa633rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x33), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa633rspEntry = TSIPSchemaEntry(EServerPackets.e8fa633rsp, k8fa633rsp, NUMFIELDS(k8fa633rsp))

# Acknowledges the test request to perform the Polaris full AGC test. If accepted, the receiver will start the test, and then send the 0x8f 0xa6 0x34 response when the test completes. If there is a problem starting the test, the response will be returned in the result field.
k8fa634ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x34), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa634ackEntry = TSIPSchemaEntry(EServerPackets.e8fa634ack, k8fa634ack, NUMFIELDS(k8fa634ack))

# Information for a single Antenna+RF Band+Histogram Bank
k8fa634rspBandResultArrayBandResult = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(5)
]

k8fa634rspBandResultArrayBandResultGroup = GroupSchemaField(k8fa634rspBandResultArrayBandResult,NUMFIELDS(k8fa634rspBandResultArrayBandResult))

# Response containing the results of the Polaris Full AGC test. Intended for factory test use only.
k8fa634rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x34), 
  UnusedSchemaField(2), 
  U8SchemaField(), 
  ArraySchemaField(k8fa634rspBandResultArrayBandResultGroup, 4, 0,0, 6), 
  DBLSchemaField(), 
  UnusedSchemaField(32), 
  ChecksumSchemaField()
]

k8fa634rspEntry = TSIPSchemaEntry(EServerPackets.e8fa634rsp, k8fa634rsp, NUMFIELDS(k8fa634rsp))

# Acknowledges the command to enable the PLT Mode for WiFi testing.
k8fa640ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x40), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa640ackEntry = TSIPSchemaEntry(EServerPackets.e8fa640ack, k8fa640ack, NUMFIELDS(k8fa640ack))

# Acknowledges the command to disable the PLT Mode for WiFi testing.
k8fa641ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x41), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa641ackEntry = TSIPSchemaEntry(EServerPackets.e8fa641ack, k8fa641ack, NUMFIELDS(k8fa641ack))

# Acknowledges the command to configure the device to operate in a specific WiFi band and channel.
k8fa642ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x42), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa642ackEntry = TSIPSchemaEntry(EServerPackets.e8fa642ack, k8fa642ack, NUMFIELDS(k8fa642ack))

# Acknowledges the command to set the transmission power of the WL18xx device.
k8fa643ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x43), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa643ackEntry = TSIPSchemaEntry(EServerPackets.e8fa643ack, k8fa643ack, NUMFIELDS(k8fa643ack))

# Acknowledges the command to enable TX test using the start_tx command.
k8fa644ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x44), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa644ackEntry = TSIPSchemaEntry(EServerPackets.e8fa644ack, k8fa644ack, NUMFIELDS(k8fa644ack))

# Acknowledges the command to disable TX test using the stop_tx command.
k8fa645ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x45), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa645ackEntry = TSIPSchemaEntry(EServerPackets.e8fa645ack, k8fa645ack, NUMFIELDS(k8fa645ack))

# Acknowledges the command to start the RX statistics.
k8fa646ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x46), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa646ackEntry = TSIPSchemaEntry(EServerPackets.e8fa646ack, k8fa646ack, NUMFIELDS(k8fa646ack))

# Response containing the RX statistics.
k8fa647rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x47), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  S16SchemaField(), 
  S16SchemaField(), 
  FLTSchemaField(), 
  ChecksumSchemaField()
]

k8fa647rspEntry = TSIPSchemaEntry(EServerPackets.e8fa647rsp, k8fa647rsp, NUMFIELDS(k8fa647rsp))

# Acknowledges the command to stop the RX statistics.
k8fa648ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa6), 
  SubIdSchemaField(0x48), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa648ackEntry = TSIPSchemaEntry(EServerPackets.e8fa648ack, k8fa648ack, NUMFIELDS(k8fa648ack))

# The auto-report settings for the current antenna, sent in response to the corresponding configuration command
k8fa70000rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa70000rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70000rsp, k8fa70000rsp, NUMFIELDS(k8fa70000rsp))
k8fa70001rspPositionEngArrayPositionEng = U8SchemaField()

# The position auto-report settings by engine, sent in response to the corresponding command
k8fa70001rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8fa70001rspPositionEngArrayPositionEng, 6, 0,0, 12), 
  ChecksumSchemaField()
]

k8fa70001rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70001rsp, k8fa70001rsp, NUMFIELDS(k8fa70001rsp))
k8fa70002rspPositionTypeArrayPositionType = U8SchemaField()

# The position auto-report settings by type, sent in response to the corresponding command
k8fa70002rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8fa70002rspPositionTypeArrayPositionType, 6, 0,0, 12), 
  ChecksumSchemaField()
]

k8fa70002rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70002rsp, k8fa70002rsp, NUMFIELDS(k8fa70002rsp))

# The position auto-report settings by flag, sent in response to the corresponding command
k8fa70003rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa70003rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70003rsp, k8fa70003rsp, NUMFIELDS(k8fa70003rsp))

# A GPS Position packet that provides a useful subset of positioning information, including an id for the antenna it came from.
k8fa70100rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa70100rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70100rsp, k8fa70100rsp, NUMFIELDS(k8fa70100rsp))

# Indicates that a GPS position wasn't generated for the given time period
k8fa70101rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa70101rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70101rsp, k8fa70101rsp, NUMFIELDS(k8fa70101rsp))

# Provides the ENU vector between two GPS antennas
k8fa70102rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa7), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa70102rspEntry = TSIPSchemaEntry(EServerPackets.e8fa70102rsp, k8fa70102rsp, NUMFIELDS(k8fa70102rsp))

# Response to the 8FA801 packet
k8fa800rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x00), 
  S8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa800rspEntry = TSIPSchemaEntry(EServerPackets.e8fa800rsp, k8fa800rsp, NUMFIELDS(k8fa800rsp))

# Ack to NTRIP params set
k8fa801ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa801ackEntry = TSIPSchemaEntry(EServerPackets.e8fa801ack, k8fa801ack, NUMFIELDS(k8fa801ack))
k8fa801rspIPAddressChar = CHARSchemaField()
k8fa801rspMountPointChar = CHARSchemaField()
k8fa801rspUserNameChar = CHARSchemaField()
k8fa801rspPasswordChar = CHARSchemaField()

# Report of the current NTRIP params. All strings are not null terminated, and the stringLength value is the number of actual characters
k8fa801rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x01), 
  U16SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fa801rspIPAddressChar, 4, 0,0, 60), 
  U8SchemaField(), 
  ArraySchemaField(k8fa801rspMountPointChar, 6, 0,0, 60), 
  U8SchemaField(), 
  ArraySchemaField(k8fa801rspUserNameChar, 8, 0,0, 60), 
  U8SchemaField(), 
  ArraySchemaField(k8fa801rspPasswordChar, 10, 0,0, 60), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  ChecksumSchemaField()
]

k8fa801rspEntry = TSIPSchemaEntry(EServerPackets.e8fa801rsp, k8fa801rsp, NUMFIELDS(k8fa801rsp))

# ACK for the set fo the GPRS Username
k8fa802ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k8fa802ackEntry = TSIPSchemaEntry(EServerPackets.e8fa802ack, k8fa802ack, NUMFIELDS(k8fa802ack))
k8fa802rspUserNameChar = CHARSchemaField()

# Report of the GPRS Username. All strings are not null terminated, and the stringLength value is the number of actual characters
k8fa802rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8fa802rspUserNameChar, 5, 0,0, 60), 
  ChecksumSchemaField()
]

k8fa802rspEntry = TSIPSchemaEntry(EServerPackets.e8fa802rsp, k8fa802rsp, NUMFIELDS(k8fa802rsp))

# ACK for the set fo the GPRS Password
k8fa803ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k8fa803ackEntry = TSIPSchemaEntry(EServerPackets.e8fa803ack, k8fa803ack, NUMFIELDS(k8fa803ack))
k8fa803rspPasswordChar = CHARSchemaField()

# Report of the GPRS Password. All strings are not null terminated, and the stringLength value is the number of actual characters
k8fa803rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8fa803rspPasswordChar, 5, 0,0, 60), 
  ChecksumSchemaField()
]

k8fa803rspEntry = TSIPSchemaEntry(EServerPackets.e8fa803rsp, k8fa803rsp, NUMFIELDS(k8fa803rsp))

# ACK for the set fo the GPRS InitString
k8fa804ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k8fa804ackEntry = TSIPSchemaEntry(EServerPackets.e8fa804ack, k8fa804ack, NUMFIELDS(k8fa804ack))
k8fa804rspInitStringChar = CHARSchemaField()

# Report of the GPRS InitString. All strings are not null terminated, and the stringLength value is the number of actual characters
k8fa804rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  U8SchemaField(), 
  ArraySchemaField(k8fa804rspInitStringChar, 5, 0,0, 60), 
  ChecksumSchemaField()
]

k8fa804rspEntry = TSIPSchemaEntry(EServerPackets.e8fa804rsp, k8fa804rsp, NUMFIELDS(k8fa804rsp))

# ACK for the set fo the GPRS CPIN
k8fa805ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k8fa805ackEntry = TSIPSchemaEntry(EServerPackets.e8fa805ack, k8fa805ack, NUMFIELDS(k8fa805ack))

# ACK from the VRS Radio Config command
k8fa806ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  UnusedSchemaField(1)
]

k8fa806ackEntry = TSIPSchemaEntry(EServerPackets.e8fa806ack, k8fa806ack, NUMFIELDS(k8fa806ack))

# Report of the current radio mode
k8fa806rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa8), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(6), 
  ChecksumSchemaField()
]

k8fa806rspEntry = TSIPSchemaEntry(EServerPackets.e8fa806rsp, k8fa806rsp, NUMFIELDS(k8fa806rsp))

# Holds various firmware and hardware version information
k8fa900rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(1), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(1), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(2), 
  StringSchemaField(32), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa900rspEntry = TSIPSchemaEntry(EServerPackets.e8fa900rsp, k8fa900rsp, NUMFIELDS(k8fa900rsp))

# Acknowledges the upgrade command, providing information on how it proceeded.
k8fa90100ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa90100ackEntry = TSIPSchemaEntry(EServerPackets.e8fa90100ack, k8fa90100ack, NUMFIELDS(k8fa90100ack))

# Provides the progress of the upgrade as it proceeds
k8fa90100rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  DBLSchemaField(), 
  ChecksumSchemaField()
]

k8fa90100rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90100rsp, k8fa90100rsp, NUMFIELDS(k8fa90100rsp))

# Acknowledges the logging control, providing information on how it proceeded.
k8fa90101ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa90101ackEntry = TSIPSchemaEntry(EServerPackets.e8fa90101ack, k8fa90101ack, NUMFIELDS(k8fa90101ack))
k8fa90101rspfilenameChar = CHARSchemaField()

# Reports the state of the logging control.
k8fa90101rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fa90101rspfilenameChar, 5, 0,0, 240), 
  ChecksumSchemaField()
]

k8fa90101rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90101rsp, k8fa90101rsp, NUMFIELDS(k8fa90101rsp))

# Acknowledges the Log dump request providing information on how the operation proceeded.
k8fa90102ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa90102ackEntry = TSIPSchemaEntry(EServerPackets.e8fa90102ack, k8fa90102ack, NUMFIELDS(k8fa90102ack))
k8fa90103rspDataData = U8SchemaField()

# A variable length data packet (pong), that is returned in response to a receiver request (ping). This allows a type of serial communication test to occur.
k8fa90103rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ArraySchemaField(k8fa90103rspDataData, 4, 0,0, 240), 
  ChecksumSchemaField()
]

k8fa90103rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90103rsp, k8fa90103rsp, NUMFIELDS(k8fa90103rsp))

# Returns the IP Address and port number for the VRS Daemon.
k8fa90104rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  StringSchemaField(20), 
  U16SchemaField(), 
  ChecksumSchemaField()
]

k8fa90104rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90104rsp, k8fa90104rsp, NUMFIELDS(k8fa90104rsp))

# Acknowledges the license file has been processed.
k8fa90105ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa90105ackEntry = TSIPSchemaEntry(EServerPackets.e8fa90105ack, k8fa90105ack, NUMFIELDS(k8fa90105ack))

# Reports the current state of the receiver automatic reboot capability
k8fa90106rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa90106rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90106rsp, k8fa90106rsp, NUMFIELDS(k8fa90106rsp))

# Returns the IP Address and port number for the CLAAS RTK NET modem
k8fa90107rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x07), 
  StringSchemaField(20), 
  U16SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8fa90107rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90107rsp, k8fa90107rsp, NUMFIELDS(k8fa90107rsp))

# Returns the IP Address for the TNFS Host Address.
k8fa90108rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x08), 
  StringSchemaField(20), 
  UnusedSchemaField(7), 
  ChecksumSchemaField()
]

k8fa90108rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90108rsp, k8fa90108rsp, NUMFIELDS(k8fa90108rsp))

# Holds the upgrade/downgrade version floor and related information
k8fa90130rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x30), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(24), 
  ChecksumSchemaField()
]

k8fa90130rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90130rsp, k8fa90130rsp, NUMFIELDS(k8fa90130rsp))

# Returns whether the upgrade/downgrade is allowed
k8fa90131rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x31), 
  S8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa90131rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90131rsp, k8fa90131rsp, NUMFIELDS(k8fa90131rsp))

# Returns the mux settings of the digital output for a particular port.
k8fa90200rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa90200rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90200rsp, k8fa90200rsp, NUMFIELDS(k8fa90200rsp))

# Returns the settings of the digital input for a particular port.
k8fa90201rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa90201rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90201rsp, k8fa90201rsp, NUMFIELDS(k8fa90201rsp))

# Returns the state of the Pollux FPGA GPO
k8fa90202rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa90202rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90202rsp, k8fa90202rsp, NUMFIELDS(k8fa90202rsp))

# Information for an antenna
k8fa90300rspAntennaArrayAntennaInfo = [
  U8SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(8)
]

k8fa90300rspAntennaArrayAntennaInfoGroup = GroupSchemaField(k8fa90300rspAntennaArrayAntennaInfo,NUMFIELDS(k8fa90300rspAntennaArrayAntennaInfo))

# Provides information about connected Antennas.
k8fa90300rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ArraySchemaField(k8fa90300rspAntennaArrayAntennaInfoGroup, 4, 0,0, 8), 
  ChecksumSchemaField()
]

k8fa90300rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90300rsp, k8fa90300rsp, NUMFIELDS(k8fa90300rsp))

# Retrieves the Radar settings
k8fa90400rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x04), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa90400rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90400rsp, k8fa90400rsp, NUMFIELDS(k8fa90400rsp))

# Acknowledgement in response to TSIP Event Log Command packet: 0x8E 0xA9 0x05.
k8fa905ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x05), 
  ChecksumSchemaField()
]

k8fa905ackEntry = TSIPSchemaEntry(EServerPackets.e8fa905ack, k8fa905ack, NUMFIELDS(k8fa905ack))

# Converted ADC Channel Reading
k8fa90600rspConvertedADCChannelReadingsADCChannelReading = [
  U8SchemaField(), 
  DBLSchemaField()
]

k8fa90600rspConvertedADCChannelReadingsADCChannelReadingGroup = GroupSchemaField(k8fa90600rspConvertedADCChannelReadingsADCChannelReading,NUMFIELDS(k8fa90600rspConvertedADCChannelReadingsADCChannelReading))

# ADC Readings
k8fa90600rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fa90600rspConvertedADCChannelReadingsADCChannelReadingGroup, 5, 0,0, 32), 
  ChecksumSchemaField()
]

k8fa90600rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90600rsp, k8fa90600rsp, NUMFIELDS(k8fa90600rsp))

# Returns the mux of the Module-A digital pins
k8fa90700rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa90700rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90700rsp, k8fa90700rsp, NUMFIELDS(k8fa90700rsp))

# Returns the PWMON Control Point Status
k8fa90701rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa90701rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90701rsp, k8fa90701rsp, NUMFIELDS(k8fa90701rsp))

# Returns the Video Input selection
k8fa90703rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa90703rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90703rsp, k8fa90703rsp, NUMFIELDS(k8fa90703rsp))

# Provides Module-A auto shutdown timer settings.
k8fa90704rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa90704rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90704rsp, k8fa90704rsp, NUMFIELDS(k8fa90704rsp))

# Returns the Module A's network interface settings.
k8fa90705rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa90705rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90705rsp, k8fa90705rsp, NUMFIELDS(k8fa90705rsp))

# Module-A hardware configuration response
k8fa90706rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x06), 
  U32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa90706rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90706rsp, k8fa90706rsp, NUMFIELDS(k8fa90706rsp))

# The socket uart device configured for Port-D on the Module-A
k8fa90707rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x07), 
  U32SchemaField(), 
  StringSchemaField(32), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa90707rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90707rsp, k8fa90707rsp, NUMFIELDS(k8fa90707rsp))

# The current counters statistics for a port on the switch
k8fa90708req = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fa90708reqEntry = TSIPSchemaEntry(EClientPackets.e8fa90708req, k8fa90708req, NUMFIELDS(k8fa90708req))

# Provides the current state of RTK correction rebroadcasting
k8fa90800rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x08), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fa90800rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90800rsp, k8fa90800rsp, NUMFIELDS(k8fa90800rsp))

# Acknowledgement in response to TSIP Command packet: 0x8E 0xA9 0x08 0x00.
k8fa909ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa909ackEntry = TSIPSchemaEntry(EServerPackets.e8fa909ack, k8fa909ack, NUMFIELDS(k8fa909ack))

# Returns the state of the Receiver LED. This is in response to TSIP Request: 0x8E 0xA9 0x08 0x00.
k8fa909rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x09), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa909rspEntry = TSIPSchemaEntry(EServerPackets.e8fa909rsp, k8fa909rsp, NUMFIELDS(k8fa909rsp))
k8fa90a00rspFeaturesFeature = U8SchemaField()

# Response with all the enabled features in the Feature Manager
k8fa90a00rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x0a), 
  SubIdSchemaField(0x00), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8fa90a00rspFeaturesFeature, 5, 0,0, 200), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa90a00rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90a00rsp, k8fa90a00rsp, NUMFIELDS(k8fa90a00rsp))

# Status of a Picus Feature Manager License
k8fa90a01rspLicensesLicenseStatus = [
  U8SchemaField(), 
  U8SchemaField()
]

k8fa90a01rspLicensesLicenseStatusGroup = GroupSchemaField(k8fa90a01rspLicensesLicenseStatus,NUMFIELDS(k8fa90a01rspLicensesLicenseStatus))

# Response with the status of all installed licenses in the Feature Manager
k8fa90a01rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x0a), 
  SubIdSchemaField(0x01), 
  UnusedSchemaField(4), 
  U8SchemaField(), 
  ArraySchemaField(k8fa90a01rspLicensesLicenseStatusGroup, 5, 0,0, 100), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa90a01rspEntry = TSIPSchemaEntry(EServerPackets.e8fa90a01rsp, k8fa90a01rsp, NUMFIELDS(k8fa90a01rsp))

# Unlock status information
k8fa910rspUnlockStatusInfoArrayUnlockStatusInfo = [
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField()
]

k8fa910rspUnlockStatusInfoArrayUnlockStatusInfoGroup = GroupSchemaField(k8fa910rspUnlockStatusInfoArrayUnlockStatusInfo,NUMFIELDS(k8fa910rspUnlockStatusInfoArrayUnlockStatusInfo))

# Receiver Unlock Status Response
k8fa910rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x10), 
  U8SchemaField(), 
  ArraySchemaField(k8fa910rspUnlockStatusInfoArrayUnlockStatusInfoGroup, 3, 0,0, 20), 
  ChecksumSchemaField()
]

k8fa910rspEntry = TSIPSchemaEntry(EServerPackets.e8fa910rsp, k8fa910rsp, NUMFIELDS(k8fa910rsp))

# Product Information Response
k8fa911rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x11), 
  StringSchemaField(15), 
  StringSchemaField(20), 
  StringSchemaField(10), 
  UnusedSchemaField(40), 
  ChecksumSchemaField()
]

k8fa911rspEntry = TSIPSchemaEntry(EServerPackets.e8fa911rsp, k8fa911rsp, NUMFIELDS(k8fa911rsp))

# Boot Count Information Response
k8fa912rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x12), 
  U16SchemaField(), 
  ChecksumSchemaField()
]

k8fa912rspEntry = TSIPSchemaEntry(EServerPackets.e8fa912rsp, k8fa912rsp, NUMFIELDS(k8fa912rsp))

# Geoidal Separation Information Response
k8fa913rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x13), 
  FLTSchemaField(), 
  ChecksumSchemaField()
]

k8fa913rspEntry = TSIPSchemaEntry(EServerPackets.e8fa913rsp, k8fa913rsp, NUMFIELDS(k8fa913rsp))

# Code Bias Calibration Table Information Response
k8fa914rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

k8fa914rspEntry = TSIPSchemaEntry(EServerPackets.e8fa914rsp, k8fa914rsp, NUMFIELDS(k8fa914rsp))
k8fa91500rspmd5Hashbyte = U8SchemaField()
k8fa91500rspclientFileIdbyte = U8SchemaField()

# Response to SysFileXferInitiate command.
k8fa91500rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  FixedArraySchemaField(k8fa91500rspmd5Hashbyte, 16), 
  U8SchemaField(), 
  ArraySchemaField(k8fa91500rspclientFileIdbyte, 10, 0,0, 128), 
  ChecksumSchemaField()
]

k8fa91500rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91500rsp, k8fa91500rsp, NUMFIELDS(k8fa91500rsp))
k8fa91501rspblockDatabyte = U8SchemaField()

# Respond to SysFileXferGetBlock request
k8fa91501rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fa91501rspblockDatabyte, 7, 0,0, 256), 
  ChecksumSchemaField()
]

k8fa91501rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91501rsp, k8fa91501rsp, NUMFIELDS(k8fa91501rsp))

# Respond with results of SysFileXferPutBlock request
k8fa91502rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91502rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91502rsp, k8fa91502rsp, NUMFIELDS(k8fa91502rsp))

# Acknowledges close of stream associated with fileId
k8fa91503rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x03), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91503rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91503rsp, k8fa91503rsp, NUMFIELDS(k8fa91503rsp))

# Returns result of SysFileXferDelete command
k8fa91504rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91504rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91504rsp, k8fa91504rsp, NUMFIELDS(k8fa91504rsp))

# Sent on errors during a file transfer operation
k8fa91599rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x15), 
  SubIdSchemaField(0x99), 
  U32SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91599rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91599rsp, k8fa91599rsp, NUMFIELDS(k8fa91599rsp))

# Indicates current mux mode of GP uart in Fusion
k8fa9160000rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa9160000rspEntry = TSIPSchemaEntry(EServerPackets.e8fa9160000rsp, k8fa9160000rsp, NUMFIELDS(k8fa9160000rsp))

# Indicates current mux mode of Tx port uart in Fusion
k8fa9160001rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa9160001rspEntry = TSIPSchemaEntry(EServerPackets.e8fa9160001rsp, k8fa9160001rsp, NUMFIELDS(k8fa9160001rsp))

# Indicates current mux mode of Radio port uart in Fusion
k8fa9160002rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa9160002rspEntry = TSIPSchemaEntry(EServerPackets.e8fa9160002rsp, k8fa9160002rsp, NUMFIELDS(k8fa9160002rsp))

# Indicates current mode of the internal AP virtual uart in Fusion
k8fa9160100rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ChecksumSchemaField()
]

k8fa9160100rspEntry = TSIPSchemaEntry(EServerPackets.e8fa9160100rsp, k8fa9160100rsp, NUMFIELDS(k8fa9160100rsp))

# Report Bluetooth state (enabled or disabled)
k8fa91602rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91602rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91602rsp, k8fa91602rsp, NUMFIELDS(k8fa91602rsp))

# Report the status of the Clear All Licenses command
k8fa91603rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91603rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91603rsp, k8fa91603rsp, NUMFIELDS(k8fa91603rsp))

# Report the status of the Remove / Restore Manufacturing Licenses command
k8fa91604rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8fa91604rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91604rsp, k8fa91604rsp, NUMFIELDS(k8fa91604rsp))

# Remove Licenses By Fragment response
k8fa91605rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  UnusedSchemaField(5), 
  ChecksumSchemaField()
]

k8fa91605rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91605rsp, k8fa91605rsp, NUMFIELDS(k8fa91605rsp))

# Returns UDS diagnostic status
k8fa91606rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x16), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa91606rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91606rsp, k8fa91606rsp, NUMFIELDS(k8fa91606rsp))

# Reports the Nav's internal IMU orientation, offsets, and calibration.
k8fa91700rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(12), 
  ChecksumSchemaField()
]

k8fa91700rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91700rsp, k8fa91700rsp, NUMFIELDS(k8fa91700rsp))

# Query if IMU-Corrected positions and streaming are enabled.
k8fa91701rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fa91701rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91701rsp, k8fa91701rsp, NUMFIELDS(k8fa91701rsp))

# IMU corrected position including roll, pitch, yaw. Stream of messages enabled by 0x8e 0xa9 0x17 0x00 command.
k8fa91702rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x02), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fa91702rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91702rsp, k8fa91702rsp, NUMFIELDS(k8fa91702rsp))

# Reports the current IMU Settings covered by Block 2.
k8fa91703rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(80), 
  ChecksumSchemaField()
]

k8fa91703rspEntry = TSIPSchemaEntry(EServerPackets.e8fa91703rsp, k8fa91703rsp, NUMFIELDS(k8fa91703rsp))

# Returns the cryptochip configuration CRC value
k8fa918rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0x18), 
  U16SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fa918rspEntry = TSIPSchemaEntry(EServerPackets.e8fa918rsp, k8fa918rsp, NUMFIELDS(k8fa918rsp))

# New 27 character passcode upgrade response packet
k8fa9a5rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xa9), 
  SubIdSchemaField(0xa5), 
  U8SchemaField(), 
  StringSchemaField(65), 
  ChecksumSchemaField()
]

k8fa9a5rspEntry = TSIPSchemaEntry(EServerPackets.e8fa9a5rsp, k8fa9a5rsp, NUMFIELDS(k8fa9a5rsp))

# Provides type of specified antenna.
k8faa00rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xaa), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8faa00rspEntry = TSIPSchemaEntry(EServerPackets.e8faa00rsp, k8faa00rsp, NUMFIELDS(k8faa00rsp))

# Reports the status of the RTX subscription and shows which connections are available
k8fab00rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x00), 
  S32SchemaField(), 
  S32SchemaField(), 
  U8SchemaField(), 
  S32SchemaField(), 
  S32SchemaField(), 
  S32SchemaField(), 
  S32SchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

k8fab00rspEntry = TSIPSchemaEntry(EServerPackets.e8fab00rsp, k8fab00rsp, NUMFIELDS(k8fab00rsp))

# Reports Centerpoint RTX fast Network Info
k8fab01rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  DBLSchemaField(), 
  S32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8fab01rspEntry = TSIPSchemaEntry(EServerPackets.e8fab01rsp, k8fab01rsp, NUMFIELDS(k8fab01rsp))

# Acknowledgment that RTX std FastRestart has been cancelled
k8fab02ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

k8fab02ackEntry = TSIPSchemaEntry(EServerPackets.e8fab02ack, k8fab02ack, NUMFIELDS(k8fab02ack))

# Reports Centerpoint and RangePoint RTX Status Information
k8fab03rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(19), 
  ChecksumSchemaField()
]

k8fab03rspEntry = TSIPSchemaEntry(EServerPackets.e8fab03rsp, k8fab03rsp, NUMFIELDS(k8fab03rsp))

# Acknowledgment that RTX FastRestart vehicle movement status has been saved in the receiver 
k8fab04ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fab04ackEntry = TSIPSchemaEntry(EServerPackets.e8fab04ack, k8fab04ack, NUMFIELDS(k8fab04ack))

# Custom RTX offset
k8fab05rspRTXOffset = [
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k8fab05rspRTXOffsetGroup = GroupSchemaField(k8fab05rspRTXOffset,NUMFIELDS(k8fab05rspRTXOffset))

# Response containing RTX output settings
k8fab05rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  GroupSchemaField(k8fab05rspRTXOffset,NUMFIELDS(k8fab05rspRTXOffset)), 
  UnusedSchemaField(51), 
  ChecksumSchemaField()
]

k8fab05rspEntry = TSIPSchemaEntry(EServerPackets.e8fab05rsp, k8fab05rsp, NUMFIELDS(k8fab05rsp))

# Reports RTK/RTX Best Type Selection Info
k8fab06rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fab06rspEntry = TSIPSchemaEntry(EServerPackets.e8fab06rsp, k8fab06rsp, NUMFIELDS(k8fab06rsp))

# Response containing the current configuration and mode of the MSS Mode Switch
k8fab07rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fab07rspEntry = TSIPSchemaEntry(EServerPackets.e8fab07rsp, k8fab07rsp, NUMFIELDS(k8fab07rsp))

# Response containing realtime RTK/RTX Offsets
k8fab08rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xab), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(32), 
  ChecksumSchemaField()
]

k8fab08rspEntry = TSIPSchemaEntry(EServerPackets.e8fab08rsp, k8fab08rsp, NUMFIELDS(k8fab08rsp))

# Response with the configuration for genral parameters
k8fac0100rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  S8SchemaField(), 
  S8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8fac0100rspEntry = TSIPSchemaEntry(EServerPackets.e8fac0100rsp, k8fac0100rsp, NUMFIELDS(k8fac0100rsp))

# 
k8fac0101rspsensorsArraysensors = [
  StringSchemaField(11), 
  U8SchemaField(), 
  S8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

k8fac0101rspsensorsArraysensorsGroup = GroupSchemaField(k8fac0101rspsensorsArraysensors,NUMFIELDS(k8fac0101rspsensorsArraysensors))

# Response with the configuration for sensor parameters
k8fac0101rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fac0101rspsensorsArraysensorsGroup, 5, 0,0, 5), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8fac0101rspEntry = TSIPSchemaEntry(EServerPackets.e8fac0101rsp, k8fac0101rsp, NUMFIELDS(k8fac0101rsp))

# 
k8fac0102rspactuatorsArrayactuators = [
  StringSchemaField(11), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  S8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField()
]

k8fac0102rspactuatorsArrayactuatorsGroup = GroupSchemaField(k8fac0102rspactuatorsArrayactuators,NUMFIELDS(k8fac0102rspactuatorsArrayactuators))

# Response with the configuration for actuator parameters
k8fac0102rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fac0102rspactuatorsArrayactuatorsGroup, 5, 0,0, 3), 
  UnusedSchemaField(20), 
  ChecksumSchemaField()
]

k8fac0102rspEntry = TSIPSchemaEntry(EServerPackets.e8fac0102rsp, k8fac0102rsp, NUMFIELDS(k8fac0102rsp))

# Request for actuator calibration state
k8fac02rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fac02rspEntry = TSIPSchemaEntry(EServerPackets.e8fac02rsp, k8fac02rsp, NUMFIELDS(k8fac02rsp))

# Request for actuator calibration status
k8fac03rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fac03rspEntry = TSIPSchemaEntry(EServerPackets.e8fac03rsp, k8fac03rsp, NUMFIELDS(k8fac03rsp))

# 
k8fac04rspZoneArrayZoneStatus = [
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField()
]

k8fac04rspZoneArrayZoneStatusGroup = GroupSchemaField(k8fac04rspZoneArrayZoneStatus,NUMFIELDS(k8fac04rspZoneArrayZoneStatus))

# 
k8fac04rspSensorsArraySensorStatus = [
  S8SchemaField(), 
  FLTSchemaField()
]

k8fac04rspSensorsArraySensorStatusGroup = GroupSchemaField(k8fac04rspSensorsArraySensorStatus,NUMFIELDS(k8fac04rspSensorsArraySensorStatus))

# Reports system information including sensor heights, zone states and alerts
k8fac04rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fac04rspZoneArrayZoneStatusGroup, 7, 0,0, 3), 
  U8SchemaField(), 
  ArraySchemaField(k8fac04rspSensorsArraySensorStatusGroup, 9, 0,0, 5), 
  ChecksumSchemaField()
]

k8fac04rspEntry = TSIPSchemaEntry(EServerPackets.e8fac04rsp, k8fac04rsp, NUMFIELDS(k8fac04rsp))

# Commands to commit system actions
k8fac05rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x05), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fac05rspEntry = TSIPSchemaEntry(EServerPackets.e8fac05rsp, k8fac05rsp, NUMFIELDS(k8fac05rsp))

# Alert description
k8fac06rspAlertArrayAlertDesc = [
  U8SchemaField(), 
  U8SchemaField(), 
  StringSchemaField(11), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField()
]

k8fac06rspAlertArrayAlertDescGroup = GroupSchemaField(k8fac06rspAlertArrayAlertDesc,NUMFIELDS(k8fac06rspAlertArrayAlertDesc))

# Reponse of a list of all active faults
k8fac06rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fac06rspAlertArrayAlertDescGroup, 4, 0,0, 20), 
  ChecksumSchemaField()
]

k8fac06rspEntry = TSIPSchemaEntry(EServerPackets.e8fac06rsp, k8fac06rsp, NUMFIELDS(k8fac06rsp))

# Devices
k8fac07rspDevicesArrayDevices = [
  U8SchemaField(), 
  U8SchemaField(), 
  StringSchemaField(11), 
  U16SchemaField(), 
  U16SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField()
]

k8fac07rspDevicesArrayDevicesGroup = GroupSchemaField(k8fac07rspDevicesArrayDevices,NUMFIELDS(k8fac07rspDevicesArrayDevices))

# Reponse of a list of all attached devices
k8fac07rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xac), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fac07rspDevicesArrayDevicesGroup, 6, 0,0, 10), 
  ChecksumSchemaField()
]

k8fac07rspEntry = TSIPSchemaEntry(EServerPackets.e8fac07rsp, k8fac07rsp, NUMFIELDS(k8fac07rsp))
k8fad00rspPasscodePasscodeVal = U8SchemaField()

# Reports Centerpoint/Rangepoint RTX Passcode if available. In case no passcodes are available, PasscodeType is set to 255. Request Packet: 0x8e 0xad 0x00
k8fad00rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fad00rspPasscodePasscodeVal, 4, 0,0, 28), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fad00rspEntry = TSIPSchemaEntry(EServerPackets.e8fad00rsp, k8fad00rsp, NUMFIELDS(k8fad00rsp))

# Acknowledges command to clear passcode. Command Packet is 0x8e 0xad 0x01
k8fad01ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x01), 
  ChecksumSchemaField()
]

k8fad01ackEntry = TSIPSchemaEntry(EServerPackets.e8fad01ack, k8fad01ack, NUMFIELDS(k8fad01ack))

# Reports Centerpoint/Rangepoint RTX position allowed flag status. Request Packet: 0x8e 0xad 0x02
k8fad02rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xad), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

k8fad02rspEntry = TSIPSchemaEntry(EServerPackets.e8fad02rsp, k8fad02rsp, NUMFIELDS(k8fad02rsp))

# Response to the Bluetooth pairing information request
k8fae00rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fae00rspEntry = TSIPSchemaEntry(EServerPackets.e8fae00rsp, k8fae00rsp, NUMFIELDS(k8fae00rsp))

# Response to setting the power state of the Bluetooth module
k8fae01rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fae01rspEntry = TSIPSchemaEntry(EServerPackets.e8fae01rsp, k8fae01rsp, NUMFIELDS(k8fae01rsp))

# Response to setting the Bluetooth pairing state of the receiver
k8fae02rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fae02rspEntry = TSIPSchemaEntry(EServerPackets.e8fae02rsp, k8fae02rsp, NUMFIELDS(k8fae02rsp))

# Reponse to unpairing all Bluetooth devices
k8fae03rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fae03rspEntry = TSIPSchemaEntry(EServerPackets.e8fae03rsp, k8fae03rsp, NUMFIELDS(k8fae03rsp))

# Paring state change event
k8fae04rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x04), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(4), 
  ChecksumSchemaField()
]

k8fae04rspEntry = TSIPSchemaEntry(EServerPackets.e8fae04rsp, k8fae04rsp, NUMFIELDS(k8fae04rsp))
k8fae05rspDeviceNameChar = CHARSchemaField()

# A notification for a Bluetooth device pairing or connection event
k8fae05rsp = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x05), 
  U32SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(k8fae05rspDeviceNameChar, 4, 0,0, 250), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fae05rspEntry = TSIPSchemaEntry(EServerPackets.e8fae05rsp, k8fae05rsp, NUMFIELDS(k8fae05rsp))

# Acknowledges the request for Bluetooth device event notifications (8eae05)
k8fae05ack = [
  IdSchemaField(0x8f), 
  SubIdSchemaField(0xae), 
  SubIdSchemaField(0x05), 
  U32SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

k8fae05ackEntry = TSIPSchemaEntry(EServerPackets.e8fae05ack, k8fae05ack, NUMFIELDS(k8fae05ack))

# Requests the PPS configuration settings. The response is sent in 0xB0 0x80.
kb000req = [
  IdSchemaField(0xb0), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kb000reqEntry = TSIPSchemaEntry(EClientPackets.eb000req, kb000req, NUMFIELDS(kb000req))

# Sets the PPS configuration settings. The command is acknowleged with a 0xB0 0x80 response.
kb000cmd = [
  IdSchemaField(0xb0), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  ChecksumSchemaField()
]

kb000cmdEntry = TSIPSchemaEntry(EClientPackets.eb000cmd, kb000cmd, NUMFIELDS(kb000cmd))

# Enables or disables the specified PPS signal. The command is acknowledged with a 0xB0 0x81 response.
kb001cmd = [
  IdSchemaField(0xb0), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kb001cmdEntry = TSIPSchemaEntry(EClientPackets.eb001cmd, kb001cmd, NUMFIELDS(kb001cmd))

# Reports the PPS configuration settings. This acknowleges the 0xB0 0x00 commands.
kb080rsp = [
  IdSchemaField(0xb0), 
  SubIdSchemaField(0x80), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  ChecksumSchemaField()
]

kb080rspEntry = TSIPSchemaEntry(EServerPackets.eb080rsp, kb080rsp, NUMFIELDS(kb080rsp))

# Reports whether the specified PPS signal is enabled or disabled. This acknowledges a 0xB0 0x01 command.
kb081rsp = [
  IdSchemaField(0xb0), 
  SubIdSchemaField(0x81), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kb081rspEntry = TSIPSchemaEntry(EServerPackets.eb081rsp, kb081rsp, NUMFIELDS(kb081rsp))

# Requests primary receiver configuration block.
kbb00req = [
  IdSchemaField(0xbb), 
  SubIdSchemaField(0x00)
]

kbb00reqEntry = TSIPSchemaEntry(EClientPackets.ebb00req, kbb00req, NUMFIELDS(kbb00req))

# Sets primary receiver configuration block.
kbb00cmd = [
  IdSchemaField(0xbb), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(13)
]

kbb00cmdEntry = TSIPSchemaEntry(EClientPackets.ebb00cmd, kbb00cmd, NUMFIELDS(kbb00cmd))

# Reports primary receiver configuration parameters in response to Command Packet 0xBB 0x00.
kbb00rsp = [
  IdSchemaField(0xbb), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(13)
]

kbb00rspEntry = TSIPSchemaEntry(EServerPackets.ebb00rsp, kbb00rsp, NUMFIELDS(kbb00rsp))

# Requests the configuration of a particular serial port
kbcreq = [
  IdSchemaField(0xbc), 
  U8SchemaField()
]

kbcreqEntry = TSIPSchemaEntry(EClientPackets.ebcreq, kbcreq, NUMFIELDS(kbcreq))

# Sets the configuration of a particular serial port. This includes the port settings and input and output protocols.
kbccmd = [
  IdSchemaField(0xbc), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

kbccmdEntry = TSIPSchemaEntry(EClientPackets.ebccmd, kbccmd, NUMFIELDS(kbccmd))

# Holds the configuration of a particular serial port. This includes the port settings and input and output protocols.
kbcrsp = [
  IdSchemaField(0xbc), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField()
]

kbcrspEntry = TSIPSchemaEntry(EServerPackets.ebcrsp, kbcrsp, NUMFIELDS(kbcrsp))
kbe40cmdPacketDataData = U8SchemaField()

# Configuration packet command to the Autopilot Navigation Controller
kbe40cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  EndTerminatedArraySchemaField(kbe40cmdPacketDataData)
]

kbe40cmdEntry = TSIPSchemaEntry(EClientPackets.ebe40cmd, kbe40cmd, NUMFIELDS(kbe40cmd))

# Requests App Version(?) configuration from the Autopilot Navigation Controller
kbe400000cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe400000cmdEntry = TSIPSchemaEntry(EClientPackets.ebe400000cmd, kbe400000cmd, NUMFIELDS(kbe400000cmd))

# Requests the App Version Config version from the Autopilot Navigation Controller
kbe400003cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x03), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe400003cmdEntry = TSIPSchemaEntry(EClientPackets.ebe400003cmd, kbe400003cmd, NUMFIELDS(kbe400003cmd))

# Requests options configuration from the Autopilot Navigation Controller
kbe400100cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe400100cmdEntry = TSIPSchemaEntry(EClientPackets.ebe400100cmd, kbe400100cmd, NUMFIELDS(kbe400100cmd))

# Requests Options(?) config version from the Autopilot Navigation Controller
kbe400103cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x03), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe400103cmdEntry = TSIPSchemaEntry(EClientPackets.ebe400103cmd, kbe400103cmd, NUMFIELDS(kbe400103cmd))
kbe401400cmdTAPStringChars = CHARSchemaField()

# Configuration packet command to get TAP parameter on the Autopilot Navigation Controller
kbe401400cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x00), 
  EndTerminatedArraySchemaField(kbe401400cmdTAPStringChars), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe401400cmdEntry = TSIPSchemaEntry(EClientPackets.ebe401400cmd, kbe401400cmd, NUMFIELDS(kbe401400cmd))
kbe401401cmdTAPStringChars = CHARSchemaField()

# Configuration packet command to set TAP parameter on the Autopilot Navigation Controller
kbe401401cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x01), 
  EndTerminatedArraySchemaField(kbe401401cmdTAPStringChars), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe401401cmdEntry = TSIPSchemaEntry(EClientPackets.ebe401401cmd, kbe401401cmd, NUMFIELDS(kbe401401cmd))
kbe41cmdPacketDataData = CHARSchemaField()

# File Transfer packet command to the Autopilot Navigation Controller
kbe41cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x41), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  EndTerminatedArraySchemaField(kbe41cmdPacketDataData), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe41cmdEntry = TSIPSchemaEntry(EClientPackets.ebe41cmd, kbe41cmd, NUMFIELDS(kbe41cmd))
kbe42cmdPacketDataData = U8SchemaField()

# Remote Monitor Engineering Data packet command to the Autopilot Navigation Controller
kbe42cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x42), 
  EndTerminatedArraySchemaField(kbe42cmdPacketDataData)
]

kbe42cmdEntry = TSIPSchemaEntry(EClientPackets.ebe42cmd, kbe42cmd, NUMFIELDS(kbe42cmd))

# Gets status information for navigation
kbe4200cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x42), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4200cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4200cmd, kbe4200cmd, NUMFIELDS(kbe4200cmd))

# Gets status information for navigation
kbe4201cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x42), 
  SubIdSchemaField(0x01), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4201cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4201cmd, kbe4201cmd, NUMFIELDS(kbe4201cmd))

# Gets status information for GNSS
kbe4202cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x42), 
  SubIdSchemaField(0x02), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4202cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4202cmd, kbe4202cmd, NUMFIELDS(kbe4202cmd))

# Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets autosteering to enabled/disabled
kbe4301cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4301cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4301cmd, kbe4301cmd, NUMFIELDS(kbe4301cmd))

# Remote Monitor Control packet command to the Autopilot Navigation Controller. Sets logging to enabled/disabled
kbe4303cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4303cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4303cmd, kbe4303cmd, NUMFIELDS(kbe4303cmd))

# Remote Monitor Control packet command to the Autopilot Navigation Controller to control Steering/Speed
kbe4306cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4306cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4306cmd, kbe4306cmd, NUMFIELDS(kbe4306cmd))

# Steers left in the simulation (angle is defined in receiver firmware)
kbe43060000cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe43060000cmdEntry = TSIPSchemaEntry(EClientPackets.ebe43060000cmd, kbe43060000cmd, NUMFIELDS(kbe43060000cmd))

# Steers right in the simulation (angle is defined in receiver firmware)
kbe43060001cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe43060001cmdEntry = TSIPSchemaEntry(EClientPackets.ebe43060001cmd, kbe43060001cmd, NUMFIELDS(kbe43060001cmd))

# Sets the Simulation Steer Angle to a specific value
kbe43060002cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe43060002cmdEntry = TSIPSchemaEntry(EClientPackets.ebe43060002cmd, kbe43060002cmd, NUMFIELDS(kbe43060002cmd))

# Increases the Simulation Speed (increment is defined in receiver firmware)
kbe43060100cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe43060100cmdEntry = TSIPSchemaEntry(EClientPackets.ebe43060100cmd, kbe43060100cmd, NUMFIELDS(kbe43060100cmd))

# Decreases the Simulation Speed (increment is defined in receiver firmware)
kbe43060101cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe43060101cmdEntry = TSIPSchemaEntry(EClientPackets.ebe43060101cmd, kbe43060101cmd, NUMFIELDS(kbe43060101cmd))

# Sets the Simulation Speed to a specific value
kbe43060102cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x02), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe43060102cmdEntry = TSIPSchemaEntry(EClientPackets.ebe43060102cmd, kbe43060102cmd, NUMFIELDS(kbe43060102cmd))

# 
kbe430bcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x0b), 
  UnusedSchemaField(2), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe430bcmdEntry = TSIPSchemaEntry(EClientPackets.ebe430bcmd, kbe430bcmd, NUMFIELDS(kbe430bcmd))

# Enables/disables simulating a GPS outage in the simulation.
kbe430dcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x0d), 
  UnusedSchemaField(2), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe430dcmdEntry = TSIPSchemaEntry(EClientPackets.ebe430dcmd, kbe430dcmd, NUMFIELDS(kbe430dcmd))
kbe44cmdPacketDataData = U8SchemaField()

# Remote Monitor General Data packet command to the Autopilot Navigation Controller
kbe44cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x44), 
  EndTerminatedArraySchemaField(kbe44cmdPacketDataData)
]

kbe44cmdEntry = TSIPSchemaEntry(EClientPackets.ebe44cmd, kbe44cmd, NUMFIELDS(kbe44cmd))
kbe45cmdPacketDataData = U8SchemaField()

# Remote Monitor Waypoint Data packet command to the Autopilot Navigation Controller
kbe45cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x45), 
  EndTerminatedArraySchemaField(kbe45cmdPacketDataData)
]

kbe45cmdEntry = TSIPSchemaEntry(EClientPackets.ebe45cmd, kbe45cmd, NUMFIELDS(kbe45cmd))
kbe46cmdPacketDataData = U8SchemaField()

# Boot Monitor packet command to the Autopilot Navigation Controller
kbe46cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x46), 
  EndTerminatedArraySchemaField(kbe46cmdPacketDataData)
]

kbe46cmdEntry = TSIPSchemaEntry(EClientPackets.ebe46cmd, kbe46cmd, NUMFIELDS(kbe46cmd))

# Used to reset the steering controller on the receiver. The AGL currently first sends the SwitchToApp command, followed by ReturnMode after a delay.
kbe4600cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x46), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4600cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4600cmd, kbe4600cmd, NUMFIELDS(kbe4600cmd))
kbe47cmdPacketDataData = U8SchemaField()

# Debug packet command to the Autopilot Navigation Controller
kbe47cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  EndTerminatedArraySchemaField(kbe47cmdPacketDataData)
]

kbe47cmdEntry = TSIPSchemaEntry(EClientPackets.ebe47cmd, kbe47cmd, NUMFIELDS(kbe47cmd))

# Gets the current diagnostic error type from the Autopilot Navigation Controller
kbe470500cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470500cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470500cmd, kbe470500cmd, NUMFIELDS(kbe470500cmd))

# Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller
kbe470501cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x01), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470501cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470501cmd, kbe470501cmd, NUMFIELDS(kbe470501cmd))

# Gets a diagnostic record item from the Autopilot Navigation Controller
kbe470502cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470502cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470502cmd, kbe470502cmd, NUMFIELDS(kbe470502cmd))

# Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller
kbe470503cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x03), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470503cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470503cmd, kbe470503cmd, NUMFIELDS(kbe470503cmd))

# Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller
kbe470504cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x04), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470504cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470504cmd, kbe470504cmd, NUMFIELDS(kbe470504cmd))

# Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller
kbe470505cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x05), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470505cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470505cmd, kbe470505cmd, NUMFIELDS(kbe470505cmd))

# Gets the description of a diagnostic record item from the Autopilot Navigation Controller
kbe470506cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x06), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470506cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470506cmd, kbe470506cmd, NUMFIELDS(kbe470506cmd))

# Acknowledge the current warning on the Autopilot Navigation Controller
kbe470507cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470507cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470507cmd, kbe470507cmd, NUMFIELDS(kbe470507cmd))

# Gets the maximum number of warnings from the Autopilot Navigation Controller
kbe470508cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x08), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470508cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470508cmd, kbe470508cmd, NUMFIELDS(kbe470508cmd))

# Gets the description of a warning from the Autopilot Navigation Controller
kbe470509cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x09), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470509cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470509cmd, kbe470509cmd, NUMFIELDS(kbe470509cmd))

# Gets the maximum number of messages from the Autopilot Navigation Controller
kbe47050acmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x0a), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe47050acmdEntry = TSIPSchemaEntry(EClientPackets.ebe47050acmd, kbe47050acmd, NUMFIELDS(kbe47050acmd))

# Gets a message description from the Autopilot Navigation Controller
kbe47050bcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x0b), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe47050bcmdEntry = TSIPSchemaEntry(EClientPackets.ebe47050bcmd, kbe47050bcmd, NUMFIELDS(kbe47050bcmd))

# Gets ADC data from the Autopilot Navigation Controller
kbe4707cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4707cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4707cmd, kbe4707cmd, NUMFIELDS(kbe4707cmd))

# Debug packet command to the Autopilot Navigation Controller. Gets current port function
kbe470e08cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x08), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470e08cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470e08cmd, kbe470e08cmd, NUMFIELDS(kbe470e08cmd))

# Debug packet command to the Autopilot Navigation Controller. Sets current port function
kbe470e09cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x09), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe470e09cmdEntry = TSIPSchemaEntry(EClientPackets.ebe470e09cmd, kbe470e09cmd, NUMFIELDS(kbe470e09cmd))

# Gets number of internal vdb's from the Autopilot Controller
kbe471400cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe471400cmdEntry = TSIPSchemaEntry(EClientPackets.ebe471400cmd, kbe471400cmd, NUMFIELDS(kbe471400cmd))

# Gets a vdb record from the Autopilot Controller
kbe471401cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x01), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe471401cmdEntry = TSIPSchemaEntry(EClientPackets.ebe471401cmd, kbe471401cmd, NUMFIELDS(kbe471401cmd))

# Sets the vdb record on the Autopilot Controller
kbe471402cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe471402cmdEntry = TSIPSchemaEntry(EClientPackets.ebe471402cmd, kbe471402cmd, NUMFIELDS(kbe471402cmd))

# Gets current IMU data from the Autopilot Controller
kbe471ecmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x1e), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe471ecmdEntry = TSIPSchemaEntry(EClientPackets.ebe471ecmd, kbe471ecmd, NUMFIELDS(kbe471ecmd))
kbe4acmdPacketDataData = U8SchemaField()

# Calibration packet command to the Autopilot Navigation Controller
kbe4acmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  EndTerminatedArraySchemaField(kbe4acmdPacketDataData)
]

kbe4acmdEntry = TSIPSchemaEntry(EClientPackets.ebe4acmd, kbe4acmd, NUMFIELDS(kbe4acmd))

# Steering angle sensor calibration information request
kbe4a0b00cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0b), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4a0b00cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4a0b00cmd, kbe4a0b00cmd, NUMFIELDS(kbe4a0b00cmd))

# 
kbe4a0b01cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0b), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4a0b01cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4a0b01cmd, kbe4a0b01cmd, NUMFIELDS(kbe4a0b01cmd))

# PGain Commands which do not take any additional request data
kbe4a0ccmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0c), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4a0ccmdEntry = TSIPSchemaEntry(EClientPackets.ebe4a0ccmd, kbe4a0ccmd, NUMFIELDS(kbe4a0ccmd))

# Steering (P-gain) Calibration Information request
kbe4a0c00cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4a0c00cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4a0c00cmd, kbe4a0c00cmd, NUMFIELDS(kbe4a0c00cmd))

# Steering (P-gain) Calibration Information request (part2)
kbe4a0c08cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x08), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4a0c08cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4a0c08cmd, kbe4a0c08cmd, NUMFIELDS(kbe4a0c08cmd))

# 
kbe4a0c09cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x09), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4a0c09cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4a0c09cmd, kbe4a0c09cmd, NUMFIELDS(kbe4a0c09cmd))
kbe4bcmdPacketDataData = U8SchemaField()

# Autotester command to the Autopilot Navigation Controller.
kbe4bcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4b), 
  EndTerminatedArraySchemaField(kbe4bcmdPacketDataData)
]

kbe4bcmdEntry = TSIPSchemaEntry(EClientPackets.ebe4bcmd, kbe4bcmd, NUMFIELDS(kbe4bcmd))

# External Device packet command to read the manual override info from the Autopilot Navigation Controller
kbe4c00000004cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x04), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c00000004cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c00000004cmd, kbe4c00000004cmd, NUMFIELDS(kbe4c00000004cmd))

# External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller
kbe4c00000104cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c00000104cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c00000104cmd, kbe4c00000104cmd, NUMFIELDS(kbe4c00000104cmd))

# External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller
kbe4c00000204cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x04), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c00000204cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c00000204cmd, kbe4c00000204cmd, NUMFIELDS(kbe4c00000204cmd))

# External Device packet command to read the Gear lever info from the Autopilot Navigation Controller
kbe4c00000704cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x04), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c00000704cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c00000704cmd, kbe4c00000704cmd, NUMFIELDS(kbe4c00000704cmd))

# Autopilot Field Computer Heartbeat packet command to the Autosteer Controller
kbe4c0100cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0100cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0100cmd, kbe4c0100cmd, NUMFIELDS(kbe4c0100cmd))

# External Device packet command to turn logging on on the Autopilot Navigation Controller
kbe4c0106cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x06), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0106cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0106cmd, kbe4c0106cmd, NUMFIELDS(kbe4c0106cmd))

# External Device packet command to turn logging off on the Autopilot Navigation Controller
kbe4c0107cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0107cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0107cmd, kbe4c0107cmd, NUMFIELDS(kbe4c0107cmd))

# External Device request to get implement width
kbe4c0108req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x08), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0108reqEntry = TSIPSchemaEntry(EClientPackets.ebe4c0108req, kbe4c0108req, NUMFIELDS(kbe4c0108req))
kbe4c0108cmdImplementWidthImplementText = CHARSchemaField()

# External Device packet command to set Implement Width
kbe4c0108cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x08), 
  EndTerminatedArraySchemaField(kbe4c0108cmdImplementWidthImplementText), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0108cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0108cmd, kbe4c0108cmd, NUMFIELDS(kbe4c0108cmd))

# External Device packet command to set close any open field
kbe4c010acmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0a), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010acmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c010acmd, kbe4c010acmd, NUMFIELDS(kbe4c010acmd))

# External Device packet request to get Control State
kbe4c010breq = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0b), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010breqEntry = TSIPSchemaEntry(EClientPackets.ebe4c010breq, kbe4c010breq, NUMFIELDS(kbe4c010breq))
kbe4c010bcmdMiscDataData = U8SchemaField()

# External Device packet Control State
kbe4c010bcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0b), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbe4c010bcmdMiscDataData), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010bcmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c010bcmd, kbe4c010bcmd, NUMFIELDS(kbe4c010bcmd))

# External Device packet request to get Aggressiveness
kbe4c010dreq = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0d), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010dreqEntry = TSIPSchemaEntry(EClientPackets.ebe4c010dreq, kbe4c010dreq, NUMFIELDS(kbe4c010dreq))

# External Device packet command to set Aggressiveness
kbe4c010dcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0d), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010dcmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c010dcmd, kbe4c010dcmd, NUMFIELDS(kbe4c010dcmd))

# External Device packet request to get Task Delay
kbe4c010ereq = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0e), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010ereqEntry = TSIPSchemaEntry(EClientPackets.ebe4c010ereq, kbe4c010ereq, NUMFIELDS(kbe4c010ereq))

# External Device packet command to set Task Delay
kbe4c010ecmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0e), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010ecmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c010ecmd, kbe4c010ecmd, NUMFIELDS(kbe4c010ecmd))

# External Device packet request to get Fix Quality
kbe4c010freq = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0f), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010freqEntry = TSIPSchemaEntry(EClientPackets.ebe4c010freq, kbe4c010freq, NUMFIELDS(kbe4c010freq))

# External Device packet command to set Fix Quality
kbe4c010fcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0f), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c010fcmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c010fcmd, kbe4c010fcmd, NUMFIELDS(kbe4c010fcmd))

# External Device packet command to Get the Nudge
kbe4c011000req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011000reqEntry = TSIPSchemaEntry(EClientPackets.ebe4c011000req, kbe4c011000req, NUMFIELDS(kbe4c011000req))

# External Device packet command to set the Nudge
kbe4c011001cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011001cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011001cmd, kbe4c011001cmd, NUMFIELDS(kbe4c011001cmd))

# External Device packet command Apply Nudge
kbe4c011002cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011002cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011002cmd, kbe4c011002cmd, NUMFIELDS(kbe4c011002cmd))

# External Device packet request Get Nudge Total
kbe4c011003req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x03), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011003reqEntry = TSIPSchemaEntry(EClientPackets.ebe4c011003req, kbe4c011003req, NUMFIELDS(kbe4c011003req))

# External Device packet response to Set Total Nudge
kbe4c011004cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011004cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011004cmd, kbe4c011004cmd, NUMFIELDS(kbe4c011004cmd))

# External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller
kbe4c0111cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x11), 
  U32SchemaField(), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0111cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0111cmd, kbe4c0111cmd, NUMFIELDS(kbe4c0111cmd))

# External Device packet command to set the GGA Adjust
kbe4c0114cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0114cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0114cmd, kbe4c0114cmd, NUMFIELDS(kbe4c0114cmd))

# Point A geodetic position
kbe4c011706cmdPointA = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011706cmdPointAGroup = GroupSchemaField(kbe4c011706cmdPointA,NUMFIELDS(kbe4c011706cmdPointA))

# Point B geodetic position
kbe4c011706cmdPointB = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011706cmdPointBGroup = GroupSchemaField(kbe4c011706cmdPointB,NUMFIELDS(kbe4c011706cmdPointB))

# Point Center geodetic position
kbe4c011706cmdCenterPoint = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011706cmdCenterPointGroup = GroupSchemaField(kbe4c011706cmdCenterPoint,NUMFIELDS(kbe4c011706cmdCenterPoint))

# Field computer pattern definition for pivot ACB patterns
kbe4c011706cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x06), 
  UnusedSchemaField(2), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  UnusedSchemaField(8), 
  GroupSchemaField(kbe4c011706cmdPointA,NUMFIELDS(kbe4c011706cmdPointA)), 
  GroupSchemaField(kbe4c011706cmdPointB,NUMFIELDS(kbe4c011706cmdPointB)), 
  GroupSchemaField(kbe4c011706cmdCenterPoint,NUMFIELDS(kbe4c011706cmdCenterPoint)), 
  DBLSchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011706cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011706cmd, kbe4c011706cmd, NUMFIELDS(kbe4c011706cmd))

# Point A geodetic position
kbe4c011710cmdPointA = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011710cmdPointAGroup = GroupSchemaField(kbe4c011710cmdPointA,NUMFIELDS(kbe4c011710cmdPointA))

# Point B geodetic position
kbe4c011710cmdPointB = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011710cmdPointBGroup = GroupSchemaField(kbe4c011710cmdPointB,NUMFIELDS(kbe4c011710cmdPointB))

# Swath by swath pattern definition command (PTRN_SWATH_BY_SWATH)
kbe4c011710cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x10), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  GroupSchemaField(kbe4c011710cmdPointA,NUMFIELDS(kbe4c011710cmdPointA)), 
  GroupSchemaField(kbe4c011710cmdPointB,NUMFIELDS(kbe4c011710cmdPointB)), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011710cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011710cmd, kbe4c011710cmd, NUMFIELDS(kbe4c011710cmd))

# 
kbe4c011711cmdPointsPoint = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011711cmdPointsPointGroup = GroupSchemaField(kbe4c011711cmdPointsPoint,NUMFIELDS(kbe4c011711cmdPointsPoint))

# Swath section pattern definition command (PTRN_SWATH_SECTION)
kbe4c011711cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x11), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(7), 
  ArraySchemaField(kbe4c011711cmdPointsPointGroup, 7, 0,0, 250), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011711cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011711cmd, kbe4c011711cmd, NUMFIELDS(kbe4c011711cmd))

# Point A geodetic position
kbe4c011713cmdPointA = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011713cmdPointAGroup = GroupSchemaField(kbe4c011713cmdPointA,NUMFIELDS(kbe4c011713cmdPointA))

# Point B geodetic position
kbe4c011713cmdPointB = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011713cmdPointBGroup = GroupSchemaField(kbe4c011713cmdPointB,NUMFIELDS(kbe4c011713cmdPointB))

# Swath by swath fragment pattern definition command (PTRN_SWATH_BY_SWATH_FRAGMENT)
kbe4c011713cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x13), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  GroupSchemaField(kbe4c011713cmdPointA,NUMFIELDS(kbe4c011713cmdPointA)), 
  GroupSchemaField(kbe4c011713cmdPointB,NUMFIELDS(kbe4c011713cmdPointB)), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011713cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011713cmd, kbe4c011713cmd, NUMFIELDS(kbe4c011713cmd))

# Point A geodetic position
kbe4c011720cmdPointA = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011720cmdPointAGroup = GroupSchemaField(kbe4c011720cmdPointA,NUMFIELDS(kbe4c011720cmdPointA))

# Point B geodetic position
kbe4c011720cmdPointB = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011720cmdPointBGroup = GroupSchemaField(kbe4c011720cmdPointB,NUMFIELDS(kbe4c011720cmdPointB))

# Swath by swath FFA pattern definition command (PTRN_SWATH_BY_SWATH_FFA)
kbe4c011720cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x20), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  GroupSchemaField(kbe4c011720cmdPointA,NUMFIELDS(kbe4c011720cmdPointA)), 
  GroupSchemaField(kbe4c011720cmdPointB,NUMFIELDS(kbe4c011720cmdPointB)), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011720cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011720cmd, kbe4c011720cmd, NUMFIELDS(kbe4c011720cmd))

# Geodetic position
kbe4c011721cmdPointsPoint = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbe4c011721cmdPointsPointGroup = GroupSchemaField(kbe4c011721cmdPointsPoint,NUMFIELDS(kbe4c011721cmdPointsPoint))

# Swath section FFA pattern definition command (PTRN_SWATH_SECTION_FFA)
kbe4c011721cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x21), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(7), 
  ArraySchemaField(kbe4c011721cmdPointsPointGroup, 7, 0,0, 250), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011721cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011721cmd, kbe4c011721cmd, NUMFIELDS(kbe4c011721cmd))

#  This packet should be sent from the Field Computer to the Controller when communication is established. It allows the controller to identify what hardware it is connected to and allows the Field Computer (from the Controller's response) to know what sort of Controller the Field Computer is connected to
kbe4c0119cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x19), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c0119cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c0119cmd, kbe4c0119cmd, NUMFIELDS(kbe4c0119cmd))

# Extended Field Computer Heartbeat packet command to the Autosteer Controller
kbe4c011acmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x1a), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c011acmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c011acmd, kbe4c011acmd, NUMFIELDS(kbe4c011acmd))

# External Device packet to request the enable state of the guidance status message
kbe4c2000req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x20), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c2000reqEntry = TSIPSchemaEntry(EClientPackets.ebe4c2000req, kbe4c2000req, NUMFIELDS(kbe4c2000req))

# External Device packet command to set the automatic update of the guidance status message
kbe4c2000cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x20), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c2000cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c2000cmd, kbe4c2000cmd, NUMFIELDS(kbe4c2000cmd))

# External Device packet to request the guidance status message
kbe4c2001req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x20), 
  SubIdSchemaField(0x01), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c2001reqEntry = TSIPSchemaEntry(EClientPackets.ebe4c2001req, kbe4c2001req, NUMFIELDS(kbe4c2001req))

# New Path command starts a new guidance path. Set points to be interpreted as Polyline or Clothoid points
kbe4c2300cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c2300cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c2300cmd, kbe4c2300cmd, NUMFIELDS(kbe4c2300cmd))

# Extend the guidance path by 1 point. Each point has a position XYZ and optional parameters for Clothoids
kbe4c2301cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c2301cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c2301cmd, kbe4c2301cmd, NUMFIELDS(kbe4c2301cmd))

# Query the usage of the clothoid guidance path for steering the vehicle.
kbe4c2302req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x02)
]

kbe4c2302reqEntry = TSIPSchemaEntry(EClientPackets.ebe4c2302req, kbe4c2302req, NUMFIELDS(kbe4c2302req))

# Send to configure usage of the clothoid guidance path for steering the vehicle.
kbe4c2302cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c2302cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c2302cmd, kbe4c2302cmd, NUMFIELDS(kbe4c2302cmd))

# Informs the NAV that a Nextswath related button was pressed on the display
kbe4c8000cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x80), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c8000cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c8000cmd, kbe4c8000cmd, NUMFIELDS(kbe4c8000cmd))

# 
kbe4c8001cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x80), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe4c8001cmdEntry = TSIPSchemaEntry(EClientPackets.ebe4c8001cmd, kbe4c8001cmd, NUMFIELDS(kbe4c8001cmd))
kbe4dcmdPacketDataData = U8SchemaField()

# GPS simulation command to the Autopilot Navigation Controller. Used for NAV to NAV communication.
kbe4dcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4d), 
  EndTerminatedArraySchemaField(kbe4dcmdPacketDataData)
]

kbe4dcmdEntry = TSIPSchemaEntry(EClientPackets.ebe4dcmd, kbe4dcmd, NUMFIELDS(kbe4dcmd))
kbe4ecmdPacketDataData = U8SchemaField()

# Piped message command to the Autopilot Navigation Controller.
kbe4ecmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4e), 
  EndTerminatedArraySchemaField(kbe4ecmdPacketDataData)
]

kbe4ecmdEntry = TSIPSchemaEntry(EClientPackets.ebe4ecmd, kbe4ecmd, NUMFIELDS(kbe4ecmd))
kbe4fcmdPacketDataData = U8SchemaField()

# This is an alias to 0x8e 0xa1.
kbe4fcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x4f), 
  EndTerminatedArraySchemaField(kbe4fcmdPacketDataData), 
  ChecksumSchemaField()
]

kbe4fcmdEntry = TSIPSchemaEntry(EClientPackets.ebe4fcmd, kbe4fcmd, NUMFIELDS(kbe4fcmd))
kbe50cmdPacketDataData = U8SchemaField()

# Configuration packet command to the Autosteer Controller
kbe50cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x50), 
  EndTerminatedArraySchemaField(kbe50cmdPacketDataData)
]

kbe50cmdEntry = TSIPSchemaEntry(EClientPackets.ebe50cmd, kbe50cmd, NUMFIELDS(kbe50cmd))
kbe5014cmdPacketDataData = U8SchemaField()

# TAP packet command to the Autosteer Controller
kbe5014cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x50), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbe5014cmdPacketDataData)
]

kbe5014cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5014cmd, kbe5014cmd, NUMFIELDS(kbe5014cmd))
kbe51cmdPacketDataData = U8SchemaField()

# File Transfer packet command to the Autosteer Controller
kbe51cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x51), 
  EndTerminatedArraySchemaField(kbe51cmdPacketDataData)
]

kbe51cmdEntry = TSIPSchemaEntry(EClientPackets.ebe51cmd, kbe51cmd, NUMFIELDS(kbe51cmd))
kbe52cmdPacketDataData = U8SchemaField()

# Remote Monitor Engineering Data packet command to the Autosteer Controller
kbe52cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x52), 
  EndTerminatedArraySchemaField(kbe52cmdPacketDataData)
]

kbe52cmdEntry = TSIPSchemaEntry(EClientPackets.ebe52cmd, kbe52cmd, NUMFIELDS(kbe52cmd))
kbe53cmdPacketDataData = U8SchemaField()

# Remote Monitor Control packet command to the Autosteer Controller
kbe53cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x53), 
  EndTerminatedArraySchemaField(kbe53cmdPacketDataData)
]

kbe53cmdEntry = TSIPSchemaEntry(EClientPackets.ebe53cmd, kbe53cmd, NUMFIELDS(kbe53cmd))

# Remote Monitor Control Steering packet command to the Autosteer Controller
kbe530600cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x53), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe530600cmdEntry = TSIPSchemaEntry(EClientPackets.ebe530600cmd, kbe530600cmd, NUMFIELDS(kbe530600cmd))

# Remote Monitor Control Speed packet command to the Autosteer Controller
kbe530601cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x53), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe530601cmdEntry = TSIPSchemaEntry(EClientPackets.ebe530601cmd, kbe530601cmd, NUMFIELDS(kbe530601cmd))
kbe54cmdPacketDataData = U8SchemaField()

# Remote Monitor General Data packet command to the Autosteer Controller
kbe54cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x54), 
  EndTerminatedArraySchemaField(kbe54cmdPacketDataData)
]

kbe54cmdEntry = TSIPSchemaEntry(EClientPackets.ebe54cmd, kbe54cmd, NUMFIELDS(kbe54cmd))
kbe55cmdPacketDataData = U8SchemaField()

# Remote Monitor Waypoint Data packet command to the Autosteer Controller
kbe55cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x55), 
  EndTerminatedArraySchemaField(kbe55cmdPacketDataData)
]

kbe55cmdEntry = TSIPSchemaEntry(EClientPackets.ebe55cmd, kbe55cmd, NUMFIELDS(kbe55cmd))
kbe56cmdPacketDataData = U8SchemaField()

# Boot Monitor packet command to the Autosteer Controller
kbe56cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x56), 
  EndTerminatedArraySchemaField(kbe56cmdPacketDataData)
]

kbe56cmdEntry = TSIPSchemaEntry(EClientPackets.ebe56cmd, kbe56cmd, NUMFIELDS(kbe56cmd))
kbe57cmdPacketDataData = U8SchemaField()

# Debug packet command to the Autosteer Controller
kbe57cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x57), 
  EndTerminatedArraySchemaField(kbe57cmdPacketDataData)
]

kbe57cmdEntry = TSIPSchemaEntry(EClientPackets.ebe57cmd, kbe57cmd, NUMFIELDS(kbe57cmd))

# Field Computer Ack Current Warning packet command to the Autosteer Controller
kbe570507cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x57), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe570507cmdEntry = TSIPSchemaEntry(EClientPackets.ebe570507cmd, kbe570507cmd, NUMFIELDS(kbe570507cmd))
kbe5acmdPacketDataData = U8SchemaField()

# Calibration packet command to the Autosteer Controller
kbe5acmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5a), 
  EndTerminatedArraySchemaField(kbe5acmdPacketDataData)
]

kbe5acmdEntry = TSIPSchemaEntry(EClientPackets.ebe5acmd, kbe5acmd, NUMFIELDS(kbe5acmd))
kbe5ccmdPacketDataData = U8SchemaField()

# External Device packet command to the Autosteer Controller
kbe5ccmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  EndTerminatedArraySchemaField(kbe5ccmdPacketDataData)
]

kbe5ccmdEntry = TSIPSchemaEntry(EClientPackets.ebe5ccmd, kbe5ccmd, NUMFIELDS(kbe5ccmd))

# Field Computer Heartbeat packet command to the Autosteer Controller
kbe5c0100cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c0100cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c0100cmd, kbe5c0100cmd, NUMFIELDS(kbe5c0100cmd))

# Field Computer Logging On packet command to the Autosteer Controller
kbe5c0106cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x06), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c0106cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c0106cmd, kbe5c0106cmd, NUMFIELDS(kbe5c0106cmd))

# Field Computer Logging Off packet command to the Autosteer Controller
kbe5c0107cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c0107cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c0107cmd, kbe5c0107cmd, NUMFIELDS(kbe5c0107cmd))

# Field Computer Close Field packet command to the Autosteer Controller
kbe5c010acmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0a), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c010acmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c010acmd, kbe5c010acmd, NUMFIELDS(kbe5c010acmd))

# Field Computer Control State packet command to the Autosteer Controller
kbe5c010bcmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0b), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c010bcmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c010bcmd, kbe5c010bcmd, NUMFIELDS(kbe5c010bcmd))

# Field Computer Get Nudge packet command to the Autosteer Controller
kbe5c011000cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011000cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011000cmd, kbe5c011000cmd, NUMFIELDS(kbe5c011000cmd))

# Field Computer Set Nudge packet command to the Autosteer Controller
kbe5c011001cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011001cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011001cmd, kbe5c011001cmd, NUMFIELDS(kbe5c011001cmd))

# Field Computer Apply Nudge packet command to the Autosteer Controller
kbe5c011002cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011002cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011002cmd, kbe5c011002cmd, NUMFIELDS(kbe5c011002cmd))

# Field Computer Get Total Nudge packet command to the Autosteer Controller
kbe5c011003cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x03), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011003cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011003cmd, kbe5c011003cmd, NUMFIELDS(kbe5c011003cmd))

# Field Computer Set Total Nudge packet command to the Autosteer Controller
kbe5c011004cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011004cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011004cmd, kbe5c011004cmd, NUMFIELDS(kbe5c011004cmd))

# Field Computer NMEA configuration packet command to the Autosteer Controller
kbe5c0111cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x11), 
  U32SchemaField(), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c0111cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c0111cmd, kbe5c0111cmd, NUMFIELDS(kbe5c0111cmd))

# Field Computer Adjust GGA position command to the Autosteer Controller
kbe5c0114cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c0114cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c0114cmd, kbe5c0114cmd, NUMFIELDS(kbe5c0114cmd))

# Field Computer Pattern Definition Parallel A/B packet command to the Autosteer Controller
kbe5c011700cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011700cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011700cmd, kbe5c011700cmd, NUMFIELDS(kbe5c011700cmd))

# Field Computer Pattern Definition Pivot packet command to the Autosteer Controller
kbe5c011706cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x06), 
  U16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011706cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011706cmd, kbe5c011706cmd, NUMFIELDS(kbe5c011706cmd))

# Field Computer Pattern Definition Swath By Swath packet command to the Autosteer Controller
kbe5c011710cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x10), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011710cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011710cmd, kbe5c011710cmd, NUMFIELDS(kbe5c011710cmd))
kbe5c011711cmdPacketDataData = U8SchemaField()

# Field Computer Pattern Definition Swath Section packet command to the Autosteer Controller
kbe5c011711cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x11), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbe5c011711cmdPacketDataData)
]

kbe5c011711cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011711cmd, kbe5c011711cmd, NUMFIELDS(kbe5c011711cmd))

# Field Computer Pattern Definition Swath By Swath Fragment packet command to the Autosteer Controller
kbe5c011713cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x17), 
  SubIdSchemaField(0x13), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c011713cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c011713cmd, kbe5c011713cmd, NUMFIELDS(kbe5c011713cmd))

# Field Computer Information packet command to the Autosteer Controller
kbe5c0119cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x19), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe5c0119cmdEntry = TSIPSchemaEntry(EClientPackets.ebe5c0119cmd, kbe5c0119cmd, NUMFIELDS(kbe5c0119cmd))
kbe60cmdPacketDataData = U8SchemaField()

# Configuration packet command to the INS feature
kbe60cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x60), 
  EndTerminatedArraySchemaField(kbe60cmdPacketDataData)
]

kbe60cmdEntry = TSIPSchemaEntry(EClientPackets.ebe60cmd, kbe60cmd, NUMFIELDS(kbe60cmd))
kbe6014cmdPacketDataData = U8SchemaField()

# TAP packet command to the Inertial Nav feature
kbe6014cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x60), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbe6014cmdPacketDataData)
]

kbe6014cmdEntry = TSIPSchemaEntry(EClientPackets.ebe6014cmd, kbe6014cmd, NUMFIELDS(kbe6014cmd))

# Remote Monitor Control Steering packet command to the Inertial Nav feature
kbe630600cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x63), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe630600cmdEntry = TSIPSchemaEntry(EClientPackets.ebe630600cmd, kbe630600cmd, NUMFIELDS(kbe630600cmd))

# Remote Monitor Control Speed packet command to the Inertial Nav feature
kbe630601cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x63), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe630601cmdEntry = TSIPSchemaEntry(EClientPackets.ebe630601cmd, kbe630601cmd, NUMFIELDS(kbe630601cmd))

# Publish Parameter Block Hardware Information packet request from the Autopilot Navigation Controller
kbe710000req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710000reqEntry = TSIPSchemaEntry(EClientPackets.ebe710000req, kbe710000req, NUMFIELDS(kbe710000req))

# Publish Parameter Block Software Information packet request from the Autopilot Navigation Controller
kbe710100req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710100reqEntry = TSIPSchemaEntry(EClientPackets.ebe710100req, kbe710100req, NUMFIELDS(kbe710100req))

# Publish Parameter Block OPS Config Information packet request from the Autopilot Navigation Controller
kbe710200req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710200reqEntry = TSIPSchemaEntry(EClientPackets.ebe710200req, kbe710200req, NUMFIELDS(kbe710200req))

# Publish Parameter Block OPS Config Information packet SET from the Display    to Autopilot Nudge and Draft
kbe710201req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710201reqEntry = TSIPSchemaEntry(EClientPackets.ebe710201req, kbe710201req, NUMFIELDS(kbe710201req))

# Publish Parameter Block Platform Config Information packet request from the Autopilot Navigation Controller
kbe710300req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710300reqEntry = TSIPSchemaEntry(EClientPackets.ebe710300req, kbe710300req, NUMFIELDS(kbe710300req))

# Publish Parameter Block Safety Config Information packet request from the Autopilot Navigation Controller
kbe710400req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x04), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710400reqEntry = TSIPSchemaEntry(EClientPackets.ebe710400req, kbe710400req, NUMFIELDS(kbe710400req))

# Publish Parameter Block Version Information packet request from the Autopilot Navigation Controller
kbe710500req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710500reqEntry = TSIPSchemaEntry(EClientPackets.ebe710500req, kbe710500req, NUMFIELDS(kbe710500req))

# Publish Parameter Block Sensor Hyd Status Information packet request from the Autopilot Navigation Controller
kbe710600req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710600reqEntry = TSIPSchemaEntry(EClientPackets.ebe710600req, kbe710600req, NUMFIELDS(kbe710600req))

# Publish Parameter Block Raw Sensor Status Information packet request from the Autopilot Navigation Controller
kbe710700req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710700reqEntry = TSIPSchemaEntry(EClientPackets.ebe710700req, kbe710700req, NUMFIELDS(kbe710700req))

# Publish Parameter Block Selected IMU Status Information packet request from the Autopilot Navigation Controller
kbe710800req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x08), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710800reqEntry = TSIPSchemaEntry(EClientPackets.ebe710800req, kbe710800req, NUMFIELDS(kbe710800req))

# Publish Parameter Block CS Information packet request from the Autopilot Navigation Controller
kbe710900req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x09), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710900reqEntry = TSIPSchemaEntry(EClientPackets.ebe710900req, kbe710900req, NUMFIELDS(kbe710900req))

# Publish Parameter Block Group1 Information packet request from the Autopilot Navigation Controller
kbe710a00req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0a), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710a00reqEntry = TSIPSchemaEntry(EClientPackets.ebe710a00req, kbe710a00req, NUMFIELDS(kbe710a00req))

# Publish Parameter Block Group2 Information packet request from the Autopilot Navigation Controller
kbe710b00req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0b), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710b00reqEntry = TSIPSchemaEntry(EClientPackets.ebe710b00req, kbe710b00req, NUMFIELDS(kbe710b00req))

# Publish Parameter Block Group3 Information packet request from the Autopilot Navigation Controller
kbe710c00req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710c00reqEntry = TSIPSchemaEntry(EClientPackets.ebe710c00req, kbe710c00req, NUMFIELDS(kbe710c00req))

# Publish Parameter Block GPS Guidance Status Information packet request from the Autopilot Navigation Controller
kbe710d00req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0d), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710d00reqEntry = TSIPSchemaEntry(EClientPackets.ebe710d00req, kbe710d00req, NUMFIELDS(kbe710d00req))

# Publish Parameter Block GPS Guidance Diag Information packet request from the Autopilot Navigation Controller
kbe710e00req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710e00reqEntry = TSIPSchemaEntry(EClientPackets.ebe710e00req, kbe710e00req, NUMFIELDS(kbe710e00req))

# Publish Parameter Block Group4 Information packet request from the Autopilot Navigation Controller
kbe710f00req = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0f), 
  SubIdSchemaField(0x00), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbe710f00reqEntry = TSIPSchemaEntry(EClientPackets.ebe710f00req, kbe710f00req, NUMFIELDS(kbe710f00req))

# FFA command to Autopilot Navigation Controller.
kbe8000cmd = [
  IdSchemaField(0xbe), 
  SubIdSchemaField(0x80), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField()
]

kbe8000cmdEntry = TSIPSchemaEntry(EClientPackets.ebe8000cmd, kbe8000cmd, NUMFIELDS(kbe8000cmd))
kbf1arspPacketDataData = U8SchemaField()

# Wraps Autopilot API NMEA messages for output in a TSIP stream.
kbf1arsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x1a), 
  EndTerminatedArraySchemaField(kbf1arspPacketDataData)
]

kbf1arspEntry = TSIPSchemaEntry(EServerPackets.ebf1arsp, kbf1arsp, NUMFIELDS(kbf1arsp))
kbf40rspPacketDataData = U8SchemaField()

# Configuration packet response from the Autopilot Navigation Controller
kbf40rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x40), 
  EndTerminatedArraySchemaField(kbf40rspPacketDataData)
]

kbf40rspEntry = TSIPSchemaEntry(EServerPackets.ebf40rsp, kbf40rsp, NUMFIELDS(kbf40rsp))

# Requests App Version(?) configuration from the Autopilot Navigation Controller
kbf400000rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  StringSchemaField(8), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(2), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  U32SchemaField(), 
  UnusedSchemaField(4), 
  UnusedSchemaField(4), 
  UnusedSchemaField(4), 
  UnusedSchemaField(4), 
  UnusedSchemaField(4), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf400000rspEntry = TSIPSchemaEntry(EServerPackets.ebf400000rsp, kbf400000rsp, NUMFIELDS(kbf400000rsp))
kbf400100rspOptionsOption = U8SchemaField()

# Requests options configuration from the Autopilot Navigation Controller
kbf400100rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  StringSchemaField(16), 
  EndTerminatedArraySchemaField(kbf400100rspOptionsOption), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf400100rspEntry = TSIPSchemaEntry(EServerPackets.ebf400100rsp, kbf400100rsp, NUMFIELDS(kbf400100rsp))
kbf401400rspTAPStringChars = CHARSchemaField()

# Configuration packet response to get TAP parameter from the Autopilot Navigation Controller
kbf401400rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x00), 
  EndTerminatedArraySchemaField(kbf401400rspTAPStringChars), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf401400rspEntry = TSIPSchemaEntry(EServerPackets.ebf401400rsp, kbf401400rsp, NUMFIELDS(kbf401400rsp))
kbf401401rspTAPStringChars = CHARSchemaField()

# Configuration packet response from setting a TAP parameter on the Autopilot Navigation Controller
kbf401401rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x40), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x01), 
  EndTerminatedArraySchemaField(kbf401401rspTAPStringChars), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf401401rspEntry = TSIPSchemaEntry(EServerPackets.ebf401401rsp, kbf401401rsp, NUMFIELDS(kbf401401rsp))
kbf41rspPacketDataData = CHARSchemaField()

# File Transfer packet response from the Autopilot Navigation Controller
kbf41rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x41), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  EndTerminatedArraySchemaField(kbf41rspPacketDataData), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf41rspEntry = TSIPSchemaEntry(EServerPackets.ebf41rsp, kbf41rsp, NUMFIELDS(kbf41rsp))
kbf42rspPacketDataData = U8SchemaField()

# Remote Monitor Engineering Data packet response from the Autopilot Navigation Controller
kbf42rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x42), 
  EndTerminatedArraySchemaField(kbf42rspPacketDataData)
]

kbf42rspEntry = TSIPSchemaEntry(EServerPackets.ebf42rsp, kbf42rsp, NUMFIELDS(kbf42rsp))

# Gets status information for navigation
kbf4200rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x42), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4200rspEntry = TSIPSchemaEntry(EServerPackets.ebf4200rsp, kbf4200rsp, NUMFIELDS(kbf4200rsp))

# Gets status information for navigation
kbf4201rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x42), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4201rspEntry = TSIPSchemaEntry(EServerPackets.ebf4201rsp, kbf4201rsp, NUMFIELDS(kbf4201rsp))

# Gets status information for GNSS
kbf4202rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x42), 
  SubIdSchemaField(0x02), 
  U32SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(1), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4202rspEntry = TSIPSchemaEntry(EServerPackets.ebf4202rsp, kbf4202rsp, NUMFIELDS(kbf4202rsp))
kbf43rspPacketDataData = U8SchemaField()

# Remote Monitor Control packet response from the Autopilot Navigation Controller
kbf43rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x43), 
  EndTerminatedArraySchemaField(kbf43rspPacketDataData)
]

kbf43rspEntry = TSIPSchemaEntry(EServerPackets.ebf43rsp, kbf43rsp, NUMFIELDS(kbf43rsp))

# Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets autosteering to enabled/disabled
kbf4301rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4301rspEntry = TSIPSchemaEntry(EServerPackets.ebf4301rsp, kbf4301rsp, NUMFIELDS(kbf4301rsp))

# Remote Monitor Control packet response from the Autopilot Navigation Controller. Sets logging to enabled/disabled
kbf4303rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x03), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4303rspEntry = TSIPSchemaEntry(EServerPackets.ebf4303rsp, kbf4303rsp, NUMFIELDS(kbf4303rsp))

# Remote Monitor Control packet response from the Autopilot Navigation Controller to control Steering/Speed
kbf4306rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x43), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4306rspEntry = TSIPSchemaEntry(EServerPackets.ebf4306rsp, kbf4306rsp, NUMFIELDS(kbf4306rsp))
kbf44rspPacketDataData = U8SchemaField()

# Remote Monitor General Data packet response from the Autopilot Navigation Controller
kbf44rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x44), 
  EndTerminatedArraySchemaField(kbf44rspPacketDataData)
]

kbf44rspEntry = TSIPSchemaEntry(EServerPackets.ebf44rsp, kbf44rsp, NUMFIELDS(kbf44rsp))
kbf45rspPacketDataData = U8SchemaField()

# Remote Monitor Waypoint Data packet response from the Autopilot Navigation Controller
kbf45rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x45), 
  EndTerminatedArraySchemaField(kbf45rspPacketDataData)
]

kbf45rspEntry = TSIPSchemaEntry(EServerPackets.ebf45rsp, kbf45rsp, NUMFIELDS(kbf45rsp))
kbf46rspPacketDataData = U8SchemaField()

# Boot Monitor packet response from the Autopilot Navigation Controller
kbf46rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x46), 
  EndTerminatedArraySchemaField(kbf46rspPacketDataData)
]

kbf46rspEntry = TSIPSchemaEntry(EServerPackets.ebf46rsp, kbf46rsp, NUMFIELDS(kbf46rsp))
kbf47rspPacketDataData = U8SchemaField()

# Debug packet response from the Autopilot Navigation Controller
kbf47rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  EndTerminatedArraySchemaField(kbf47rspPacketDataData)
]

kbf47rspEntry = TSIPSchemaEntry(EServerPackets.ebf47rsp, kbf47rsp, NUMFIELDS(kbf47rsp))

# Gets the current diagnostic error type from the Autopilot Navigation Controller
kbf470500rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470500rspEntry = TSIPSchemaEntry(EServerPackets.ebf470500rsp, kbf470500rsp, NUMFIELDS(kbf470500rsp))

# Clears the diagnostic summary of the current error and updates the summary on the Autopilot Navigation Controller
kbf470501rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x01), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470501rspEntry = TSIPSchemaEntry(EServerPackets.ebf470501rsp, kbf470501rsp, NUMFIELDS(kbf470501rsp))
kbf470502rspErrorValuesValue = FLTSchemaField()

# Gets a diagnostic record item from the Autopilot Navigation Controller
kbf470502rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  FixedArraySchemaField(kbf470502rspErrorValuesValue, 3), 
  U16SchemaField(), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470502rspEntry = TSIPSchemaEntry(EServerPackets.ebf470502rsp, kbf470502rsp, NUMFIELDS(kbf470502rsp))
kbf470503rspErrorValuesValue = FLTSchemaField()

# Clears the diagnostic summary of the specified error and returns it on the Autopilot Navigation Controller
kbf470503rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x03), 
  U16SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  FixedArraySchemaField(kbf470503rspErrorValuesValue, 3), 
  U16SchemaField(), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470503rspEntry = TSIPSchemaEntry(EServerPackets.ebf470503rsp, kbf470503rsp, NUMFIELDS(kbf470503rsp))
kbf470504rspErrorValuesValue = FLTSchemaField()

# Gets a diagnostic record item for the specified component from the Autopilot Navigation Controller
kbf470504rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x04), 
  U16SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  FixedArraySchemaField(kbf470504rspErrorValuesValue, 3), 
  U16SchemaField(), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470504rspEntry = TSIPSchemaEntry(EServerPackets.ebf470504rsp, kbf470504rsp, NUMFIELDS(kbf470504rsp))

# Gets the maximum number of error diagnostic items (error types) from the Autopilot Navigation Controller
kbf470505rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x05), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470505rspEntry = TSIPSchemaEntry(EServerPackets.ebf470505rsp, kbf470505rsp, NUMFIELDS(kbf470505rsp))
kbf470506rspStringCharacter = CHARSchemaField()

# Gets the description of a diagnostic record item from the Autopilot Navigation Controller
kbf470506rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x06), 
  U16SchemaField(), 
  EndTerminatedArraySchemaField(kbf470506rspStringCharacter), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470506rspEntry = TSIPSchemaEntry(EServerPackets.ebf470506rsp, kbf470506rsp, NUMFIELDS(kbf470506rsp))

# Acknowledge the current warning on the Autopilot Navigation Controller
kbf470507rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470507rspEntry = TSIPSchemaEntry(EServerPackets.ebf470507rsp, kbf470507rsp, NUMFIELDS(kbf470507rsp))

# Gets the maximum number of warnings from the Autopilot Navigation Controller
kbf470508rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x08), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470508rspEntry = TSIPSchemaEntry(EServerPackets.ebf470508rsp, kbf470508rsp, NUMFIELDS(kbf470508rsp))
kbf470509rspStringCharacter = CHARSchemaField()

# Gets the description of a warning from the Autopilot Navigation Controller
kbf470509rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x09), 
  U16SchemaField(), 
  EndTerminatedArraySchemaField(kbf470509rspStringCharacter), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470509rspEntry = TSIPSchemaEntry(EServerPackets.ebf470509rsp, kbf470509rsp, NUMFIELDS(kbf470509rsp))

# Gets the maximum number of messages from the Autopilot Navigation Controller
kbf47050arsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x0a), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf47050arspEntry = TSIPSchemaEntry(EServerPackets.ebf47050arsp, kbf47050arsp, NUMFIELDS(kbf47050arsp))
kbf47050brspStringCharacter = CHARSchemaField()

# Gets a message description from the Autopilot Navigation Controller
kbf47050brsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x0b), 
  U16SchemaField(), 
  EndTerminatedArraySchemaField(kbf47050brspStringCharacter), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf47050brspEntry = TSIPSchemaEntry(EServerPackets.ebf47050brsp, kbf47050brsp, NUMFIELDS(kbf47050brsp))
kbf4707rspHighPrecisionADCHighPrecisionADCChannel = FLTSchemaField()
kbf4707rspLowPrecisionADCLowPrecisionADCChannel = FLTSchemaField()

# Gets ADC data from the Autopilot Navigation Controller
kbf4707rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x07), 
  UnusedSchemaField(3), 
  FixedArraySchemaField(kbf4707rspHighPrecisionADCHighPrecisionADCChannel, 8), 
  FixedArraySchemaField(kbf4707rspLowPrecisionADCLowPrecisionADCChannel, 17), 
  U32SchemaField(), 
  UnusedSchemaField(1), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4707rspEntry = TSIPSchemaEntry(EServerPackets.ebf4707rsp, kbf4707rsp, NUMFIELDS(kbf4707rsp))
kbf470e06rspPacketDataChars = CHARSchemaField()

# Debug packet response from the Autopilot Navigation Controller. Contains .dbg file header
kbf470e06rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x06), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(kbf470e06rspPacketDataChars, 6, 0,0, 170), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470e06rspEntry = TSIPSchemaEntry(EServerPackets.ebf470e06rsp, kbf470e06rsp, NUMFIELDS(kbf470e06rsp))
kbf470e07rspPacketDataChars = CHARSchemaField()

# Debug packet response from the Autopilot Navigation Controller. Contains .dbg file data
kbf470e07rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x07), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(kbf470e07rspPacketDataChars, 6, 0,0, 170), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470e07rspEntry = TSIPSchemaEntry(EServerPackets.ebf470e07rsp, kbf470e07rsp, NUMFIELDS(kbf470e07rsp))

# Debug packet response from the Autopilot Navigation Controller. Gets current port function
kbf470e08rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x08), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470e08rspEntry = TSIPSchemaEntry(EServerPackets.ebf470e08rsp, kbf470e08rsp, NUMFIELDS(kbf470e08rsp))

# Debug packet response from the Autopilot Navigation Controller. Sets current port function
kbf470e09rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x09), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf470e09rspEntry = TSIPSchemaEntry(EServerPackets.ebf470e09rsp, kbf470e09rsp, NUMFIELDS(kbf470e09rsp))

# Gets number of internal vdb's from the Autopilot Controller
kbf471400rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf471400rspEntry = TSIPSchemaEntry(EServerPackets.ebf471400rsp, kbf471400rsp, NUMFIELDS(kbf471400rsp))

# Gets a vdb record from the Autopilot Controller
kbf471401rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x01), 
  U16SchemaField(), 
  StringSchemaField(16), 
  StringSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf471401rspEntry = TSIPSchemaEntry(EServerPackets.ebf471401rsp, kbf471401rsp, NUMFIELDS(kbf471401rsp))

# Sets the vdb record on the Autopilot Controller
kbf471402rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x14), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  StringSchemaField(16), 
  StringSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf471402rspEntry = TSIPSchemaEntry(EServerPackets.ebf471402rsp, kbf471402rsp, NUMFIELDS(kbf471402rsp))

# Gets current IMU data from the Autopilot Controller
kbf471ersp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x47), 
  SubIdSchemaField(0x1e), 
  U32SchemaField(), 
  U32SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(1), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf471erspEntry = TSIPSchemaEntry(EServerPackets.ebf471ersp, kbf471ersp, NUMFIELDS(kbf471ersp))
kbf4arspPacketDataData = U8SchemaField()

# Calibration packet response from the Autopilot Navigation Controller
kbf4arsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4a), 
  EndTerminatedArraySchemaField(kbf4arspPacketDataData)
]

kbf4arspEntry = TSIPSchemaEntry(EServerPackets.ebf4arsp, kbf4arsp, NUMFIELDS(kbf4arsp))

# Steering angle sensor calibration information response
kbf4a0b00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0b), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4a0b00rspEntry = TSIPSchemaEntry(EServerPackets.ebf4a0b00rsp, kbf4a0b00rsp, NUMFIELDS(kbf4a0b00rsp))

# 
kbf4a0b01rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0b), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4a0b01rspEntry = TSIPSchemaEntry(EServerPackets.ebf4a0b01rsp, kbf4a0b01rsp, NUMFIELDS(kbf4a0b01rsp))

# 
kbf4a0c00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4a0c00rspEntry = TSIPSchemaEntry(EServerPackets.ebf4a0c00rsp, kbf4a0c00rsp, NUMFIELDS(kbf4a0c00rsp))

# 
kbf4a0c08rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4a), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x08), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4a0c08rspEntry = TSIPSchemaEntry(EServerPackets.ebf4a0c08rsp, kbf4a0c08rsp, NUMFIELDS(kbf4a0c08rsp))
kbf4brspPacketDataData = U8SchemaField()

# Autotester response to the Autopilot Navigation Controller.
kbf4brsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4b), 
  EndTerminatedArraySchemaField(kbf4brspPacketDataData)
]

kbf4brspEntry = TSIPSchemaEntry(EServerPackets.ebf4brsp, kbf4brsp, NUMFIELDS(kbf4brsp))

# External Device packet command to read the manual override info from the Autopilot Navigation Controller
kbf4c00000004rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c00000004rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c00000004rsp, kbf4c00000004rsp, NUMFIELDS(kbf4c00000004rsp))

# External Device packet command to read the Left Pump Transducer info from the Autopilot Navigation Controller
kbf4c00000104rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c00000104rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c00000104rsp, kbf4c00000104rsp, NUMFIELDS(kbf4c00000104rsp))

# External Device packet command to read the Right Pump Transducer info from the Autopilot Navigation Controller
kbf4c00000204rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c00000204rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c00000204rsp, kbf4c00000204rsp, NUMFIELDS(kbf4c00000204rsp))

# External Device packet command to read the Gear lever info from the Autopilot Navigation Controller
kbf4c00000704rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c00000704rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c00000704rsp, kbf4c00000704rsp, NUMFIELDS(kbf4c00000704rsp))

# Autopilot Field Computer Heartbeat packet response from the Autosteer Client
kbf4c0101rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0101rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0101rsp, kbf4c0101rsp, NUMFIELDS(kbf4c0101rsp))
kbf4c0108rspImplementWidthImplementText = CHARSchemaField()

# External Device packet command to set close any open field
kbf4c0108rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x08), 
  EndTerminatedArraySchemaField(kbf4c0108rspImplementWidthImplementText), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0108rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0108rsp, kbf4c0108rsp, NUMFIELDS(kbf4c0108rsp))

# External Device packet command to set close any open field
kbf4c010arsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0a), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kbf4c010arspEntry = TSIPSchemaEntry(EServerPackets.ebf4c010arsp, kbf4c010arsp, NUMFIELDS(kbf4c010arsp))
kbf4c010brspMiscDataData = U8SchemaField()

# External Device packet Control State
kbf4c010brsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0b), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbf4c010brspMiscDataData), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c010brspEntry = TSIPSchemaEntry(EServerPackets.ebf4c010brsp, kbf4c010brsp, NUMFIELDS(kbf4c010brsp))

# External Device packet response with Aggressiveness
kbf4c010drsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0d), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c010drspEntry = TSIPSchemaEntry(EServerPackets.ebf4c010drsp, kbf4c010drsp, NUMFIELDS(kbf4c010drsp))

# External Device packet response with Task Delay
kbf4c010ersp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0e), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c010erspEntry = TSIPSchemaEntry(EServerPackets.ebf4c010ersp, kbf4c010ersp, NUMFIELDS(kbf4c010ersp))

# External Device packet response with Fix Quality
kbf4c010frsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0f), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c010frspEntry = TSIPSchemaEntry(EServerPackets.ebf4c010frsp, kbf4c010frsp, NUMFIELDS(kbf4c010frsp))

# External Device packet response to Get Nudge
kbf4c011000rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011000rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011000rsp, kbf4c011000rsp, NUMFIELDS(kbf4c011000rsp))

# External Device packet response to set Nudge
kbf4c011001rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011001rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011001rsp, kbf4c011001rsp, NUMFIELDS(kbf4c011001rsp))

# External Device packet response to Apply Nudge
kbf4c011002rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011002rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011002rsp, kbf4c011002rsp, NUMFIELDS(kbf4c011002rsp))

# External Device packet response to Get Total
kbf4c011003rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x03), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011003rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011003rsp, kbf4c011003rsp, NUMFIELDS(kbf4c011003rsp))

# External Device response to Set Total Nudge
kbf4c011004rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011004rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011004rsp, kbf4c011004rsp, NUMFIELDS(kbf4c011004rsp))

# External Device packet command to set the NMEA message rate on the Autopilot Navigation Controller
kbf4c0111rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x11), 
  U32SchemaField(), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0111rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0111rsp, kbf4c0111rsp, NUMFIELDS(kbf4c0111rsp))

# External Device packet response to set the GGA Adjust
kbf4c0114rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0114rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0114rsp, kbf4c0114rsp, NUMFIELDS(kbf4c0114rsp))

# Point A geodetic position
kbf4c011806rspPointA = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbf4c011806rspPointAGroup = GroupSchemaField(kbf4c011806rspPointA,NUMFIELDS(kbf4c011806rspPointA))

# Point B geodetic position
kbf4c011806rspPointB = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbf4c011806rspPointBGroup = GroupSchemaField(kbf4c011806rspPointB,NUMFIELDS(kbf4c011806rspPointB))

# Point Center geodetic position
kbf4c011806rspCenterPoint = [
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField()
]

kbf4c011806rspCenterPointGroup = GroupSchemaField(kbf4c011806rspCenterPoint,NUMFIELDS(kbf4c011806rspCenterPoint))

# Field computer pattern definition for pivot ACB patterns
kbf4c011806rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  SubIdSchemaField(0x06), 
  UnusedSchemaField(2), 
  U8SchemaField(), 
  UnusedSchemaField(4), 
  UnusedSchemaField(8), 
  GroupSchemaField(kbf4c011806rspPointA,NUMFIELDS(kbf4c011806rspPointA)), 
  GroupSchemaField(kbf4c011806rspPointB,NUMFIELDS(kbf4c011806rspPointB)), 
  GroupSchemaField(kbf4c011806rspCenterPoint,NUMFIELDS(kbf4c011806rspCenterPoint)), 
  DBLSchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011806rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011806rsp, kbf4c011806rsp, NUMFIELDS(kbf4c011806rsp))

# Swath by swath pattern definition response (PTRN_SWATH_BY_SWATH)
kbf4c011810rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  SubIdSchemaField(0x10), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011810rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011810rsp, kbf4c011810rsp, NUMFIELDS(kbf4c011810rsp))

# Swath section pattern definition response (PTRN_SWATH_SECTION)
kbf4c011811rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  SubIdSchemaField(0x11), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(7), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011811rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011811rsp, kbf4c011811rsp, NUMFIELDS(kbf4c011811rsp))

# Swath by swath fragment pattern definition response (PTRN_SWATH_BY_SWATH_FRAGMENT)
kbf4c011813rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  SubIdSchemaField(0x13), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011813rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011813rsp, kbf4c011813rsp, NUMFIELDS(kbf4c011813rsp))

# Swath by swath FFA pattern definition response (PTRN_SWATH_BY_SWATH_FFA)
kbf4c011820rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  SubIdSchemaField(0x20), 
  S16SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(7), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011820rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011820rsp, kbf4c011820rsp, NUMFIELDS(kbf4c011820rsp))

# Swath section FFA pattern definition response (PTRN_SWATH_SECTION_FFA)
kbf4c011821rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  SubIdSchemaField(0x21), 
  S16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(7), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011821rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011821rsp, kbf4c011821rsp, NUMFIELDS(kbf4c011821rsp))

# Response to the Field Computer Information Command (tsip::Sbe4c0119cmd)
kbf4c0119rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x19), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0119rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0119rsp, kbf4c0119rsp, NUMFIELDS(kbf4c0119rsp))

# Extended Field Computer Heartbeat packet response from the Autosteer Client
kbf4c011arsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x1a), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c011arspEntry = TSIPSchemaEntry(EServerPackets.ebf4c011arsp, kbf4c011arsp, NUMFIELDS(kbf4c011arsp))

# 
kbf4c0120rspPointsPointDiff = [
  FLTSchemaField(), 
  FLTSchemaField()
]

kbf4c0120rspPointsPointDiffGroup = GroupSchemaField(kbf4c0120rspPointsPointDiff,NUMFIELDS(kbf4c0120rspPointsPointDiff))

# Path to be plotted on Field Computer map. Reference point is first point of path (only plot for first message). Included with all packets though.
kbf4c0120rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x20), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  ArraySchemaField(kbf4c0120rspPointsPointDiffGroup, 5, 0,0, 28), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0120rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0120rsp, kbf4c0120rsp, NUMFIELDS(kbf4c0120rsp))

# Sent by the NAV to the display when updating an opis device, like a SAM-300
kbf4c0500rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c0500rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c0500rsp, kbf4c0500rsp, NUMFIELDS(kbf4c0500rsp))

# External Device packet response to return the guidance status enable
kbf4c2000rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x20), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c2000rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c2000rsp, kbf4c2000rsp, NUMFIELDS(kbf4c2000rsp))
kbf4c2001rspCanMsgData = U8SchemaField()

# External Device packet response to update the guidance status
kbf4c2001rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x20), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(3), 
  ArraySchemaField(kbf4c2001rspCanMsgData, 5, 0,0, 64), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c2001rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c2001rsp, kbf4c2001rsp, NUMFIELDS(kbf4c2001rsp))

# Clothoid New Path Response
kbf4c2300rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c2300rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c2300rsp, kbf4c2300rsp, NUMFIELDS(kbf4c2300rsp))

# Clothoid Append Path Response
kbf4c2301rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x01), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c2301rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c2301rsp, kbf4c2301rsp, NUMFIELDS(kbf4c2301rsp))

# Clothoid Activate Clothoid Guidance Response
kbf4c2302rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x23), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c2302rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c2302rsp, kbf4c2302rsp, NUMFIELDS(kbf4c2302rsp))

# An event.
kbf4c8000rspSequenceEventsSequenceEvent = [
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField()
]

kbf4c8000rspSequenceEventsSequenceEventGroup = GroupSchemaField(kbf4c8000rspSequenceEventsSequenceEvent,NUMFIELDS(kbf4c8000rspSequenceEventsSequenceEvent))

# Updates the display with FFA status
kbf4c8000rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x80), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  S16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(kbf4c8000rspSequenceEventsSequenceEventGroup, 25, 0,0, 3), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c8000rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c8000rsp, kbf4c8000rsp, NUMFIELDS(kbf4c8000rsp))
kbf4c8001rspPacketDataData = U8SchemaField()

# 
kbf4c8001rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x80), 
  SubIdSchemaField(0x01), 
  EndTerminatedArraySchemaField(kbf4c8001rspPacketDataData), 
  ChecksumSchemaField()
]

kbf4c8001rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c8001rsp, kbf4c8001rsp, NUMFIELDS(kbf4c8001rsp))

# External Device packet response to update the guidance status
kbf4c8002rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4c), 
  SubIdSchemaField(0x80), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf4c8002rspEntry = TSIPSchemaEntry(EServerPackets.ebf4c8002rsp, kbf4c8002rsp, NUMFIELDS(kbf4c8002rsp))
kbf4drspPacketDataData = U8SchemaField()

# GPS simulation response from the Autopilot Navigation Controller. Used for NAV to NAV communication.
kbf4drsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4d), 
  EndTerminatedArraySchemaField(kbf4drspPacketDataData)
]

kbf4drspEntry = TSIPSchemaEntry(EServerPackets.ebf4drsp, kbf4drsp, NUMFIELDS(kbf4drsp))
kbf4erspPacketDataData = U8SchemaField()

# Piped message response from the Autopilot Navigation Controller.
kbf4ersp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4e), 
  EndTerminatedArraySchemaField(kbf4erspPacketDataData)
]

kbf4erspEntry = TSIPSchemaEntry(EServerPackets.ebf4ersp, kbf4ersp, NUMFIELDS(kbf4ersp))
kbf4frspPacketDataData = U8SchemaField()

# This is an alias to 0x8f 0xa1.
kbf4frsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x4f), 
  EndTerminatedArraySchemaField(kbf4frspPacketDataData), 
  ChecksumSchemaField()
]

kbf4frspEntry = TSIPSchemaEntry(EServerPackets.ebf4frsp, kbf4frsp, NUMFIELDS(kbf4frsp))
kbf5014rspPacketDataData = U8SchemaField()

# TAP packet response to the Autosteer Controller
kbf5014rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x50), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbf5014rspPacketDataData)
]

kbf5014rspEntry = TSIPSchemaEntry(EServerPackets.ebf5014rsp, kbf5014rsp, NUMFIELDS(kbf5014rsp))

# Remote Monitor Control Steering packet response to the Autosteer Controller
kbf530600rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x53), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf530600rspEntry = TSIPSchemaEntry(EServerPackets.ebf530600rsp, kbf530600rsp, NUMFIELDS(kbf530600rsp))

# Remote Monitor Control Speed packet response to the Autosteer Controller
kbf530601rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x53), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf530601rspEntry = TSIPSchemaEntry(EServerPackets.ebf530601rsp, kbf530601rsp, NUMFIELDS(kbf530601rsp))

# Field Computer Ack Current Warning packet response to the Autosteer Controller
kbf570507rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x57), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf570507rspEntry = TSIPSchemaEntry(EServerPackets.ebf570507rsp, kbf570507rsp, NUMFIELDS(kbf570507rsp))

# Field Computer Heartbeat packet response from the Autosteer Client
kbf5c0101rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0101rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0101rsp, kbf5c0101rsp, NUMFIELDS(kbf5c0101rsp))

# Field Computer Logging On packet response to the Autosteer Controller
kbf5c0106rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x06), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0106rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0106rsp, kbf5c0106rsp, NUMFIELDS(kbf5c0106rsp))

# Field Computer Logging Off packet response to the Autosteer Controller
kbf5c0107rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x07), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0107rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0107rsp, kbf5c0107rsp, NUMFIELDS(kbf5c0107rsp))

# Field Computer Control State packet response to the Autosteer Client
kbf5c010brsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x0b), 
  U8SchemaField(), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c010brspEntry = TSIPSchemaEntry(EServerPackets.ebf5c010brsp, kbf5c010brsp, NUMFIELDS(kbf5c010brsp))

# Field Computer Get Nudge packet response to the Autosteer Controller
kbf5c011000rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c011000rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c011000rsp, kbf5c011000rsp, NUMFIELDS(kbf5c011000rsp))

# Field Computer Set Nudge packet response to the Autosteer Controller
kbf5c011001rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c011001rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c011001rsp, kbf5c011001rsp, NUMFIELDS(kbf5c011001rsp))

# Field Computer Apply Nudge packet response to the Autosteer Controller
kbf5c011002rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x02), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c011002rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c011002rsp, kbf5c011002rsp, NUMFIELDS(kbf5c011002rsp))

# Field Computer Get Total Nudge packet response to the Autosteer Controller
kbf5c011003rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x03), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c011003rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c011003rsp, kbf5c011003rsp, NUMFIELDS(kbf5c011003rsp))

# Field Computer Set Total Nudge packet response to the Autosteer Controller
kbf5c011004rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x10), 
  SubIdSchemaField(0x04), 
  FLTSchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c011004rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c011004rsp, kbf5c011004rsp, NUMFIELDS(kbf5c011004rsp))

# Field Computer NMEA configuration packet response to the Autosteer Client
kbf5c0111rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x11), 
  U32SchemaField(), 
  U32SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0111rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0111rsp, kbf5c0111rsp, NUMFIELDS(kbf5c0111rsp))

# Field Computer Adjust GGA position response to the Autosteer Controller
kbf5c0114rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0114rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0114rsp, kbf5c0114rsp, NUMFIELDS(kbf5c0114rsp))

# Field Computer Pattern Definition packet response to the Autosteer Client
kbf5c0118rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x18), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0118rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0118rsp, kbf5c0118rsp, NUMFIELDS(kbf5c0118rsp))

# Field Computer Information packet response to the Autosteer Client
kbf5c0119rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x5c), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x19), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf5c0119rspEntry = TSIPSchemaEntry(EServerPackets.ebf5c0119rsp, kbf5c0119rsp, NUMFIELDS(kbf5c0119rsp))
kbf6014rspPacketDataData = U8SchemaField()

# TAP packet response to the Inertial Nav feature
kbf6014rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x60), 
  SubIdSchemaField(0x14), 
  U8SchemaField(), 
  EndTerminatedArraySchemaField(kbf6014rspPacketDataData)
]

kbf6014rspEntry = TSIPSchemaEntry(EServerPackets.ebf6014rsp, kbf6014rsp, NUMFIELDS(kbf6014rsp))

# Remote Monitor Control Steering packet response to the Inertial Nav feature
kbf630600rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x63), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf630600rspEntry = TSIPSchemaEntry(EServerPackets.ebf630600rsp, kbf630600rsp, NUMFIELDS(kbf630600rsp))

# Remote Monitor Control Speed packet response to the Inertial Nav feature
kbf630601rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x63), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf630601rspEntry = TSIPSchemaEntry(EServerPackets.ebf630601rsp, kbf630601rsp, NUMFIELDS(kbf630601rsp))

# Roll/Pitch corrected Position and Attitude packet from the Inertial Nav feature.
kbf6800rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x68), 
  SubIdSchemaField(0x00), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

kbf6800rspEntry = TSIPSchemaEntry(EServerPackets.ebf6800rsp, kbf6800rsp, NUMFIELDS(kbf6800rsp))

# Indicates that a GPS position wasn't generated for the given time period
kbf6801rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x68), 
  SubIdSchemaField(0x01), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  DBLSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(8), 
  ChecksumSchemaField()
]

kbf6801rspEntry = TSIPSchemaEntry(EServerPackets.ebf6801rsp, kbf6801rsp, NUMFIELDS(kbf6801rsp))
kbf710000rspOptionsOptionsData = U8SchemaField()

# Publish Parameter Block Hardware Information packet response from the Autopilot Navigation Controller
kbf710000rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  StringSchemaField(22), 
  U8SchemaField(), 
  FixedArraySchemaField(kbf710000rspOptionsOptionsData, 14), 
  UnusedSchemaField(3), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710000rspEntry = TSIPSchemaEntry(EServerPackets.ebf710000rsp, kbf710000rsp, NUMFIELDS(kbf710000rsp))

# Publish Parameter Block Software Information packet response from the Autopilot Navigation Controller
kbf710100rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  StringSchemaField(20), 
  U8SchemaField(), 
  U8SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  StringSchemaField(20), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710100rspEntry = TSIPSchemaEntry(EServerPackets.ebf710100rsp, kbf710100rsp, NUMFIELDS(kbf710100rsp))

# Publish Parameter Block OPS Config Information packet response from the Autopilot Navigation Controller
kbf710200rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710200rspEntry = TSIPSchemaEntry(EServerPackets.ebf710200rsp, kbf710200rsp, NUMFIELDS(kbf710200rsp))

# Publish Parameter Block OPS Config Information packet SET confirmation    response from Autopilot
kbf710201rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x01), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(8), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710201rspEntry = TSIPSchemaEntry(EServerPackets.ebf710201rsp, kbf710201rsp, NUMFIELDS(kbf710201rsp))
kbf710300rspExtIOFctArrayExtIOFctData = U32SchemaField()
kbf710300rspVdmIOFctArrayVdmIOFctData = U32SchemaField()

# Publish Parameter Block Platform Config Information packet response from the Autopilot Navigation Controller
kbf710300rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x03), 
  SubIdSchemaField(0x00), 
  StringSchemaField(16), 
  U32SchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  FixedArraySchemaField(kbf710300rspExtIOFctArrayExtIOFctData, 14), 
  FixedArraySchemaField(kbf710300rspVdmIOFctArrayVdmIOFctData, 12), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710300rspEntry = TSIPSchemaEntry(EServerPackets.ebf710300rsp, kbf710300rsp, NUMFIELDS(kbf710300rsp))

# Publish Parameter Block Safety Config Information packet response from the Autopilot Navigation Controller
kbf710400rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x04), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710400rspEntry = TSIPSchemaEntry(EServerPackets.ebf710400rsp, kbf710400rsp, NUMFIELDS(kbf710400rsp))

# Publish Parameter Block Version Information packet response from the Autopilot Navigation Controller
kbf710500rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x05), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  StringSchemaField(22), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710500rspEntry = TSIPSchemaEntry(EServerPackets.ebf710500rsp, kbf710500rsp, NUMFIELDS(kbf710500rsp))

# Publish Parameter Sensor Hyd State Information packet response from the Autopilot Navigation Controller
kbf710600rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x06), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U32SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710600rspEntry = TSIPSchemaEntry(EServerPackets.ebf710600rsp, kbf710600rsp, NUMFIELDS(kbf710600rsp))

# Publish Parameter Raw Sensor Status Information packet response from the Autopilot Navigation Controller
kbf710700rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x07), 
  SubIdSchemaField(0x00), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710700rspEntry = TSIPSchemaEntry(EServerPackets.ebf710700rsp, kbf710700rsp, NUMFIELDS(kbf710700rsp))

# Publish Parameter Block Selected IMU Status Information packet response from the Autopilot Navigation Controller
kbf710800rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x08), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  S32SchemaField(), 
  S32SchemaField(), 
  U8SchemaField(), 
  StringSchemaField(11), 
  U8SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  U32SchemaField(), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710800rspEntry = TSIPSchemaEntry(EServerPackets.ebf710800rsp, kbf710800rsp, NUMFIELDS(kbf710800rsp))
kbf710900rspCSValues = U32SchemaField()

# Publish Parameter Block CS Information packet response from the Autopilot Navigation Controller
kbf710900rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x09), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  U32SchemaField(), 
  ArraySchemaField(kbf710900rspCSValues, 5, 0,0, 128), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710900rspEntry = TSIPSchemaEntry(EServerPackets.ebf710900rsp, kbf710900rsp, NUMFIELDS(kbf710900rsp))

# Publish Parameter Block Group1 Information packet response from the Autopilot Navigation Controller
kbf710a00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0a), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U32SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710a00rspEntry = TSIPSchemaEntry(EServerPackets.ebf710a00rsp, kbf710a00rsp, NUMFIELDS(kbf710a00rsp))

# Publish Parameter Block Group2 Information packet response from the Autopilot Navigation Controller
kbf710b00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0b), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710b00rspEntry = TSIPSchemaEntry(EServerPackets.ebf710b00rsp, kbf710b00rsp, NUMFIELDS(kbf710b00rsp))

# Publish Parameter Block Group3 Information packet response from the Autopilot Navigation Controller
kbf710c00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0c), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710c00rspEntry = TSIPSchemaEntry(EServerPackets.ebf710c00rsp, kbf710c00rsp, NUMFIELDS(kbf710c00rsp))

# Publish Parameter Block GPS Guidance Status Information packet response from the Autopilot Navigation Controller
kbf710d00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0d), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(11), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710d00rspEntry = TSIPSchemaEntry(EServerPackets.ebf710d00rsp, kbf710d00rsp, NUMFIELDS(kbf710d00rsp))

# Publish Parameter Block GPS Guidance Diag Information packet response from the Autopilot Navigation Controller
kbf710e00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0e), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  UnusedSchemaField(16), 
  CheckedLengthSchemaField(), 
  ChecksumSchemaField()
]

kbf710e00rspEntry = TSIPSchemaEntry(EServerPackets.ebf710e00rsp, kbf710e00rsp, NUMFIELDS(kbf710e00rsp))

# Publish Parameter Block Group4 Information packet response from the Autopilot Navigation Controller
kbf710f00rsp = [
  IdSchemaField(0xbf), 
  SubIdSchemaField(0x71), 
  SubIdSchemaField(0x0f), 
  SubIdSchemaField(0x00), 
  U32SchemaField(), 
  UnusedSchemaField(16), 
  ChecksumSchemaField()
]

kbf710f00rspEntry = TSIPSchemaEntry(EServerPackets.ebf710f00rsp, kbf710f00rsp, NUMFIELDS(kbf710f00rsp))

# Requests satellite constellation report from receiver. One or more 0xd5 0x00 packets are sent in response.
kc500req = [
  IdSchemaField(0xc5), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kc500reqEntry = TSIPSchemaEntry(EClientPackets.ec500req, kc500req, NUMFIELDS(kc500req))

# Set which satellite systems are enabled/disabled
kc501cmd = [
  IdSchemaField(0xc5), 
  SubIdSchemaField(0x01), 
  U16SchemaField(), 
  ChecksumSchemaField()
]

kc501cmdEntry = TSIPSchemaEntry(EClientPackets.ec501cmd, kc501cmd, NUMFIELDS(kc501cmd))

# Request report which satellite system is enabled/disabled
kc502req = [
  IdSchemaField(0xc5), 
  SubIdSchemaField(0x02), 
  ChecksumSchemaField()
]

kc502reqEntry = TSIPSchemaEntry(EClientPackets.ec502req, kc502req, NUMFIELDS(kc502req))
kc60000cmdChallengeResponseChallengeData = U8SchemaField()
kc60000cmdDigestDigestData = U8SchemaField()

# TBIP authenticated command to set the allowed GeoFencing Regions.
kc60000cmd = [
  IdSchemaField(0xc6), 
  SubIdSchemaField(0x00), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U16SchemaField(), 
  StringSchemaField(32), 
  FixedArraySchemaField(kc60000cmdChallengeResponseChallengeData, 16), 
  U32SchemaField(), 
  UnusedSchemaField(16), 
  FixedArraySchemaField(kc60000cmdDigestDigestData, 16), 
  ChecksumSchemaField()
]

kc60000cmdEntry = TSIPSchemaEntry(EClientPackets.ec60000cmd, kc60000cmd, NUMFIELDS(kc60000cmd))
kc60100cmdChallengeResponseChallengeData = U8SchemaField()

# Authorized base array entry
kc60100cmdAuthorizedBaseArrayAuthorizedBaseEntry = [
  U8SchemaField(), 
  U32SchemaField(), 
  U16SchemaField()
]

kc60100cmdAuthorizedBaseArrayAuthorizedBaseEntryGroup = GroupSchemaField(kc60100cmdAuthorizedBaseArrayAuthorizedBaseEntry,NUMFIELDS(kc60100cmdAuthorizedBaseArrayAuthorizedBaseEntry))
kc60100cmdDigestDigestData = U8SchemaField()

# TBIP authenticated command to set list of authorized SecureRTK bases.
kc60100cmd = [
  IdSchemaField(0xc6), 
  SubIdSchemaField(0x01), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U16SchemaField(), 
  StringSchemaField(32), 
  FixedArraySchemaField(kc60100cmdChallengeResponseChallengeData, 16), 
  FixedArraySchemaField(kc60100cmdAuthorizedBaseArrayAuthorizedBaseEntryGroup, 5), 
  UnusedSchemaField(16), 
  FixedArraySchemaField(kc60100cmdDigestDigestData, 16), 
  ChecksumSchemaField()
]

kc60100cmdEntry = TSIPSchemaEntry(EClientPackets.ec60100cmd, kc60100cmd, NUMFIELDS(kc60100cmd))
kc60200cmdChallengeResponseChallengeData = U8SchemaField()
kc60200cmdAuthorizedFixEngineArrayAuthorizedFixEngineAccuracyLevel = U8SchemaField()
kc60200cmdDigestDigestData = U8SchemaField()

# TBIP authenticated command to authorize the output of GPS fix engines (per antenna) by accuracy level.
kc60200cmd = [
  IdSchemaField(0xc6), 
  SubIdSchemaField(0x02), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U16SchemaField(), 
  StringSchemaField(32), 
  FixedArraySchemaField(kc60200cmdChallengeResponseChallengeData, 16), 
  FixedArraySchemaField(kc60200cmdAuthorizedFixEngineArrayAuthorizedFixEngineAccuracyLevel, 4), 
  UnusedSchemaField(16), 
  FixedArraySchemaField(kc60200cmdDigestDigestData, 16), 
  ChecksumSchemaField()
]

kc60200cmdEntry = TSIPSchemaEntry(EClientPackets.ec60200cmd, kc60200cmd, NUMFIELDS(kc60200cmd))
kc60400cmdChallengeResponseChallengeData = U8SchemaField()
kc60400cmdDigestDigestData = U8SchemaField()

# TBIP authenticated command to allow RTX datum selection.
kc60400cmd = [
  IdSchemaField(0xc6), 
  SubIdSchemaField(0x04), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U16SchemaField(), 
  StringSchemaField(32), 
  FixedArraySchemaField(kc60400cmdChallengeResponseChallengeData, 16), 
  U8SchemaField(), 
  UnusedSchemaField(16), 
  FixedArraySchemaField(kc60400cmdDigestDigestData, 16), 
  ChecksumSchemaField()
]

kc60400cmdEntry = TSIPSchemaEntry(EClientPackets.ec60400cmd, kc60400cmd, NUMFIELDS(kc60400cmd))

# Lock or Unlock all stinger channels. The action is persistent unless a command forces the existing state to change. This packet is for diagnostic purposes only and may change without notice. Acknowledge Packet: 0xD7 0x00
kc700cmd = [
  IdSchemaField(0xc7), 
  SubIdSchemaField(0x00), 
  U16SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kc700cmdEntry = TSIPSchemaEntry(EClientPackets.ec700cmd, kc700cmd, NUMFIELDS(kc700cmd))

# Request setting of Band and Filter switches for a signal.
kc701req = [
  IdSchemaField(0xc7), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kc701reqEntry = TSIPSchemaEntry(EClientPackets.ec701req, kc701req, NUMFIELDS(kc701req))

# Set Band and Filter switches for a signal.  0xd7 0x01 is the acknowledge packet.
kc701cmd = [
  IdSchemaField(0xc7), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(10), 
  ChecksumSchemaField()
]

kc701cmdEntry = TSIPSchemaEntry(EClientPackets.ec701cmd, kc701cmd, NUMFIELDS(kc701cmd))

# Type and SNR for a single frequency band
kd500rspSatInfoArraySatInfoFreqBandArrayFreqBandInfo = [
  U8SchemaField(), 
  U16SchemaField()
]

kd500rspSatInfoArraySatInfoFreqBandArrayFreqBandInfoGroup = GroupSchemaField(kd500rspSatInfoArraySatInfoFreqBandArrayFreqBandInfo,NUMFIELDS(kd500rspSatInfoArraySatInfoFreqBandArrayFreqBandInfo))

# Info for a single satellite
kd500rspSatInfoArraySatInfo = [
  U16SchemaField(), 
  U8SchemaField(), 
  FLTSchemaField(), 
  FLTSchemaField(), 
  U16SchemaField(), 
  FixedArraySchemaField(kd500rspSatInfoArraySatInfoFreqBandArrayFreqBandInfoGroup, 3)
]

kd500rspSatInfoArraySatInfoGroup = GroupSchemaField(kd500rspSatInfoArraySatInfo,NUMFIELDS(kd500rspSatInfoArraySatInfo))

# Reports satellite constellation info. Note that multiple packets may be required to describe entire constellation.
kd500rsp = [
  IdSchemaField(0xd5), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  U8SchemaField(), 
  U8SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U16SchemaField(), 
  U8SchemaField(), 
  ArraySchemaField(kd500rspSatInfoArraySatInfoGroup, 8, 0,0, 10), 
  ChecksumSchemaField()
]

kd500rspEntry = TSIPSchemaEntry(EServerPackets.ed500rsp, kd500rsp, NUMFIELDS(kd500rsp))

# Report which satellite system is enabled/disabled
kd502rsp = [
  IdSchemaField(0xd5), 
  SubIdSchemaField(0x02), 
  U16SchemaField(), 
  ChecksumSchemaField()
]

kd502rspEntry = TSIPSchemaEntry(EServerPackets.ed502rsp, kd502rsp, NUMFIELDS(kd502rsp))

# Acknowledges the success or failure of an authenticated command
kd6ack = [
  IdSchemaField(0xd6), 
  U8SchemaField(), 
  U8SchemaField(), 
  S8SchemaField(), 
  ChecksumSchemaField()
]

kd6ackEntry = TSIPSchemaEntry(EServerPackets.ed6ack, kd6ack, NUMFIELDS(kd6ack))

# Lock or Unlock all stinger channels. This packet is for diagnostic purposes only and may change without notice. Command Packet: 0xC7 0x00
kd700ack = [
  IdSchemaField(0xd7), 
  SubIdSchemaField(0x00), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kd700ackEntry = TSIPSchemaEntry(EServerPackets.ed700ack, kd700ack, NUMFIELDS(kd700ack))

# Acknowledge RF Band and Filter Switches setting command.
kd701ack = [
  IdSchemaField(0xd7), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  ChecksumSchemaField()
]

kd701ackEntry = TSIPSchemaEntry(EServerPackets.ed701ack, kd701ack, NUMFIELDS(kd701ack))

# Return the RF Band and Filter Switch setting for the signal requested.
kd701rsp = [
  IdSchemaField(0xd7), 
  SubIdSchemaField(0x01), 
  U8SchemaField(), 
  U8SchemaField(), 
  UnusedSchemaField(10), 
  ChecksumSchemaField()
]

kd701rspEntry = TSIPSchemaEntry(EServerPackets.ed701rsp, kd701rsp, NUMFIELDS(kd701rsp))

kCommonSchemaFieldsList = [
  kCHARSchemaField,
  kU8SchemaField,
  kS8SchemaField,
  kU16SchemaField,
  kS16SchemaField,
  kU32SchemaField,
  kS32SchemaField,
  kFLTSchemaField,
  kDBLSchemaField,
  k00cmdPacketDataData,
  k00rspPacketDataData,
  k13rspPacketDataData,
  k1a00cmdRTCMDataData,
  k1a01rspNMEADataChar,
  k1a0200cmdDCOLTypesData,
  k1a0200rspDCOLTypesData,
  k1a0201cmdDCOLMessageData,
  k1a0201rspDCOLMessageData,
  k1a0202cmdDCOLMessageData,
  k1a0300cmdCanIdsData,
  k1a0300rspCanIdsData,
  k1a0301cmdCanMsgData,
  k1a0301rspCanMsgData,
  k45rspv1BCDSerialNumberBCDData,
  k58rspSVDatabytes,
  k5f01rspDiagMsgChar,
  k5f10rspDiagDataData,
  k5f2201rspMsgMsg,
  k6drspSatsInViewSat,
  k6f21rspPayloadData,
  k893308rspStationIdsStationId,
  k893308rspLinkQualityLinkQuality,
  k893308rspLastCMRTimeLastCMRTime,
  k897002rspSupportedModesMode,
  k897002rspSupportedCountriesCountryCode,
  k8e931500reqPathChar,
  k8e93150101reqFilenameChar,
  k8e93150104reqFilenameChar,
  k8e93150201reqFilenameChar,
  k8e93150202reqDataBlockData,
  k8e931503reqFilenameChar,
  k8ea1cmdPacketDataData,
  k8ea644cmdSourceMACSourceMACHex,
  k8ea644cmdDestMACDestMACHex,
  k8ea646cmdSourceMACSourceMACHex,
  k8ea646cmdDestMACDestMACHex,
  k8ea70001cmdPositionEngArrayPositionEng,
  k8ea70002cmdPositionTypeArrayPositionType,
  k8ea801cmdIPAddressChar,
  k8ea801cmdMountPointChar,
  k8ea801cmdUserNameChar,
  k8ea801cmdPasswordChar,
  k8ea802cmdUserNameChar,
  k8ea803cmdPasswordChar,
  k8ea804cmdInitStringChar,
  k8ea805cmdCPINChar,
  k8ea90100cmdFilenameChar,
  k8ea90101cmdprefixChar,
  k8ea90102cmdFilenameChar,
  k8ea90103cmdDataData,
  k8ea90105cmdFilenameChar,
  k8ea905cmdLogMessageChar,
  k8ea91500cmdclientFileIdbyte,
  k8ea91502cmdblockDatabyte,
  k8ea91605cmdFragmentChar,
  k8f77rspSampleData,
  k8f770rspSampleData,
  k8f8brspActivationCodeData,
  k8f9306rspDebugMsgChar,
  k8f931500rspFilenameChar,
  k8f93150100rspFilenameChar,
  k8f93150101rspDataBlockData,
  k8f93150104rspHashByte,
  k8f93150104rspFilenameChar,
  k8f93150200rspFilenameChar,
  k8f931503rspFilenameChar,
  k8fa1rspPacketDataData,
  k8fa302rspStationIdsStationId,
  k8fa602rspExternalInputsInputPinState,
  k8fa622rspMac1AddrMac1Hex,
  k8fa622rspMac2AddrMac2Hex,
  k8fa622rspMac3AddrMac3Hex,
  k8fa622rspMac4AddrMac4Hex,
  k8fa623rspAltUniqueIdFieldAltUniqueId,
  k8fa629rspsignatureSignatureByte,
  k8fa70001rspPositionEngArrayPositionEng,
  k8fa70002rspPositionTypeArrayPositionType,
  k8fa801rspIPAddressChar,
  k8fa801rspMountPointChar,
  k8fa801rspUserNameChar,
  k8fa801rspPasswordChar,
  k8fa802rspUserNameChar,
  k8fa803rspPasswordChar,
  k8fa804rspInitStringChar,
  k8fa90101rspfilenameChar,
  k8fa90103rspDataData,
  k8fa90a00rspFeaturesFeature,
  k8fa91500rspmd5Hashbyte,
  k8fa91500rspclientFileIdbyte,
  k8fa91501rspblockDatabyte,
  k8fad00rspPasscodePasscodeVal,
  k8fae05rspDeviceNameChar,
  kbe40cmdPacketDataData,
  kbe401400cmdTAPStringChars,
  kbe401401cmdTAPStringChars,
  kbe41cmdPacketDataData,
  kbe42cmdPacketDataData,
  kbe44cmdPacketDataData,
  kbe45cmdPacketDataData,
  kbe46cmdPacketDataData,
  kbe47cmdPacketDataData,
  kbe4acmdPacketDataData,
  kbe4bcmdPacketDataData,
  kbe4c0108cmdImplementWidthImplementText,
  kbe4c010bcmdMiscDataData,
  kbe4dcmdPacketDataData,
  kbe4ecmdPacketDataData,
  kbe4fcmdPacketDataData,
  kbe50cmdPacketDataData,
  kbe5014cmdPacketDataData,
  kbe51cmdPacketDataData,
  kbe52cmdPacketDataData,
  kbe53cmdPacketDataData,
  kbe54cmdPacketDataData,
  kbe55cmdPacketDataData,
  kbe56cmdPacketDataData,
  kbe57cmdPacketDataData,
  kbe5acmdPacketDataData,
  kbe5ccmdPacketDataData,
  kbe5c011711cmdPacketDataData,
  kbe60cmdPacketDataData,
  kbe6014cmdPacketDataData,
  kbf1arspPacketDataData,
  kbf40rspPacketDataData,
  kbf400100rspOptionsOption,
  kbf401400rspTAPStringChars,
  kbf401401rspTAPStringChars,
  kbf41rspPacketDataData,
  kbf42rspPacketDataData,
  kbf43rspPacketDataData,
  kbf44rspPacketDataData,
  kbf45rspPacketDataData,
  kbf46rspPacketDataData,
  kbf47rspPacketDataData,
  kbf470502rspErrorValuesValue,
  kbf470503rspErrorValuesValue,
  kbf470504rspErrorValuesValue,
  kbf470506rspStringCharacter,
  kbf470509rspStringCharacter,
  kbf47050brspStringCharacter,
  kbf4707rspHighPrecisionADCHighPrecisionADCChannel,
  kbf4707rspLowPrecisionADCLowPrecisionADCChannel,
  kbf470e06rspPacketDataChars,
  kbf470e07rspPacketDataChars,
  kbf4arspPacketDataData,
  kbf4brspPacketDataData,
  kbf4c0108rspImplementWidthImplementText,
  kbf4c010brspMiscDataData,
  kbf4c2001rspCanMsgData,
  kbf4c8001rspPacketDataData,
  kbf4drspPacketDataData,
  kbf4erspPacketDataData,
  kbf4frspPacketDataData,
  kbf5014rspPacketDataData,
  kbf6014rspPacketDataData,
  kbf710000rspOptionsOptionsData,
  kbf710300rspExtIOFctArrayExtIOFctData,
  kbf710300rspVdmIOFctArrayVdmIOFctData,
  kbf710900rspCSValues,
  kc60000cmdChallengeResponseChallengeData,
  kc60000cmdDigestDigestData,
  kc60100cmdChallengeResponseChallengeData,
  kc60100cmdDigestDigestData,
  kc60200cmdChallengeResponseChallengeData,
  kc60200cmdAuthorizedFixEngineArrayAuthorizedFixEngineAccuracyLevel,
  kc60200cmdDigestDigestData,
  kc60400cmdChallengeResponseChallengeData,
  kc60400cmdDigestDigestData,

]

kNumCommonSchemaFields = NUMFIELDS(kCommonSchemaFieldsList)

kCommonGroupSchemaList = [
  k47rspSignalLevelsInfoArraySignalLevelInfoGroup,
  k890000rspOverallSystemStatusGroup,
  k890000rspIndividualKeysStatusKeyStatusGroup,
  k8960rspBaseVectorGroup,
  k8961rspBasePositionGroup,
  k897005rspChannelArrayChannelInfoGroup,
  k897005rspBandingGroup,
  k8e7ccmdConfigBlockV3FixedDefBoilerPlateGroup,
  k8e7ccmdConfigBlockV3FixedDefRxDefGroup,
  k8e7ccmdConfigBlockV3FixedDefGroup,
  k8e7ccmdConfigBlockV3UserDefPortConfigPortConfigGroup,
  k8e7ccmdConfigBlockV3UserDefGroup,
  k8e7ccmdConfigBlockV3Group,
  k8e9ecmdSourceInfoArrayGroup,
  k8e9f00cmdChannelCfgCANChannelCfgGroup,
  k8e9f02cmdMsgCfgArrayMsgCfgGroup,
  k8e9f03cmdMsgCfgArrayMsgCfgGroup,
  k8e9f04cmdMsgCfgArrayMsgCfgGroup,
  k8ea500cmdSBASInfoArraySBASInfoGroup,
  k8eab05cmdRTXOffsetGroup,
  k8eac0001cmdsensorsArraysensorsGroup,
  k8eac0002cmdactuatorsArrayactuatorsGroup,
  k8eac04cmdManualZoneArrayZoneManGroup,
  k8f7brspConfigBlockV3FixedDefBoilerPlateGroup,
  k8f7brspConfigBlockV3FixedDefRxDefGroup,
  k8f7brspConfigBlockV3FixedDefGroup,
  k8f7brspConfigBlockV3UserDefPortConfigPortConfigGroup,
  k8f7brspConfigBlockV3UserDefGroup,
  k8f7brspConfigBlockV3Group,
  k8f7frspConfigBlockV3FixedDefBoilerPlateGroup,
  k8f7frspConfigBlockV3FixedDefRxDefGroup,
  k8f7frspConfigBlockV3FixedDefGroup,
  k8f7frspConfigBlockV3UserDefPortConfigPortConfigGroup,
  k8f7frspConfigBlockV3UserDefGroup,
  k8f7frspConfigBlockV3Group,
  k8f85rspChannelDataArrayChannelDataBlockGroup,
  k8f9erspSourceInfoArrayGroup,
  k8f9f00rspChannelCfgCANChannelCfgGroup,
  k8f9f01rspChannelCfgCANChannelCfgGroup,
  k8f9f02rspMsgCfgArrayMsgCfgGroup,
  k8f9f03rspMsgCfgArrayMsgCfgGroup,
  k8f9f04rspMsgCfgArrayMsgCfgGroup,
  k8fa303rspStationInfoArrayStationInfoGroup,
  k8fa500rspSBASInfoArraySBASInfoGroup,
  k8fa634rspBandResultArrayBandResultGroup,
  k8fa90300rspAntennaArrayAntennaInfoGroup,
  k8fa90600rspConvertedADCChannelReadingsADCChannelReadingGroup,
  k8fa90a01rspLicensesLicenseStatusGroup,
  k8fa910rspUnlockStatusInfoArrayUnlockStatusInfoGroup,
  k8fab05rspRTXOffsetGroup,
  k8fac0101rspsensorsArraysensorsGroup,
  k8fac0102rspactuatorsArrayactuatorsGroup,
  k8fac04rspZoneArrayZoneStatusGroup,
  k8fac04rspSensorsArraySensorStatusGroup,
  k8fac06rspAlertArrayAlertDescGroup,
  k8fac07rspDevicesArrayDevicesGroup,
  kbe4c011706cmdPointAGroup,
  kbe4c011706cmdPointBGroup,
  kbe4c011706cmdCenterPointGroup,
  kbe4c011710cmdPointAGroup,
  kbe4c011710cmdPointBGroup,
  kbe4c011711cmdPointsPointGroup,
  kbe4c011713cmdPointAGroup,
  kbe4c011713cmdPointBGroup,
  kbe4c011720cmdPointAGroup,
  kbe4c011720cmdPointBGroup,
  kbe4c011721cmdPointsPointGroup,
  kbf4c011806rspPointAGroup,
  kbf4c011806rspPointBGroup,
  kbf4c011806rspCenterPointGroup,
  kbf4c0120rspPointsPointDiffGroup,
  kbf4c8000rspSequenceEventsSequenceEventGroup,
  kc60100cmdAuthorizedBaseArrayAuthorizedBaseEntryGroup,
  kd500rspSatInfoArraySatInfoFreqBandArrayFreqBandInfoGroup,
  kd500rspSatInfoArraySatInfoGroup,

  0 # Bogus item to ensure at least one thing is in the array
]

kNumCommonGroupSchemaFields = NUMFIELDS(kCommonGroupSchemaList) - 1


kClientSchemaList = [
  k00cmdEntry,
  k1a00cmdEntry,
  k1a0200cmdEntry,
  k1a0201cmdEntry,
  k1a0202cmdEntry,
  k1a0300cmdEntry,
  k1a0301cmdEntry,
  k1e4bcmdEntry,
  k1freqEntry,
  k1freqv1Entry,
  k20reqEntry,
  k21reqEntry,
  k22cmdEntry,
  k25cmdEntry,
  k26reqEntry,
  k27reqEntry,
  k2creqEntry,
  k2ccmdEntry,
  k33reqEntry,
  k35reqEntry,
  k35cmdEntry,
  k38cmdEntry,
  k3breqEntry,
  k3creqEntry,
  k3f02cmdEntry,
  k3f2200reqEntry,
  k3f2200cmdEntry,
  k62reqEntry,
  k62cmdEntry,
  k65reqEntry,
  k690000reqEntry,
  k690001reqEntry,
  k690002cmdEntry,
  k690003cmdEntry,
  k6932reqEntry,
  k6940reqEntry,
  k6940cmdEntry,
  k6941reqEntry,
  k6950reqEntry,
  k6950cmdEntry,
  k6951reqEntry,
  k6960reqEntry,
  k6961reqEntry,
  k6962reqEntry,
  k697000reqEntry,
  k697001reqEntry,
  k697002reqEntry,
  k697003reqEntry,
  k697004reqEntry,
  k697005reqEntry,
  k697006cmdEntry,
  k697007cmdEntry,
  k697008cmdEntry,
  k697009cmdEntry,
  k69700acmdEntry,
  k69700bcmdEntry,
  k697100reqEntry,
  k697100cmdEntry,
  k697101reqEntry,
  k697101cmdEntry,
  k697103reqEntry,
  k697103cmdEntry,
  k6a01reqEntry,
  k6a01cmdEntry,
  k6b00reqEntry,
  k6b00cmdEntry,
  k6b02reqEntry,
  k6e03cmdEntry,
  k70cmdEntry,
  k77reqEntry,
  k77cmdEntry,
  k7a07reqEntry,
  k7a07cmdEntry,
  k7a08reqEntry,
  k7a08cmdEntry,
  k7a80reqEntry,
  k7a80cmdEntry,
  k7a86reqEntry,
  k7a8600cmdEntry,
  k7a8602cmdEntry,
  k7a8603cmdEntry,
  k7a8604cmdEntry,
  k7a8605cmdEntry,
  k7c00reqEntry,
  k7c00cmdEntry,
  k7c01reqEntry,
  k7c01cmdEntry,
  k7c02reqEntry,
  k7c02cmdEntry,
  k7c09reqEntry,
  k7c09cmdEntry,
  k8e7breqEntry,
  k8e7ccmdEntry,
  k8e7freqEntry,
  k8e80reqEntry,
  k8e81reqEntry,
  k8e84cmdEntry,
  k8e85reqEntry,
  k8e88reqEntry,
  k8e88cmdEntry,
  k8e89reqEntry,
  k8e89cmdEntry,
  k8e8breqEntry,
  k8e8c00cmdEntry,
  k8e8c01reqEntry,
  k8e8c03reqEntry,
  k8e8c03cmdEntry,
  k8e8c04reqEntry,
  k8e8c04cmdEntry,
  k8e8c05cmdEntry,
  k8e8freqEntry,
  k8e91reqEntry,
  k8e91cmdEntry,
  k8e931500reqEntry,
  k8e93150101reqEntry,
  k8e93150102reqEntry,
  k8e93150103reqEntry,
  k8e93150104reqEntry,
  k8e93150201reqEntry,
  k8e93150202reqEntry,
  k8e93150203reqEntry,
  k8e931503reqEntry,
  k8e9areqEntry,
  k8e9ereqEntry,
  k8e9ecmdEntry,
  k8e9f00reqEntry,
  k8e9f00cmdEntry,
  k8e9f01reqEntry,
  k8e9f02reqEntry,
  k8e9f02cmdEntry,
  k8e9f03reqEntry,
  k8e9f03cmdEntry,
  k8e9f04reqEntry,
  k8e9f04cmdEntry,
  k8ea0cmdEntry,
  k8ea1cmdEntry,
  k8ea2reqEntry,
  k8ea3reqEntry,
  k8ea304cmdEntry,
  k8ea305cmdEntry,
  k8ea306cmdEntry,
  k8ea307cmdEntry,
  k8ea4reqEntry,
  k8ea405cmdEntry,
  k8ea406cmdEntry,
  k8ea407cmdEntry,
  k8ea500reqEntry,
  k8ea500cmdEntry,
  k8ea501reqEntry,
  k8ea501cmdEntry,
  k8ea502cmdEntry,
  k8ea601cmdEntry,
  k8ea602reqEntry,
  k8ea608reqEntry,
  k8ea617reqEntry,
  k8ea622reqEntry,
  k8ea623reqEntry,
  k8ea624reqEntry,
  k8ea625cmdEntry,
  k8ea626reqEntry,
  k8ea627cmdEntry,
  k8ea628cmdEntry,
  k8ea629reqEntry,
  k8ea630reqEntry,
  k8ea631reqEntry,
  k8ea632reqEntry,
  k8ea632cmdEntry,
  k8ea633reqEntry,
  k8ea634reqEntry,
  k8ea640cmdEntry,
  k8ea641cmdEntry,
  k8ea642cmdEntry,
  k8ea643cmdEntry,
  k8ea644cmdEntry,
  k8ea645cmdEntry,
  k8ea646cmdEntry,
  k8ea647reqEntry,
  k8ea648cmdEntry,
  k8ea70000cmdEntry,
  k8ea70001cmdEntry,
  k8ea70002cmdEntry,
  k8ea70003cmdEntry,
  k8ea70100reqEntry,
  k8ea70101reqEntry,
  k8ea70102reqEntry,
  k8ea70103reqEntry,
  k8ea800reqEntry,
  k8ea801cmdEntry,
  k8ea801reqEntry,
  k8ea802cmdEntry,
  k8ea802reqEntry,
  k8ea803cmdEntry,
  k8ea803reqEntry,
  k8ea804cmdEntry,
  k8ea804reqEntry,
  k8ea805cmdEntry,
  k8ea806cmdEntry,
  k8ea806reqEntry,
  k8ea900reqEntry,
  k8ea90100cmdEntry,
  k8ea90101cmdEntry,
  k8ea90101reqEntry,
  k8ea90102cmdEntry,
  k8ea90103cmdEntry,
  k8ea90104reqEntry,
  k8ea90104cmdEntry,
  k8ea90105cmdEntry,
  k8ea90106reqEntry,
  k8ea90106cmdEntry,
  k8ea90107reqEntry,
  k8ea90107cmdEntry,
  k8ea90108reqEntry,
  k8ea90108cmdEntry,
  k8ea90130reqEntry,
  k8ea90131reqEntry,
  k8ea90200reqEntry,
  k8ea90200cmdEntry,
  k8ea90201reqEntry,
  k8ea90201cmdEntry,
  k8ea90202reqEntry,
  k8ea90202cmdEntry,
  k8ea90300reqEntry,
  k8ea90301cmdEntry,
  k8ea90400reqEntry,
  k8ea90400cmdEntry,
  k8ea905cmdEntry,
  k8ea90600reqEntry,
  k8ea90700reqEntry,
  k8ea90700cmdEntry,
  k8ea90701reqEntry,
  k8ea90701cmdEntry,
  k8ea90703reqEntry,
  k8ea90703cmdEntry,
  k8ea90704reqEntry,
  k8ea90704cmdEntry,
  k8ea90705reqEntry,
  k8ea90705cmdEntry,
  k8ea90706reqEntry,
  k8ea90707reqEntry,
  k8ea90707cmdEntry,
  k8ea90708reqEntry,
  k8ea90800reqEntry,
  k8ea90800cmdEntry,
  k8ea909reqEntry,
  k8ea909cmdEntry,
  k8ea90a00reqEntry,
  k8ea90a01reqEntry,
  k8ea910reqEntry,
  k8ea911reqEntry,
  k8ea912reqEntry,
  k8ea913reqEntry,
  k8ea91500cmdEntry,
  k8ea91501cmdEntry,
  k8ea91502cmdEntry,
  k8ea91503cmdEntry,
  k8ea91504cmdEntry,
  k8ea9160000reqEntry,
  k8ea9160000cmdEntry,
  k8ea9160001reqEntry,
  k8ea9160001cmdEntry,
  k8ea9160002reqEntry,
  k8ea9160002cmdEntry,
  k8ea9160100reqEntry,
  k8ea9160100cmdEntry,
  k8ea91602reqEntry,
  k8ea91602cmdEntry,
  k8ea91603cmdEntry,
  k8ea91604cmdEntry,
  k8ea91605cmdEntry,
  k8ea91606reqEntry,
  k8ea91700reqEntry,
  k8ea91700cmdEntry,
  k8ea91701cmdEntry,
  k8ea91701reqEntry,
  k8ea91702reqEntry,
  k8ea91703reqEntry,
  k8ea91703cmdEntry,
  k8ea918reqEntry,
  k8ea9a5reqEntry,
  k8eaa00reqEntry,
  k8eaa00cmdEntry,
  k8eab00reqEntry,
  k8eab01reqEntry,
  k8eab02cmdEntry,
  k8eab03reqEntry,
  k8eab04cmdEntry,
  k8eab05cmdEntry,
  k8eab05reqEntry,
  k8eab06cmdEntry,
  k8eab07reqEntry,
  k8eab07cmdEntry,
  k8eab08reqEntry,
  k8eac0000cmdEntry,
  k8eac0001cmdEntry,
  k8eac0002cmdEntry,
  k8eac0100reqEntry,
  k8eac0101reqEntry,
  k8eac0102reqEntry,
  k8eac02cmdEntry,
  k8eac03reqEntry,
  k8eac04cmdEntry,
  k8eac05cmdEntry,
  k8eac06reqEntry,
  k8eac07reqEntry,
  k8ead00reqEntry,
  k8ead01cmdEntry,
  k8ead02reqEntry,
  k8ead03cmdEntry,
  k8eae00reqEntry,
  k8eae01cmdEntry,
  k8eae02cmdEntry,
  k8eae03cmdEntry,
  k8eae04reqEntry,
  k8eae05reqEntry,
  k8fa90708reqEntry,
  kb000reqEntry,
  kb000cmdEntry,
  kb001cmdEntry,
  kbb00reqEntry,
  kbb00cmdEntry,
  kbcreqEntry,
  kbccmdEntry,
  kbe40cmdEntry,
  kbe400000cmdEntry,
  kbe400003cmdEntry,
  kbe400100cmdEntry,
  kbe400103cmdEntry,
  kbe401400cmdEntry,
  kbe401401cmdEntry,
  kbe41cmdEntry,
  kbe42cmdEntry,
  kbe4200cmdEntry,
  kbe4201cmdEntry,
  kbe4202cmdEntry,
  kbe4301cmdEntry,
  kbe4303cmdEntry,
  kbe4306cmdEntry,
  kbe43060000cmdEntry,
  kbe43060001cmdEntry,
  kbe43060002cmdEntry,
  kbe43060100cmdEntry,
  kbe43060101cmdEntry,
  kbe43060102cmdEntry,
  kbe430bcmdEntry,
  kbe430dcmdEntry,
  kbe44cmdEntry,
  kbe45cmdEntry,
  kbe46cmdEntry,
  kbe4600cmdEntry,
  kbe47cmdEntry,
  kbe470500cmdEntry,
  kbe470501cmdEntry,
  kbe470502cmdEntry,
  kbe470503cmdEntry,
  kbe470504cmdEntry,
  kbe470505cmdEntry,
  kbe470506cmdEntry,
  kbe470507cmdEntry,
  kbe470508cmdEntry,
  kbe470509cmdEntry,
  kbe47050acmdEntry,
  kbe47050bcmdEntry,
  kbe4707cmdEntry,
  kbe470e08cmdEntry,
  kbe470e09cmdEntry,
  kbe471400cmdEntry,
  kbe471401cmdEntry,
  kbe471402cmdEntry,
  kbe471ecmdEntry,
  kbe4acmdEntry,
  kbe4a0b00cmdEntry,
  kbe4a0b01cmdEntry,
  kbe4a0ccmdEntry,
  kbe4a0c00cmdEntry,
  kbe4a0c08cmdEntry,
  kbe4a0c09cmdEntry,
  kbe4bcmdEntry,
  kbe4c00000004cmdEntry,
  kbe4c00000104cmdEntry,
  kbe4c00000204cmdEntry,
  kbe4c00000704cmdEntry,
  kbe4c0100cmdEntry,
  kbe4c0106cmdEntry,
  kbe4c0107cmdEntry,
  kbe4c0108reqEntry,
  kbe4c0108cmdEntry,
  kbe4c010acmdEntry,
  kbe4c010breqEntry,
  kbe4c010bcmdEntry,
  kbe4c010dreqEntry,
  kbe4c010dcmdEntry,
  kbe4c010ereqEntry,
  kbe4c010ecmdEntry,
  kbe4c010freqEntry,
  kbe4c010fcmdEntry,
  kbe4c011000reqEntry,
  kbe4c011001cmdEntry,
  kbe4c011002cmdEntry,
  kbe4c011003reqEntry,
  kbe4c011004cmdEntry,
  kbe4c0111cmdEntry,
  kbe4c0114cmdEntry,
  kbe4c011706cmdEntry,
  kbe4c011710cmdEntry,
  kbe4c011711cmdEntry,
  kbe4c011713cmdEntry,
  kbe4c011720cmdEntry,
  kbe4c011721cmdEntry,
  kbe4c0119cmdEntry,
  kbe4c011acmdEntry,
  kbe4c2000reqEntry,
  kbe4c2000cmdEntry,
  kbe4c2001reqEntry,
  kbe4c2300cmdEntry,
  kbe4c2301cmdEntry,
  kbe4c2302reqEntry,
  kbe4c2302cmdEntry,
  kbe4c8000cmdEntry,
  kbe4c8001cmdEntry,
  kbe4dcmdEntry,
  kbe4ecmdEntry,
  kbe4fcmdEntry,
  kbe50cmdEntry,
  kbe5014cmdEntry,
  kbe51cmdEntry,
  kbe52cmdEntry,
  kbe53cmdEntry,
  kbe530600cmdEntry,
  kbe530601cmdEntry,
  kbe54cmdEntry,
  kbe55cmdEntry,
  kbe56cmdEntry,
  kbe57cmdEntry,
  kbe570507cmdEntry,
  kbe5acmdEntry,
  kbe5ccmdEntry,
  kbe5c0100cmdEntry,
  kbe5c0106cmdEntry,
  kbe5c0107cmdEntry,
  kbe5c010acmdEntry,
  kbe5c010bcmdEntry,
  kbe5c011000cmdEntry,
  kbe5c011001cmdEntry,
  kbe5c011002cmdEntry,
  kbe5c011003cmdEntry,
  kbe5c011004cmdEntry,
  kbe5c0111cmdEntry,
  kbe5c0114cmdEntry,
  kbe5c011700cmdEntry,
  kbe5c011706cmdEntry,
  kbe5c011710cmdEntry,
  kbe5c011711cmdEntry,
  kbe5c011713cmdEntry,
  kbe5c0119cmdEntry,
  kbe60cmdEntry,
  kbe6014cmdEntry,
  kbe630600cmdEntry,
  kbe630601cmdEntry,
  kbe710000reqEntry,
  kbe710100reqEntry,
  kbe710200reqEntry,
  kbe710201reqEntry,
  kbe710300reqEntry,
  kbe710400reqEntry,
  kbe710500reqEntry,
  kbe710600reqEntry,
  kbe710700reqEntry,
  kbe710800reqEntry,
  kbe710900reqEntry,
  kbe710a00reqEntry,
  kbe710b00reqEntry,
  kbe710c00reqEntry,
  kbe710d00reqEntry,
  kbe710e00reqEntry,
  kbe710f00reqEntry,
  kbe8000cmdEntry,
  kc500reqEntry,
  kc501cmdEntry,
  kc502reqEntry,
  kc60000cmdEntry,
  kc60100cmdEntry,
  kc60200cmdEntry,
  kc60400cmdEntry,
  kc700cmdEntry,
  kc701reqEntry,
  kc701cmdEntry,
  0 # Bogus item to ensure at least one thing is in the array
]

kServerSchemaList = [
  k00rspEntry,
  k13rspEntry,
  k1a01rspEntry,
  k1a0200rspEntry,
  k1a0201rspEntry,
  k1a0300rspEntry,
  k1a0301rspEntry,
  k40rspEntry,
  k41rspEntry,
  k42rspEntry,
  k43rspEntry,
  k45rspEntry,
  k45rspv1Entry,
  k46rspEntry,
  k47rspEntry,
  k48rspEntry,
  k4arspEntry,
  k4arspv1Entry,
  k4arspv2Entry,
  k4brspEntry,
  k4crspEntry,
  k4frspEntry,
  k53rspEntry,
  k55rspEntry,
  k58rspEntry,
  k5822rspEntry,
  k5823rspEntry,
  k5824rspEntry,
  k5825rspEntry,
  k5826rspEntry,
  k5brspEntry,
  k5crspEntry,
  k5f01rspEntry,
  k5f02rspEntry,
  k5f10rspEntry,
  k5f2200rspEntry,
  k5f2201rspEntry,
  k6a01rspEntry,
  k6drspEntry,
  k6f01rspEntry,
  k6f10rspEntry,
  k6f20rspEntry,
  k6f21rspEntry,
  k70rspEntry,
  k78rspEntry,
  k7b07rspEntry,
  k7b08ackEntry,
  k7b08rspEntry,
  k7b80rspEntry,
  k7b8600rspEntry,
  k7b8602rspEntry,
  k7b8603rspEntry,
  k7b8605rspEntry,
  k7b860604rspEntry,
  k7d00rspEntry,
  k7d01rspEntry,
  k7d02rspEntry,
  k7d09rspEntry,
  k82rspEntry,
  k82rspv1Entry,
  k83rspEntry,
  k890000rspEntry,
  k890001rspEntry,
  k890002rspEntry,
  k890003rspEntry,
  k893308rspEntry,
  k8940rspEntry,
  k8941rspEntry,
  k8950rspEntry,
  k8951rspEntry,
  k8960rspEntry,
  k8961rspEntry,
  k8962rspEntry,
  k897000rspEntry,
  k897001rspEntry,
  k897002rspEntry,
  k897003rspEntry,
  k897004rspEntry,
  k897005rspEntry,
  k897006ackEntry,
  k897007ackEntry,
  k897008ackEntry,
  k897009ackEntry,
  k89700aackEntry,
  k89700backEntry,
  k89700cackEntry,
  k89700drspEntry,
  k897100rspEntry,
  k897100ackEntry,
  k897101rspEntry,
  k897101ackEntry,
  k897103rspEntry,
  k897103ackEntry,
  k8b00rspEntry,
  k8b02rspEntry,
  k8frspEntry,
  k8f77rspEntry,
  k8f770rspEntry,
  k8f7brspEntry,
  k8f7cackEntry,
  k8f7frspEntry,
  k8f80rspEntry,
  k8f84ackEntry,
  k8f85rspEntry,
  k8f89rspEntry,
  k8f89ackEntry,
  k8f8brspEntry,
  k8f8cackEntry,
  k8f8c01rspEntry,
  k8f8c02rspEntry,
  k8f8c03rspEntry,
  k8f8c04rspEntry,
  k8f8frspEntry,
  k8f91rspEntry,
  k8f91ackEntry,
  k8f9306rspEntry,
  k8f931500rspEntry,
  k8f93150100rspEntry,
  k8f93150101rspEntry,
  k8f93150102rspEntry,
  k8f93150103rspEntry,
  k8f93150104rspEntry,
  k8f93150200rspEntry,
  k8f93150201rspEntry,
  k8f93150202rspEntry,
  k8f93150203rspEntry,
  k8f931503rspEntry,
  k8f9arspEntry,
  k8f9erspEntry,
  k8f9f00rspEntry,
  k8f9f00ackEntry,
  k8f9f01rspEntry,
  k8f9f02rspEntry,
  k8f9f02ackEntry,
  k8f9f03rspEntry,
  k8f9f03ackEntry,
  k8f9f04rspEntry,
  k8f9f04ackEntry,
  k8fa0rspEntry,
  k8fa1rspEntry,
  k8fa2rspEntry,
  k8fa300rspEntry,
  k8fa301rspEntry,
  k8fa302rspEntry,
  k8fa303rspEntry,
  k8fa304rspEntry,
  k8fa305rspEntry,
  k8fa306rspEntry,
  k8fa307ackEntry,
  k8fa405rspEntry,
  k8fa406rspEntry,
  k8fa407rspEntry,
  k8fa500rspEntry,
  k8fa501rspEntry,
  k8fa502ackEntry,
  k8fa601ackEntry,
  k8fa602rspEntry,
  k8fa608rspEntry,
  k8fa617rspEntry,
  k8fa622rspEntry,
  k8fa623rspEntry,
  k8fa624rspEntry,
  k8fa625ackEntry,
  k8fa626rspEntry,
  k8fa627ackEntry,
  k8fa628ackEntry,
  k8fa629rspEntry,
  k8fa630rspEntry,
  k8fa631rspEntry,
  k8fa632rspEntry,
  k8fa632ackEntry,
  k8fa633rspEntry,
  k8fa634ackEntry,
  k8fa634rspEntry,
  k8fa640ackEntry,
  k8fa641ackEntry,
  k8fa642ackEntry,
  k8fa643ackEntry,
  k8fa644ackEntry,
  k8fa645ackEntry,
  k8fa646ackEntry,
  k8fa647rspEntry,
  k8fa648ackEntry,
  k8fa70000rspEntry,
  k8fa70001rspEntry,
  k8fa70002rspEntry,
  k8fa70003rspEntry,
  k8fa70100rspEntry,
  k8fa70101rspEntry,
  k8fa70102rspEntry,
  k8fa800rspEntry,
  k8fa801ackEntry,
  k8fa801rspEntry,
  k8fa802ackEntry,
  k8fa802rspEntry,
  k8fa803ackEntry,
  k8fa803rspEntry,
  k8fa804ackEntry,
  k8fa804rspEntry,
  k8fa805ackEntry,
  k8fa806ackEntry,
  k8fa806rspEntry,
  k8fa900rspEntry,
  k8fa90100ackEntry,
  k8fa90100rspEntry,
  k8fa90101ackEntry,
  k8fa90101rspEntry,
  k8fa90102ackEntry,
  k8fa90103rspEntry,
  k8fa90104rspEntry,
  k8fa90105ackEntry,
  k8fa90106rspEntry,
  k8fa90107rspEntry,
  k8fa90108rspEntry,
  k8fa90130rspEntry,
  k8fa90131rspEntry,
  k8fa90200rspEntry,
  k8fa90201rspEntry,
  k8fa90202rspEntry,
  k8fa90300rspEntry,
  k8fa90400rspEntry,
  k8fa905ackEntry,
  k8fa90600rspEntry,
  k8fa90700rspEntry,
  k8fa90701rspEntry,
  k8fa90703rspEntry,
  k8fa90704rspEntry,
  k8fa90705rspEntry,
  k8fa90706rspEntry,
  k8fa90707rspEntry,
  k8fa90800rspEntry,
  k8fa909ackEntry,
  k8fa909rspEntry,
  k8fa90a00rspEntry,
  k8fa90a01rspEntry,
  k8fa910rspEntry,
  k8fa911rspEntry,
  k8fa912rspEntry,
  k8fa913rspEntry,
  k8fa914rspEntry,
  k8fa91500rspEntry,
  k8fa91501rspEntry,
  k8fa91502rspEntry,
  k8fa91503rspEntry,
  k8fa91504rspEntry,
  k8fa91599rspEntry,
  k8fa9160000rspEntry,
  k8fa9160001rspEntry,
  k8fa9160002rspEntry,
  k8fa9160100rspEntry,
  k8fa91602rspEntry,
  k8fa91603rspEntry,
  k8fa91604rspEntry,
  k8fa91605rspEntry,
  k8fa91606rspEntry,
  k8fa91700rspEntry,
  k8fa91701rspEntry,
  k8fa91702rspEntry,
  k8fa91703rspEntry,
  k8fa918rspEntry,
  k8fa9a5rspEntry,
  k8faa00rspEntry,
  k8fab00rspEntry,
  k8fab01rspEntry,
  k8fab02ackEntry,
  k8fab03rspEntry,
  k8fab04ackEntry,
  k8fab05rspEntry,
  k8fab06rspEntry,
  k8fab07rspEntry,
  k8fab08rspEntry,
  k8fac0100rspEntry,
  k8fac0101rspEntry,
  k8fac0102rspEntry,
  k8fac02rspEntry,
  k8fac03rspEntry,
  k8fac04rspEntry,
  k8fac05rspEntry,
  k8fac06rspEntry,
  k8fac07rspEntry,
  k8fad00rspEntry,
  k8fad01ackEntry,
  k8fad02rspEntry,
  k8fae00rspEntry,
  k8fae01rspEntry,
  k8fae02rspEntry,
  k8fae03rspEntry,
  k8fae04rspEntry,
  k8fae05rspEntry,
  k8fae05ackEntry,
  kb080rspEntry,
  kb081rspEntry,
  kbb00rspEntry,
  kbcrspEntry,
  kbf1arspEntry,
  kbf40rspEntry,
  kbf400000rspEntry,
  kbf400100rspEntry,
  kbf401400rspEntry,
  kbf401401rspEntry,
  kbf41rspEntry,
  kbf42rspEntry,
  kbf4200rspEntry,
  kbf4201rspEntry,
  kbf4202rspEntry,
  kbf43rspEntry,
  kbf4301rspEntry,
  kbf4303rspEntry,
  kbf4306rspEntry,
  kbf44rspEntry,
  kbf45rspEntry,
  kbf46rspEntry,
  kbf47rspEntry,
  kbf470500rspEntry,
  kbf470501rspEntry,
  kbf470502rspEntry,
  kbf470503rspEntry,
  kbf470504rspEntry,
  kbf470505rspEntry,
  kbf470506rspEntry,
  kbf470507rspEntry,
  kbf470508rspEntry,
  kbf470509rspEntry,
  kbf47050arspEntry,
  kbf47050brspEntry,
  kbf4707rspEntry,
  kbf470e06rspEntry,
  kbf470e07rspEntry,
  kbf470e08rspEntry,
  kbf470e09rspEntry,
  kbf471400rspEntry,
  kbf471401rspEntry,
  kbf471402rspEntry,
  kbf471erspEntry,
  kbf4arspEntry,
  kbf4a0b00rspEntry,
  kbf4a0b01rspEntry,
  kbf4a0c00rspEntry,
  kbf4a0c08rspEntry,
  kbf4brspEntry,
  kbf4c00000004rspEntry,
  kbf4c00000104rspEntry,
  kbf4c00000204rspEntry,
  kbf4c00000704rspEntry,
  kbf4c0101rspEntry,
  kbf4c0108rspEntry,
  kbf4c010arspEntry,
  kbf4c010brspEntry,
  kbf4c010drspEntry,
  kbf4c010erspEntry,
  kbf4c010frspEntry,
  kbf4c011000rspEntry,
  kbf4c011001rspEntry,
  kbf4c011002rspEntry,
  kbf4c011003rspEntry,
  kbf4c011004rspEntry,
  kbf4c0111rspEntry,
  kbf4c0114rspEntry,
  kbf4c011806rspEntry,
  kbf4c011810rspEntry,
  kbf4c011811rspEntry,
  kbf4c011813rspEntry,
  kbf4c011820rspEntry,
  kbf4c011821rspEntry,
  kbf4c0119rspEntry,
  kbf4c011arspEntry,
  kbf4c0120rspEntry,
  kbf4c0500rspEntry,
  kbf4c2000rspEntry,
  kbf4c2001rspEntry,
  kbf4c2300rspEntry,
  kbf4c2301rspEntry,
  kbf4c2302rspEntry,
  kbf4c8000rspEntry,
  kbf4c8001rspEntry,
  kbf4c8002rspEntry,
  kbf4drspEntry,
  kbf4erspEntry,
  kbf4frspEntry,
  kbf5014rspEntry,
  kbf530600rspEntry,
  kbf530601rspEntry,
  kbf570507rspEntry,
  kbf5c0101rspEntry,
  kbf5c0106rspEntry,
  kbf5c0107rspEntry,
  kbf5c010brspEntry,
  kbf5c011000rspEntry,
  kbf5c011001rspEntry,
  kbf5c011002rspEntry,
  kbf5c011003rspEntry,
  kbf5c011004rspEntry,
  kbf5c0111rspEntry,
  kbf5c0114rspEntry,
  kbf5c0118rspEntry,
  kbf5c0119rspEntry,
  kbf6014rspEntry,
  kbf630600rspEntry,
  kbf630601rspEntry,
  kbf6800rspEntry,
  kbf6801rspEntry,
  kbf710000rspEntry,
  kbf710100rspEntry,
  kbf710200rspEntry,
  kbf710201rspEntry,
  kbf710300rspEntry,
  kbf710400rspEntry,
  kbf710500rspEntry,
  kbf710600rspEntry,
  kbf710700rspEntry,
  kbf710800rspEntry,
  kbf710900rspEntry,
  kbf710a00rspEntry,
  kbf710b00rspEntry,
  kbf710c00rspEntry,
  kbf710d00rspEntry,
  kbf710e00rspEntry,
  kbf710f00rspEntry,
  kd500rspEntry,
  kd502rspEntry,
  kd6ackEntry,
  kd700ackEntry,
  kd701ackEntry,
  kd701rspEntry,
  0 # Bogus item to ensure at least one thing is in the array
]


