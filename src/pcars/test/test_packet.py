from pcars.enums import GameState, SessionState, RaceState, TyreFlags, FlagColour,\
    Sector, PitMode, PitSchedule
from pcars.packet import Packet, TelemetryPacket
from io import BytesIO
from unittest import TestCase
import os


_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestPacket(TestCase):

    def testParsePacketHeader(self):
        p = Packet.readFrom(BytesIO(b"\xd2\x04\x03"))
        self.assertEqual(1234, p.buildVersion)
        self.assertEqual(3, p.packetType)

    def testParseSamplePacket0(self):
        f = open(os.path.join(_location, "packet_0.bin"), "rb")
        p = Packet.readFrom(f)
        self.assertEqual(TelemetryPacket, p.__class__)
        self.assertEqual(1122, p.buildVersion)
        self.assertEqual(0, p.packetType)
        self.assertEqual(0, p.sequenceNumber)
        self.assertEqual(SessionState.RACE, p["sessionState"])
        self.assertEqual(GameState.INGAME_PLAYING, p["gameState"])
        self.assertEqual(0, p["viewedParticipantIndex"])
        self.assertEqual(21, p["numParticipants"])

        self.assertEqual(0, p["gear"])
        self.assertEqual(6, p["numGears"])

        self.assertEqual(PitMode.NONE, p["pitMode"])
        self.assertEqual(PitSchedule.NONE, p["pitSchedule"])

        self.assertEqual(TyreFlags.ATTACHED + TyreFlags.INFLATED + TyreFlags.IS_ON_GROUND, p["tyres"][0]["tyreFlags"])
        self.assertEqual(0.0, p["tyres"][1]["tyreRPS"])  # Hmm, we're stopped in the test data!
        self.assertEqual(729, p["tyres"][2]["brakeTempCelsius"])
        self.assertAlmostEqual(0.06453919, p["tyres"][3]["rideHeight"], 8)

        self.assertEqual(15, p["ambientTemperature"])

        participant0 = p["participants"][0]
        self.assertEqual(0, participant0["currentLapDistance"])
        self.assertEqual(1, participant0["racePosition"])
        self.assertEqual(-123.0, participant0["lastSectorTime"])
        self.assertEqual(False, participant0["classSameAsPlayer"])
        self.assertEqual(Sector.SECTOR_2, participant0["sector"])

        self.assertAlmostEqual(3890.4072, p["trackLength"], 4)

        self.assertEqual(RaceState.NOT_STARTED, p["raceState"])
        self.assertEqual(FlagColour.NONE, p["highestFlagColour"])
