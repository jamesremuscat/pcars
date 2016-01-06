from pcars.packet import Packet
from unittest import TestCase
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestPacket(TestCase):

    def testParsePacketHeader(self):
        p = Packet.readFrom('\xd2\x04\x01')
        self.assertEqual(1234, p.buildVersion)
        self.assertEqual(1, p.packetType)

    def testParseSamplePacket0(self):
        f = read_into_buffer(os.path.join(__location__, "packet_0.bin"))
        p = Packet.readFrom(f)
        self.assertEqual(1122, p.buildVersion)
        self.assertEqual(0, p.packetType)


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf
