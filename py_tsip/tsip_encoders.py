from .tsip_packets import *
import logging
from struct import *


def _has_variable_length_field(packetS, packetData):
    """
    Check if packet has EndTerminatedArrayField (identified by '*' marker).
    
    The XSL transform tsippacketshpy.xsl automatically generates '*' as a 
    placeholder for all EndTerminatedArrayField elements.
    This represents variable-length data that needs dynamic sizing at encode time.
    
    Args:
        packetS (str): Struct format string (e.g., '=BBHB*')
        packetData: Packet data with _fields attribute
        
    Returns:
        bool: True if packet contains EndTerminatedArrayField needing dynamic sizing
    """
    return '*' in packetS and hasattr(packetData, '_fields')

def _resolve_variable_length_fields(packetS, packetData):
    """
    Resolve EndTerminatedArrayField markers ('*') in struct format string.
    
    The '*' character indicates a variable-length field (EndTerminatedArrayField) 
    that needs to be replaced with the actual length of the data at encode time.
    
    Args:
        packetS (str): Struct format string potentially containing '*' markers
        packetData: Packet data namedtuple
        
    Returns:
        tuple: (resolved_format_string, resolved_data_tuple)
    """
    if '*' not in packetS:
        return packetS, tuple(packetData)
    
    if not hasattr(packetData, '_fields'):
        # Fallback: can't resolve without field info
        return packetS, tuple(packetData)
    
    # Find the variable-length field (should be bytes/str/bytearray type)
    for field_name in packetData._fields:
        field_value = getattr(packetData, field_name)
        if isinstance(field_value, (bytes, str, bytearray)):
            actual_length = len(field_value)
            
            # Check if there's an explicit length field (like PacketDataLength)
            length_field_name = field_name + 'Length'
            if hasattr(packetData, length_field_name):
                explicit_length = getattr(packetData, length_field_name)
                # Use the explicit length instead of calculating from data
                actual_length = explicit_length
            
            # Replace '*' with actual data length
            resolved_format = packetS.replace('*', f'{actual_length}s', 1)
            
            # Prepare resolved data, converting strings to bytes if needed
            resolved_data = []
            for field in packetData._fields:
                field_val = getattr(packetData, field)
                if field == field_name:
                    if isinstance(field_val, str):
                        # Convert string to bytes for struct packing
                        field_val = field_val.encode('utf-8')
                    elif isinstance(field_val, bytearray):
                        # Convert bytearray to bytes for struct packing
                        field_val = bytes(field_val)
                resolved_data.append(field_val)
            
            return resolved_format, tuple(resolved_data)
    
    # No variable field found - fallback
    return packetS, tuple(packetData)

def _resolve_optional_fields(packetS, packetData):
    """
    Resolve optional CheckedLengthField markers ('?') in struct format string.
    
    The '?' character indicates an optional CheckedLengthField that may or may not 
    be present in the packet data structure. This handles legacy compatibility where
    some packets have CheckedLengthField as metadata only, while others include it
    as an actual data field.
    
    Args:
        packetS (str): Struct format string potentially containing '?' markers
        packetData: Packet data namedtuple
        
    Returns:
        tuple: (resolved_format_string, data_tuple_to_pack)
    """
    if '?' not in packetS:
        return packetS, tuple(packetData)
    
    if not hasattr(packetData, '_fields'):
        # Fallback: assume no optional fields
        return packetS.replace('?', ''), tuple(packetData)
    
    # Check if the data structure has a 'Length' field (CheckedLengthField)
    has_length_field = 'Length' in packetData._fields
    
    if has_length_field:
        # Include the optional field - replace '?' with 'B'
        resolved_format = packetS.replace('?', 'B')
        return resolved_format, tuple(packetData)
    else:
        # Skip the optional field - remove '?'
        resolved_format = packetS.replace('?', '')
        # Remove the Length field from data if it exists (shouldn't, but safety)
        data_tuple = tuple(getattr(packetData, field) for field in packetData._fields if field != 'Length')
        return resolved_format, data_tuple


def _dynamic_pack(packetS, packetData):
    """
    Handle variable-length EndTerminatedArrayField encoding and optional CheckedLengthField.
    
    This function handles two special cases:
    1. EndTerminatedArrayField elements: '*' placeholders get replaced with actual length
    2. Optional CheckedLengthField: '?' markers get resolved based on data structure
    
    Example:
        XML: <EndTerminatedArrayField name="PacketData">
        Generated format: '=B*'  
        Actual data: PacketData="hello"
        Dynamic format: '=B5s'
        
        XML: <CheckedLengthField/>
        Generated format: '=BB?'
        With Length field: '=BBB' 
        Without Length field: '=BB'
        
    Args:
        packetS (str): Struct format string with special markers
        packetData: Packet data namedtuple
        
    Returns:
        bytes: Packed binary data with resolved format
    """
    # logging.debug(f"_dynamic_pack called with format='{packetS}', data={packetData}")
    
    # First resolve optional fields (CheckedLengthField markers)
    resolved_format, resolved_data = _resolve_optional_fields(packetS, packetData)
    
    # Then resolve variable length fields (EndTerminatedArrayField markers)
    if '*' in resolved_format:
        final_format, final_data = _resolve_variable_length_fields(resolved_format, packetData)
    else:
        final_format, final_data = resolved_format, resolved_data
    
    # Pack with the fully resolved format
    return pack(final_format, *final_data)


