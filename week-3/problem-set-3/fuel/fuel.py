def main():
    while True:
        try:
            fuel_gauge_indicator()
            break
        except (ValueError, ZeroDivisionError):
            pass


def fuel_gauge_indicator():
    fraction = input("Enter the fraction: ")

    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError

    percentage = round(x / y * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
