from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        ja = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    j = Jar(10)
    j.deposit(5)
    assert str(j) == "🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        j.deposit(-1)




def test_withdraw():
    j = Jar(10)
    j.deposit(5)
    j.withdraw(2)
    assert str(j) == "🍪🍪🍪"

    with pytest.raises(ValueError):
        j.withdraw(10)

