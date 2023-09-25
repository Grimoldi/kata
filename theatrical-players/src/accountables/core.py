from pathlib import Path
from typing import Protocol


def get_play_accountable_name() -> str:
    return Path(__file__).name.split(".")[0].upper()


class PlayAccountable(Protocol):
    audience: int
    base_price: float | None
    threshold: int | None
    increment: float | None
    supplement: float | None
    quota: float | None

    @property
    def credit(self) -> float:
        ...

    @property
    def amount(self) -> float:
        ...
