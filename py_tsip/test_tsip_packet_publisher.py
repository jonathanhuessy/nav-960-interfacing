import pytest
from .data_buffer import BinaryBuffer
from .tsip_packet_publisher import TsipPacketPublisherGroup
from .tsip_schema import TSIP_DECODER_PACKET_AVAILABLE
from .tsip_packets import ServerPacketDecoder, EServerPackets

"""
To get VS Code test explorer (the beaker icon) to show the tests and run them (including debugging),
add this to testautomation/.vscode/settings.json:

    "python.testing.pytestArgs": [
        "./drivers/py_tsip/py_tsip"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,

You can also run this file from the command line with 'pytest drivers/py_tsip/py_tsip'.
"""

class PktObs:
  def HandlePacket(self, packetId, packet):
    assert packetId == EServerPackets.ebf401400rsp

# Two tests to do something very similar - check the packetId we get from
# decoding a TAP response packet.
# This first test uses the Packet Publisher and registers a callback that
# checks the packetId. PacketPublisher makes up an ID if ProcessPacket fails
# and we don't want that here.
# @pytest.mark.skip()
def test_publish_packet_decodes_correct_packet_id():
  decoder = ServerPacketDecoder()
  pkt = BinaryBuffer()
  pub = TsipPacketPublisherGroup(None)
  data = [0xbf, 0x40, 0x14, 0x00, 19,
        ord('v'), ord('m'), ord('s'), ord(':'), ord('D'),
        ord('e'), ord('f'), ord('a'), ord('u'), ord('l'),
        ord('t'), ord(' '), ord('V'), ord('e'), ord('h'),
        ord('i'), ord('c'), ord('l'), ord('e'),
        23]
  cksm = pub.CalcChecksum(data)
  data.append((cksm & 0xff00) >> 8)
  data.append(cksm & 0xff)
  pkt.Append(bytes(data))

  obs = PktObs()
  pub.RegisterObserver([EServerPackets.ebf401400rsp], obs)
  pub.PublishPacket(pkt)

# This second test uses the Packet Decoder directly to make sure it picks
# the correct packetId schema.
def test_decoder_packet_id_is_correct():
  decoder = ServerPacketDecoder()
  pkt = BinaryBuffer()
  pub = TsipPacketPublisherGroup(None)
  data = [0xbf, 0x40, 0x14, 0x00, 19,
        ord('v'), ord('m'), ord('s'), ord(':'), ord('D'),
        ord('e'), ord('f'), ord('a'), ord('u'), ord('l'),
        ord('t'), ord(' '), ord('V'), ord('e'), ord('h'),
        ord('i'), ord('c'), ord('l'), ord('e'),
        23]
  cksm = pub.CalcChecksum(data)
  data.append((cksm & 0xff00) >> 8)
  data.append(cksm & 0xff)
  pkt.Append(bytes(data))

  assert decoder.Decode(pkt) == TSIP_DECODER_PACKET_AVAILABLE
  packetId = decoder.GetEntryType()
  assert packetId == EServerPackets.ebf401400rsp

class PktObsDbgData:
  def __init__(self, exp_pkt_id, exp_pkt_number, exp_pkt_count, exp_dbg_pkt_data):
    self._ExpPacketId = exp_pkt_id
    self._ExpPacketNumber = exp_pkt_number
    self._ExpPacketCount = exp_pkt_count
    # Could be the header or the data.
    self._ExpDbgPacketData = exp_dbg_pkt_data

  def HandlePacket(self, packetId, decoded_message):
    assert packetId == self._ExpPacketId
    assert decoded_message.PacketNumber == self._ExpPacketNumber
    assert len(decoded_message.PacketData) == len(self._ExpDbgPacketData)
    # The last 6 bytes of data are length and checksum. Before that, the data ends with 0x47.
    assert decoded_message.PacketData[0] == self._ExpDbgPacketData[0]
    assert decoded_message.PacketData[-1] == self._ExpDbgPacketData[-1]
    assert decoded_message.PacketCount == self._ExpPacketCount

