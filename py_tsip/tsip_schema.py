#===============================================================================
# @file tsipschema.py
# This file contains the implementation of the TSIP encoding/decoding functionality
#
# NOTE TO DEVELOPERS: If you need to use the packet dump diagnostics, you must
#                     set the log level to "9". This is one below the standard
#                     DEBUG level to prevent spamming the logging of modules that
#                     consume this facility.
#===============================================================================

from enum import Enum
import sys
import logging
from struct import *
from .data_schema import *
from .data_buffer import *

# Module-level logger
logger = logging.getLogger("py_tsip")
logger.setLevel(logging.WARNING)

kDLE = 0x10  # < DLE value
kETX = 0x03  # < ETX value

TSIP_ENDIAN = SCHEMA_BIG_ENDIAN
TSIPSCHEMA_MAX_PACKET_SIZE = 512

TSIP_DECODER_NEED_MORE_DATA = 1
TSIP_DECODER_PACKET_AVAILABLE = 0
TSIP_DECODER_EXPECTED_DLE = -1
TSIP_DECODER_UNKNOWN_PACKET = -2
TSIP_DECODER_BUFFER_ERROR = -3
TSIP_DECODER_NO_SCHEMA = -4
TSIP_DECODER_UNEXPECTED_PACKET_SIZE = -5
TSIP_DECODER_PACKET_ERROR = -6


class ETSIPFieldType(Enum):
    kFirstTSIPFieldType = 11
    eId =                 kFirstTSIPFieldType + 1  # An Id field (8 bit)
    eSubId =              kFirstTSIPFieldType + 2  # A sub Id field (8 bit)
    eFixedArray =         kFirstTSIPFieldType + 3  # A fixed array of items
    eString =             kFirstTSIPFieldType + 4  # A string of characters (fixed-length)
    eArray =              kFirstTSIPFieldType + 5  # An array of items
    eEndTerminatedArray = kFirstTSIPFieldType + 6  # An array of items terminated by the end of data
    eUnused =             kFirstTSIPFieldType + 7  # Spare bytes filled with a ant value
    eChecksum =           kFirstTSIPFieldType + 8  # A 16 bit checksum field (sumanusmed bytes)
    eCheckedLength =      kFirstTSIPFieldType + 9  # An end array with length checking
    kLastTSIPFieldType =  kFirstTSIPFieldType + 10  # The number of field types


class EState(Enum):
    eStateComplete = 0
    eStateCollectDataResetError = 1
    eStateCollectData = 2
    eStateCollectDLE = 3


class TSIPOutBuffer(OutBuffer):
    def __init__(self):
        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        self.mData = bytearray(tmplist)
        super().__init__(self.mData, TSIPSCHEMA_MAX_PACKET_SIZE)


"""
#=============================================================================
# IdSchemaField
#=============================================================================
"""
class IdSchemaField(SchemaField):
    def __init__(self, Id, Name=None, Description=None):
        super().__init__(ETSIPFieldType.eId, Name, Description)
        self.mId = Id

    def GetId(self):
        return self.mId

    def GetAsInteger(self, Data, Index):
        return self.mId

    def GetAsFloat(self, Data, Index):
        return self.mId

    def GetAsString(self, Data, String, Length):
        return "0x%02X" % self.mId

    def GetSize(self, Type, DecodedSize):
        if DecodedSize == True:
            return 0
        else:
            return 1

    def HasValue(self):
        return True

    def GetValue(self):
        return self.mId

    def Decode(self, Parent, InBuf, OutBuf, endian):
        id = [0x00, 0x00]
        InBuf.read_to_array(id, 1)
        return (id[0] == self.mId)

    def Encode(self, Parent, InBuf, OutBuf, endian):
        return OutBuf.write_1(self.mId)

"""
#=============================================================================
# SubIdSchemaField
#=============================================================================
"""
class SubIdSchemaField(SchemaField):
    def __init__(self, SubId, Name=None, Description=None):
        super().__init__(ETSIPFieldType.eSubId, Name, Description)
        self.mSubId = SubId

    def GetSubId(self):
        return self.mSubId

    def GetAsInteger(self, Data, Index):
        return self.mSubId

    def GetAsFloat(self, Data, Index):
        return self.mSubId

    def GetAsString(self, Data, Index, String, Length):
        return "0x%02X" % self.mSubId

    def GetSize(self, Type, DecodedSize):
        if DecodedSize == True:
            return 0
        else:
            return 1

    def HasValue(self):
        return True

    def GetValue(self):
        self.mSubId

    def Decode(self, Parent, InBuf, OutBuf, endian):
        id = [0x00, 0x00]
        InBuf.read_to_array(id, 1)
        return (id[0] == self.mSubId)

    def Encode(self, Parent, InBuf, OutBuf, endian):
        return OutBuf.write_1(self.mSubId)

