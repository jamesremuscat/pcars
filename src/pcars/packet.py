import binio


PACKET_HEADER = [
    (1, binio.types.t_u16, "buildVersion"),
    (1, binio.types.t_u8, "seq_packet"),
]


class Packet(object):

    HEADER = binio.new(PACKET_HEADER)

    def __init__(self):
        self.buildVersion = -1
        self.sequenceNumber = -1
        self.packetType = -1

    @staticmethod
    def readFrom(buf):
        header = Packet.HEADER.read_dict(buf)
        p = Packet()
        p.buildVersion = header['buildVersion']
        p.sequenceNumber = header['seq_packet'] & 0xFC
        p.packetType = header['seq_packet'] & 0x3
        return p