def test_decodes_bf470e06_dbg_header():
  decoder = ServerPacketDecoder()
  pub = TsipPacketPublisherGroup(None)

  # These 4 packets came from a session where I was starting DBG logging. The data is the
  # DBG header from the Nav. I wrote this unit test because py_tsip was failing to decode the
  # packets because the array size was decoded wrong (AAT-2582, py_tsip SHA 4e62c3560143020072).
  # This unit test will fail (and should fail) if you use py_tsip older than that.
  data = bytes.fromhex('bf470e060401aa000000000000000000000000000000000000000000000000000000000000000000000000000000002054696d6520536563202020202020040754696d65204e73656320202020200407494d5520417474205961772020200408494d552041747420526f6c6c20200408494d5520417474205920526174650408494d5520417474205220526174650408494d552042696173204779726f5a0408494d552056656c20486f727a2020040847b02378')
  pkt = BinaryBuffer(data)
  assert decoder.Decode(pkt) == TSIP_DECODER_PACKET_AVAILABLE
  packetId = decoder.GetEntryType()
  assert packetId == EServerPackets.ebf470e06rsp

  # If the decoder returns TSIP_DECODER_PACKET_AVAILABLE, it means py_tsip figured out
  # what kind of packet it is. Next, TsipPacketPublisher.ProcessPacket will do the
  # unpacking to the named struct. This happens in the PublishPacket call stack so
  # we need to make sure it's working here.
  obs = PktObsDbgData(EServerPackets.ebf470e06rsp, 1, 4, data[7:177])
  pub.RegisterObserver([EServerPackets.ebf470e06rsp], obs)
  pub.PublishPacket(pkt)

  data = bytes.fromhex('bf470e060402aa505320506f7320416e74204520080947505320506f7320416e74204e20080947505320506f7320416e7420552008094750532048656164696e67202020040847505320486f727a2056656c2020040847505320506f732054797065202001024163632058202020202020202020040841636320592020202020202020200408416363205a20202020202020202004084779726f2058202020202020202004084779726f20592020202020b02856')
  pkt = BinaryBuffer(data)
  assert decoder.Decode(pkt) == TSIP_DECODER_PACKET_AVAILABLE
  packetId = decoder.GetEntryType()
  assert packetId == EServerPackets.ebf470e06rsp

  data = bytes.fromhex('bf470e060403aa20202004084779726f205a202020202020202004085374656572696e6720416e676c65040858544520202020202020202020200408436d6420416e676c6520202020200408464620416e676c652020202020200408506174682048656164696e672020040850617468506f7345617374202020080950617468506f734e6f7274682020080950494420636d6420312020202020040853797374656d205374617465202001025377617468b02cc5')
  pkt = BinaryBuffer(data)
  assert decoder.Decode(pkt) == TSIP_DECODER_PACKET_AVAILABLE
  packetId = decoder.GetEntryType()
  assert packetId == EServerPackets.ebf470e06rsp

def test_decodes_bf470e06_dbg_header_last_packet():
  decoder = ServerPacketDecoder()
  pub = TsipPacketPublisherGroup(None)

  # Decode a shorter packet.
  data = bytes.fromhex('bf470e0604042b204f66667365742020020456656820446972656374696f6e2001024748462048656164696e672020200408310ca4')
  pkt = BinaryBuffer(data)
  assert decoder.Decode(pkt) == TSIP_DECODER_PACKET_AVAILABLE
  packetId = decoder.GetEntryType()
  assert packetId == EServerPackets.ebf470e06rsp

  obs = PktObsDbgData(EServerPackets.ebf470e06rsp, 4, 4, data[7:50])
  pub.RegisterObserver([EServerPackets.ebf470e06rsp], obs)
  pub.PublishPacket(pkt)

def test_decodes_bf470e07_dbg_data():
  decoder = ServerPacketDecoder()
  pub = TsipPacketPublisherGroup(None)

  data = bytes.fromhex('bf470e070101890000034439fecd40409be2553ff3b2493ac36da1bc0f51e03a14f323000000000000000000000000000000000000000000000000000000000000000000000000003a2fcd0fbd086de6bf8015933dac4c6cbc0b9cf93b06f3990000000000000000000000000000000000000000000000000000000000000000000000000000000002000002000000008f18bd')
  pkt = BinaryBuffer(data)
  assert decoder.Decode(pkt) == TSIP_DECODER_PACKET_AVAILABLE
  packetId = decoder.GetEntryType()
  assert packetId == EServerPackets.ebf470e07rsp

  obs = PktObsDbgData(EServerPackets.ebf470e07rsp, 1, 1, data[7:144])
  pub.RegisterObserver([EServerPackets.ebf470e07rsp], obs)
  pub.PublishPacket(pkt)
