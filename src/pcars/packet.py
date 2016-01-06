from pcars.enums import GameState, SessionState, Tyres
import binio


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
        sequenceNumber = (header['seq_packet'] & 0xFC) >> 2
        packetType = header['seq_packet'] & 0x3
        pClass = PACKET_TYPES.get(packetType, Packet)
        return pClass(buildVersion, sequenceNumber, packetType, buf)


class TelemetryPacket(Packet):

    STRUCTURE = binio.new([
        (1, binio.types.t_u8, "gameSessionState"),
        (1, binio.types.t_int8, "viewedParticipantIndex"),
        (1, binio.types.t_int8, "numParticipants"),
        # Unfiltered input
        (1, binio.types.t_u8, "unfilteredThrottle"),
        (1, binio.types.t_u8, "unfilteredBrake"),
        (1, binio.types.t_int8, "unfilteredSteering"),
        (1, binio.types.t_u8, "unfilteredClutch"),
        # ?
        (1, binio.types.t_u8, "raceStateFlags"),
        (1, binio.types.t_u8, "lapsInEvent"),
        # Timing info
        (1, binio.types.t_float32, "bestLapTime"),
        (1, binio.types.t_float32, "lastLapTime"),
        (1, binio.types.t_float32, "currentTime"),
        (1, binio.types.t_float32, "splitTimeAhead"),
        (1, binio.types.t_float32, "splitTimeBehind"),
        (1, binio.types.t_float32, "splitTime"),
        (1, binio.types.t_float32, "eventTimeRemaining"),
        (1, binio.types.t_float32, "personalFastestLapTime"),
        (1, binio.types.t_float32, "worldFastestLapTime"),
        (1, binio.types.t_float32, "currentSector1Time"),
        (1, binio.types.t_float32, "currentSector2Time"),
        (1, binio.types.t_float32, "currentSector3Time"),
        (1, binio.types.t_float32, "fastestSector1Time"),
        (1, binio.types.t_float32, "fastestSector2Time"),
        (1, binio.types.t_float32, "fastestSector3Time"),
        (1, binio.types.t_float32, "personalFastestSector1Time"),
        (1, binio.types.t_float32, "personalFastestSector2Time"),
        (1, binio.types.t_float32, "personalFastestSector3Time"),
        (1, binio.types.t_float32, "worldFastestSector1Time"),
        (1, binio.types.t_float32, "worldFastestSector2Time"),
        (1, binio.types.t_float32, "worldFastestSector3Time"),
        # Joypad state?
        (1, binio.types.t_u16, "joyPad"),
        # Flags
        (1, binio.types.t_u8, "highestFlag"),
        # Pit schedule
        (1, binio.types.t_u8, "pitModeSchedule"),
        # Car state
        (1, binio.types.t_int16, "oilTempCelsius"),
        (1, binio.types.t_u16, "oilPressureKPa"),
        (1, binio.types.t_int16, "waterTempCelsius"),
        (1, binio.types.t_u16, "waterPressureKPa"),
        (1, binio.types.t_u16, "fuelPressureKPa"),
        (1, binio.types.t_u8, "carFlags"),
        (1, binio.types.t_u8, "fuelCapacity"),
        (1, binio.types.t_u8, "brake"),
        (1, binio.types.t_u8, "throttle"),
        (1, binio.types.t_u8, "clutch"),
        (1, binio.types.t_int8, "steering"),
        (1, binio.types.t_float32, "fuelLevel"),
        (1, binio.types.t_float32, "speed"),
        (1, binio.types.t_u16, "rpm"),
        (1, binio.types.t_u16, "maxRpm"),
        (1, binio.types.t_u8, "gearNumGears"),
        (1, binio.types.t_u8, "boostAmount"),
        (1, binio.types.t_int8, "enforcedPitStopLap"),
        (1, binio.types.t_u8, "crashState"),
        # Motion and device
        (1, binio.types.t_float32, "odometerKM"),
        (1, binio.types.t_float32, "orientationX"),
        (1, binio.types.t_float32, "orientationY"),
        (1, binio.types.t_float32, "orientationZ"),
        (1, binio.types.t_float32, "localVelocityX"),
        (1, binio.types.t_float32, "localVelocityY"),
        (1, binio.types.t_float32, "localVelocityZ"),
        (1, binio.types.t_float32, "worldVelocityX"),
        (1, binio.types.t_float32, "worldVelocityY"),
        (1, binio.types.t_float32, "worldVelocityZ"),
        (1, binio.types.t_float32, "angularVelocityX"),
        (1, binio.types.t_float32, "angularVelocityY"),
        (1, binio.types.t_float32, "angularVelocityZ"),
        (1, binio.types.t_float32, "localAccelerationX"),
        (1, binio.types.t_float32, "localAccelerationY"),
        (1, binio.types.t_float32, "localAccelerationZ"),
        (1, binio.types.t_float32, "worldAccelerationX"),
        (1, binio.types.t_float32, "worldAccelerationY"),
        (1, binio.types.t_float32, "worldAccelerationZ"),
        (1, binio.types.t_float32, "extentsCentreX"),
        (1, binio.types.t_float32, "extentsCentreY"),
        (1, binio.types.t_float32, "extentsCentreZ"),
    ])

    TYRES_STRUCTURE = [  # This is a list of binio typedefs - each is repeated for each tyre before the next.
        (1, binio.types.t_u8, "tyreFlags"),
    ]

    def __init__(self, buildVersion, sequenceNumber, packetType, buf):
        super(TelemetryPacket, self).__init__(buildVersion, sequenceNumber, packetType, buf)  # everything up to tyre information
        self.tyres = [{}, {}, {}, {}]

        for datapoint in TelemetryPacket.TYRES_STRUCTURE:
            self.forEachTyre(datapoint, buf)

    def forEachTyre(self, datapoint, buf):
        thisField = binio.new([datapoint])
        for i in Tyres:
            self.tyres[i.value][datapoint[2]] = thisField.read_dict(buf)[datapoint[2]]

    @property
    def gameState(self):
        return GameState(self.data["gameSessionState"] & 0x07)

    @property
    def sessionState(self):
        return SessionState((self.data["gameSessionState"] & 0x38) >> 2)

    @property
    def currentGear(self):
        return self.data['gearNumGears'] & 0x0F

    @property
    def numGears(self):
        return (self.data['gearNumGears'] & 0xF0) >> 4

    def getValue(self, key):
        return self.data[key]

PACKET_TYPES = {
    0: TelemetryPacket
}
