import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]

        if play["type"] == "tragedy":
            this_amount = _get_tragedy_amount(perf["audience"])
        elif play["type"] == "comedy":
            this_amount = _get_comedy_amount(perf["audience"])

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf["audience"] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


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
