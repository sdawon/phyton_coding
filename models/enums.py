from enum import Enum


class TaskStatus(str, Enum):
    INBOX = "INBOX"
    PLANNED = "PLANNED"
    IN_PROGRESS = "IN_PROGRESS"
    ON_HOLD = "ON_HOLD"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class TaskScope(str, Enum):
    PROJECT = "PROJECT"
    LAB = "LAB"
    COMMON = "COMMON"
    PERSONAL = "PERSONAL"


class WaitStatus(str, Enum):
    WAITING = "WAITING"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"
