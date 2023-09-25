from dataclasses import dataclass

from models import PlayType


def get_play_accountable_name() -> PlayType:
    return PlayType.PASTORAL


@dataclass
class Pastoral:
    audience: int
    base_price: float = 250_00
    threshold: int = 15
    increment: float = 5_00
    supplement: float = 0
    quota: float = 0
    credit_quota: int = 30

    @property
    def credit(self) -> float:
        return max(self.audience - self.credit_quota, 0)

    @property
    def amount(self) -> float:
        this_amount = self.base_price
        if self.audience > self.threshold:
            this_amount += self.supplement + self.increment * (
                self.audience - self.threshold
            )
        this_amount += self.quota * self.audience

        return this_amount
