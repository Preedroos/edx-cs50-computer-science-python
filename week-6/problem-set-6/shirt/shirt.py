import sys
from PIL import Image, ImageOps


def main(args):

    # Exits if the user doesn't inputs any argument
    if len(args) < 2:
        sys.exit("Too few command-line arguments")

    # Exits if the user inputs more than 1 argument
    if len(args) > 2:
        sys.exit("Too many command-line arguments")

    # Exits if those files end in .jpg, .jpeg, or .png, case-insensitively
    [sys.exit("Invalid input")
     for file in args if not file.lower().endswith((".jpg", ".jpeg", ".png"))]

    # Exits if those files aren't the same extension
    if args[0].split(".")[-1] != args[1].split(".")[-1]:
        sys.exit("Input and output have different extensions")

    # Exits if the input file does not exist
    try:
        with Image.open(args[0]) as img:

            # Resizes the input image to 600x600 pixels
            img = ImageOps.fit(img, (600, 600))

            # Pastes the shirt.png image on top of the input image
            img.paste(Image.open("shirt.png"), Image.open("shirt.png"))

            # Saves the image
            img.save(args[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main(sys.argv[1:])
