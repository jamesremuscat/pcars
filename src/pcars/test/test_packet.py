from pcars.packet import Packet, TelemetryPacket
from StringIO import StringIO
from unittest import TestCase
import os
from pcars.enums import GameSessionState

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestPacket(TestCase):

    def testParsePacketHeader(self):
        p = Packet.readFrom(StringIO('\xd2\x04\x01'))
        self.assertEqual(1234, p.buildVersion)
        self.assertEqual(1, p.packetType)

    def testParseSamplePacket0(self):
        f = open(os.path.join(__location__, "packet_0.bin"), 'rb')
        p = Packet.readFrom(f)
        self.assertEqual(TelemetryPacket, p.__class__)
        self.assertEqual(1122, p.buildVersion)
        self.assertEqual(0, p.packetType)
        self.assertEqual(GameSessionState.SESSION_TEST, p.gameSessionState)
        self.assertEqual(0, p.viewedParticipantIndex)
        self.assertEqual(21, p.numParticipants)
