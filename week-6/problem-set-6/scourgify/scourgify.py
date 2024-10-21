import sys
import csv


def main(args):

    # Exits if the user doesn't inputs any argument
    if len(args) < 2:
        sys.exit("Too few command-line arguments")

    # Exits if the user inputs more than 1 argument
    if len(args) > 2:
        sys.exit("Too many command-line arguments")

    before, after = args

    # Exits if the file is not a CSV file
    if not before.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(before, "r") as file:

            # Initializes the CSV reader
            csv_reader = csv.reader(file)

            with open(after, "w", newline='') as file:

                # Initializes the CSV writer
                csv_writer = csv.writer(file)

                # Writes the headers
                csv_writer.writerow(["first", "last", "house"])

                # Skips the headers
                next(csv_reader)

                # Writes the data
                for name, house in csv_reader:
                    last, first = name.replace(" ","").split(",")
                    csv_writer.writerow([first, last, house])

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main(sys.argv[1:])
