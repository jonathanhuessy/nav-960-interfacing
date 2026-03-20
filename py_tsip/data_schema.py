#=============================================================================
# @file data_schema.py
# Utility classes for handling data with a schema
#
# Copyright (c) 2017 Trimble Navigation Limited
#=============================================================================
from struct import *
from enum import Enum
from .data_buffer import DataField
import abc
import logging
import sys

# Module-level logger
logger = logging.getLogger("py_tsip")
logger.setLevel(logging.WARNING)

SCHEMA_BIG_ENDIAN = 0x00FF
SCHEMA_LITTLE_ENDIAN = 0xFF00
SCHEMA_MACHINE_ORDER = sys.byteorder
if SCHEMA_MACHINE_ORDER == "little":
    SCHEMA_MACHINE_ENDIAN = SCHEMA_LITTLE_ENDIAN
else:
    SCHEMA_MACHINE_ENDIAN = SCHEMA_BIG_ENDIAN


class ESchemaFieldType(Enum):
    eCHAR = 0   # A character
    eU8 = 1     # An unsigned 8 bit integer
    eS8 = 2     # A signed 8 bit integer
    eU16 = 3    # An unsigned 16 bit integer
    eS16 = 4    # A signed 16 bit integer
    eU32 = 5    # An unsigned 32 bit integer
    eS32 = 6    # A signed 32 bit integer
    eFLT = 7    # A single precision floating point number
    eDBL = 8    # A double precision floating point number
    eGroup = 9  # A grouping of fields
    kLastSchemaFieldType = 10  # The number of field types
    kInvalidField = -1  # An invalid field indicator


class ESizeType(Enum):
    eActualSize = 0
    eMinSize = 1
    eMaxSize = 2

"""
#=============================================================================
# SchemaField
#=============================================================================
"""
class SchemaField(abc.ABC):
    #----------------------------------------------------------------------
    # SchemaField defines a schema field entry that indicates how
    # to decode a buffer of memory
    # This structure is used internally to allow static initialization
    # of a generic schema field
    def __init__(self, Type, Name=None, Description=None):
        self.mType = Type
        self.mName = Name
        self.mDescription = Description
        self.value = None
        self.hasValue = False

    @abc.abstractmethod
    def GetSize(self, eSizeType, boolDecodedSize):
        return 0

    def GetType(self):
        return self.mType

    def GetName(self):
        return self.mName

    def GetDescription(self):
        return self.mDescription

    def GetActualSize(self, DecodedSize=True):
        return self.GetSize(ESizeType.eActualSize, DecodedSize)

    def GetMinSize(self, DecodedSize=True):
        return self.GetSize(ESizeType.eMinSize, DecodedSize)

    def GetMaxSize(self, DecodedSize=True):
        return self.GetSize(ESizeType.eMaxSize, DecodedSize)

    def AdjustData(self, Data):
        return Data

    def GetAsInteger(self, Data, Index):
        return -1

    def GetAsFloat(self, Data, Index):
        return -1.0

    def GetAsString(self, Data, Index, String, Length):
        return None

    def GetNumFields(self, DF):
        return 0

    def GetField(self, Index):
        return None

    def GetFields(self):
        return None

    def HasValue(self):
        return self.hasValue

    def GetValue(self):
        return self.Value

    def Clear(self):
        self.hasValue = False
        self.Value = None

    def SetValue(self, data):
        pass

    def Decode(self, Parent, InBuf, OutBuf, endian):
        actualSize = self.GetActualSize()
        tmplist = actualSize * [0x00]
        tmpdata = bytearray(tmplist)
        if InBuf.read_to_array(tmpdata, actualSize):
            if (actualSize > 1) and (endian != SCHEMA_MACHINE_ENDIAN):
                self.swapBytes(tmpdata, actualSize)
            OutBuf.write_data(tmpdata, actualSize)
            self.SetValue(tmpdata)
            return True
        return False

    def Encode(self, Parent, InBuf, OutBuf, endian):
        actualSize = self.GetActualSize()
        tmplist = actualSize * [0x00]
        tmpdata = bytearray(tmplist)
        if InBuf.read_to_array(tmpdata, actualSize):
            if (actualSize > 1) and (endian != SCHEMA_MACHINE_ENDIAN):
                self.swapBytes(tmpdata, actualSize)
            OutBuf.write_data(tmpdata, actualSize)
            self.SetValue(tmpdata)
            return True
        return False

    #------------------------------------------------------------------------
    # Endianizes a chunk of data with respect to TSIP and the machine endian
    # ordering
    def swapBytes(self, Data, Length):
        loopSize = int(Length / 2)
        for i in range(loopSize):
            j = (Length - 1) - i
            tmp = Data[i]
            Data[i] = Data[j]
            Data[j] = tmp