"""
#=============================================================================
# FixedArraySchemaField
#=============================================================================
"""
class FixedArraySchemaField(SchemaField):
    def __init__(self, Item, ArrayLength, Name=None, Description=None):
        super().__init__(ETSIPFieldType.eFixedArray, Name, Description)
        self.mprItem = Item
        self.mArrayLength = ArrayLength

    def GetArrayLength(self):
        return self.mArrayLength

    def GetAsInteger(self, Data, Index):
        return -1

    def GetAsFloat(self, Data, Index):
        return -1.0

    def GetAsString(self, Data, Index, String, Length):
        if Length > 0:
            String[0] = 0
        return String

    def GetSize(self, Type, DecodedSize):
        return self.mArrayLength * self.mprItem.GetSize(Type, DecodedSize)

    def GetNumFields(self, Parent):
        return self.mArrayLength

    def GetField(self, Index):
        if Index < self.mArrayLength:
            return self.mprItem
        else:
            return 0

    def SetValue(self, data):
        self.Value = data
        self.hasValue = True

    def Decode(self, Parent, InBuf, OutBuf, endian):
        #  Get the array length, and make sure it's valid
        arrayField = SchemaDataField(self, OutBuf.used(), 0)
        for i in range(self.mArrayLength):
            if self.mprItem.Decode(arrayField, InBuf, OutBuf, endian) == False:
                return False
            arrayField.moveEnd(self.mprItem.GetActualSize())
        self.SetValue(arrayField.get_data())
        return True

    def Encode(self, Parent, InBuf, OutBuf, endian):
        #  Get the array length, and make sure it's valid
        arrayField = SchemaDataField(self, OutBuf.used(), 0)
        for i in range(self.mArrayLength):
            if self.mprItem.Encode(arrayField, InBuf, OutBuf, endian) == False:
                return False
            arrayField.moveEnd(self.mprItem.GetActualSize())
        self.SetValue(arrayField.get_data())
        return True

"""
#=============================================================================
# StringSchemaField
#=============================================================================
"""
kStringCHARSchemaField = CHARSchemaField()


class StringSchemaField(FixedArraySchemaField):
    def __init__(self, MaxLength, Name=None, Description=None):
        super().__init__(kStringCHARSchemaField, MaxLength, Name, Description)
        self.mType = ETSIPFieldType.eString

    def GetAsString(self, Data, String, Length):
        if Length - 1 > self.mArrayLength:
            len = Length - 1
        else:
            len = self.mArrayLength
        String = Data[0:len]
        return String

