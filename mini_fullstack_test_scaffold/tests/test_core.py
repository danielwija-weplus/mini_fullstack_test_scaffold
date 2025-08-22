import pytest
from app.core import total_paid_by_user, top_user_by_paid_amount, to_snake_case

TXNS = [
  {"user": "anna", "amount": 12000, "status": "PAID"},
  {"user": "budi", "amount": 8000,  "status": "PENDING"},
  {"user": "anna", "amount": 3000,  "status": "PAID"},
  {"user": "cici", "amount": 15000, "status": "PAID"},
  {"user": "budi", "amount": 7000,  "status": "FAILED"}
]

def test_total_paid_by_user():
    # Expected: anna=15000, cici=15000
    out = total_paid_by_user(TXNS)
    assert out == {"anna": 15000, "cici": 15000}

def test_top_user_by_paid_amount_basic():
    user, total = top_user_by_paid_amount(TXNS)
    # anna dan cici sama-sama 15000 -> ambil alfabetis terkecil: 'anna'
    assert (user, total) == ("anna", 15000)

@pytest.mark.parametrize("src,expected", [
    ("HelloWorld", "hello_world"),
    ("already_snake_case", "already_snake_case"),
    ("mixed-Case Label", "mixed_case_label"),
])
def test_to_snake_case(src, expected):
    assert to_snake_case(src) == expected
