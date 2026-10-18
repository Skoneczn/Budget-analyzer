import pytest

from budget import categorize_transaction
from budget import categories


@pytest.mark.parametrize(
    "description, expected_category",[
        ("ORLEN 1234 WROCLAW",   "Fuel"),
        ("SHELL STACJA 123", "Fuel"),
        ("BIEDRONKA 1234", "Groceries"),
        ("LIDL WROCLAW", "Groceries"),
        ("NETFLIX.COM", "Subscriptions"),
        ("orlen 1234 wroclaw", "Fuel"),
        ("OrLeN STACJA", "Fuel"),
        ("lidl wroclaw", "Groceries"),
        ("Netflix.com", "Subscriptions"),
        ("AMAZON", "Uncategorized"),
        ("", "Uncategorized"),
    ])
def test_categorize_transaction(description, expected_category):
    transaction = {
        "date": "2026-09-03",
        "description": description,
        "amount": -100
    }

    result = categorize_transaction(transaction, categories)
    assert result == expected_category
