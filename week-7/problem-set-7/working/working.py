import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Check if the input is in 12-hour format
    match = re.match(
        r"^(([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)) to (([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM))$", s)

    try:
        # If the input is not in 12-hour format, raise a ValueError
        if not match:
            raise ValueError

        # If the input is in 12-hour format, convert it to 24-hour format
        else:
            return f"{convert_to_24h(match.group(1))} to {convert_to_24h(match.group(5))}"
    except ValueError:
        raise ValueError()


def convert_to_24h(time_12h):
    # Split the time into the time part and the AM/PM part
    time_part, period = time_12h.split()  # e.g., "02:30", "PM"

    if ":" not in time_part:
        time_part = time_part + ":00"

    # Split the time into hours and minutes
    hour, minute = time_part.split(":")  # e.g., "02", "30"
    hour = int(hour)  # Convert hour to integer

    # Convert hour based on AM or PM
    if period == "PM" and hour != 12:
        hour += 12  # Convert PM hours to 24-hour format, except for 12 PM
    elif period == "AM" and hour == 12:
        hour = 0  # Convert 12 AM to 00 hours (midnight)

    # Return the time in 24-hour format as a string
    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()
