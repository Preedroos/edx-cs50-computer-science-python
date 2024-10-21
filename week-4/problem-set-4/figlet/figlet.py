from pyfiglet import Figlet
import random
import sys


def main(args):

    # Gets the list of fonts
    fonts = Figlet().getFonts()

    # Exits if the user inputs more than 2 arguments or only 1 argument
    if len(args) > 2 or len(args) == 1:
        sys.exit("Invalid usage")

    if len(args) == 2:
        # Exits if the user inputs an argument that is not -f or --font
        if not args[0] == "-f" and not args[0] == "--font":
            sys.exit("Invalid usage")

        # Exits if the user inputs an invalid font
        if not args[1] in fonts:
            sys.exit("Invalid font")

    # Gets the text from the user
    text = input("Input: ")

    if len(args) == 0:
        # Sets a random font if the user inputs no arguments
        figlet = Figlet(font=random.choice(fonts))
    else:
        # Otherwise, sets the font to the user input
        figlet = Figlet(font=args[1])

    # Prints the text in the font
    print(figlet.renderText(text))


main(sys.argv[1:])