"""
#=============================================================================
# ArraySchemaField
#=============================================================================
"""
class ArraySchemaField(SchemaField):
    def __init__(self, Item, LengthIndex, LengthMask, LengthShift, MaxLength, Name=None, Description=None):
        super().__init__(ETSIPFieldType.eArray, Name, Description)
        self.mprItem = Item
        self.mArrayLengthIndex = LengthIndex
        self.mArrayLengthMask = LengthMask
        self.mArrayLengthShift = LengthShift
        self.mMaxArrayLength = MaxLength
        self.mArrayActualLength = 0
        self.mArrayLengthSet = False

    def GetArrayLengthIndex(self):
        return self.mArrayLengthIndex

    def GetArrayLengthMask(self):
        return self.mArrayLengthMask

    def GetArrayLengthShift(self):
        return self.mArrayLengthShift

    def GetMaxArrayLength(self):
        return self.mMaxArrayLength

    def GetArrayLength(self):
        return self.mArrayActualLength

    def SetArrayLength(self, length):
        self.mArrayActualLength = length
        self.mArrayLengthSet = True

    def GetAsInteger(self, Data):
        return -1

    def GetAsFloat(self, Data):
        return -1.0

    def GetAsString(self, Data, String, Length):
        if Length > 0:
            String = None
        return String

    def SetValue(self, data):
        self.Value = data
        self.hasValue = True

    def Clear(self):
        self.Value = None
        self.hasValue = False
        self.mArrayActualLength = 0
        self.mArrayLengthSet = False

    def GetSize(self, Type, DecodedSize):
        if DecodedSize or Type == ESizeType.eMaxSize:
            return self.mMaxArrayLength * self.mprItem.GetSize(Type, DecodedSize)
        elif Type == ESizeType.eMinSize:
            return 0
        # See if we decoded this already and kept the size
        elif DecodedSize == False and Type == ESizeType.eActualSize and self.mArrayLengthSet:
            return self.mArrayActualLength
        #  It is non-trivial to work out the encoded actual-size.
        return -1

    def GetNumFields(self, DataField):
        if DataField == None or DataField.GetParent() == None:
            # Fib a bit
            return self.mMaxArrayLength
        # Get the array size field, and determine the number of items in the array.
        numFields = DataField.GetParent().GetField(
            self.GetArrayLengthIndex()).GetAsInteger()
        if self.GetArrayLengthMask() != 0:
            numFields = (numFields & self.GetArrayLengthMask()
                         ) >> self.GetArrayLengthShift()
        return numFields

    def GetField(self, Index):
        if Index < self.mMaxArrayLength:
            return self.mprItem
        else:
            return 0

    def Decode(self, Parent, InBuf, OutBuf, endian):
        indexField = Parent.GetField(self.mArrayLengthIndex, False)
        if indexField == None or indexField.GetSchema() == 0:
            return False
        arrayLength = indexField.GetAsInteger()
        if self.mArrayLengthMask != 0:
            arrayLength &= (0x000003FF & self.mArrayLengthMask)
            arrayLength >>= self.mArrayLengthShift
        if arrayLength > self.mMaxArrayLength:
            return False
        self.SetArrayLength(arrayLength)
        itemSize = self.mprItem.GetActualSize()
        if itemSize < 0:
            return False
        #  Get the array length, and make sure it's valid
        arrayField = SchemaDataField(self, OutBuf.used(), 0)
        for i in range(arrayLength):
            if self.mprItem.Decode(arrayField, InBuf, OutBuf, endian) == False:
                return False
            arrayField.moveEnd(self.mprItem.GetActualSize())
        self.SetValue(arrayField.get_data())
        if OutBuf.fill(0, (self.mMaxArrayLength - arrayLength) * itemSize) == False:
            return False
        return True

    def Encode(self, Parent, InBuf, OutBuf, endian):
        indexField = Parent.GetField(self.mArrayLengthIndex, True)
        if indexField == None or indexField.GetSchema() == None:
            return False
        arrayLength = indexField.GetAsInteger()
        if self.mArrayLengthMask != 0:
            arrayLength &= (0x000003FF & self.mArrayLengthMask)
            arrayLength >>= self.mArrayLengthShift
        if arrayLength > self.mMaxArrayLength:
            return False
        itemSize = self.mprItem.GetActualSize()
        if itemSize < 0:
            return False
        #  Get the array length, and make sure it's valid
        arrayField = SchemaDataField(self, InBuf.remaining(), 0)
        for i in range(arrayLength):
            if self.mprItem.Encode(arrayField, InBuf, OutBuf, endian) == False:
                return False
            arrayField.moveEnd(itemSize)
        self.SetValue(arrayField.get_data())

        # If there is nothing left to encode, assume that encoding is complete.
        if InBuf.remainingLength() == 0:
            return True

        # This step assumes that you have always filled out the whole array up to maxLength items.
        # This is a super subtle result since many packets using the ArraySchemaField do not
        # actually expect this behavior.
        if InBuf.skip((self.mMaxArrayLength - arrayLength) * itemSize) == False:
            return False

        return True

