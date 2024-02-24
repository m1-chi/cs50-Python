from twttr import shorten


def test_lowercase():
    assert shorten("Hello") == "Hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("H.E.L.L,O") == "H..L.L,"

if __name__ == "__main__":
    main()