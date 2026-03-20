import copy

#=============================================================================
# @file data_buffer.hpp
# Utility classes for handling buffered data.
#=============================================================================

#----------------------------------------------------------------------
# DataField<...>
#-----------------------------------------------------------------------------
# A bookmark in memory indicating the size and location of data.
#-----------------------------------------------------------------------------


class DataField:
    # Construct a data-field from the provided memory location and size
    # @param data Memory location of the data
    # @param length The number of data items at this location
    def __init__(self, data=None, length=0):
        self.m_data = data
        self.m_length = length
        self.m_start = 0
        if type(data) != int and type(data) != bool and data != None:
            self.m_actualLength = len(data)
        else:
            self.m_actualLength = 0

    # @returns the data pointed to
    def get_data(self):
        if self.m_length < 0 or self.m_data == None:
            return None
        else:
            end = self.m_start + self.m_length
            return self.m_data[self.m_start:end]

    def get_storage(self):
        if self.m_actualLength > 0:
            return self.m_data
        else:
            return False

    def add_data(self, data, length):
        if (self.m_start + self.m_length + length) > self.m_actualLength:
            return False
        elif data == None:
            return False
        else:
            offset = self.m_start + self.m_length
            for i in range(length):
                self.m_data[offset + i] = data[i]
        return True

       # @returns the number of data items represented
    def get_length(self):
        if self.m_actualLength == 0:
            return 0
        return self.m_length

    # Sets the data field
    # @param data Memory location of the data
    # @param length Number of data items at the location
    # use larger of my storage or the new storage
    def set(self, data, length):
        if length < self.m_actualLength:
            for i in range(length):
                self.m_data[i] = data[i]
        else:
            self.m_data = data
            self.m_actualLength = len(self.m_data)
        self.m_length = length
        self.m_start = 0

    def reset(self):
        self.m_start = 0
        self.m_length = self.m_actualLength

    # Move the start location of data being pointed at
    # @param length The number of data items to move the start (can be back -ve)
    def moveStart(self, length):
        tmpStart = self.m_start + length
        if tmpStart > self.m_actualLength or tmpStart < 0:
            return None
        self.m_start = tmpStart
        self.m_length -= length

    # Move the end location of the data being pointed at
    # @param length The number of data items to move the end (can be back -ve)
    def moveEnd(self, length):
        tmplength = self.m_length + length
        if tmplength < 0 or tmplength > self.m_actualLength:
            return None
        self.m_length = tmplength


"""
#----------------------------------------------------------------------
# TBuffer<...>
#-----------------------------------------------------------------------------
# A buffer of data objects in memory.
# Allows easy access to the remaining data in the buffer, and the data
# already used.
#-----------------------------------------------------------------------------
"""

class DataBuffer:
    def __init__(self, data, length):
        self.m_remaining = DataField(data, length)
        self.m_used = DataField(data, 0)

    def reset(self):
        self.m_used.reset()
        self.m_remaining.reset()
        self.m_used.moveEnd(-self.m_remaining.get_length())

    # Set the buffer to the new data source
    def setData(self, data, length):
        self.m_remaining.set(data, length)
        self.m_used.set(data, 0)

    def copyData(self, df):
        self.setData(df.data(), df.get_length())

    # @returns a data-field representing the remaining data in the buffer
    def remaining(self):
        return self.m_remaining.get_data()

    # @returns a data-field representing the used data in the buffer
    def used(self):
        return self.m_used.get_data()

    # @returns the number of remaining data items in the buffer
    def remainingLength(self):
        return self.m_remaining.get_length()

    # @returns the number of used data items in the buffer
    def usedLength(self):
        return self.m_used.get_length()

    def get_storage(self):
        return self.m_used.get_storage()

    def move(self, length):
        self.m_used.moveEnd(length)
        self.m_remaining.moveStart(length)

"""
#----------------------------------------------------------------------
# InBuffer<...>
#-----------------------------------------------------------------------------
# A input buffer containing data to be consumed.
# The used data is the data already consumed.
# The remaining data is the data available.
# The data inside cannot be modified.
#-----------------------------------------------------------------------------
"""

class InBuffer(DataBuffer):
    def __init__(self, data, length):
        super().__init__(data, length)

    # Take data from the input buffer
    # @param outBuf The buffer to populate with the data
    # @param length The number of data items to retrieve
    def read_to_buff(self, outBuf, length):
        if length > outBuf.remainingLength() or length > self.remainingLength():
            return False
        data = self.remaining()
        self.move(length)
        return outBuf.write(data, length)

    # Take data from the input buffer
    # @param outData The data to populate from the input buffer
    # @param length The number of data items to take
    def read_to_array(self, outData, length):
        if length > self.remainingLength():
            return False
        tmpData = self.remaining()
        for i in range(length):
            outData[i] = tmpData[i]
        self.move(length)
        return True

    # @return the data pointer
    def read_all(self):
        return self.remaining()

    # Skip some of the input data
    # @param length The number of data items to skip
    def skip(self, length):
        if length > self.remainingLength():
            return False
        self.move(length)
        return True


