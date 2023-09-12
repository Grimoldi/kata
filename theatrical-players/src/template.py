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
    def result(self) -> str:
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
    def result(self) -> str:
        """Returns the bill."""
        return self._result


class HtmlTemplate:
    """Class to export the results as HTML."""

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
    def result(self) -> str:
        """Returns the bill."""
        ...
