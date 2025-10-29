import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(2, 1) == 1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
