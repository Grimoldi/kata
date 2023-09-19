import json

import pytest
import src.models as m
from approval_utilities.utils import get_adjacent_file
from approvaltests import verify
from src.statement import statement


def test_statement_with_new_play_types():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays))


def test_statement_with_new_play_types_as_html():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays, m.OutputType.HTML))
