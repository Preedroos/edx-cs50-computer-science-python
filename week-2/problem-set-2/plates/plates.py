def main():
    # prompts the user for the desired plate
    plate = input("Plate: ")

    # verifies the user's desired plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate: str):
    # verifies the plate length (min 2 and max 6)
    if 2 <= len(plate) <= 6:

        # returns true if all characters are alphabetic
        if plate.isalpha():
            return True

        # verifies if all characters in the string are alphanumeric
        if plate.isalnum():

            # verifies if at least the first two digits are letters
            if plate[0:2].isalpha():

                # returs true if it just has length equal 2
                if len(plate) == 2:
                    return True

                for c in plate[2:]:

                    if c.isnumeric():
                        # returns false if the first number is equals to zero
                        if c == "0":
                            return False

                        # returns true if all characters after the first number are also a number
                        elif plate[plate.find(c):].isnumeric():
                            return True


main()
