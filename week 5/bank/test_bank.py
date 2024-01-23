from bank import value

def test_1():
    assert value("Hello how are you ?") == 0
    assert value("hello, boy") == 0
    assert value("HELLO, man") == 0

def test_2():
    assert value("Hey there") == 20
    assert value("hi baby") == 20

def test_3():
    assert value("ali") == 100
    assert value("Ali Ensafdoust") == 100


if __name__ == "__main__":
    main()
