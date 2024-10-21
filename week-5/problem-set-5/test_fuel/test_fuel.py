import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("three/four")


def test_convert():
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
