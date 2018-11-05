"""
Mees Kuipers
11288477

This program wil make the stairs of mario
The height of the stairs depends on the input

"""

from cs50 import get_int


def main():
    # Make sure that the input value is a int between 0 and 24
    while True:
        height = get_int("height: ")
        if height >= 0 and height < 24:
            break
    # Print an amount of # and blank spaces dependend of the height
    for i in range(height):
        print(" " * (height - 1 - i), end="")
        print("#" * (1 + i), end="")
        print("  ", end="")
        print("#" * (1 + i), end="")
        print()
    return 0


if __name__ == "__main__":
    main()
