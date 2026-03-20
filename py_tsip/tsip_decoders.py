from .tsip_packets import *
import logging
from struct import calcsize, unpack
from struct import error as struct_error

# Module-level logger
logger = logging.getLogger("py_tsip")
logger.setLevel(logging.WARNING)

def _resolve_variable_length_fields_decode(packetS, packetData, packetT):
    """
    Resolve EndTerminatedArrayField markers ('*') in struct format string for decoding.
    
    The '*' character indicates a variable-length field that needs to be replaced
    with the actual length of the received data. For B* patterns, the B is a length
    field that tells us how much variable data follows.
    
    Args:
        packetS (str): Struct format string potentially containing '*' markers
        packetData (bytes): Raw packet data received
        packetT: Tuple class for creating the result
        
    Returns:
        tuple: (resolved_format_string, resolved_data_tuple)
    """
    if '*' not in packetS:
        return packetS, packetData
    
    # Find the variable-length field in the format string
    # Format like '=BBBHB*' means: fixed fields + length byte + variable data
    if 'B*' in packetS:
        # Split around the B* pattern
        before_star = packetS.split('*')[0]  # e.g., '=BBBHB'
        after_star = packetS.split('*')[1] if len(packetS.split('*')) > 1 else ''  # e.g., '?'
        
        # Calculate size of fields before the variable part
        before_size = calcsize(before_star) if before_star != '=' else 0
        after_size = calcsize('=' + after_star) if after_star else 0
        
        # Extract the variable data length from the length byte
        if len(packetData) >= before_size:
            # The last byte in before_star is the length field
            length_byte_offset = before_size - 1
            variable_data_length = packetData[length_byte_offset] if length_byte_offset >= 0 else 0
            
            # Verify we have enough data for the specified length
            expected_total_size = before_size + variable_data_length + after_size
            if len(packetData) >= expected_total_size:
                # Replace '*' with actual length as 's' format
                resolved_format = packetS.replace('*', f'{variable_data_length}s')
                return resolved_format, packetData
            else:
                # Not enough data - use what we have
                available_data_length = len(packetData) - before_size - after_size
                available_data_length = max(0, available_data_length)
                resolved_format = packetS.replace('*', f'{available_data_length}s')
                return resolved_format, packetData
        else:
            # Not enough data - fallback
            resolved_format = packetS.replace('*', '0s')
            return resolved_format, packetData
    
    # Other '*' patterns - fallback to removing the marker
    resolved_format = packetS.replace('*', '0s')
    return resolved_format, packetData

def _resolve_optional_fields_decode(packetS, packetData, packetT):
    """
    Resolve optional CheckedLengthField markers ('?') in struct format string for decoding.
    
    The '?' character indicates an optional CheckedLengthField that may or may not 
    be present in the actual received data. This handles legacy compatibility where
    some packets have CheckedLengthField as metadata only, while others include it
    as an actual data field.
    
    Args:
        packetS (str): Struct format string potentially containing '?' markers
        packetData (bytes): Raw packet data received
        packetT: Tuple class for creating the result
        
    Returns:
        tuple: (resolved_format_string, should_add_default_length)
    """
    if '?' not in packetS:
        return packetS, False
    
    # Calculate expected size with and without the optional field
    format_with_optional = packetS.replace('?', 'B')
    format_without_optional = packetS.replace('?', '')
    
    expected_size_with = calcsize(format_with_optional)
    expected_size_without = calcsize(format_without_optional)
    actual_size = len(packetData)
    
    # Check if the data structure expects a Length field
    has_length_field = hasattr(packetT, '_fields') and 'Length' in packetT._fields
    
    if actual_size == expected_size_with:
        # Received data includes the optional field
        return format_with_optional, False
    elif actual_size == expected_size_without:
        # Received data doesn't include the optional field
        if has_length_field:
            # Need to add a default Length value when creating the tuple
            return format_without_optional, True
        else:
            # Legacy packet - no Length field expected
            return format_without_optional, False
    else:
        # Size mismatch - fall back to without optional field and let error handling deal with it
        return format_without_optional, has_length_field

def pretty_print_rsp(response, response_name=None):
    """ Pretty print the named tuples TSIP response

    Arguments:
        response {NamedTuple} -- Named tuple that a packet handler returns from pytsip

    Keyword Arguments:
        test_name {str} -- Name of test running (default: {None})
    """
    if not response:
        return

    if response_name:
        logger.info("[py-tsip]      <---- Received response for %s", response_name)

    # Get max field length in tuple for pretty formatting
    max_length = max([len(x) for x in response._fields])
    for field in response._fields:
        value = getattr(response, field)
        if isinstance(value, bytes):
            try:
                value = value.decode()
            except UnicodeDecodeError:
                try:
                    for index, byte in enumerate(value):
                        if byte == 0:  # Null terminator found
                            null_index = index
                            break
                    value = value[:null_index].decode()
                except UnicodeDecodeError:
                    logger.warning("[py-tsip] Unable to decode value from: %s", field)
                    continue
        spaces = 8 * " " + (max_length - len(field)) * " "
        logger.info('[py-tsip]            %s%s= %s', field, spaces, value)