"""
#=============================================================================
# TsipMessageEncoder
#=============================================================================
"""
class TsipMessageEncoder:

    def EncodeMessage(self, packetId, packetData):
        if isinstance(packetId, EServerPackets):
            structArray = ServerStructList
            packetArray = EServerPackets
        elif isinstance(packetId, EClientPackets):
            structArray = ClientStructList
            packetArray = EClientPackets
        else:
            return None

        packstring = structArray[packetId.value]
        encoder = None
        # Look for an array in the structure file

        packetName = packetArray(packetId).name
        encoderName = packetName + "_encoder"
        try:
            encoder = getattr(self, encoderName)
        except:
            senddata = None

        if encoder != None:
            try:
                senddata = encoder(packetId, packetData)
            except Exception as e:
                logging.error(e)
                logging.error("the custom encoding for %s failed" % (packetId))
                senddata = None
        else:
            # Allow ? and * characters for CheckedLengthField and EndTerminatedArrayField markers
            special_chars = set(packstring) - set('=<>!@#$%^&()bBhHiIlLqQfdcs0123456789?*')
            if not special_chars:
                try:
                    senddata = _dynamic_pack(packstring, packetData)
                except:
                    logging.error("unable to pack packet %s", packetId)
                    senddata = None
            else:
                logging.error("%s needs special encoding that does not currently exist" % (packetId))


        return senddata

    """
    #=============================================================================
    # e8ea801cmd
    #=============================================================================
    """
    def e8ea801cmd_encoder(self, packetId, packetData):
        PacketS = '=HB60sB60sB60sB60s'
        sendData = pack(PacketS, *packetData)
        return sendData

    """
    #=============================================================================
    # File Transfer Listing Request... '=B511B'
    #=============================================================================
    """
    # def e8e931500req_encoder(self, packetId, packetData):
    #     (pathLength, path) = packetData
    #     PacketS1 = '=B%ds' % packetData.PathLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #=============================================================================
    # Requests that file be opened for reading. File Transfer Get... '=B511B'
    #=============================================================================
    """
    # def e8e93150101req_encoder(self, packetId, packetData):
    #     (fileNameLength, fileName) = packetData
    #     PacketS1 = '=B%ds' % packetData.FilenameLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #=============================================================================
    # Requests that file be opened for writing. File Transfer Put... '=B511B'
    #=============================================================================
    """
    # def e8e93150201req_encoder(self, packetId, packetData):
    #     (fileNameLength, fileName) = packetData
    #     PacketS1 = '=B%ds' % packetData.FilenameLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #===================================================================================
    # Requests to write block of data to open file. File Transfer Put... '=LLBB511B'
    #===================================================================================
    """
    # def e8e93150202req_encoder(self, packetId, packetData):
    #     (FileId, Offset, Size, DataBlockLength, DataBlock) = packetData
    #     PacketS1 = '=LLBB%ds' % packetData.DataBlockLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #===================================================================================
    # Requests that the receiver install licenses with a given file... '=B?c'
    #===================================================================================
    """
    def e8ea90105cmd_encoder(self, packetId, packetData):
        PacketS1 = '=B250s'
        sendData = pack(PacketS1, *packetData)
        return sendData

    """
    #===================================================================================
    # Remove Licenses By Fragment command... '=B?c'
    #===================================================================================
    """
    def e8ea91605cmd_encoder(self, packetId, packetData):
        PacketS1 = '=B200s'
        sendData = pack(PacketS1, *packetData)
        return sendData

    """
    #===================================================================================
    # File Transfer Delete Request... '=B511B'
    #===================================================================================
    """
    # def e8e931503req_encoder(self, packetId, packetData):
    #     PacketS1 = '=B%ds' % packetData.FilenameLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #===================================================================================
    # DGPS Priority Command... '=B?'
    #===================================================================================
    """
    def e8e9ecmd_encoder(self, packetId, packetData):
        PacketS1 = '=B4s'
        sendData = pack(PacketS1, *packetData)
        return sendData

    """
    #===================================================================================
    # Picus Logging Control Command... '=BB?c'
    #===================================================================================
    """
    def e8ea90101cmd_encoder(self, packetId, packetData):
        PacketS1 = '=BB240s'
        sendData = pack(PacketS1, *packetData)
        return sendData

    """
    #===================================================================================
    # Picus Upgrade Command... '=BB?c'
    #===================================================================================
    """
    def e8ea90100cmd_encoder(self, packetId, packetData):
        PacketS1 = '=BB%ds' % packetData.FilenameLen
        sendData = pack(PacketS1, *packetData)
        return sendData

    """
    #===================================================================================
    # Get Autopilot tap value... '=B511B'
    #===================================================================================
    """
    # def ebe401400cmd_encoder(self, packetId, packetData):
    #     # Must specify the exact number of bytes to pack().
    #     # Handle new tuple format with Length field - only pack TAPStringLength and TAPString
    #     PacketS1 = '=B%ds' % packetData.TAPStringLength
    #     sendData = pack(PacketS1, packetData.TAPStringLength, packetData.TAPString)
    #     return sendData

    """
    #===================================================================================
    # Set Autopilot tap value... '=B511B'
    #===================================================================================
    """
    # def ebe401401cmd_encoder(self, packetId, packetData):
    #     # Must specify the exact number of bytes to pack().
    #     # Handle new tuple format with Length field - only pack TAPStringLength and TAPString
    #     PacketS1 = '=B%ds' % packetData.TAPStringLength
    #     sendData = pack(PacketS1, packetData.TAPStringLength, packetData.TAPString)
    #     return sendData

    """
    #===================================================================================
    # Autopilot file transfer... '=BBHB511B'
    #===================================================================================
    """
    # def ebe41cmd_encoder(self, packetId, packetData):
    #     # Must specify the exact number of bytes to pack().
    #     # This packet has structure: FileId, CmdId, PacketNumber, PacketDataLength, PacketData
    #     # Note: no 'status' field in client packets, unlike server response packets
    #     PacketS1 = '=BBHB%dsB' % packetData.PacketDataLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #=============================================================================
    # SBAS Satellite Control Response
    #=============================================================================
    """
    def e8ea500cmd_encoder(self, packetId, packetData):
        # Start the array with the number of svs
        sendData = pack('=B',packetData.NumSvs)

        for sbasInfo in packetData.SBASInfoArray:
            sendData += pack(S8ea500cmdSBASInfo_bin, *sbasInfo)

        return sendData

    """
    #===================================================================================
    # Centerpoint RTX Output Settings Command (datum or custom offset)
    #===================================================================================
    """
    def e8eab05cmd_encoder(self, packetId, packetData):
        PacketS1 = '=BBfff51x'
        sendData = pack(PacketS1,
                        packetData.RTXOutputDatum,
                        packetData.RTXOffset.enabled,
                        packetData.RTXOffset.east,
                        packetData.RTXOffset.north,
                        packetData.RTXOffset.up
                        )
        return sendData

    """
    #===================================================================================
    # Autopilot file transfer... '=BBHB511B'
    #===================================================================================
    """
    # def ebe4c011711cmd_encoder(self, packetId, packetData):
    #     # Must specify the exact number of bytes to pack().
    #     PacketS1 = '=hHHHBBBBBBBB%ds' % packetData.PacketDataLength
    #     sendData = pack(PacketS1, *packetData)
    #     return sendData

    """
    #===================================================================================
    # [Manufacturing Test] Enable Continuous TX Test Command (was) '=BLBHLBBB6?B6?BB'
    #===================================================================================
    """
    def e8ea644cmd_encoder(self, packetId, packetData):
        PacketS1 = '=BLBHLBBB6s6sB'
        src_as_bytearray=bytearray.fromhex(packetData.SourceMAC.replace(':',''))
        dst_as_bytearray=bytearray.fromhex(packetData.DestMAC.replace(':',''))
        sendData = pack(PacketS1,
                        packetData.ProductId,
                        packetData.Delay,
                        packetData.Rate,
                        packetData.Size,
                        packetData.Mode,
                        packetData.GuardInterval,
                        packetData.Options1,
                        packetData.Options2,
                        src_as_bytearray,
                        dst_as_bytearray,
                        packetData.ChannelWidth
                        )
        return sendData

    """
    #===================================================================================
    # [Manufacturing Test] Start RX Statistics Command (was) '=B6?B6?B'
    #===================================================================================
    """
    def e8ea646cmd_encoder(self, packetId, packetData):
        PacketS1 = '=B6s6s'
        src_as_bytearray=bytearray.fromhex(packetData.SourceMAC.replace(':',''))
        dst_as_bytearray=bytearray.fromhex(packetData.DestMAC.replace(':',''))
        sendData = pack(PacketS1,
                        packetData.ProductId,
                        src_as_bytearray,
                        dst_as_bytearray
                        )
        return sendData