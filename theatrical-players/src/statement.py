from pathlib import Path
from typing import Any

import models as m
import template as t
from accountable import get_plugin, load_plugins_from_folder, plugin_exists

ACCOUNTS = Path(__file__).parent / "accountables"


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
    load_plugins_from_folder(str(ACCOUNTS))

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        audience = perf["audience"]
        play_type = m.PlayType(play["type"].lower())
        play_name = play["name"]

        this_amount = _get_play_amount(play_type, audience)
        total_amount += this_amount
        volume_credits += _get_credit(play_type, audience)
        output_template.add_record(play_name, this_amount, audience)

    output_template.add_total(total_amount)
    output_template.add_credits(volume_credits)
    return output_template.bill


def _get_play_amount(play_type: m.PlayType, audience: int) -> float:
    """Gets the billed amount by play type."""
    if not plugin_exists(play_type):
        raise ValueError(f"unknown type: {play_type.title()}")
    accountable = get_plugin(play_type)

    return accountable(audience).amount  # type: ignore


def _get_credit(play_type: m.PlayType, audience: int) -> float:
    """Add volume credits."""
    accountable = get_plugin(play_type)

    return accountable(audience).credit  # type: ignore
