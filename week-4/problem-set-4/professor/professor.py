import random
import math


def main():
    # Gets the level from the user
    level = get_level()

    # Generates 10 problems based on the level
    problems = generate_problems(level)

    score = 0

    for question, answer in problems:
        for i in range(3):
            # Asks the user for the answer to each problem
            user_answer = get_num(question)
            if user_answer == answer:
                score += 1
                break
            elif i == 2:
                # If the user gets the problem wrong 3 times, the correct answer is printed
                print(question, answer, sep="")
            else:
                # If the user gets the problem wrong, they are prompted to try again
                print("EEE")

    # Outputs the user's score
    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not level in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_problems(level):
    problems = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problems.append((f"{x} + {y} = ", x + y))
    return problems


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


def get_num(output):
    while True:
        try:
            num = int(input(output))
            if num < 1:
                raise ValueError
            return num
        except ValueError:
            return


if __name__ == "__main__":
    main()
