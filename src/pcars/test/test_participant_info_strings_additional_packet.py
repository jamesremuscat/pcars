# -*- coding: utf-8 -*-
from pcars.packet import Packet, ParticipantInfoStringsAdditionalPacket
from unittest import TestCase
import os


_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestParticipantInfoStringsAdditionalPacket(TestCase):

    def testParseSamplePacket(self):
        f = open(os.path.join(_location, "ParticipantInfoStringsAdditionalPacket_1.bin"), "rb")
        p = Packet.readFrom(f)
        self.assertEqual(ParticipantInfoStringsAdditionalPacket, p.__class__)

        # Packet Header
        self.assertEqual(1235, p.buildVersion)
        self.assertEqual(2, p.packetType)
        self.assertEqual(32, p.sequenceNumber)

        # Packet Data
        self.assertEqual(32, p["offset"])

        # Participants
        self.assertEqual(16, len(p["participants"]))
        self.assertEqual("Abdullah El Khereiji", p["participants"][0]["name"])

        expect_name = u"Dominic Schönberner"

        self.assertEqual(expect_name, p["participants"][15]["name"])
