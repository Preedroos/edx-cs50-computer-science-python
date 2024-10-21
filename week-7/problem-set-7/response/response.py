from validator_collection import validators


def main():
    email_address = input("What's your email address? ")
    try:
        if validators.email(email_address):
            print("Valid")
        else:
            raise ValueError
    except:
        print("Invalid")


if __name__ == "__main__":
    main()
