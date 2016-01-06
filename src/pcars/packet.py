import binio
from pcars.enums import GameSessionState


PACKET_HEADER = [
    (1, binio.types.t_u16, "buildVersion"),
    (1, binio.types.t_u8, "seq_packet"),
]


class Packet(object):

    HEADER = binio.new(PACKET_HEADER)

    def __init__(self, buildVersion, sequenceNumber, packetType, buf):
        self.buildVersion = buildVersion
        self.sequenceNumber = sequenceNumber
        self.packetType = packetType
        self.data = {}
        if hasattr(self.__class__, "STRUCTURE"):
            self.data = self.__class__.STRUCTURE.read_dict(buf)

    @staticmethod
    def readFrom(buf):
        header = Packet.HEADER.read_dict(buf)
        buildVersion = header['buildVersion']
        sequenceNumber = header['seq_packet'] & 0xFC
        packetType = header['seq_packet'] & 0x3
        pClass = PACKET_TYPES.get(packetType, Packet)
        return pClass(buildVersion, sequenceNumber, packetType, buf)


class TelemetryPacket(Packet):

    STRUCTURE = binio.new([
        (1, binio.types.t_u8, "gameSessionState"),
        (1, binio.types.t_int8, "viewedParticipantIndex"),
        (1, binio.types.t_int8, "numParticipants"),
    ])

    @property
    def gameSessionState(self):
        return GameSessionState(self.data["gameSessionState"] & 0x0F)

    @property
    def viewedParticipantIndex(self):
        return self.data["viewedParticipantIndex"]

    @property
    def numParticipants(self):
        return self.data["numParticipants"]

PACKET_TYPES = {
    0: TelemetryPacket
}
