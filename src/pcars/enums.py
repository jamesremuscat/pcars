from enum import Enum


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


class Tyres(Enum):
    FRONT_LEFT = 0
    FRONT_RIGHT = 1
    REAR_LEFT = 2
    REAR_RIGHT = 3
