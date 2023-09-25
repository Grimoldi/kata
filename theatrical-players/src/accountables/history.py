from dataclasses import dataclass

from models import PlayType


def get_play_accountable_name() -> PlayType:
    return PlayType.HISTORY


@dataclass
class History:
    audience: int
    base_price: float = 500_00
    threshold: int = 40
    increment: float = 4_00
    supplement: float = 120_00
    quota: float = 3_00
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
