Using The Trimble py_tsip Package

Download and Installation The package is in the TestAutomation
repository found on Trimble Tools BitBucket website in the Agriculture
project directory. Clone the repo into a local directory. At the time of
this writing you will need to checkout the PythonTsipLib branch. the
py_tsip package is the py_tsip directory under TestAutomation. The
package can be installed from the local directory using pip3 (as
admin/superuser):

> sudo pip3 install ./py_tsip

Package Initialization The package is setup to import the package as a
whole:

> import py_tsip

To start the tsip engine running it needs have the port manager
initialized with the com port name. This would be something like `com1`
for the pc or `/dev/ttyUSB0` for the linux.

> portManager = py_tsip.TsipPortManager(portName)

This must be done first before sending or registering to receive
packets.

Receiving TSIP packets There are two ways to receive packets from the
library. First, the application code should include a HandlePacket()
function defined as defined below. Second the PacketPublisher has a
waitForTsipResponse() call that will wait for a single response of the
specified type (with timeout) and return the packet data. This is not
dependent on having the packet in the list of packets yoou are listening
for.

HandlePacket()

> def HandlePacket(self, packetId, packetData):

This will be called for every valid packet that you are listening for
that is received. The ID code of the packets you want to receive must be
registered with the packet publisher. The list of ID codes are
EClientPackets and EServerPackets enums. The format for the enum is
small `e` followed by the 2 digit binary packet ID and any and all
subIDs (always 2 digits) and then one of the following type specifiers:
`req`, `cmd`,`rsp` or `ack`.

A list of known commands can be found in the file
py_tsip/py_tsip/src/tsippackets.html, along with a description of any
applicable parameters. Create a python list of the packets you want to
receive. This should include any response/acknowledge you expect to
receive for packets you will send.

> PacketList = [py_tsip.EServerPackets.e13rsp,
>
> :   py_tsip.EServerPackets.e45rsp, py_tsip.EServerPackets.e41rsp,
>     py_tsip.EServerPackets.e46rsp]
>
It is prudent to always include packet e13rsp since this is the tsip
format error packet that tells you that you sent a bad tsip packet to
the receiver. You may want to include other debug packets as your
application requires. Once you have the list, it needs to be registered
with the packetPublisher.

> packetPublisher = self.portManager.GetPublisherGroup()
> packetPublisher.RegisterObserver(PacketList, self)

The HandlePacket function will be called anytime one of the packets in
your list is received and will give you packetId and packetData fro the
packet. Your application will need to handle it from here. If you have a
large number of packets, the following HandlePacket() code may make it
easier for by always calling [handlePacket]()\<packetID\> (.ie.
handlePacket_e8f89rsp).

If the response has data it will be returned as a tuple that can be
found in the tsip_packets.py file. For our current example that would
be:

> S8f89rsp_tup = namedtuple(\'S8f89rsp_tup\', \' DGPSSrcMode BeaconAcqMode BeaconFreq0
>
> :   BeaconFreq1 BeaconRTCMTimeout SatelliteFrequency SatelliteBitRates
>
> > SatelliteRTCMTimeout WAASTimeout CorrectionOptions
> > SatConfigSource\')

The values can be extracted directly from packetData as:

> packetData.DGPSSrcMode packetData.BeaconAcqMode packetData.BeaconFreq0
> \...

waitForTsipResponse() This call is made using the same packet
definitions used in HandlePacket(), but only takes a single packet type
along with a timeout in seconds:

> waitForTsipResponse(packetType, timeoutSecs)

waitForTsipResponse() will return when the packet is received or the
timeout is reached. If the packet is received, the call will return the
packet data, and if the timeout is reached a \"None\" value will be
returned.

Sending TSIP packets

Find the command you want to use in the tsippackets.html document as
shown in the previously, for instance the `DGPS Source Control Command`.
This will show you the command ID (ie. 8e89) and the structure of the
command. So the code ID to set the parameters is
py_tsip.EClientPackets.e8e89cmd. The response packet for these is
e8f89rsp in EServerPackets Enum, so the code ID for this is
EServerPackets .e8f89rsp and would need to be in the receive packets
list

Once you know the codes, prepending a capital `S` to the command ID
instead of a small `e` and searching the tsip_packets.py file you will
find the \* _tup that is used to transfer the data. This is the
structure with the variable names. The packet ID can be used to get the
tuple form the appropriate tuple list:

> packetId = py_tsip.EClientPackets.e8e89cmd packetTuple =
> py_tsip.ClientTupleList\[packetId.value\]

S8e89cmd_tup = namedtuple(\'S8e89cmd_tup\', \' DGPSSrcMode
BeaconAcqMode BeaconFreq0 BeaconFreq1 BeaconRTCMTimeout
SatelliteFrequency SatelliteBitRate SatelliteRTCMTimeout WAASTimeout
CorrectionOptions SatConfigSource\')

To send a command, create the tuple with the values you need (tuples are
immutable so you cannot create the tuple and then set the values).

> DGPSSrcMode = 0x03 \# WAAS differential only
>
> :   BeaconAcqMode = 0x01 \# Auto Distance mode BeaconFreq0 = 0 \#
>     don\'t change BeaconFreq1 = 0 \# don\'t change BeaconRTCMTimeout =
>     20 \#seconds SatelliteFrequency = 1557861500.0 SatelliteBitRate =
>     2400.0 SatelliteRTCMTimeout = 20 \# sec WAASTimeout = 20 \# sec
>     CorrectionOptions = 0 SatConfigSource = 0 \# Values must be in the
>     correct order packetData = packetTuple( DGPSSrcMode,
>     BeaconAcqMode, BeaconFreq0, BeaconFreq1, BeaconRTCMTimeout,
>     SatelliteFrequency, SatelliteBitRate, SatelliteRTCMTimeout,
>     WAASTimeout, CorrectionOptions, SatConfigSource )
>
Then the command can sent through the packetPublisher.

> packetPublisher.TsipSendPacket(packetId, packetData)

Updating Packet Definitions

The file tsip_packets.py, which holds all the packet definitions, is
created from a master tsippackets.xml file. This file is taken from the
picus code base in which ever branch is the most current with respect to
TSIP packets (currently the shifter branch). To update the
tsip_packets.py file the following files need to be copied into the
py_tsip/py_tsip/src directory from the picus/tsippackets:

> src/tsippackets.xml src/tsippacketscommon.xsl tsippacketsconfig.xsl

Once the files are copied, from a command line change directories to the
src directory and run make. This will generate the tsip_packets.py and
tsippackets.html files. If the tsip_packets.py file is updated then the
version should be changed in py_tsip/setup.py and the package updated
on any systems it is currently being used on.

TsipPortManager Diagram

This diagram shows the state machine that TsipPortManager uses to manage
connections to the device under test.

<https://lucid.app/lucidchart/b6370dd2-adfc-46f9-85d4-633b0e7b0d64/edit?invitationId=inv_f43a27f3-5b4e-417d-bf75-a6fd0ab5cb93>
