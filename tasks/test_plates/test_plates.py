from plates import is_valid


def test_more_than_two_characters():
    assert is_valid("HELLO") == True

def test_more_than_six_characters():
    assert is_valid("HELLO, WORLD") == False

def test_numbers():
    assert is_valid("CS50") == True

def test_first_number_zero():
    assert is_valid("CS05") == False

def test_not_beginning_with_two_letters():
    assert is_valid("50") == False

def test_less_two_characters():
    assert is_valid("A") == False

def test_punctuation():
    assert is_valid("PI3.14") == False

def test_number_middle():
    assert is_valid("CS50P") == False


if __name__ == "__main__":
    main()