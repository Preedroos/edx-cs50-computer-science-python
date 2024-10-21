from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == True


def test_deposit_full():
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.deposit(11)


def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    assert jar.withdraw(1) == True


def test_withdraw_empty():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(1)
