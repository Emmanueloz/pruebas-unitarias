import sys
import os
from unittest.mock import patch
from io import StringIO
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import main


def test_integration_add():
    with patch("builtins.input", side_effect=["1", "10", "5", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "10.0 + 5.0 = 15.0" in fake_out.getvalue()


def test_integration_subtract():
    with patch("builtins.input", side_effect=["2", "10", "5", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "10.0 - 5.0 = 5.0" in fake_out.getvalue()


def test_integration_multiply():
    with patch("builtins.input", side_effect=["3", "10", "5", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "10.0 * 5.0 = 50.0" in fake_out.getvalue()


def test_integration_divide():
    with patch("builtins.input", side_effect=["4", "10", "5", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "10.0 / 5.0 = 2.0" in fake_out.getvalue()


def test_integration_divide_by_zero():
    with patch("builtins.input", side_effect=["4", "10", "0", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "Cannot divide by zero" in fake_out.getvalue()


def test_invalid_input():
    with patch("builtins.input", side_effect=["1", "a", "5", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "Invalid input. Please enter a number." in fake_out.getvalue()


def test_invalid_choice():
    with patch("builtins.input", side_effect=["6", "5"]):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            assert "Invalid Input" in fake_out.getvalue()
