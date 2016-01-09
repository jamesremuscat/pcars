from pcars.enums import GameState, SessionState, RaceState, Tyres, FlagColour, FlagReason,\
    Sector, PitMode, PitSchedule
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

    TYRES_STRUCTURE = [  # This is a list of binio typedefs - each is repeated for each wheel before the next typedef.
        (1, binio.types.t_u8, "tyreFlags"),
        (1, binio.types.t_u8, "terrain"),
        (1, binio.types.t_float32, "tyreY"),
        (1, binio.types.t_float32, "tyreRPS"),
        (1, binio.types.t_float32, "tyreSlipSpeed"),
        (1, binio.types.t_u8, "tyreTemp"),
        (1, binio.types.t_u8, "tyreGrip"),
        (1, binio.types.t_float32, "tyreHeightAboveGround"),
        (1, binio.types.t_float32, "tyreLateralStiffness"),
        (1, binio.types.t_u8, "tyreWear"),
        (1, binio.types.t_u8, "brakeDamage"),
        (1, binio.types.t_u8, "suspensionDamage"),
        (1, binio.types.t_int16, "brakeTempCelsius"),
        (1, binio.types.t_u16, "tyreTreadTemp"),
        (1, binio.types.t_u16, "tyreLayerTemp"),
        (1, binio.types.t_u16, "tyreCarcassTemp"),
        (1, binio.types.t_u16, "tyreRimTemp"),
        (1, binio.types.t_u16, "tyreInternalAirTemp"),
        (1, binio.types.t_float32, "wheelLocalPositionY"),
        (1, binio.types.t_float32, "rideHeight"),
        (1, binio.types.t_float32, "suspensionTravel"),
        (1, binio.types.t_float32, "suspensionVelocity"),
        (1, binio.types.t_u16, "airPressure"),
    ]

    EXTRAS_WEATHER_STRUCTURE = binio.new([
        (1, binio.types.t_float32, "engineSpeed"),
        (1, binio.types.t_float32, "engineTorque"),
        (1, binio.types.t_u8, "aeroDamage"),
        (1, binio.types.t_u8, "engineDamage"),
        (1, binio.types.t_int8, "ambientTemperature"),
        (1, binio.types.t_int8, "trackTemperature"),
        (1, binio.types.t_u8, "rainDensity"),
        (1, binio.types.t_int8, "windSpeed"),
        (1, binio.types.t_int8, "windDirectionX"),
        (1, binio.types.t_int8, "windDirectionY"),
    ])

    PARTICIPANT_INFO_STRUCTURE = binio.new([
        (1, binio.types.t_int16, "worldPositionX"),
        (1, binio.types.t_int16, "worldPositionY"),
        (1, binio.types.t_int16, "worldPositionZ"),
        (1, binio.types.t_u16, "currentLapDistance"),
        (1, binio.types.t_u8, "racePosition"),
        (1, binio.types.t_u8, "lapsCompleted"),
        (1, binio.types.t_u8, "currentLap"),
        (1, binio.types.t_u8, "sector"),
        (1, binio.types.t_float32, "lastSectorTime"),
    ])

    EPILOGUE_STRUCTURE = binio.new([
        (1, binio.types.t_float32, "trackLength"),
        (1, binio.types.t_u8, "wings1"),
        (1, binio.types.t_u8, "wings2"),
        (1, binio.types.t_u8, "dPad"),
        #(1, binio.types.t_u16, "padding")
    ])

    def __init__(self, buildVersion, sequenceNumber, packetType, buf):
        super(TelemetryPacket, self).__init__(buildVersion, sequenceNumber, packetType, buf)  # everything up to tyre information
        self.tyres = [{}, {}, {}, {}]

        for datapoint in TelemetryPacket.TYRES_STRUCTURE:
            self.forEachTyre(datapoint, buf)

        self.data.update(TelemetryPacket.EXTRAS_WEATHER_STRUCTURE.read_dict(buf))

        self.participants = []

        for _ in range(0, 56):
            p = TelemetryPacket.PARTICIPANT_INFO_STRUCTURE.read_dict(buf)
            # Unpack some data within
            p["isActive"] = (p["racePosition"] & 0x80) >> 7
            p["racePosition"] = p["racePosition"] & 0x7F

            p["lapInvalidated"] = (p["lapsCompleted"] & 0x80) >> 7
            p["lapsCompleted"] = p["lapsCompleted"] & 0x7F

            p["classSameAsPlayer"] = (p["sector"] & 0x08) > 0
            p["sector"] = Sector(p["sector"] & 0x07)

            self.participants.append(p)

        self.data.update(TelemetryPacket.EPILOGUE_STRUCTURE.read_dict(buf))

        # Unpack data
        self.data["gameState"] = GameState(self.data["gameSessionState"] & 0x07)
        self.data["sessionState"] = SessionState((self.data["gameSessionState"] & 0x38) >> 2)

        self.data["raceState"] = RaceState(self.data["raceStateFlags"] & 0x7)
        self.data["lapInvalidated"] = (self.data["raceStateFlags"] & 8) > 0
        self.data["antiLockActive"] = (self.data["raceStateFlags"] & 16) > 0
        self.data["boostActive"] = (self.data["raceStateFlags"] & 32) > 0

        self.data["gear"] = self.data['gearNumGears'] & 0x0F
        self.data["numGears"] = (self.data['gearNumGears'] & 0xF0) >> 4

        self.data["pitMode"] = PitMode(self.data["pitModeSchedule"] & 0x07)
        self.data["pitSchedule"] = PitSchedule((self.data["pitModeSchedule"] & 0xF0) << 4)

        self.data["highestFlagColour"] = FlagColour(self.data["highestFlag"] & 0x7)
        self.data["highestFlagReason"] = FlagReason((self.data["highestFlag"] & 0xF0) << 4)

    def forEachTyre(self, datapoint, buf):
        thisField = binio.new([datapoint])
        for i in Tyres:
            self.tyres[i.value][datapoint[2]] = thisField.read_dict(buf)[datapoint[2]]

    def getValue(self, key):
        return self.data[key]

PACKET_TYPES = {
    0: TelemetryPacket
}
