import json

import pytest
from approval_utilities.utils import get_adjacent_file
from approvaltests import verify
from statement import statement  # type: ignore


def test_example_statement():
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays))
