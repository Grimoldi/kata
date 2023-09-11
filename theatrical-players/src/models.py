from dataclasses import dataclass
from enum import StrEnum, auto


class PlayType(StrEnum):
    """Enumeration for play category."""

    COMEDY = auto()
    HISTORY = auto()
    PASTORAL = auto()
    TRAGEDY = auto()


class OutputType(StrEnum):
    """Enumeration for output type."""

    HTML = auto()
    PLAIN = auto()


@dataclass
class Performance:
    """Dataclass for a single performance."""

    _id: str
    name: str
    typology: PlayType


@dataclass
class Invoice:
    """Dataclass for a single invoice."""

    customer: str
    audience: int

    performance_id: str
