from pcars.packet import Packet
from unittest import TestCase


class TestPacket(TestCase):

    def testParsePacket(self):
        p = Packet.readFrom('\xd2\x04\x01')
        self.assertEqual(1234, p.buildVersion)
        self.assertEqual(1, p.packetType)
