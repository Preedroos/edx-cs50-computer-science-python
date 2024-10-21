import re


def main():
    print(count(input("Text: ")))


def count(s):
    # counts the number of "um" in a string
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))


if __name__ == "__main__":
    main()
