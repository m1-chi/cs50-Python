from fuel import convert, gauge
import pytest

def test_fraction():
    assert convert("1/2") == 50 and gauge(50) == "50%"


def test_output_E():
    assert convert("1/100") == 1 and gauge(1) == "E"


def test_output_F():
    assert convert("4/4") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")
        
def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")