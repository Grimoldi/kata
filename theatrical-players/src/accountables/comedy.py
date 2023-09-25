import math
from dataclasses import dataclass

from models import PlayType


def get_play_accountable_name() -> PlayType:
    return PlayType.COMEDY


@dataclass
class Comedy:
    audience: int
    base_price: float = 300_00
    threshold: int = 20
    increment: float = 5_00
    supplement: float = 100_00
    quota: float = 3_00
    credit_quota: int = 30

    @property
    def credit(self) -> float:
        base = max(self.audience - self.credit_quota, 0)
        increment = math.floor(self.audience / 5)
        return base + increment

    @property
    def amount(self) -> float:
        this_amount = self.base_price
        if self.audience > self.threshold:
            this_amount += self.supplement + self.increment * (
                self.audience - self.threshold
            )
        this_amount += self.quota * self.audience

        return this_amount
