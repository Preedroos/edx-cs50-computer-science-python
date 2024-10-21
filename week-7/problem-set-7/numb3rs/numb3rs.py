import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Checks whether the first byte of the IPv4 address is in range
    if not re.match(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.", ip):
        return False

    if re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
