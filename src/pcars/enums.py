from enum import Enum, IntEnum


class SessionState(Enum):
    INVALID = 0
    PRACTICE = 1
    TEST = 2
    QUALIFY = 3
    FORMATION_LAP = 4
    RACE = 5
    TIME_ATTACK = 6


class GameState(Enum):
    EXITED = 0
    FRONT_END = 1
    INGAME_PLAYING = 2
    INGAME_PAUSED = 3
    INGAME_RESTARTING = 4
    INGAME_REPLAYING = 5


class RaceState(Enum):
    INVALID = 0
    NOT_STARTED = 1
    RACING = 2
    FINISHED = 3
    DISQUALIFIED = 4
    RETIRED = 5
    DNF = 6


class Sector(Enum):
    INVALID = 0
    START = 1
    SECTOR_1 = 2
    SECTOR_2 = 3
    FINISH = 4
    STOP = 5


class FlagColour(Enum):
    NONE = 0           # Not used for actual flags, only for some query functions
    GREEN = 1          # End of danger zone, or race started
    BLUE = 2           # Faster car wants to overtake the participant
    WHITE = 3          # Approaching a slow car
    YELLOW = 4         # Danger on the racing surface itself
    DOUBLE_YELLOW = 5  # Danger that wholly or partly blocks the racing surface
    BLACK = 6          # Participant disqualified
    CHEQUERED = 7      # Chequered flag


class FlagReason(Enum):
    NONE = 0
    SOLO_CRASH = 1
    VEHICLE_CRASH = 2
    VEHICLE_OBSTRUCTION = 3


class PitMode(Enum):
    NONE = 0
    DRIVING_INTO_PITS = 1
    IN_PIT = 2
    DRIVING_OUT_OF_PITS = 3
    IN_GARAGE = 4


class PitSchedule(Enum):
    NONE = 0
    STANDARD = 1
    DRIVE_THROUGH = 2
    STOP_GO = 3


class CarFlags(Enum):
    HEADLIGHT = 1
    ENGINE_ACTIVE = 2
    ENGINE_WARNING = 4
    SPEED_LIMITER = 8
    ABS = 16
    HANDBRAKE = 32


class Tyres(Enum):
    FRONT_LEFT = 0
    FRONT_RIGHT = 1
    REAR_LEFT = 2
    REAR_RIGHT = 3


class TyreFlags(IntEnum):
    ATTACHED = 1
    INFLATED = 2
    IS_ON_GROUND = 4


class Terrain(Enum):
    TERRAIN_ROAD = 0
    TERRAIN_LOW_GRIP_ROAD = 1
    TERRAIN_BUMPY_ROAD1 = 2
    TERRAIN_BUMPY_ROAD2 = 3
    TERRAIN_BUMPY_ROAD3 = 4
    TERRAIN_MARBLES = 5
    TERRAIN_GRASSY_BERMS = 6
    TERRAIN_GRASS = 7
    TERRAIN_GRAVEL = 8
    TERRAIN_BUMPY_GRAVEL = 9
    TERRAIN_RUMBLE_STRIPS = 10
    TERRAIN_DRAINS = 11
    TERRAIN_TYREWALLS = 12
    TERRAIN_CEMENTWALLS = 13
    TERRAIN_GUARDRAILS = 14
    TERRAIN_SAND = 15
    TERRAIN_BUMPY_SAND = 16
    TERRAIN_DIRT = 17
    TERRAIN_BUMPY_DIRT = 18
    TERRAIN_DIRT_ROAD = 19
    TERRAIN_BUMPY_DIRT_ROAD = 20
    TERRAIN_PAVEMENT = 21
    TERRAIN_DIRT_BANK = 22
    TERRAIN_WOOD = 23
    TERRAIN_DRY_VERGE = 24
    TERRAIN_EXIT_RUMBLE_STRIPS = 25
    TERRAIN_GRASSCRETE = 26
    TERRAIN_LONG_GRASS = 27
    TERRAIN_SLOPE_GRASS = 28
    TERRAIN_COBBLES = 29
    TERRAIN_SAND_ROAD = 30
    TERRAIN_BAKED_CLAY = 31
    TERRAIN_ASTROTURF = 32
    TERRAIN_SNOWHALF = 33
    TERRAIN_SNOWFULL = 34
