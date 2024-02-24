import pytest
from project import check_length, check_if_number, check_special_characters, check_if_uppercase, check_if_lowercase


def main():
    test_check_length()
    test_check_if_number()
    test_check_special_characters()
    test_check_if_uppercase()
    test_check_if_lowercase()

def test_check_length():

    assert check_length("12345679") == True
    assert check_length("12345678") == True
    assert check_length("1234567") == None


def test_check_if_number():
    assert check_if_number("12345679") == True
    assert check_if_number("1234567a") == True
    assert check_if_number("abcdefgh") == None

def test_check_special_characters():

    assert check_special_characters("12345679") == None
    assert check_special_characters("1234567a") == None
    assert check_special_characters("1234567!") == True
    assert check_special_characters("123A$678") == True

def test_check_if_uppercase():

    assert check_if_uppercase("12345679") == None
    assert check_if_uppercase("1234567a") == None
    assert check_if_uppercase("1234567!") == None
    assert check_if_uppercase("123A$678") == True
    assert check_if_uppercase("123a$678") == None

def test_check_if_lowercase():

    assert check_if_lowercase("12345679") == None
    assert check_if_lowercase("1234567a") == True
    assert check_if_lowercase("1234567!") == None
    assert check_if_lowercase("123A$678") == None
    assert check_if_lowercase("123a$678") == None
    assert check_if_lowercase("123aA$678") == True

if __name__ == "__main__":
    main()