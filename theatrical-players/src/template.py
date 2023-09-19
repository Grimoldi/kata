from typing import Protocol


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


class Template(Protocol):
    """Protocol class for any output template."""

    def __init__(self) -> None:
        ...

    def add_customer(self, customer: str) -> None:
        """Add the customer to the billing."""
        ...

    def add_record(self, play_name: str, amount: float, audience: int) -> None:
        """Add a record to the template."""
        ...

    def add_total(self, amount: float) -> None:
        """Add the total amount to the template."""
        ...

    def add_credits(self, credit: float) -> None:
        """Add credits to the billing."""
        ...

    @property
    def bill(self) -> str:
        """Returns the bill."""
        ...


class RawTextTemplate:
    """Class to export the results as raw text."""

    def __init__(self) -> None:
        self._result = ""

    def add_customer(self, customer: str) -> None:
        """Add the customer to the billing."""
        self._result += f"Statement for {customer}\n"

    def add_record(self, play_name: str, amount: float, audience: int) -> None:
        """Add a record to the template."""
        self._result += (
            f" {play_name}: {format_as_dollars(amount/100)} ({audience} seats)\n"
        )

    def add_total(self, amount: float) -> None:
        """Add the total amount to the template."""
        self._result += f"Amount owed is {format_as_dollars(amount/100)}\n"

    def add_credits(self, credit: float) -> None:
        """Add credits to the billing."""
        self._result += f"You earned {credit} credits\n"

    @property
    def bill(self) -> str:
        """Returns the bill."""
        return self._result


class HtmlTemplate:
    """Class to export the results as HTML."""

    def __init__(self) -> None:
        self._customer = ""
        self._records = list()
        self._total = 0.0
        self._credit = 0.0

    def add_customer(self, customer: str) -> None:
        """Add the customer to the billing."""
        self._customer = customer

    def add_record(self, play_name: str, amount: float, audience: int) -> None:
        """Add a record to the template."""
        self._records.append((play_name, format_as_dollars(amount / 100), audience))

    def add_total(self, amount: float) -> None:
        """Add the total amount to the template."""
        self._total = amount

    def add_credits(self, credit: float) -> None:
        """Add credits to the billing."""
        self._credit = credit

    @property
    def bill(self) -> str:
        """Returns the bill."""
        content_rows = ""
        for record in self._records:
            content_rows += (
                "\n\t\t\t<tr>"
                f"<td>{record[0]}</td>"
                f"<td>{record[1]}</td>"
                f"<td>{record[2]} seats"
                "</tr>"
            )
        return (
            "<html>"
            "\n\t<style>"
            "\n\t\tth, td {"
            "\n\t\t\tpadding: 15px;"
            "\n\t\t}"
            "\n\t</style>"
            "\n\t<body>"
            "\n\t\t<table border=1>"
            f'\n\t\t\t<tr><td colspan=3><p align="right">{self._customer}</td></tr>'
            f"{content_rows}"
            f"\n\t\t\t<tr><td colspan=3>Amount owed is <font color=orange>{format_as_dollars(self._total/100)}</font>.</td></tr>"
            f"\n\t\t\t<tr><td colspan=3>You earned <font color=green>{self._credit} credits</font>.</td></tr>"
            "\n\t\t</table>"
            "\n\t</body>"
            "\n</html>"
        )
