def main():
    # prompts the user for an arithmetic expression
    expression = input("Expression: ")

    # splits the expression into three values
    x, y, z = expression.split(" ")

    # calculates the result
    result = calculate(y, int(x), int(z))

    # checks if the expression is valid
    if result == None:
        print("Invalid expression!")
        return 1

    # formats to one decimal place
    result = f"{result:.1f}"

    # outputs the result
    print(result)


def calculate(y: str, x: int, z: int):
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z

    return None


main()
