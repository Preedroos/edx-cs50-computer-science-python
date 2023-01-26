def main():
    # prompts the user for the meal price
    dollars = dollars_to_float(input("How much was the meal? "))

    # prompts the user for the tip percentage
    percent = percent_to_float(
        input("What percentage would you like to tip? "))

    # calculates the tip
    tip = dollars * percent

    # prints the tip
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # removes the leading
    d = d.replace("$", "")

    # parse str to float
    d = float(d)

    return d


def percent_to_float(p):
    # removes the trailing
    p = p.replace("%", "")

    # parse percentage to float
    p = float(p) / 100

    return p


main()
