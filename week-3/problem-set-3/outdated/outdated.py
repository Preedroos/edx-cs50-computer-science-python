MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ")
        try:
            month, day, year = parse_date(date)
            if validate_date(month, day, year):
                print(f"{year}-{month:02}-{day:02}")
                break
        except TypeError:
            pass


def parse_date(date):
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
        elif "," in date:
            month, day, year = date.split(" ")
            month = MONTHS.index(month.capitalize()) + 1
            day = day.replace(",", "")
        else:
            return False

        day = int(day)
        year = int(year)
    except ValueError:
        False

    return month, day, year


def validate_date(month, day, year):
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 0:
            return False

        return True


main()
