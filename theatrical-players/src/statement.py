import math
from typing import Any


def statement(invoice: dict[str, Any], plays: dict[str, Any]):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]

        this_amount = _get_play_amount(play["type"], perf["audience"])

        volume_credits += _get_credit(play["type"], perf["audience"])

        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


def _get_play_amount(play_type: str, audience: int) -> float:
    """Gets the billed amount by play type."""
    if play_type == "tragedy":
        this_amount = _get_tragedy_amount(audience)
    elif play_type == "comedy":
        this_amount = _get_comedy_amount(audience)
    else:
        raise ValueError(f"unknown type: {play_type}")

    return this_amount


def _get_tragedy_amount(audience: int) -> float:
    this_amount = 40_000
    if audience > 30:
        this_amount += 1_000 * (audience - 30)

    return this_amount


def _get_comedy_amount(audience: int) -> float:
    this_amount = 30_000
    if audience > 20:
        this_amount += 10_000 + 500 * (audience - 20)

    this_amount += 300 * audience
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
