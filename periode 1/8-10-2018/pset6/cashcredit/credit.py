from cs50 import get_int


def main():
    while True:
        card_number = get_int("creditcardnumber: ")
        if card_number > 10**14 and card_number < 10**16:
            break
        print("invalid input")

    card_number1 = card_number
    combound = 0

    while True:
        modulo = int(card_number % 10)
        combound = combound + modulo

        card_number = card_number / 10

        modulo = (int(card_number % 10) * 2)
        if modulo > 9:
            modulo1 = modulo % 10
            count = int((modulo - modulo1) / 10) + int(modulo1)
            combound = combound + count

        elif modulo < 9:
            combound = combound + modulo

        else:
            print("invalid input")
            break

        card_number = card_number / 10

        if card_number < 1:
            break

    if combound % 10 != 0:
        print("INVALID")

    if card_number1 > 10**15:
        if card_number1 >= 51 * 10**14 and card_number1 < 56 * 10**14:
            print("MASTERCARD")
        elif card_number1 >= 4 * 10**15 and card_number1 < 5 * 10**15:
            print("VISA")
        else:
            print("INVALID")

    elif card_number1 > 10**14:
        if card_number1 >= 34 * 10**13 and card_number1 < 35 * 10**13 or card_number1 >= 37 * 10**13 and card_number1 < 38 * 10**13:
            print("AMEX")
        else:
            print("INVALID")

    elif card_number1 >= 4 * 10**12 and card_number1 < 5 * 10**12:
        print("VISA")

    else:
        print("INVALID4")
    return 0


if __name__ == "__main__":
    main()
