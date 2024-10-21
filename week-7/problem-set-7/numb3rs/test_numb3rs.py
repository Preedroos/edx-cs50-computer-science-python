import pytest
from numb3rs import validate


def test_range():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("123.321.1.1") == False


def test_format():
    assert validate("255.1.1") == False
    assert validate("1.2..3") == False


def test_type():
    assert validate("cat") == False
