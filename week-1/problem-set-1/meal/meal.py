def main():
    # prompts the user for time
    time = input("What time is it? ")

    # converts time into its corresponding number of hours as a float
    number_of_hours = convert(time)

    # tells what to eat based on number_of_hours
    meal = meal_time(number_of_hours)

    # checks if it isn't time for any meal
    if meal == None:
        return 1

    # outputs the meal
    print(meal)


def convert(time: str):
    # splits the time into hours and left
    hour, minute = time.split(":")

    if "a.m." in minute or "p.m." in minute:
        minute, part_time = minute.split(" ")

        # returns the float proporcional to the 12h time
        if "p.m." in part_time:
            return (int(hour) + 12) + (int(minute) / 60)

    # returns the float proporcional to the 24h time
    return int(hour) + (int(minute) / 60)


def meal_time(number_of_hours: float):
    if 7 <= number_of_hours <= 8:
        return "breakfast time"
    if 12 <= number_of_hours <= 13:
        return "lunch time"
    if 18 <= number_of_hours <= 19:
        return "dinner time"

    return None


if __name__ == "__main__":
    main()
