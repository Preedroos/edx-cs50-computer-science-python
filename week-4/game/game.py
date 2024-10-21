import random


def main():

    # Gets the level from the user
    level = get_num("Level: ")

    # Generates a random number between 1 and the level
    random_number = random.randint(1, level)

    # Checks if the number is smaller or larger than the random number
    while True:
        guess = get_num("Guess: ")

        if guess == random_number:
            exit("Just right!")
        elif guess < random_number:
            print("Too small!")
        else:
            print("Too large!")


def get_num(output):
    while True:
        try:
            level = int(input(output))
            if level < 1:
                raise ValueError
            return level
        except ValueError:
            pass


main()
