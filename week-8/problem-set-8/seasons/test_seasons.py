from seasons import check_date, minutes_to_words


def test_check_date():
    assert check_date("2003-02-21") == True


def test_minutes_to_words():
    assert minutes_to_words(
        11386627) == "Eleven million, three hundred eighty-six thousand, six hundred twenty-seven minutes"
