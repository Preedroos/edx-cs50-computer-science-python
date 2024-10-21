from bank import value


def test_lower():
    assert value("hello") == 0


def test_upper():
    assert value("HELLO") == 0


def test_number():
    assert value("0") == 100


def test_ponctuation():
    assert value("!") == 100


def test_first_letter():
    assert value("how's it going") == 20


def test_hello_in_phrase():
    assert value("Hello, Pedro") == 0
