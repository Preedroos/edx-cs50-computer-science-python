from plates import is_valid


def test_no_only_numeric():
    assert is_valid("111") == False


def test_no_middle_numeric():
    assert is_valid("AA11BB") == False


def test_no_ponctuations():
    assert is_valid("AA.33") == False


def test_plate_length():
    assert is_valid("A") == False
    assert is_valid("2") == False
    assert is_valid("AAAA222") == False


def test_no_zero_first():
    assert is_valid("AAA012") == False
