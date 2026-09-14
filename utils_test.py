import pytest
from utils import reversed, formatter


def test_reversed_string():
    with pytest.raises((TypeError, ValueError)):
        reversed("12345")


def test_reversed_float():
    with pytest.raises((TypeError, ValueError)):
        reversed(123.45)


def test_reversed_integer():
    assert reversed(12345) == 54321


def test_formatter_string():
    with pytest.raises((TypeError, ValueError)):
        formatter("10")


def test_formatter_float():
    with pytest.raises((TypeError, ValueError)):
        formatter(10.5)


def test_formatter_integer():
    assert formatter(10) == ("0b1010", "0o12")