"""
#=============================================================================
# EndTerminatedArraySchemaField
#=============================================================================
"""
class EndTerminatedArraySchemaField(SchemaField):
    def __init__(self, Item, Name=None, Description=None):
        super().__init__(ETSIPFieldType.eEndTerminatedArray, Name, Description)
        self.mprItem = Item
        self.mprSizeField = sys.getsizeof(Item)

    def GetAsInteger(self, Data):
        return -1

    def GetAsFloat(self, Data):
        return -1.0

    def GetAsString(self, Data, String, Length):
        if Length > 0:
            String[0] = 0
        return String

    def GetSize(self, Type, DecodedSize):
        if DecodedSize or (Type == ESizeType.eMaxSize):
            return TSIPSCHEMA_MAX_PACKET_SIZE
        elif Type == ESizeType.eMinSize:
            return 0
        #  It is non-trivial to work out the encoded actual-size.
        return -1

    def GetNumFields(self, DataField):
        if DataField == None:
            # Fib a bit
            return 511
        # The first piece of data is the length of the array.
        return DataField.data()[0]

    def GetField(self, Index):
        return self.mprItem

    def SetValue(self, data):
        self.Value = data
        self.hasValue = True

    def Decode(self, Parent, InBuf, OutBuf, endian):
        length = InBuf.remainingLength()
        parentSchema = Parent.GetSchema()
        childSchema = 0
        i = parentSchema.GetNumFields() - 1
        childSchema = parentSchema.GetField(i)
        while i >= 0 and childSchema != self:
            length = length - childSchema.GetActualSize(False)
            i = i - 1
            childSchema = parentSchema.GetField(i)
        if length > TSIPSCHEMA_MAX_PACKET_SIZE or length < 0:
            return False
        actualSize = self.mprItem.GetActualSize()
        if length % actualSize != 0:
            return False
        lengthValue = int(length / actualSize)
        if lengthValue > 255:
            lengthValue = 255
        if OutBuf.write_1(lengthValue) == False:
            return False
        etaField = SchemaDataField(self, OutBuf.used(), 0)
        for i in range(lengthValue):
            if self.mprItem.Decode(etaField, InBuf, OutBuf, endian) == False:
                return False
            etaField.moveEnd(self.mprItem.GetActualSize())
        # The end-terminated array stores size data, which should not be counted as
        # the first data byte.
        self.SetValue(OutBuf.used()[1:])
        return True

    def Encode(self, Parent, InBuf, OutBuf, endian):
        data = InBuf.read_all()
        length = int(data[0])
        if length <= 0:
            return False
        InBuf.skip(1)
        itemSize = self.mprItem.GetActualSize()
        if itemSize < 0:
            return False
        etaField = SchemaDataField(self, InBuf.remaining(), 0)
        for i in range(length):
            if self.mprItem.Encode(etaField, InBuf, OutBuf, endian) == False:
                return False
            etaField.moveEnd(itemSize)
        self.SetValue(InBuf.used())
        return True

"""
#=============================================================================
# UnusedSchemaField
#=============================================================================
"""
class UnusedSchemaField(SchemaField):
    def __init__(self, Size):
        super().__init__(ETSIPFieldType.eUnused)
        self.mLength = Size

    def GetLength(self):
        return self.mLength

    def GetAsInteger(self, Data):
        return -1

    def GetAsFloat(self, Data):
        return -1

    def GetAsString(self, Data, String, Length):
        String[0] = '0'
        return None

    def GetSize(self, Type, DecodedSize):
        if DecodedSize:
            return 0
        else:
            return self.mLength

    def Decode(self, Parent, InBuf, OutBuf, endian):
        return InBuf.skip(self.mLength)

    def Encode(self, Parent, InBuf, OutBuf, endian):
        return OutBuf.fill(0, self.mLength)


"""
#=============================================================================
# ChecksumSchemaField
#=============================================================================
"""
class ChecksumSchemaField(SchemaField):
    def __init__(self):
        super().__init__(ETSIPFieldType.eChecksum)

    def GetAsInteger(self, Data):
        return Data

    def GetAsFloat(self, Data):
        return Data

    def GetAsString(self, Data, String, Length):
        return "0x%04X" % Data

    def GetSize(self, Type, DecodedSize):
        if DecodedSize:
            return 0
        else:
            return 2

    def Decode(self, Parent, InBuf, OutBuf, endian):
        oldcsa = bytearray(b'\x00\x00')
        csdata = InBuf.used()
        cslength = InBuf.usedLength()
        # Special case packet 45 - this packet is messed up - checksum is bizzar magic of partial packet#
        if csdata[0] == 0x45 and cslength == 95:
            return True
      
        chksum = self.CalcChecksum(csdata, cslength)
        if InBuf.read_to_array(oldcsa, 2):
            if endian != SCHEMA_MACHINE_ENDIAN:
                self.swapBytes(oldcsa, 2)
        else:
            return False
        oldcs = unpack("=H", oldcsa)
        if oldcs[0] == chksum:
            return True
        else:
            logger.error("[py-tsip] Checksum failed for packet %02x", csdata[0])
            return False

    def Encode(self, Parent, InBuf, OutBuf, endian):
        chksum = self.CalcChecksum(OutBuf.used(), OutBuf.usedLength())
        chksa = bytearray(pack("=H", chksum))
        if (endian != SCHEMA_MACHINE_ENDIAN):
            self.swapBytes(chksa, 2)
        return (OutBuf.write_data(chksa, 2))

    def CalcChecksum(self, Data, Length):
        cs = 0
        # always skip the first byte (ID is not included in checksum)
        for i in range(1, Length):
            cs += Data[i]
        return cs
