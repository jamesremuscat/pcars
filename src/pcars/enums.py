from enum import Enum


class SessionState(Enum):
    SESSION_INVALID = 0
    SESSION_PRACTICE = 1
    SESSION_TEST = 2
    SESSION_QUALIFY = 3
    SESSION_FORMATION_LAP = 4
    SESSION_RACE = 5
    SESSION_TIME_ATTACK = 6


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
