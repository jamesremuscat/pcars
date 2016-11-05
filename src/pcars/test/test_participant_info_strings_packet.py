from pcars.packet import Packet, ParticipantInfoStringsPacket
from unittest import TestCase
import os


_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestParticipantInfoStringsPacket(TestCase):

    def testParseSamplePacket(self):
        f = open(os.path.join(_location, "ParticipantInfoStringsPacket_1.bin"), "rb")
        p = Packet.readFrom(f)
        self.assertEqual(ParticipantInfoStringsPacket, p.__class__)

        # Packet Header
        self.assertEqual(1235, p.buildVersion)
        self.assertEqual(1, p.packetType)
        self.assertEqual(8, p.sequenceNumber)

        # Packet Data
        self.assertEqual("Mitsubishi Lancer Evolution X FQ400", p["carName"])
        self.assertEqual("Road C1", p["carClassName"])
        self.assertEqual("Cadwell", p["trackLocation"])
        self.assertEqual("Woodland", p["trackVariation"])

        # Participants
        self.assertEqual(16, len(p["participants"]))
        participant0 = p["participants"][0]
        self.assertEqual("Andrew", participant0["name"])
        self.assertAlmostEqual(62.403419494628906, participant0["fastestLapTime"])
