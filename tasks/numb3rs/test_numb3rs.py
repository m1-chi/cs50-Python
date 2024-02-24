from numb3rs import validate


def test_maxthree():
    assert validate("123.123.123.123") == True
    assert validate("1234.1234.1234.1234") == False

def test_minone():
    assert validate("1.1.1.1") == True
    assert validate(".1.1.1") == False

def test_splitbypoint():
    assert validate("1.1.1.1") == True
    assert validate("1_1.1.1") == False

def test_0_255():
    assert validate("255.255.0.0") == True
    assert validate("256.255.0.0") == False
    assert validate("23.256.0.0") == False
    assert validate("23.45.256.0") == False
    assert validate("23.45.25.256") == False

def test_characters():
    assert validate("dog") == False


