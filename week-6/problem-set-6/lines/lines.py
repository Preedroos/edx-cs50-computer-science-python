import sys


def main(args):

    # Exits if the user doesn't inputs any argument
    if len(args) == 1:
        sys.exit("Too few command-line arguments")

    # Exits if the user inputs more than 2 argument
    if len(args) > 2:
        sys.exit("Too many command-line arguments")

    path = args[1]

    # Exits if the file is not a Python file
    if not path.endswith(".py"):
        sys.exit("Not a Python file")

    lines_counter = 0

    try:
        with open(path, "r") as file:
            for line in file:
                # Ignores empty lines or comments
                if line.strip() != "" and not line.strip().startswith("#"):
                    lines_counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(lines_counter)


if __name__ == "__main__":
    main(sys.argv)