#-----------------------------------------------------------------------------
# fill(....)
#-----------------------------------------------------------------------------

def fill(self, data, value, length):
    if length > len(data):
        length = len(data)
    for i in range(length):
        data[i] = value

"""
#-----------------------------------------------------------------------------
# OutBuffer<...>
#-----------------------------------------------------------------------------
# An output buffer is filled by other data sources.
# The used data holds the currently filled data.
# The remaining data is the free space.
#-----------------------------------------------------------------------------
"""

class OutBuffer(DataBuffer):
    def __init__(self, data, length):
        super().__init__(data, length)

    # Fill the output buffer from the input buffer
    # @param in The input buffer containing the data to copy
    # @param length The number of data items to copy
    def write_from_buf(self, inBuf, length):
        if length < inBuf.remainingLength() or length > self.remainingLength():
            return False
        data = None
        inBuf.read_to_array(data, length)
        self.move(length)
        return self.write_data(data, length)

    # Fill the output buffer from the data field
    # @param df The data to fill the output buffer with
    def write_from_field(self, df):
        return self.write_data(df.data(), df.get_length())

    # Fill the output buffer from the memory
    # @param data The data to copy into the output buffer
    # @param length The length of the data to copy
    def write_1(self, data):
        dataArray = [data]
        return self.write_data(dataArray, 1)

    def write_data(self, data, length):
        if length > self.remainingLength():
            return False
        self.m_used.add_data(data, length)
        self.move(length)
        return True

    # Fill the output buffer with the given value
    # @param value The value to copy into the buffer
    # @param length the number of copies to make
    def fill(self, value, length):
        if length > self.remainingLength() - 1:
            length = self.remainingLength() - 1
        data = [value] * length
        self.m_used.add_data(data, length)
        self.move(length)
        return True


"""
#-----------------------------------------------------------------------------
# BinaryBuffer<...>
#-----------------------------------------------------------------------------
# An output buffer is filled by other data sources.
# The used data holds the currently filled data.
# The remaining data is the free space.
#-----------------------------------------------------------------------------
"""

class BinaryBuffer():
    def __init__(self, data=None):
        if data == None:
            self._Data = bytearray()
        else:
            self._Data = bytearray(data)

    #-----------------------------------------------------------------------------
# def Clear(...)
#-----------------------------------------------------------------------------
    def Clear(self):
        size = len(self._Data)
        del self._Data[:size]

#-----------------------------------------------------------------------------
# def Truncate(...)
#-----------------------------------------------------------------------------
    def Truncate(self, remaining):
        trim = len(self._Data) - remaining
        if trim > 0:
            del self._Data[:trim]

#-----------------------------------------------------------------------------
# def Get(...)
#-----------------------------------------------------------------------------
    def Get(self):
        return self._Data

#-----------------------------------------------------------------------------
# def GetSize(...)
#-----------------------------------------------------------------------------
    def Length(self):
        return len(self._Data)

#-----------------------------------------------------------------------------
# def Append(...)
#-----------------------------------------------------------------------------
    def Append(self, data):
        if isinstance(data, bytearray) or isinstance(data, bytes):
            self._Data.extend(data)
        else:
            self._Data.append(data)

#-----------------------------------------------------------------------------
# def PopAll(...)
#-----------------------------------------------------------------------------
    def PopAll(self, data):
        data = copy.deepcopy(self._Data)
        size = len(self._Data)
        del self._Data[:size]
        return size


#-----------------------------------------------------------------------------
# def PopData(...)
#-----------------------------------------------------------------------------
    def PopData(self, data, length):
        size = length
        if len(self._Data) < length:
            size = len(self._Data)
        data = self._Data[:size]
        del self._Data[:size]
        return size


#-----------------------------------------------------------------------------
# def Pop1(...)
#-----------------------------------------------------------------------------
    def Pop1(self):
        return self._Data.pop(0)

#-----------------------------------------------------------------------------
# def NotEmpty(...)
#-----------------------------------------------------------------------------
    def NotEmpty(self):
        return (len(self._Data) > 0)

#-----------------------------------------------------------------------------
# def __getitem__(...)
#-----------------------------------------------------------------------------
    def __getitem__(self, key):
        if key > len(self._Data):
            return None
        else:
         return self._Data[key]
