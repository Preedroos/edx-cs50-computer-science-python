def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters
    if not 2 <= len(s) <= 6:
        return False

    # All vanity plates must start with at least two letters
    if not s[0:2].isalpha():
        return False

    decimalAppearance = False

    for c in s[2:]:

        if c.isalpha() and not decimalAppearance:
            continue

        # The first number used cannot be a ‘0’
        if not decimalAppearance and c == "0":
            return False

        if c.isdecimal():
            decimalAppearance = True

            # Numbers cannot be used in the middle of a plate; they must come at the end.
            if not s[s.find(c):].isdecimal():
                return False

    return True


main()
