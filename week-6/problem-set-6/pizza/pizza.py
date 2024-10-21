import sys
import csv
from tabulate import tabulate


def main(args):

    # Exits if the user doesn't inputs any argument
    if len(args) == 0:
        sys.exit("Too few command-line arguments")

    # Exits if the user inputs more than 1 argument
    elif len(args) > 1:
        sys.exit("Too many command-line arguments")

    pizza = args[0]

    # Exits if the file is not a CSV file
    if not pizza.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(pizza, "r") as file:

            # Reads the CSV file
            csv_reader = csv.reader(file)

            # Gets the headers
            headers = next(csv_reader)

            # Gets the data
            data = [row for row in csv_reader]

            # Prints the data in a table format
            print(tabulate(data, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main(sys.argv[1:])