"""
//=============================================================================
// CheckedLengthSchemaField
//=============================================================================
"""
class CheckedLengthSchemaField(SchemaField):
    def __init__(self, Name=None, Description=None):
        super().__init__(ETSIPFieldType.eCheckedLength, Name, Description)

    def GetAsUnsignedInteger(self, Data):
        value = unpack_from(">B", Data, 0)
        return value[0]

    def GetAsInteger(self, Data):
        value = unpack_from(">B", Data, 0)
        return value[0]

    def GetAsFloat(self, Data):
        self.GetAsInteger(Data)

    def GetAsString(self, Data, String, Length):
        value = self.GetAsInteger(Data)
        return "%d" % value

    def GetSize(self, Type, DecodedSize):
        return 1

    def SetValue(self, data):
        self.Value = data
        self.hasValue = True

    def Decode(self, Parent, InBuf, OutBuf, endian):
        # read_all doesn't move the buffer forward so we skip at the end of this function
        Data = InBuf.read_all()
        CalculatedLength = InBuf.usedLength() - 1
        DecodedLength = self.GetAsUnsignedInteger(Data) # Let us be nice, and treat decoded length as unsigned
        logger.log(9, "[py-tsip] checked length decode: calc = %d, decode = %d" % (CalculatedLength, DecodedLength))
        # Move ahead so the checksum includes the string length.
        # **MUST do this after saving CalculatedLength.**
        InBuf.skip(1)
        return (CalculatedLength == DecodedLength)

    def Encode(self, Parent, InBuf, OutBuf, endian):
        length = OutBuf.usedLength() - 1
        result = (OutBuf.write_1(length))
        logger.log(9, "[py-tsip] checked length encode: len = %d" % length)
        return result

"""
NOTE C code from .cpp file

  def Decode(const CSchemaConstDataField* /*Parent*/,
                                    CInBuffer& In, COutBuffer& /*Out*/,
                                    unsigned short /*endian*/) const
    U8 decodedLength;
    U8 calculatedLength = In.usedLength()-1;
    return (In.get((unsigned char*)&decodedLength, 1) && (decodedLength == calculatedLength));

  def Encode(const CSchemaConstDataField* /*Parent*/,
                                    CInBuffer& /*In*/, COutBuffer& Out,
                                    unsigned short /*endian*/) const
    U8 length = Out.usedLength()-1;
    return (Out.put((unsigned char*)&length, 1));
"""

"""
#=============================================================================
# TSIPSchemaEntry
#=============================================================================
"""
class TSIPSchemaEntry(SchemaEntry):
    def __init__(self, Type, Fields=None, NumFields=0, IdName=None, Name=None, Description=None):
        super().__init__(Type, Fields, NumFields, IdName, Name, Description)
        self.m_numIds = 0
        for i in range(NumFields):
            fieldType = self.mprFields[i].GetType()
            if fieldType == ETSIPFieldType.eId or fieldType == ETSIPFieldType.eSubId:
                self.m_numIds += 1
            else:
                break

    def GetNumIds(self):
        return self.m_numIds

"""
#=============================================================================
# PacketData
#=============================================================================
"""
class PacketData(SchemaDataField):
    def __init__(self, entry, Data, Length, endian):
        super().__init__(entry, Data, Length)
        self.m_endian = endian

    def GetEntryType(self):
        if self.mprSchema:
            return self.GetSchema().GetEntryType()
        else:
            return -1

    def SetSchema(self, entry):
        self.mprSchema = entry

    def GetSchema(self):
        return self.mprSchema

"""
#=============================================================================
# PacketEncoder
#=============================================================================
"""
class PacketEncoder(PacketData):
    def __init__(self, framer, entry, Data, Length, endian):
        super().__init__(entry, Data, Length, endian)
        tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
        self.m_outData = bytearray(tmplist)
        self.m_outbuf = OutBuffer(self.m_outData, TSIPSCHEMA_MAX_PACKET_SIZE)
        self.m_framer = framer

    def setFramer(self, framer):
        self.m_framer = framer

    def Encode(self, InBuf, OutBuf):
        if self.m_framer == None:
            return False
        if self.GetSchema() == None:
            return False
        self.m_outbuf.reset()
        if self.GetSchema().Encode(None, InBuf, self.m_outbuf, self.m_endian) == False:
            return False
        tmpBuf = InBuffer(self.m_outbuf.used(), self.m_outbuf.usedLength())
        return self.m_framer.frame(tmpBuf, OutBuf)

