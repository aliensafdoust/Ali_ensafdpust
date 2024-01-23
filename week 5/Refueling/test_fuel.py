from fuel import convert, gauge

def test_1():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_2():
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"



if __name__ == "__main__":
    main()
