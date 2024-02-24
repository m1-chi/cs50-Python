from working import convert
import pytest


def test_correct_time():
    assert convert("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert convert("12:00 AM to 1 PM") == "00:00 to 13:00"
    assert convert("1 PM to 12:00 AM") == "13:00 to 00:00"


def test_valueerror():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 PM to 14 AM")