"""
#=============================================================================
# TSIPFramer
#=============================================================================
"""
class TSIPFramer():
    def frame(self, inBuffer, outBuffer):
        if outBuffer.write_1(kDLE) == False:
            return False
        b = bytearray([0] * 2)
        while inBuffer.read_to_array(b, 1):
            if outBuffer.write_1(b[0]) == False:
                return False
            if (b[0] == kDLE) and outBuffer.write_1(b[0]) == False:
                return False
        if outBuffer.write_1(kDLE) == False or outBuffer.write_1(kETX) == False:
            return False
        return True

"""
#=============================================================================
# TSIPDeframer
#=============================================================================
"""
class TSIPDeframer():
    def __init__(self):
        self.m_state = EState.eStateComplete
        self.m_errorBuffer = BinaryBuffer()
        self.offset = 0

    def getErrorData(self):
        return self.m_errorBuffer.Get()

    # Retrieve the packet data from framed protocol data
    def deframe(self, inBuffer, outBuffer):
        self.offset = 0
        res = 0
        data = inBuffer.Get()
        if self.m_state == EState.eStateComplete:
            logger.log(9, "[py-tsip] Looking for packet in:")
        else:
            logger.log(9, "[py-tsip] Continuing packet deframe with:")
        TsipUtils().PacketDump(data)
        while inBuffer.NotEmpty():
            byte = inBuffer.Pop1()
            res = self.processByte(byte, outBuffer)
            if res != TSIP_DECODER_NEED_MORE_DATA:
                return res
        # Still need more data to complete a tsip packet.
        return TSIP_DECODER_NEED_MORE_DATA

    def processByte(self, byte, outBuffer):
        self.offset += 1
        if self.m_state == EState.eStateComplete:
            outBuffer.Clear()
            self.m_errorBuffer.Clear()
            #self.m_errorBuffer.write_1(byte)
            if byte == kDLE:
                #  Start of a new message has been found...
                logger.log(9, "[py-tsip] found packet start at %d" % (self.offset))
                self.m_state = EState.eStateCollectData
            else:
                return TSIP_DECODER_EXPECTED_DLE
        elif self.m_state == EState.eStateCollectDataResetError:
                # This is a special state where the error data needs to be adjusted
                # before the next data byte is collected.
                # It happens when a DLE is found at an unexpected place, and we then
                # assume it is the start of a new packet...
            self.m_errorBuffer.Clear()
            #self.m_errorBuffer.write_1(kDLE)
            #self.m_errorBuffer.write_1(id)
            self.m_state = EState.eStateCollectData
            #self.m_errorBuffer.write_1(byte)
            if byte == kDLE:
                # A DLE was found
                self.m_state = EState.eStateCollectDLE
            else:
                #  Found a valid data byte...
                if outBuffer.Append(byte) == False:
                    self.m_state = EState.eStateComplete
                    return TSIP_DECODER_BUFFER_ERROR
            # Fall-through....
        elif self.m_state == EState.eStateCollectData:
            #self.m_errorBuffer.write_1(byte)
            if byte == kDLE:
                # A DLE was found
                self.m_state = EState.eStateCollectDLE
            else:
                #  Found a valid data byte...
                if outBuffer.Append(byte) == False:
                    self.m_state = EState.eStateComplete
                    return TSIP_DECODER_BUFFER_ERROR
        elif self.m_state == EState.eStateCollectDLE:
            self.m_errorBuffer.Append(byte)
            if byte == kETX:
                #  A complete message has been uncovered.
                logger.log(9, "[py-tsip] found packet end at %d" % (self.offset))
                self.m_state = EState.eStateComplete
                return TSIP_DECODER_PACKET_AVAILABLE
            elif byte == kDLE:
                #  A 0x10 byte was found...
                if outBuffer.Append(byte) == False:
                    self.m_state = EState.eStateComplete
                    return TSIP_DECODER_BUFFER_ERROR
                self.m_state = EState.eStateCollectData
            else:
                # Shouldn't ever get a non DLE/ETX byte here...
                # Treat the last DLE as the start of a new packet
                self.m_state = EState.eStateCollectDataResetError
                logger.log(9,
                    "[py-tsip] found stray DLE at %d, assuming new packet start" % (self.offset))
                outBuffer.Clear()
                outBuffer.Append(byte)
                #return TSIP_DECODER_EXPECTED_DLE
        return TSIP_DECODER_NEED_MORE_DATA

