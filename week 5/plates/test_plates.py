from plates import is_valid

def test_1():
    assert is_valid("98563") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
    assert is_valid("ECTO88") == True
    assert is_valid("AAAAABBAAAAA") == False
    assert is_valid("0ABCDEH") == False
    assert is_valid("AER0236") == False


def test_2():
    assert is_valid("AABC93") == True
    assert is_valid("OUTATIME") == False
    assert is_valid("M") == False
    assert is_valid("AS923G") == False
    assert is_valid("AWBY!H23") == False


if __name__ == "__main__":
    main()
