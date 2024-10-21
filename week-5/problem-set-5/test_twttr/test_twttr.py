from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_number():
    assert shorten("0") == "0"

def test_ponctuation():
    assert shorten("!") == "!"