"""
#=============================================================================
# ServerMessageDecoder
#=============================================================================
"""
class ServerMessageDecoder:

    def DecodeMessage(self, packetId, packetData):
        packetT = ServerTupleList[packetId.value]
        packetS = ServerStructList[packetId.value]
        decoder = None
        
        # Add detailed logging for the problematic packet
        packetName = EServerPackets(packetId).name if hasattr(EServerPackets, 'name') else str(packetId)
        logger.log(9, f"[py-tsip] DecodeMessage: Processing {packetName} (ID: {packetId}) with format '{packetS}' and {len(packetData)} bytes")

        # If we have a MonTsip packet don't try and decode it, just pass it through
        if len(packetData) > 2 and packetData[0] == 0x8f and packetData[1] == 0xa1:
                retdata = packetData
        # Look for an array in the structure file
        else:
            packetName = EServerPackets(packetId).name
            decoderName = packetName + "_decoder"
            try:
                decoder = getattr(self, decoderName)
            except:
                decoder = None

            if decoder != None:
                try:
                    retdata = decoder(packetId, packetData)
                except Exception as ex:
                    logger.exception("[py-tsip] custom decoder was unable to unpack packet %s , passing raw packet", packetId)
                    retdata = packetData

            else:
                # Handle both optional CheckedLengthField (?) and variable-length EndTerminatedArrayField (*) markers
                # First resolve variable-length fields
                temp_format, temp_data = _resolve_variable_length_fields_decode(packetS, packetData, packetT)
                # Then resolve optional fields
                resolved_format, add_default_length = _resolve_optional_fields_decode(temp_format, temp_data, packetT)
                
                try:
                    unpacked_data = unpack(resolved_format, temp_data)
                    if add_default_length:
                        # Add default Length=0 for CheckedLengthField compatibility
                        unpacked_data = unpacked_data + (0,)
                    retdata = packetT._make(unpacked_data)
                except struct_error as e:
                    # Handle EndTerminatedArrayField (511B) vs CheckedLengthField (trailing B)
                    expected_size = calcsize(packetS)
                    actual_size = len(packetData)
                    logger.info(f"[py-tsip] Dealing w/ variable length or CheckedLengthField for {packetName}: format='{packetS}', expected={expected_size}, actual={actual_size}, struct_error={e}")
                    
                    # CheckedLengthField pattern: firmware doesn't send Length byte, but format expects it
                    if expected_size == actual_size + 1 and packetS.endswith('B') and '511B' not in packetS:
                        # Remove trailing 'B' for CheckedLengthField
                        shorter_format = packetS[:-1]
                        logger.debug(f"[py-tsip] CheckedLengthField auto-fix for {packetName}: '{packetS}' -> '{shorter_format}'")
                        try:
                            retdata = packetT._make(unpack(shorter_format, packetData))
                        except struct_error as e2:
                            logger.error(f"[py-tsip] CheckedLengthField auto-fix failed for {packetName}: {e2}")
                            # Create minimal response as fallback
                            field_count = len(packetT._fields)
                            minimal_data = [0] * (field_count - 1) + [packetData]
                            retdata = packetT._make(minimal_data)
                            logger.warning(f"[py-tsip] Created minimal response for {packetName}")
                    elif '511B' in packetS:
                        # EndTerminatedArrayField: Check if this is a simple or complex packet
                        if packetS == '=B511B':
                            # Simple case - just length and data
                            if len(packetData) > 0:
                                packet_data_length = packetData[0]  # First byte is length
                                packet_data = packetData[1:]        # Rest is data
                                retdata = packetT._make([packet_data_length, packet_data])
                            else:
                                retdata = packetT._make([0, b''])
                        else:
                            # Complex case - try to handle it properly instead of returning raw data
                            logger.warning(f"[py-tsip] Complex EndTerminatedArrayField format {packetS} for {packetName} - attempting dynamic decode")
                            
                            # Try to extract the variable length data field
                            try:
                                # For formats like =BBBHB511BB, we need to handle the 511B part dynamically
                                if packetS.count('511B') == 1:
                                    before_511B, after_511B = packetS.split('511B')
                                    before_fields = before_511B.count('B') + before_511B.count('H') + before_511B.count('L')
                                    after_fields = after_511B.count('B')
                                    
                                    # Extract the fixed fields before the variable data
                                    fixed_size = calcsize(before_511B) if before_511B != '=' else 0
                                    variable_data_start = fixed_size
                                    variable_data_end = len(packetData) - after_fields
                                    variable_data = packetData[variable_data_start:variable_data_end]
                                    
                                    # Reconstruct the packet data
                                    if before_511B != '=':
                                        before_data = list(unpack(before_511B, packetData[:fixed_size]))
                                    else:
                                        before_data = []
                                    
                                    after_data = list(packetData[variable_data_end:]) if after_fields > 0 else []
                                    
                                    # Combine all fields
                                    all_fields = before_data + [variable_data] + after_data
                                    retdata = packetT._make(all_fields)
                                    logger.debug(f"[py-tsip] Successfully decoded complex EndTerminatedArrayField for {packetName}")
                                else:
                                    raise ValueError("Multiple 511B fields not supported")
                                    
                            except Exception as decode_ex:
                                logger.error(f"[py-tsip] Failed to decode complex EndTerminatedArrayField {packetS} for {packetName}: {decode_ex}")
                                # Create a minimal response to avoid returning raw data
                                try:
                                    # Try to create a minimal valid response based on the expected fields
                                    field_count = len(packetT._fields)
                                    minimal_data = [0] * (field_count - 1) + [packetData]  # Put raw data in last field
                                    retdata = packetT._make(minimal_data)
                                    logger.warning(f"[py-tsip] Created minimal response for {packetName} with raw data in last field")
                                except:
                                    logger.error(f"[py-tsip] Cannot create minimal response for {packetName}, returning raw data")
                                    retdata = packetData
                    else:
                        logger.error(f"[py-tsip] Unknown struct_error for {packetName}: format='{packetS}', expected={expected_size}, actual={actual_size}, error={e}")
                        raise  # Re-raise if neither case applies

        return retdata

    """
    #=============================================================================
    # e6drsp
    #=============================================================================
    """
    def e6drsp_decoder(self, packetId, PacketData):
        packetT = ServerTupleList[packetId.value]
        PacketS1 = '=Bffff'
        PacketT1 = namedtuple('PacketT1', ' FixMode PDOP HDOP VDOP TDOP')
        data1 = PacketData[:17]
        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        fixmode = retdata1.FixMode
        sats = (fixmode & 0xf0) >> 4
        SatsInView = PacketData[17:17 + sats]
        retdata = packetT(retdata1.FixMode, retdata1.PDOP,
                          retdata1.HDOP, retdata1.VDOP, retdata1.TDOP, SatsInView)
        return retdata

    """
    #=============================================================================
    # e13rsp
    #=============================================================================
    """
    def e13rsp_decoder(self, packetId, PacketData):
        logger.error(f'[py-tsip] Receiver sent a 0x13 response to {PacketData[0]:02x}{PacketData[2:].hex()}')
        return S13rsp_tup._make((PacketData[0], PacketData[1], PacketData[2:]))

    """
    #=============================================================================
    # e8f7brsp
    #=============================================================================
    """
    def e8f7brsp_decoder(self, packetId, PacketData):
        packetT = ServerTupleList[packetId.value]
        PacketS1 = '=B20sBBBBB'
        PacketT1 = namedtuple('PacketT1', ' PortNumber Name FirmwareMajVersion FirmwareMinVersion FirmwareMonth FirmwareDay FirmwareYear')
        data1 = PacketData[:26]
        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        ConfigBlock = PacketData[26:]
        retdata = packetT(retdata1.PortNumber, retdata1.Name, retdata1.FirmwareMajVersion, retdata1.FirmwareMinVersion,
                          retdata1.FirmwareMonth, retdata1.FirmwareDay, retdata1.FirmwareYear, ConfigBlock)
        return retdata

    """
    #=============================================================================
    # e8f9f00rsp
    #=============================================================================
    """
    def e8f9f00rsp_decoder(self, packetId, PacketData):
        packetT = ServerTupleList[packetId.value]
        NumChannels = unpack('=B', PacketData[:1])[0]
        if NumChannels == 2:
            PacketS1 = '=B' + '10s' * NumChannels
            PacketT1 = namedtuple('PacketT1', 'NumChannels ChannelCfg1 ChannelCfg2')
            data1 = PacketData[:21]
        else:
            PacketS1 = '=B' + '10s' * NumChannels
            PacketT1 = namedtuple('PacketT1', 'NumChannels ChannelCfg1')
            data1 = PacketData[:11]

        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        return retdata1

    """
    #=============================================================================
    # e8fae05rsp
    #=============================================================================
    """
    def e8fae05rsp_decoder(self, packetId, PacketData):
        packetT = ServerTupleList[packetId.value]
        PacketS1 = '=LB250s'
        PacketT1 = namedtuple('PacketT1', 'DeviceEventType DeviceNameLength DeviceName')

        data1 = PacketData[:255]
        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        retdata = packetT(retdata1.DeviceEventType, retdata1.DeviceNameLength, retdata1.DeviceName)
        return retdata

    """
    #=============================================================================
    # e8fa801rsp... '=HB?cB?cB?cB?c'
    #=============================================================================
    """
    def e8fa801rsp_decoder(self, packetId, PacketData):
        # ArraySchemaField uses max length (therefore use max length size)
        # This can be fixed by commenting out line 329 (OutBuf.fill) in tsip_schema.py but needs more investigation.
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=HB60sB60sB60sB60s'
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata

    """
    #=============================================================================
    # Omnistar XP/HP Status Response... '=hBffBBlB?l'
    #=============================================================================
    """
    def e8fa302rsp_decoder(self, packetId, PacketData):
        # S8fa302rsp_tup = namedtuple('S8fa302rsp_tup', ' EngineStatus SolutionStatus CorrectionAge EstimatedError AutoseedStatus PositionType GlobalStationId NumStations StationIds')
        # S8fa302rsp_bin = '=hBffBBlB?l'
        packetT = ServerTupleList[packetId.value]
        PacketS1 = '=HBffBBl'
        PacketT1 = namedtuple('PacketT1', ' EngineStatus SolutionStatus CorrectionAge EstimatedError AutoseedStatus PositionType GlobalStationId')
        data1 = PacketData[:17]
        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        stationsCnt = PacketData[27]
        stationData = PacketData[28:28 + (stationsCnt * 4)]
        retdata = packetT(retdata1.EngineStatus,
                          retdata1.SolutionStatus,
                          retdata1.CorrectionAge,
                          retdata1.EstimatedError,
                          retdata1.AutoseedStatus,
                          retdata1.PositionType,
                          retdata1.GlobalStationId,
                          stationsCnt,
                          stationData)
        return retdata

    """
    #=============================================================================
    # e45v1rsp
    #=============================================================================
    """
    def e45rspv1_decoder(self, packetId, PacketData):
        #S45rspv1_tup = namedtuple('S45rspv1_tup', ' NavProcMajVersion NavProcMinVersion NavProcMonth NavProcDay NavProcYear SigProcMajVersion SigProcMinVersion SigProcMonth SigProcDay SigProcYear, BCDSerialNumber BCDChecksum Revision ConfigLength NumChannels RTCMInput RTCMOutput FixRate SynchMeas Miscellaneous NMEAOutput PPSOutput ProductId')
        #S45rspv1_bin = '=BBBBBBBBBB6?BBHBBBBBBBBBB'
        datasize = len(PacketData)
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=BBBBBBBBBB6sBBHBBBBBBBBB'
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata


    """
    #=============================================================================
    # e58rsp
    #=============================================================================
    """
    def e58rsp_decoder(self, packetId, PacketData):
        #S58rsp_tup = namedtuple('S58rsp_tup', ' Operation DataType PRN NumBytes SVData')
        #S58rsp_bin = '=BBBB?B'
        packetT1 = namedtuple('packetT1', ' Operation DataType PRN NumBytes')
        packetS1 = '=BBBB'
        decode1 = packetT1._make(unpack_from(packetS1, PacketData, 0))
        PacketT = ServerTupleList[packetId.value]
        size = decode1.NumBytes
        length = len(PacketData)
        if (size+4) < length:
            size = length-4
        PacketS = '=BBBB%ds' % size
        retdata = PacketT._make(unpack_from(PacketS, PacketData, 0))
        return retdata

    def e6f21rsp_decoder(self, packetId, PacketData):
        #S6f21rsp_tup = namedtuple('S6f21rsp_tup', ' PacketLength MeasurementNumber GpsTime NumSVs, PayloadLength, Payload')
        #S6f21rsp_bin = '=hBdBB511B'
        datasize = len(PacketData)
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=hBdBB%ds' % (len(PacketData) - 13)
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata



    """
    #=============================================================================
    # e1a01rsp
    #=============================================================================
    """
    def e1a01rsp_decoder(self, packetId, PacketData):
        #S1a01rsp_tup = namedtuple('S1a01rsp_tup', ' NumBytes NMEAData')
        #S1a01rsp_bin = '=B?c'
        size = PacketData[0]
        PacketT = ServerTupleList[packetId.value]
        PacketS1 = '=B%ds' % size
        retdata = PacketT._make(unpack_from(PacketS1, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # ebf1arsp TSIP-wrapped NMEA
    #=============================================================================
    """
    def ebf1arsp_decoder(self, packetId, PacketData):
        packetT1 = namedtuple('packetT1', ' TsipWrappedPageId PacketDataLength')
        packetS1 = '=BB'
        decode1 = packetT1._make(unpack_from(packetS1, PacketData, 0))
        size = decode1.PacketDataLength
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=BB%ds' % size
        retdata = PacketT._make(unpack_from(PacketS, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Autopilot External Device FFA HeartBeat Response
    #=============================================================================
    """
    def ebf4c8000rsp_decoder(self, packetId, PacketData):
        packetT1 = namedtuple('packetT1', ' version swathDisposition requestedSwath progress signal indicators audibleAlert UIMessage nextSwathEnable trueSwathEnable left right sequenceEndOfRow sequenceStartOfRow dismiss accept FFAEngage acceptLiabililty declineLiability turnStartAuto turnStartManual, eventDataLength')
        packetS1 = '=BBHBBBBBBBBBBBBBBBBBBB'
        decode1 = packetT1._make(unpack_from(packetS1, PacketData, 0))
        size = decode1.eventDataLength
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=BBHBBBBBBBBBBBBBBBBBBB%ds' % size
        retdata = PacketT._make(unpack_from(PacketS, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Picus Upgrade Progress Response
    #=============================================================================
    """
    def e8fa90100rsp_decoder(self, packetId, PacketData):
        PacketT = ServerTupleList[packetId.value]
        PacketS1 = "<Bd"
        retdata = PacketT._make(unpack_from(PacketS1, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Picus Logging Control Response... '=BB?c'
    #=============================================================================
    """
    def e8fa90101rsp_decoder(self, packetId, PacketData):
        PacketT = ServerTupleList[packetId.value]
        PacketS1 = "<BB240s"
        retdata = PacketT._make(unpack_from(PacketS1, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Info for File Transfer Listing Request... '=BBB511B'
    #=============================================================================
    """
    def e8f931500rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', 'EntryIndex NumEntries FilenameLength')
        PacketS1 = "<BBB"
        tmpData = PacketT1._make(unpack_from(PacketS1, PacketData, 0))
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '<BBB%ds' % tmpData.FilenameLength
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Info for transfer sent in response to File Transfer Get... '=LLB511B'
    #=============================================================================
    """
    def e8f93150100rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', 'FileId TotalSize FilenameLength')
        PacketS1 = "<LLB"
        tmpData = PacketT1._make(unpack_from(PacketS1, PacketData, 0))
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '<LLB%ds' % tmpData.FilenameLength
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Info for transfer sent in response to File Transfer Put... '=LLB511B'
    #=============================================================================
    """
    def e8f93150200rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', 'FileId TotalSize FilenameLength')
        PacketS1 = "<LLB"
        tmpData = PacketT1._make(unpack_from(PacketS1, PacketData, 0))
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '<LLB%ds' % tmpData.FilenameLength
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Block of file data sent in response to File Transfer Get... '=LLBB511B'
    #=============================================================================
    """
    def e8f93150101rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', ' FileId Offset Size DataBlockLength')
        PacketS1 = "<LLBB"
        tmpData = PacketT1._make(unpack_from(PacketS1, PacketData, 0))
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '<LLBB%ds' % tmpData.Size
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # File Transfer Delete Response... '=BB511B'
    #=============================================================================
    """
    def e8f931503rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', ' StatusCode FilenameLength')
        PacketS1 = "<BB"
        tmpData = PacketT1._make(unpack_from(PacketS1, PacketData, 0))
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '<BB%ds' % tmpData.FilenameLength
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # DGPS Source Tracking Status Response... '=B?S8f85rspChannelDataBlock'
    #=============================================================================
    """
    def e8f85rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', ' NumChannels')
        PacketS1 = "=B"
        data1 = PacketData[:1]
        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        channelDataSize = 30*retdata1.NumChannels
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '=B%ds' % channelDataSize
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Omnistar XP/HP Base Station Response... '=B?S8fa303rspStationInfo'
    #=============================================================================
    """
    def e8fa303rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', ' NumStations')
        PacketS1 = "=B"
        data1 = PacketData[:1]
        retdata1 = PacketT1._make(unpack(PacketS1, data1))
        stationDataSize = 17*retdata1.NumStations
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '=B%ds' % stationDataSize
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Provides RTK Base Info... '=H9sLd?B'
    #=============================================================================
    """
    def e8960rsp_decoder(self, packetId, PacketData):
        # PacketT = ServerTupleList[packetId.value]
        # PacketS = '=H9sLd24s'
        # Note: Since this is fixed width decoder, we replace BaseVector
        #       with East, North, Up for final split out results.
        PacketT1 = namedtuple('PacketT1', ' BaseId BaseName BaseFlags DistToBase East North Up')
        PacketS1 = '=H9sLdddd'
        retdata = PacketT1._make(unpack(PacketS1, PacketData))
        return retdata

    """
    #=============================================================================
    # Satellite Constellation Report... '=BBBHHHB?Sd500rspSatInfo'
    #=============================================================================
    """
    def ed500rsp_decoder(self, packetId, PacketData):
        # ArraySchemaField uses max length (therefore use max length size)
        # This can be fixed by commenting out line 329 (OutBuf.fill) in tsip_schema.py but needs more investigation.
        # Use commented out code if and when max length issue if fixed.
            # packetT = ServerTupleList[packetId.value]
            # PacketT1 = namedtuple('PacketT1', ' AntennaId NumPackets SequenceId TotalNumSats NumSatsUsedInFix ConstellationFlags NumSatsInPacket')
            # PacketS1 = "=BBBHHHB"
            # data1 = PacketData[:10]
            # retdata1 = PacketT1._make(unpack(PacketS1, data1))
            # SatInfoArraySize = 22*retdata1.NumSatsInPacket
            # SatInfoArray = PacketData[10:10+SatInfoArraySize]
            # retdata = packetT(retdata1.AntennaId, retdata1.NumPackets, retdata1.SequenceId, retdata1.TotalNumSats,
            #                 retdata1.NumSatsUsedInFix, retdata1.ConstellationFlags, retdata1.NumSatsInPacket, SatInfoArray)
            # return retdata
        PacketT = ServerTupleList[packetId.value]
        # 220s = 10 max length of Array times # of bytes per report (22)
        PacketS = '=BBBHHHB220s'
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata

    """
    #=============================================================================
    # DGPS priorities. Up to four different DGPS sources can be reported... '=B?'
    #=============================================================================
    """
    def e8f9ersp_decoder(self, packetId, PacketData):
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=B4s'
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata

    """
    #=============================================================================
    # Receiver Unlock Status Response... '=B?S8fa910rspUnlockStatusInfo'
    #=============================================================================
    """
    def e8fa910rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', ' NumUnlockTypes')
        PacketS1 = "=B"
        first_part = PacketData[:1]
        retdata1 = PacketT1._make(unpack(PacketS1, first_part))
        PacketT2 = ServerTupleList[packetId.value]
        PacketS2 = '=B%ds' % (5 * retdata1.NumUnlockTypes)
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Provides capabilities of managed RTK radio (if any)... '=BB?BbB?B'
    #=============================================================================
    """
    def e897002rsp_decoder(self, packetId, PacketData):
        # ArraySchemaField uses max length (therefore use max length size)
        # This can be fixed by commenting out line 329 (OutBuf.fill) in tsip_schema.py but needs more investigation.
        # Use commented out code if and when max length issue if fixed.
            # PacketT1 = namedtuple('PacketT1', ' CapabilityFlags NumModes')
            # PacketS1 = "=BB"
            # first_part = PacketData[:2]
            # retdata1 = PacketT1._make(unpack(PacketS1, first_part))

            # PacketT2 = namedtuple('PacketT1', ' CapabilityFlags NumModes SupportedModes NumSingleFreqHops NumCountries')
            # PacketS2 = '=BB%dsBB' % (retdata1.NumModes)
            # second_part = PacketData[:4+retdata1.NumModes]
            # retdata2 = PacketT2._make(unpack(PacketS2, second_part))

            # PacketT3 = ServerTupleList[packetId.value]
            # PacketS3 = '=BB%dsBB%ds' % (retdata2.NumModes, retdata2.NumCountries)
            # retdata = PacketT3._make(unpack_from(PacketS3, PacketData, 0))
            # return retdata
        PacketT = ServerTupleList[packetId.value]
        PacketS = '=BB64sBB10s'
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata

    """
    #=============================================================================
    # Provides config specific to 450MHz RTK radio (if any)... '=BB?S897005rspChannelInfoB?B'
    #=============================================================================
    """
    def e897005rsp_decoder(self, packetId, PacketData):
        # ArraySchemaField uses max length (therefore use max length size)
        # This can be fixed by commenting out line 329 (OutBuf.fill) in tsip_schema.py but needs more investigation.
        # Use commented out code if and when max length issue if fixed.
            # PacketT1 = namedtuple('PacketT1', ' ChannelId NumChannels')
            # PacketS1 = "=BB"
            # first_part = PacketData[:2]
            # retdata1 = PacketT1._make(unpack(PacketS1, first_part))
            # PacketT2 = ServerTupleList[packetId.value]
            # PacketS2 = '=BB%dsB12s' % (5 * retdata1.NumChannels)
            # retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
            # return retdata
        PacketT = ServerTupleList[packetId.value]
        # 100s = 20 max length of Array times # of bytes per report (5)
        PacketS = '=BB100sB12s'
        retdata = PacketT._make(unpack(PacketS, PacketData))
        return retdata

    """
    #=============================================================================
    # Status of SecureRTK and the 5 rover keys. =BB?B5?S890000rspKeyStatus
    #=============================================================================
    """
    def e890000rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', 'Version NumberOfKeys')
        PacketS1 = "=BB"
        first_part = PacketData[:2]
        retdata1 = PacketT1._make(unpack(PacketS1, first_part))
        PacketT2 = namedtuple('PacketT2', 'Version NumberOfKeys SystemStatus DaysToExpiry IndividualKeysStatus')
        PacketS2 = '=BBBH%ds' % (4 * retdata1.NumberOfKeys)
        retdata = PacketT2._make(unpack_from(PacketS2, PacketData, 0))
        return retdata

    """
    #=============================================================================
    # Diagnostic Data - Diagnostic data output from the receiver
    #=============================================================================
    """
    def e5f01rsp_decoder(self, packetId, PacketData):
        return namedtuple('PacketT1', 'DiagData')._make([PacketData[1:].decode("ascii")])

    def e5f2201rsp_decoder(self, packetId, PacketData):
        PacketT1 = namedtuple('PacketT1', 'Type Time Msg')
        PacketS1 = '=cd%dp'%(len(PacketData)-9)
        retdata = PacketT1._make(unpack(PacketS1, PacketData))
        return retdata

    """
    #=============================================================================
    # Get TAP parameter
    #=============================================================================
    """
    def ebf401400rsp_decoder(self, packetId, PacketData):
        # Unpacking strings only works if the length is exact
        PacketS1 = f'=B{len(PacketData)-1}s'
        retdata = Sbf401400rsp_tup._make(unpack(PacketS1, PacketData))
        return retdata

    """
    #=============================================================================
    # Set TAP parameter
    #=============================================================================
    """
    def ebf401401rsp_decoder(self, packetId, PacketData):
        # Unpacking strings only works if the length is exact
        PacketS1 = f'=B{len(PacketData)-1}s'
        retdata = Sbf401401rsp_tup._make(unpack(PacketS1, PacketData))
        return retdata

    """
    #=============================================================================
    # Get romcfg options
    #=============================================================================
    """
    def ebf400100rsp_decoder(self, packetId, PacketData):
        PacketS1 = f'=16sB{len(PacketData)-17}s'
        retdata = Sbf400100rsp_tup._make(unpack(PacketS1, PacketData))
        return retdata

    """
    #===================================================================================
    # Autopilot file transfer... '=BBHB511B'
    #===================================================================================
    """
    def ebf41rsp_decoder(self, packetId, PacketData):
        PacketS1 = '=BBBHB%ds' % (len(PacketData) - 6)
        retdata = Sbf41rsp_tup._make(unpack(PacketS1, PacketData))
        return retdata

    """
    #=============================================================================
    # SBAS Satellite Control Response
    #=============================================================================
    """
    def e8fa500rsp_decoder(self, packetId, PacketData):
        NumSvs = int(PacketData[0])
        raw_SBASInfoArray = unpack_from('=%dB' % (2 * NumSvs), PacketData, 1)
        SBASInfoArray = tuple(S8fa500rspSBASInfo_tup._make(raw_SBASInfoArray[x:x + 2]) for x in range(0, len(raw_SBASInfoArray), 2))
        raw_ret = (NumSvs,SBASInfoArray)

        return S8fa500rsp_tup._make(raw_ret)

    """
    #=============================================================================
    # Centerpoint RTX Output Settings
    #  - Response containing RTX output settings (RTX output datum control)
    #=============================================================================
    """
    def e8fab05rsp_decoder(self, packetId, PacketData):
        datum = int(PacketData[0])
        offset = S8fab05rspRTXOffset_tup._make(unpack_from(S8fab05rspRTXOffset_bin, PacketData, 1))
        raw_rsp = (datum,offset)
        return S8fab05rsp_tup._make(raw_rsp)

    """
    #=============================================================================
    # Picus Feature Manager Features Rsp
    #  - Response with all the enabled features in the Feature Manager
    #=============================================================================
    """
    def e8fa90a00rsp_decoder(self, packetId, PacketData):
        NumFeatures = int(PacketData[0])
        raw_feature_list = unpack_from(f'={NumFeatures}B', PacketData, 1)
        raw_ret = (NumFeatures,raw_feature_list)

        return S8fa90a00rsp_tup._make(raw_ret)

    """
    #=============================================================================
    # Picus Feature Manager Licenses Rsp
    #  - Response with the status of all installed licenses in the Feature Manager
    #=============================================================================
    """
    def e8fa90a01rsp_decoder(self, packetId, PacketData):
        NumLicenses = int(PacketData[0])

        raw_license_list = unpack_from('=%dB' % (2 * NumLicenses), PacketData, 1)
        license_list = tuple(S8fa90a01rspLicenseStatus_tup._make(raw_license_list[x:x + 2]) for x in range(0, len(raw_license_list), 2))

        raw_ret = (NumLicenses,license_list)

        return S8fa90a01rsp_tup._make(raw_ret)

    """
    #===================================================================================
    # fault report from the Autopilot Navigation Controller... '=HLLLHH3fHH'
    #===================================================================================
    """
    def ebf470502rsp_decoder(self, packetId, PacketData):
        PacketS1 = '=HLLLHH3fHH'
        data = unpack(PacketS1, PacketData)
        data = data[0],data[1],data[2],data[3],data[4],data[5],[data[6], data[7], data[8]],data[9],data[10]
        retdata = Sbf470502rsp_tup._make(data)
        return retdata

    """
    #=============================================================================
    # DBG Log Header
    #=============================================================================
    """
    def ebf470e06rsp_decoder(self, packetId, PacketData):
        size = PacketData[2]
        PacketS1 = f'=BBB{size}s'
        # The decoder is padding PacketData with 0's to make it 170 bytes long so
        # the last packet will fail unless we trim it to the right size.
        retdata = Sbf470e06rsp_tup._make(unpack(PacketS1, PacketData[0:3+size]))
        return retdata

    """
    #=============================================================================
    # DBG Log Data
    #=============================================================================
    """
    def ebf470e07rsp_decoder(self, packetId, PacketData):
        size = PacketData[2]
        PacketS1 = f'=BBB{size}s'
        # The decoder is padding PacketData with 0's to make it 170 bytes long so
        # the last packet will fail unless we trim it to the right size.
        retdata = Sbf470e07rsp_tup._make(unpack(PacketS1, PacketData[0:3+size]))
        return retdata

    """
    #===================================================================================
    # Polaris Full AGC Test Response Decoder
    # - see notes about making this multi-packet if that becomes necessary due to
    #   band expansion on future products
    #===================================================================================
    """
    def e8fa634rsp_decoder(self, packetId, PacketData):
        # This packet has provision for becoming multi-packet if
        # the total number of bands trying to be transmitted will
        # exceed a max packet size. These are the definitions
        # for the multipacket offsets. The unused byetes are stripped
        # from PacketData, so these won't "just work"
        # BandArrayStartOffset = 3
        # BandArrayFieldIndex = 6
        # NumRfBandsOffsetIndex = 2
        # SequenceId = int(PacketData[1])
        # NumRfBands = int(PacketData[2])

        NumRfBandsOffsetIndex = 0
        BandArrayStartOffset = 1
        BandArrayFieldIndex = 5
        # The Band Array GroupField has it's reserved bytes stripped here when trying to
        # decode, so even though the HTML may say that the GroupField is of size 24,
        # the real number is 24 minus the unused/reserved fields that made it a multiple of 8.
        # If you are updating this because one of the reserved bytes got used, make sure you
        # account for the new unused size (e.g. if you consumed 4 bytes for a float, then
        # the new GroupField size is 24 - 1 = 23)
        BandArrayGroupFieldSize = 19

        NumRfBands = int(PacketData[NumRfBandsOffsetIndex])
        raw_PolarisAGCTestBandResults = [S8fa634rspBandResult_tup._make(thing) for thing in iter_unpack('=BBBffff', PacketData[BandArrayStartOffset:BandArrayGroupFieldSize*NumRfBands+BandArrayStartOffset])]

        # The array schema always buffers up the max array length of bytes in PacketData even if that isn't what was sent
        # Here, try to use the ArrayGroup field's mMaxArrayLength to get to the next field and unpack it.
        frequency_offset_offset = BandArrayGroupFieldSize*k8fa634rsp[BandArrayFieldIndex].mMaxArrayLength+BandArrayStartOffset

        # multipacket version:
        # raw_ret = (NumPackets, SequenceId, NumRfBands,raw_PolarisAGCTestBandResults,unpack('=d', PacketData[frequency_offset_offset:frequency_offset_offset+8])[0])

        raw_ret = (NumRfBands, raw_PolarisAGCTestBandResults,unpack('=d', PacketData[frequency_offset_offset:frequency_offset_offset+8])[0])

        return S8fa634rsp_tup._make(raw_ret)

    """
    #===================================================================================
    # "FFT Report" Decoders
    # - See TSIP documentation on these packets for the respective shenanigans
    # - This 8f770 is the "Page Zero" packet, containing metadata and number of
    #   expected points. One could derive the number of following "pages"
    #===================================================================================
    """
    def e8f770rsp_decoder(self, packetId, PacketData):
        PacketS1 = "=ddBBHf"
        PacketT1 = namedtuple('PacketT1', 'Frequency BinSize InputSquared NumIntegrations NumBins MaxLevel')
        FFTReportPage0 = PacketT1._make(unpack(PacketS1, PacketData[0:24]))
        NumSamples = len(PacketData[24:])
        PacketS2 = '=%dB' % NumSamples
        samples = unpack(PacketS2, PacketData[24:])
        # logging.info(f'Page 0 FFT report with {NumSamples}/{FFTReportPage0.NumBins} @ {FFTReportPage0.Frequency}')
        return S8f770rsp_tup._make(FFTReportPage0+(samples,))

    """
    #===================================================================================
    # "FFT Report" Page 1-N decoder
    # - This 8f77 is the "Page N" packet.
    #===================================================================================
    """
    def e8f77rsp_decoder(self, packetId, PacketData):
        PageId = PacketData[0]
        SampleLength = PacketData[1]
        PacketS2 = '=%dB' % SampleLength
        samples = unpack(PacketS2, PacketData[2:])
        # logging.info(f'Page {PageId} FFT report with {SampleLength} samples')
        return S8f77rsp_tup._make((PageId,SampleLength,(samples,)))
    
    """
    #===================================================================================
    # Alternate Unique ID Response
    #===================================================================================
    """
    def e8fa623rsp_decoder(self, packetId, PacketData):

        IdSize = PacketData[0]
        EndPosition = IdSize + 1
        AltUniqueIdField = PacketData[1:EndPosition].hex()

        return S8fa623rsp_tup._make((IdSize,AltUniqueIdField))

    """
    #===================================================================================
    # MAC Address Report
    #===================================================================================
    """
    def e8fa622rsp_decoder(self, packetId, PacketData):
        PacketS = '=BB6sB6sB6sB6s'
        unpackedResult = unpack(PacketS, PacketData)
        # The FixedArray MAC addresses, when decoded, are byte arrays that aren't easily human readable, so they also emit format errors.
        # This line creates the same tuple as S8fa622rsp_tup, but with custom formatting for the MAC addresses to convert them from bytearrays to ":" separated strings.
        tupleResult = unpackedResult[0], unpackedResult[1], unpackedResult[2].hex(":"), unpackedResult[3], unpackedResult[4].hex(":"), unpackedResult[5], unpackedResult[6].hex(":"), unpackedResult[7], unpackedResult[8].hex(":")
        result = S8fa622rsp_tup._make(tupleResult)

        return result

    """
    #===================================================================================
    # Autopilot Field Computer Heartbeat Response
    # Handle firmware sending shorter format than XML expects due to CheckedLengthField change
    #===================================================================================
    """
    def ebf4c0101rsp_decoder(self, packetId, PacketData):
        # Firmware sends variable length but XML expects multiple fields due to CheckedLengthField changes
        packetT = ServerTupleList[packetId.value] 
        packetS = ServerStructList[packetId.value]
        expected_length = calcsize(packetS)
        actual_length = len(PacketData)

        logger.debug(f"[py-tsip] ebf4c0101rsp_decoder: Got {actual_length} bytes, expected {expected_length}, format='{packetS}'")
        
        if actual_length < expected_length:
            # Handle shorter firmware format
            if actual_length == 6:
                # Very old 6-byte format: AutosteerVersion, AutosteerState, APIVersion, SystemState, WarningState, Length
                PacketS1 = '=BBBBBB'
                AutosteerVersion, AutosteerState, APIVersion, SystemState, WarningState, Length = unpack(PacketS1, PacketData)
                # Map to expected 13-field structure with reasonable defaults for missing fields
                retdata = packetT(AutosteerVersion, AutosteerState, APIVersion, SystemState, 
                                 WarningState, 0, 0, 0, 0, 0, 0, 0, Length)
            elif actual_length == 13:
                # Current firmware 13-byte format - just needs 1 more byte, pad with 0
                PacketS1 = '=BBBBBBBBHBBB'  # 13 bytes format (remove last B from expected)
                unpacked = unpack(PacketS1, PacketData)
                # Use factory function to add the missing field
                retdata = packetT._make(unpacked + (0,))  # Add default value for missing field
            else:
                # Unknown short format, return raw data and log details
                logger.info(f"[py-tsip] ebf4c0101rsp_decoder: Unexpected packet length {actual_length}, expected {expected_length}, data={PacketData.hex()}")
                return PacketData
        else:
            # Use standard decoding for full format  
            retdata = packetT._make(unpack(packetS, PacketData))
        return retdata

    """
    #===================================================================================
    # Handle other problematic response packets with CheckedLengthField issues
    #===================================================================================
    """
    def ebf470507rsp_decoder(self, packetId, PacketData):
        # Handle empty or short packets gracefully
        packetT = ServerTupleList[packetId.value]
        if len(PacketData) == 0:
            # Return raw data for empty packets
            return PacketData
        else:
            # Try standard decoding, fallback to raw data if it fails
            try:
                packetS = ServerStructList[packetId.value]
                retdata = packetT._make(unpack(packetS, PacketData))
                return retdata
            except:
                logger.warning("[py-tsip] ebf470507rsp_decoder: Unable to decode packet, returning raw data")
                return PacketData

"""
#=============================================================================
# ClientMessageDecoder
#=============================================================================
"""
class ClientMessageDecoder:

    def DecodeMessage(self, packetId, packetData):
        packetT = ClientTupleList[packetId.value]
        packetS = ClientStructList[packetId.value]

        # Handle both optional CheckedLengthField (?) and variable-length EndTerminatedArrayField (*) markers
        # First resolve variable-length fields
        temp_format, temp_data = _resolve_variable_length_fields_decode(packetS, packetData, packetT)
        # Then resolve optional fields
        resolved_format, add_default_length = _resolve_optional_fields_decode(temp_format, temp_data, packetT)
        
        try:
            unpacked_data = unpack(resolved_format, temp_data)
            if add_default_length:
                # Add default Length=0 for CheckedLengthField compatibility
                unpacked_data = unpacked_data + (0,)
            retdata = packetT._make(unpacked_data)
        except struct_error as e:
            logger.error(f"[py-tsip] Failed to decode packet {packetId} with format '{resolved_format}': {e}")
            retdata = packetData
        return retdata

