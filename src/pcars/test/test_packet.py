from pcars.enums import GameState, SessionState, RaceState, TyreFlags, FlagColour,\
    Sector
from pcars.packet import Packet, TelemetryPacket
from StringIO import StringIO
from unittest import TestCase
import os

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
        self.assertEqual(0, p.sequenceNumber)
        self.assertEqual(SessionState.FORMATION_LAP, p.getValue("sessionState"))
        self.assertEqual(GameState.INGAME_PLAYING, p.getValue("gameState"))
        self.assertEqual(0, p.getValue("viewedParticipantIndex"))
        self.assertEqual(21, p.getValue("numParticipants"))

        self.assertEqual(0, p.getValue("gear"))
        self.assertEqual(6, p.getValue("numGears"))

        self.assertEqual(TyreFlags.ATTACHED + TyreFlags.INFLATED + TyreFlags.IS_ON_GROUND, p.tyres[0]["tyreFlags"])
        self.assertEqual(0.0, p.tyres[1]["tyreRPS"])  # Hmm, we're stopped in the test data!
        self.assertEqual(729, p.tyres[2]["brakeTempCelsius"])
        self.assertAlmostEqual(0.06453919, p.tyres[3]["rideHeight"], 8)

        self.assertEqual(15, p.data["ambientTemperature"])

        participant0 = p.participants[0]
        self.assertEqual(0, participant0["currentLapDistance"])
        self.assertEqual(1, participant0["racePosition"])
        self.assertEqual(-123.0, participant0["lastSectorTime"])
        self.assertEqual(False, participant0["classSameAsPlayer"])
        self.assertEqual(Sector.SECTOR_2, participant0["sector"])

        self.assertAlmostEqual(3890.4072, p.data["trackLength"], 4)

        self.assertEqual(RaceState.NOT_STARTED, p.data["raceState"])
        self.assertEqual(FlagColour.NONE, p.data["highestFlagColour"])
