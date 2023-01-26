def main():
    # prompts the user for input
    phrase = input("input: ")

    # converts input's emoticons to emojis
    phrase = convert(phrase)

    # prints the result
    print(phrase)


def convert(phrase):
    # replaces :) to slightly smiling face
    phrase = phrase.replace(":)", "🙂")

    # replaces :( to slightly frowning face
    phrase = phrase.replace(":(", "🙁")

    return phrase


main()
