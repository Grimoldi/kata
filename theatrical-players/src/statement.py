import math
from typing import Any

import src.models as m


def statement(
    invoice: dict[str, Any],
    plays: dict[str, Any],
    output: m.OutputType = m.OutputType.PLAIN,
):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        audience = perf["audience"]
        play_type = play["type"]
        play_name = play["name"]

        this_amount = _get_play_amount(play_type, audience)
        total_amount += this_amount
        volume_credits += _get_credit(play_type, audience)

        # print line for this order
        result += (
            f" {play_name}: {format_as_dollars(this_amount/100)} ({audience} seats)\n"
        )

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


def _get_play_amount(play_type: str, audience: int) -> float:
    """Gets the billed amount by play type."""
    amount_calculator = PLAY_MAPPING.get(play_type)
    if amount_calculator is None:
        raise ValueError(f"unknown type: {play_type}")

    return amount_calculator(audience)


def _get_comedy_amount(audience: int) -> float:
    this_amount = 300_00
    if audience > 20:
        this_amount += 100_00 + 5_00 * (audience - 20)
    this_amount += 3_00 * audience
    return this_amount


def _get_history_amount(audience: int) -> float:
    this_amount = 500_00
    if audience > 40:
        this_amount += 120_00 + 4_00 * (audience - 40)

    this_amount += 3_00 * audience
    return this_amount


def _get_pastoral_amount(audience: int) -> float:
    this_amount = 250_00
    if audience > 15:
        this_amount += 5_00 * (audience - 15)

    return this_amount


def _get_tragedy_amount(audience: int) -> float:
    this_amount = 400_00
    if audience > 30:
        this_amount += 10_00 * (audience - 30)

    return this_amount


def _get_credit(play_type: str, audience: int) -> float:
    """Add volume credits."""
    volume_credits = _get_volume_credits(audience)
    if play_type == "comedy":
        volume_credits += _get_comedy_credit_increment(audience)
    return volume_credits


def _get_volume_credits(audience: int) -> float:
    return max(audience - 30, 0)


def _get_comedy_credit_increment(audience: int) -> float:
    """Add extra credit for every ten comedy attendees."""
    return math.floor(audience / 5)


PLAY_MAPPING = {
    "comedy": _get_comedy_amount,
    "history": _get_history_amount,
    "pastoral": _get_pastoral_amount,
    "tragedy": _get_tragedy_amount,
}
