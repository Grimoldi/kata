import math
from typing import Any

import src.models as m
import src.template as t


def _get_template(output_type: m.OutputType) -> t.Template:
    """From the output type get the proper template."""
    MAPPING = {
        m.OutputType.PLAIN: t.RawTextTemplate,
        m.OutputType.HTML: t.HtmlTemplate,
    }
    template = MAPPING.get(output_type)
    if template is None:
        raise ValueError(
            f"Unknown template type {output_type}.\n"
            f"Please choose between {', '.join([t for t in m.OutputType])}."
        )
    return template()


def statement(
    invoice: dict[str, Any],
    plays: dict[str, Any],
    output: m.OutputType = m.OutputType.PLAIN,
):
    output_template = _get_template(output)
    total_amount = 0
    volume_credits = 0
    output_template.add_customer(invoice["customer"])

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        audience = perf["audience"]
        play_type = play["type"]
        play_name = play["name"]

        this_amount = _get_play_amount(play_type, audience)
        total_amount += this_amount
        volume_credits += _get_credit(play_type, audience)
        output_template.add_record(play_name, this_amount, audience)

    output_template.add_total(total_amount)
    output_template.add_credits(volume_credits)
    return output_template.bill


def _get_play_amount(play_type: str, audience: int) -> float:
    """Gets the billed amount by play type."""
    PLAY_MAPPING = {
        m.PlayType.COMEDY: _get_comedy_amount,
        m.PlayType.HISTORY: _get_history_amount,
        m.PlayType.PASTORAL: _get_pastoral_amount,
        m.PlayType.TRAGEDY: _get_tragedy_amount,
    }
    amount_calculator = PLAY_MAPPING.get(m.PlayType(play_type))
    if amount_calculator is None:
        raise ValueError(f"unknown type: {play_type}")

    return amount_calculator(audience)


def _get_comedy_amount(audience: int) -> float:
    """Get the amount for the comedy play type."""
    THRESHOLD = 20
    this_amount = 300_00
    if audience > THRESHOLD:
        this_amount += 100_00 + 5_00 * (audience - THRESHOLD)
    this_amount += 3_00 * audience
    return this_amount


def _get_history_amount(audience: int) -> float:
    """Get the amount for the history play type."""
    THRESHOLD = 40
    this_amount = 500_00
    if audience > THRESHOLD:
        this_amount += 120_00 + 4_00 * (audience - THRESHOLD)

    this_amount += 3_00 * audience
    return this_amount


def _get_pastoral_amount(audience: int) -> float:
    """Get the amount for the pastoral play type."""
    THRESHOLD = 15
    this_amount = 250_00
    if audience > THRESHOLD:
        this_amount += 5_00 * (audience - THRESHOLD)

    return this_amount


def _get_tragedy_amount(audience: int) -> float:
    """Get the amount for the tragedy play type."""
    THRESHOLD = 30
    this_amount = 400_00
    if audience > THRESHOLD:
        this_amount += 10_00 * (audience - THRESHOLD)

    return this_amount


def _get_credit(play_type: str, audience: int) -> float:
    """Add volume credits."""
    volume_credits = _get_credits_volume(audience)
    if play_type == "comedy":
        volume_credits += _get_comedy_credit_increment(audience)
    return volume_credits


def _get_credits_volume(audience: int) -> float:
    """Get the default credit for audience volume."""
    return max(audience - 30, 0)


def _get_comedy_credit_increment(audience: int) -> float:
    """Add extra credit for every five comedy attendees."""
    return math.floor(audience / 5)
