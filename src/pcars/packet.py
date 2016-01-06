import struct


class Packet(object):

    def __init__(self):
        self.buildVersion = -1
        self.sequenceNumber = -1
        self.packetType = -1

    @staticmethod
    def readFrom(buf):
        buildVersion, packetType = struct.unpack_from('HB', buf)
        p = Packet()
        p.buildVersion = buildVersion
        p.sequenceNumber = packetType & 0xFC
        p.packetType = packetType & 0x3
        return p
