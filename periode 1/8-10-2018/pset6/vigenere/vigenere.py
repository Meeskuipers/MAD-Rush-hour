"""
Mees Kuipers
11288477

This program can encrypt your sentence with a key. The key can be written in
words. The letters in the words are equal to the number in the alfabeth. The
key and the sentence is an input for the user.

"""

import sys
from cs50 import get_string


def main():
    # Makes sure that the command line excist out of two strings
    if len(sys.argv) != 2:
        print("Invalid input")
        sys.exit(1)

    key = sys.argv[1]

    # Makes sure that the string only excist out of alphabetic letters
    if not str.isalpha(key):
        print("Invalid input")
        sys.exit(1)

    secret = get_string("secret sentence: ")
    print("ciphertext: ", end="")

    counter = 0
    for c in secret:
        # Makes sure that if the key is smaller then the sentence that the key
        # starts over again
        modul = counter % len(key)
        # Every capital letter should stay capital and otherwise
        if str.isupper(c):
            # ord and chr are used for the ascii value
            if str.isupper(key[modul]):
                keyletter = ord(key[modul]) - ord('A')
                change = (keyletter + ord(secret[counter]) - ord('A')) % 26 + ord('A')
                print(chr(change), end="")
                # This counter that itterate over the whole secret sentence
                counter += 1

            elif str.islower(key[modul]):
                keyletter = ord(key[modul]) - (ord('a') - ord('A')) - ord('A')
                change = (keyletter + ord(secret[counter]) - ord('A')) % 26 + ord('A')
                print(chr(change), end="")
                counter += 1

        elif str.islower(c):
            if str.isupper(key[modul]):
                keyletter = ord(key[modul]) + (ord('a') - ord('A')) - ord('a')
                change = (keyletter + ord(secret[counter]) - ord('a')) % 26 + ord('a')
                print(chr(change), end="")
                counter += 1

            elif str.islower(key[modul]):
                keyletter = ord(key[modul]) - ord('a')
                change = (keyletter + ord(secret[counter]) - ord('a')) % 26 + ord('a')
                print(chr(change), end="")
                counter += 1

        else:
            # all blank spaces should not be itterate over the key
            print(c, end="")
    print()
    return 0


if __name__ == "__main__":
    main()
