"""
Mees Kuipers
11288477

This program will calculated how many coins you will return by a specific
amount of money
The amount of money is an input by the user
"""
from cs50 import get_float
# Make sure that the input is a float above the 0.01


def main():
    while True:
        cash = get_float("cash: ")
        if cash >= 0.01:
            break
    # The dollars are conferted to pennys
    cash = cash * 100
    round(cash)

    # Calculate how many coins there is needed
    coins = int(cash / 25)
    cash = cash % 25

    coins = int(cash / 10 + coins)
    cash = cash % 10

    coins = int(cash / 5 + coins)
    cash = cash % 5

    coins = coins + cash

    print(round(coins))
    return 0


if __name__ == "__main__":
    main()