"""
#=============================================================================
# PacketDecoder
#=============================================================================
"""
class PacketDecoder(PacketData):
    def __init__(self, entry, Data, Length, endian):
        super().__init__(entry, Data, Length, endian)

    def Decode(self, InBuf):
        if InBuf.Length() > 0:
            inTmp = InBuffer(InBuf.Get(), InBuf.Length())
            tmpdata = self.get_storage()
            outTmp = OutBuffer(tmpdata, len(tmpdata))
            return self.DecodeData(inTmp, outTmp)
        else:
            logger.log(9, "[py-tsip] Deframed empty packet\n")
            return TSIP_DECODER_PACKET_ERROR

    def DecodeData(self, InBuf, OutBuf):
        logger.log(9, "[py-tsip] Decoding a new packet")
        if self.GetSchema() == None:
            return TSIP_DECODER_NO_SCHEMA
        if self.GetSchema().Decode(None, InBuf, OutBuf, self.m_endian) == True:
            logger.log(9, "[py-tsip] Decoded new Packet\n")
            return TSIP_DECODER_PACKET_AVAILABLE
        logger.debug("[py-tsip] Found an unknown packet")
        return TSIP_DECODER_UNKNOWN_PACKET

"""
#=============================================================================
# TSIPPacketEncoder
#=============================================================================
"""
class TSIPPacketEncoder(PacketEncoder):

    def __init__(self, entry, Data, Length):
        super().__init__(TSIPFramer(), entry, Data, Length, TSIP_ENDIAN)

"""
#=============================================================================
# TSIPGroupPacketEncoder
#=============================================================================
"""
class TSIPGroupPacketEncoder(TSIPPacketEncoder):
    def __init__(self, schemaArray, numEntries, Data, Length):
        super().__init__(None, Data, Length)
        self.m_numEntries = numEntries
        self.m_schemaArray = schemaArray
        self.SetSchemaArray(schemaArray, numEntries)

    def SetSchemaArray(self, schemaArray, numEntries):
        self.m_numEntries = numEntries
        self.m_schemaArray = schemaArray
        self.SetSchema(None)

    def SetCurrentSchema(self, i):
        self.SetSchema(self.m_schemaArray[i])
        self.m_schemaArray[i].Clear()

    def GetNumEntries(self):
        return self.m_numEntries

"""
#=============================================================================
# TSIPPacketDecoder
#=============================================================================
"""
class TSIPPacketDecoder(PacketDecoder):
    def __init__(self, entry, Data, Length):
        super().__init__(entry, Data, Length, TSIP_ENDIAN)
        self.m_tsipDeframer = TSIPDeframer()

    def getErrorData(self):
        return self.m_tsipDeframer.getErrorData()

