def main():
    # prompts the user for an answer
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # filters the user's answer
    answer = answer.lower().strip()

    # checks if the user's answer is correct
    if is_correct(answer):
        print("Yes")
    else:
        print("No")


def is_correct(answer: str):
    # returns if the user's answer is in the list of correct answers
    return answer in ["42", "forty-two", "forty two"]


main()
