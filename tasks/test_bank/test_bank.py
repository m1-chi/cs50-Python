from bank import value

def test_hello_lower():
    assert value("hello, there") == 0

def test_hello_upper():
    assert value("Hello, there") == 0

def test_starting_h_lower():
    assert value("hi") == 20

def test_starting_h_upper():
    assert value("Hi") == 20

def test_else_lower():
    assert value("what's up?") == 100

def test_else_upper():
    assert value("What's up?") == 100

def test_numbers():
    assert value("50Hl") == 100


if __name__ == "__main__":
    main()