"""
#=============================================================================
# TSIPGroupPacketDecoder
#=============================================================================
"""
class TSIPGroupPacketDecoder(TSIPPacketDecoder):
    def __init__(self, schemaArray, numEntries, Data, Length):
        # if we aren't passed in storage create it
        if Length == 0:
            tmplist = TSIPSCHEMA_MAX_PACKET_SIZE * [0x00]
            self.m_storage = bytearray(tmplist)
            Data = self.m_storage
            Length = TSIPSCHEMA_MAX_PACKET_SIZE
        super().__init__(None, Data, Length)
        self.m_numEntries = 0
        self.m_schemaArray = None
        self.SetSchemaArray(schemaArray, numEntries)

    def SetSchemaArray(self, schemaArray, numEntries):
        self.m_numEntries = numEntries
        #self.m_schemaArray = self.sortedSchemaArray(schemaArray, numEntries)
        self.m_schemaArray = schemaArray
        self.SetSchema(None)

    def SetCurrentSchema(self, i):
        self.SetSchema(self.m_schemaArray[i])
        self.m_schemaArray[i].Clear()

    def GetNumEntries(self):
        return self.m_numEntries

    def SchemaEntryCompare(self, a, b):
        if a.GetNumFields() == 0 or a.GetFields()[0].GetType() != ETSIPFieldType.eId:
            return 1
        if b.GetNumFields() == 0 or b.GetFields()[0].GetType() != ETSIPFieldType.eId:
            return -1

        # First sort by id...
        aId = a.GetFields()[0]
        bId = b.GetFields()[0]
        if aId.GetId() < bId.GetId():
            return -1
        elif aId.GetId() > bId.GetId():
            return 1
        i = 1
        # Next sort by sub-id...
        while i < a.GetNumFields() and i < b.GetNumFields():
            aSubId = a.GetFields()[i]
            bSubId = b.GetFields()[i]
            if (aSubId == None and bSubId == None):
                # Same number of sub-ids, sort by size...
                break
            # Sort by number of sub-ids
            if aSubId == 0:
                return 1
            elif bSubId == 0:
                return -1
            # Both have this level of sub-id - order by sub-id
            if aSubId.GetSubId() < bSubId.GetSubId():
                return -1
            elif aSubId.GetSubId() > bSubId.GetSubId():
                return 1
            i += 1
        # Same number of sub-ids - order by maximum size
        aMaxSize = a.GetMaxSize(False)
        bMaxSize = b.GetMaxSize(False)
        if aMaxSize < bMaxSize:
            return -1
        elif aMaxSize > bMaxSize:
            return 1
        # For all intents and purposes - the same.
        return 0

    def sortedSchemaArray(self, SchemaEntries, NumSchemaEntries):
        if SchemaEntries == 0 or NumSchemaEntries == 0:
            return None
        entries = list()
        for i in range(NumSchemaEntries):
            entries.append(SchemaEntries[i])
        entries.sort(cmp=self.SchemaEntryCompare)
        #qsort(entries, NumSchemaEntries, sizeof(TSIPSchemaEntry), SchemaEntryCompare)
        return entries

    def DecodeData(self, InBuf, OutBuf):
        error = TSIP_DECODER_UNKNOWN_PACKET
        inData = InBuf.remaining()
        self.mprSchema = None

        # Reversing the schema array to match on more specific command first
        reversed_schemaArray = self.m_schemaArray.copy()
        reversed_schemaArray.reverse()
        
        for entry in reversed_schemaArray:
            if type(entry) is not TSIPSchemaEntry:
                continue
            entry.Clear()
            idSF = entry.GetFields()[0]
            if type(idSF) is IdSchemaField:
                if idSF.GetId() != inData[0]:
                    #  Next entry...
                    continue
            else:
                #  Hmm, that's odd, just skip it...
                continue
            if idSF.GetId() == inData[0]:
                #  Found the a matching id - try to match subid
                potentialMatch = True
            else:
                return TSIP_DECODER_UNKNOWN_PACKET
            j = 1

            if entry.GetNumIds() > 1:
                while j < entry.GetNumFields() and j < InBuf.remainingLength():
                    subIdSF = entry.GetFields()[j]
                    if type(subIdSF) is SubIdSchemaField:
                        #  Make sure the subid matches...
                        if subIdSF.GetSubId() == inData[j]:
                            #  Next field...
                            j += 1
                            continue
                        else:
                            #  Next entry...
                            potentialMatch = False
                            break
                    else:
                        break
            if potentialMatch:
                #  This entry is a possibility - see if the size is good
                size = entry.GetActualSize(False)
                minSize = entry.GetMinSize(False)
                maxSize = entry.GetMaxSize(False)
                remaining = InBuf.remainingLength()
                if (size == remaining) or (size == -1 and minSize <= remaining and maxSize >= remaining):
                    #  This is the one.
                    self.mprSchema = entry
                    if self.mprSchema.Decode(0, InBuf, OutBuf, self.m_endian):
                        # save the packet locally
                        self.set(OutBuf.used(), OutBuf.usedLength())
                        return TSIP_DECODER_PACKET_AVAILABLE
                    return TSIP_DECODER_BUFFER_ERROR
                else:
                    error = TSIP_DECODER_UNEXPECTED_PACKET_SIZE
        return error


"""
#=============================================================================
# TsipUtils
#=============================================================================
"""
class TsipUtils():
    def PacketDump(self, data):
        size = len(data)
        i = 0
        while size >= 8:
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, " %
                          (data[i], data[i + 1], data[i + 2], data[i + 3], data[i + 4], data[i + 5], data[i + 6], data[i + 7]))
            i = i + 8
            size = size - 8
        if (size == 1):
            logger.log(9, "[py-tsip] 0x%02x" % (data[i]))
        elif (size == 2):
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x" % (data[i], data[i + 1]))
        elif (size == 3):
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x, 0x%02x" %
                          (data[i], data[i + 1], data[i + 2]))
        elif (size == 4):
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x, 0x%02x, 0x%02x" %
                          (data[i], data[i + 1], data[i + 2], data[i + 3]))
        elif (size == 5):
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x" % (
                data[i], data[i + 1], data[i + 2], data[i + 3], data[i + 4]))
        elif (size == 6):
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x" % (
                data[i], data[i + 1], data[i + 2], data[i + 3], data[i + 4], data[i + 5]))
        elif (size == 7):
            logger.log(9, "[py-tsip] 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x" % (
                data[i], data[i + 1], data[i + 2], data[i + 3], data[i + 4], data[i + 5], data[i + 6]))
