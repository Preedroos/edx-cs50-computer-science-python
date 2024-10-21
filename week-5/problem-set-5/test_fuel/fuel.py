def main():
    while True:
        try:
            # Gets the fraction from the user
            fraction = input("Fraction: ")

            # Converts the fraction to a percentage
            percentage = convert(fraction)

            # Prints the gauge
            print(gauge(percentage))

            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        if numerator > denominator:
            raise ValueError
        return int(numerator) / int(denominator) * 100
    except ValueError:
        raise ValueError()
    except ZeroDivisionError:
        raise ZeroDivisionError()


def gauge(percentage):
    match percentage:
        case range(0, 1):
            return "E"
        case range(99, 100):
            return "F"
        case _:
            return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
