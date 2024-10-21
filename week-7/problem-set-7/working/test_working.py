import working
import pytest


def test_convert():
    assert working.convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_to_omitted():
    with pytest.raises(ValueError):
        working.convert("7 AM 8 PM")


def test_time_range():
    with pytest.raises(ValueError):
        working.convert("13:00 PM to 12:00 AM")
