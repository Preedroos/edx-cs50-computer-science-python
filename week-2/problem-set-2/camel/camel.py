def main():
    # prompts the user for the name of a variable in camel case
    camel_case = input("camelCase: ")

    # tranforms the camel case to snake case
    snake_case = camel_to_snake(camel_case)

    # outputs the corresponding name in snake case
    print(f"snake_case: {snake_case}")


def camel_to_snake(camel_case: str):
    snake_case = ""
    for s in camel_case:
        if s.isupper():
            snake_case = snake_case + "_"

        snake_case = snake_case + s.lower()

    return snake_case


main()
