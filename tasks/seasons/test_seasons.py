import pytest
from seasons import calculate

def main():
    test()

def test():
    assert calculate("2022-01-20") == "Nine hundred eleven thousand, five hundred twenty minutes"
    assert calculate("2021-01-20") == "One million, four hundred thirty-seven thousand, one hundred twenty minutes"
    with pytest.raises(SystemExit, match="Invalid"):
        calculate("Januar 6th, 1998")



if __name__ == "__main__":
    main()