"""
#=============================================================================
# CHARSchemaField
#=============================================================================
"""
class CHARSchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eCHAR, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">B", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        if len(Data) >= Index + Length:
            String = Data[Index:Index + Length]
            return String
        else:
            return None

    def SetValue(self, data):
        tmp = unpack_from("=B", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 1
    
"""
#=============================================================================
# U8SchemaField
#=============================================================================
"""
class U8SchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eU8, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">B", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsInteger(self, Data, Index)
        return "0x%02X" % value

    def SetValue(self, data):
        tmp = unpack_from("=B", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 1

"""
#=============================================================================
# S8SchemaField
#=============================================================================
"""
class S8SchemaField(SchemaField):
    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eS8, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">b", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsInteger(self, Data, Index)
        return "0x%02X" % value

    def SetValue(self, data):
        tmp = unpack_from("=b", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 1

"""
#=============================================================================
# U16SchemaField
#=============================================================================
"""
class U16SchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eU16, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">H", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsInteger(self, Data, Index)
        return "0x%d" % value

    def SetValue(self, data):
        tmp = unpack_from("=H", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 2

"""
#=============================================================================
# S16SchemaField
#=============================================================================
"""
class S16SchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eS16, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">h", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsInteger(self, Data, Index)
        return "0x%d" % value

    def SetValue(self, data):
        tmp = unpack_from("=h", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 2

"""
#=============================================================================
# U32SchemaField
#=============================================================================
"""
class U32SchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eU32, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">L", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsInteger(self, Data, Index)
        return "0x%d" % value

    def SetValue(self, data):
        tmp = unpack_from("=L", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 4

"""
#=============================================================================
# S32SchemaField
#=============================================================================
"""
class S32SchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eS32, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = unpack_from(">l", Data, Index)
        return value[0]

    def GetAsFloat(self, Data, Index):
        self.GetAsInteger(self, Data, Index)

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsInteger(self, Data, Index)
        return "0x%d" % value

    def SetValue(self, data):
        tmp = unpack_from("=l", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 4

"""
#=============================================================================
# FLTSchemaField
#=============================================================================
"""
class FLTSchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eFLT, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = self.GetAsFloat(self, Data, Index)
        return int(value)

    def GetAsFloat(self, Data, Index):
        value = unpack_from(">f", Data, Index)
        return value[0]

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsFloat(self, Data, Index)
        return "0x%f" % value

    def SetValue(self, data):
        tmp = unpack_from("=f", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 4

"""
#=============================================================================
# DBLSchemaField
#=============================================================================
"""
class DBLSchemaField(SchemaField):

    def __init__(self, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eDBL, Name, Description)

    def GetAsInteger(self, Data, Index):
        value = self.GetAsFloat(self, Data, Index)
        return int(value)

    def GetAsFloat(self, Data, Index):
        value = unpack_from(">d", Data, Index)
        return value[0]

    def GetAsString(self, Data, Index, String, Length):
        value = self.GetAsFloat(self, Data, Index)
        return "0x%f" % value

    def SetValue(self, data):
        tmp = unpack_from("=d", data)
        self.Value = tmp[0]
        self.HasValue = True

    def GetSize(self, Type, DecodedSize):
        return 8

"""
#=============================================================================
# GroupSchemaField
#=============================================================================
"""
class GroupSchemaField(SchemaField):
    def __init__(self, Fields, NumFields, Name=None, Description=None):
        super().__init__(ESchemaFieldType.eGroup, Name, Description)
        self.mprFields = Fields
        self.mNumFields = NumFields

    def GetFields(self):
        return self.mprFields

    def GetSize(self, Type, DecodedSize):
        size = 0
        if self.mNumFields == 0:
            return -1
        for i in range(self.mNumFields):
            itemSize = self.mprFields[i].GetSize(Type, DecodedSize)
            #  If an itemSize ends up being -1, then it is non-trivial to work
            #  out the requested size - return -1
            if itemSize == -1:
                return -1
            size = size + itemSize
        return size

    def GetField(self, Index):
        field = None
        if Index < self.mNumFields:
            field = self.mprFields[Index]
        return field

    def GetNumFields(self):
        return self.mNumFields

    def Clear(self):
        for i in range(self.mNumFields):
            self.GetField(i).Clear()

    def Decode(self, Parent, InBuf, OutBuf, endian):
        #  Get the array length, and make sure it's valid
        groupfield = SchemaDataField(
            self, InBuf.remaining(), InBuf.remainingLength())
        for i in range(self.mNumFields):
            item = self.GetField(i)
            if item.Decode(groupfield, InBuf, OutBuf, endian) == False:
                logger.debug("[py-tsip] GroupSchemaField decode failed at item #%d", i)
                return False
        return True

    def Encode(self, Parent, InBuf, OutBuf, endian):
        groupfield = SchemaDataField(
            self, InBuf.remaining(), InBuf.remainingLength())
        #  Get the array length, and make sure it's valid
        for i in range(self.mNumFields):
            item = self.GetField(i)
            if item.Encode(groupfield, InBuf, OutBuf, endian) == False:
                logger.debug("[py-tsip] GroupSchemaField encode failed at item #%d", i)
                return False
        return True

"""
#------------------------------------------------------------------------
# SchemaEntry
#------------------------------------------------------------------------
"""
class SchemaEntry(GroupSchemaField):
    def __init__(self, Type, Fields, NumFields, IdName, Name, Description):
        super().__init__(Fields, NumFields, Name, Description)
        self.mType = Type
        self.mIdName = IdName

    def GetEntryType(self):
        return self.mType

    def GetIdName(self):
        return self.mIdName

"""
#------------------------------------------------------------------------
# SchemaDataField
#------------------------------------------------------------------------
"""
class SchemaDataField(DataField):
    def __init__(self, Schema, Data, Length, Parent=None):
        super().__init__(Data, Length)
        self.mprParent = Parent
        self.mprSchema = Schema

    def GetSchema(self):
        return self.mprSchema

    def GetParent(self):
        return self.mprParent

    def GetAsInteger(self):
        return self.mprSchema.GetAsInteger(self.m_data, 0)

    def GetAsFloat(self):
        return self.mprSchema.GetAsFloat(self.m_data, 0)

    def GetAsString(self, String, Length):
        if Length == 0:
            return None
        return self.mprSchema.GetAsString(self.m_data, 0, String, Length)

    def HasValue(self):
        return self.mprSchema.HasValue()

    def GetValue(self):
        return self.mprSchema.GetValue()

    def Clear(self):
        return self.mprSchema.Clear()

    def GetNumFields(self):
        return self.mprSchema.GetNumFields()

    def GetField(self, Index, DecodedSize=True):
        # If the index is out of range, then return a null schema field.
        if Index >= self.GetNumFields():
            return None
        # Find the data field of interest.  Allow the schema to adjust the pointer
        # in case of special handling.
        # Construct a new schema data field for data
        tmpSchema = self.mprSchema.GetField(Index)
        offset = 0
        for i in range(Index):
            tmpOffset = self.mprSchema.GetField(i).GetActualSize(DecodedSize)
            if tmpOffset < 0:
                return None
            offset += tmpOffset
        inData = self.get_data()
        tmpData = inData[offset:]
        tmpSize = tmpSchema.GetActualSize()
        return SchemaDataField(tmpSchema, tmpData, tmpSize, self)
