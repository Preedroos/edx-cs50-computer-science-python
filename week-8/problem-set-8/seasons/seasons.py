import inflect
import datetime
import re
import sys


def main():
    birthdate = input("Date of Birth: ")

    # Check if the date is valid
    if check_date(birthdate):

        # Convert a date to minutes from now
        minutes = date_to_minutes(birthdate)

        # Prints the minutes in a human readable format
        print(minutes_to_words(minutes))


def check_date(date):
    try:
        # Check if the date is a valid date
        birthdate = datetime.date.fromisoformat(date)

        return True
    except ValueError:
        sys.exit(1)


def date_to_minutes(date):

    # Parses the date to a datetime object
    birthdate = datetime.date.fromisoformat(date)

    # Gets the current date
    today = datetime.date.today()

    # Calculates the minutes between the two dates
    minutes = int((today - birthdate).total_seconds() / 60)

    return minutes


def minutes_to_words(minutes):
    p = inflect.engine()
    # Converts the minutes to a human readable format
    words = p.number_to_words(minutes, andword="").capitalize() + " minutes"

    return words


if __name__ == '__main__':
    main()
