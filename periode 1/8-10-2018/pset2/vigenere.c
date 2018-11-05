/**
 * Mees Kuipers
 * 11288477
 *
 * This program can encrypt your sentence with a key. The key can be written in
 * words. The letters in the words are equal to the number in the alfabeth. The
 * key and the sentence is an input for the user.
 *
 */


#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
long long getal;

int main(int argc, string argv[])
{
    // makes sure that the command line excist out of two strings
    if (argc != 2)
    {
        printf("invalid input\n");
        return 1;
    }
    // makes sure that the string only excist out of alphabetic letters
    string key = argv[1];
    int lenk = strlen(argv[1]);
    for (int j = 0; j < lenk; j++)
    {
        if (!isalpha(key[j]))
        {
            printf("invalid input\n");
            return 1;
        }
    }
    string secret = get_string("secret sentence: \n");
    int lenc = strlen(secret);
    printf("ciphertext: ");
    int w = 0;
    // this loop takes every letter of the sentences and add the number of the
    // key
    for (int i = 0; i < lenc; i++)
    {
        // the key is almost never equal to the size of the sentence
        // when the 4th letter of the sentence should be add to the firts letter
        // of the key, when the key exict out of three letters
        int mod = w % lenk;
        // all the upper letters of the sentence should stay upper
        if (isupper(secret[i]))
        {
            // the ascii value of captial letters are different for small
            // letters, so the formula is different and it should be done in
            // two different statements
            if (isupper(key[mod]))
            {
                int keyletter = key[mod] - 'A';
                int ciphernumber = secret[i];
                int captial = (((keyletter + ciphernumber) - 'A') % 26) + 'A';
                char p = captial;
                printf("%c", p);
                // makes sure that the spaces do not count in the sentence
                w++;
            }
            else if (islower(key[mod]))
            {
                int keyletter = key[mod] - ('a' - 'A') - 'A';
                int ciphernumber = secret[i];
                int captial = (((keyletter + ciphernumber) - 'A') % 26) + 'A';
                char p = captial;
                printf("%c", p);
                w++;
            }
        }
        //if it is not a capital letter it should stay that way
        else if (islower(secret[i]))
        {
            if (isupper(key[mod]))
            {
                int keyletter = (key[mod] + ('a' - 'A')) - 'a';
                int ciphernumber = secret[i];
                int letter = (((keyletter + ciphernumber) - 'a') % 26) + 'a';
                char p = letter;
                printf("%c", p);
                w++;
            }
            else if (islower(key[mod]))
            {
                int keyletter = key[mod] - 'a';
                int ciphernumber = secret[i];
                int letter = (((keyletter + ciphernumber) - 'a') % 26) + 'a';
                char p = letter;
                printf("%c", p);
                w++;
            }
        }
        //else the charater should stay the same
        else
        {
            printf("%c", secret[i]);
        }
    }
    printf("\n");
}