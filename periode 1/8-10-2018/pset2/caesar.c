/**
 * Mees Kuipers
 * 11288477
 *
 * This program can encrypt your sentence with a key. The key can be given in
 * numbers. The key is add to all the letter in the sentence. Every letter
 * in the alfabeth is equal to the number of the place in the alfabeth (A = 0).
 * The key and the sentence is an input for the user.
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
    if (argc == 2)
    {
        string n = argv[1];
        int key = atoi(n);
        int len1 = strlen(argv[1]);
        //Checking if every value of the keyis a number, otherwise it is
        //invalid (see 21)
        for (int i = 0; i < len1; i++)
        {
            if (n[i] <= '0' || n[i] >= '9')
            {
                printf("invalid input\n");
                return 1;
            }
        }
        //The key needs a higher value then 0, otherwise there is no ciphertext
        if (key > 0)
        {
            string secret = get_string("secret sentence: \n");
            int len2 = strlen(secret);
            printf("ciphertext: ");
            //every charater in the secret sentence should be evaluated
            for (int i = 0; i < len2; i++)
            {
                //All the letter should change places. The amount of places
                //depends of the key
                //if it is a capital letter it should stay a capital letter
                if (isupper(secret[i]))
                {
                    int captial = (((secret[i] + key) - 65) % 26) + 65;
                    char p = captial;
                    printf("%c", p);
                }
                //if it is not a capital letter it should stay that way
                else if (islower(secret[i]))
                {
                    int alfabetic = (((secret[i] + key) - 97) % 26) + 97;
                    char p = alfabetic;
                    printf("%c", p);
                }
                //else the charater should stay the same
                else
                {
                    printf("%c", secret[i]);
                }
            }
            printf("\n");
        }
        else
        {
            printf("invalid input\n");
        }
    }
    else
    {
        printf("invalid input\n");
        return 1;
    }

}





