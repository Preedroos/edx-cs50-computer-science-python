def main():
    word = shorten(input("Input: "))
    shortened = shorten(word)
    print(f"Output: {shortened}")


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([c for c in word if c.casefold() not in vowels])


if __name__ == "__main__":
    main()
