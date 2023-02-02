def main():
    # prompts the user for a greeting
    greet = input("Greeting: ")

    # ignores any leading whitespace in the user’s greeting
    greet = greet.lstrip().casefold()

    # checks if the greeting starts with "hello"
    cashback = get_cashback(greet)

    # prints the cashback
    print(cashback)


def get_cashback(greet: str):
    # no cashback to "hello" greeting
    if greet.startswith("hello"):
        return "$0"

    # 20% to greetings that starts with "h"
    if greet.startswith("h"):
        return "$20"

    # total cashback to no greeting
    return "$100"


main()
