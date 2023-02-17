owed_value = 50

while owed_value > 0:
    # prints the due
    print(f"Amount Due: {owed_value}")

    # prompts the user to insert a coin
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        # subtracts the coin from the owed value
        owed_value = owed_value - coin

# outputs the change the user is owed
print(f"Change Owed: {abs(owed_value)}")
