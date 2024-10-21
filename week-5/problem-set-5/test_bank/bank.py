def main():
    greeting = input("Greeting: ")
    payback = value(greeting)
    print(f"${payback}")


def value(greeting):
    greeting = greeting.casefold()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
