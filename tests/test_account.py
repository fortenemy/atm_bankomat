import pathlib
import sys

import pytest

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from atm import Account


def test_deposit_increases_balance():
    acc = Account('Alice', 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw_decreases_balance_when_sufficient():
    acc = Account('Bob', 200)
    acc.withdraw(70)
    assert acc.balance == 130


def test_withdraw_too_much_leaves_balance_unchanged():
    acc = Account('Carol', 50)
    acc.withdraw(70)
    assert acc.balance == 50
