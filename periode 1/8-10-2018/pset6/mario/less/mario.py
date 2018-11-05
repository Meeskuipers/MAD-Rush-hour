from cs50 import get_int

while True:
    height = get_int("height: ")
    if height > 0 and height < 24:
        break
for i in range(height):
    print(" " * (height - 1 - i), end="")
    print("#" * (2 + i), end="")
    print()