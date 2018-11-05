/**
 * Mees Kuipers
 * 11288477
 *
 * This program can crack some passwords that excist out of 1 to 5 alphabetic
 * numbers. It uses brute force to do this.
 *
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <unistd.h>
#include <crypt.h>

int main(int argc, string argv[])
{
    // makes sure that the command line excist out of two strings
    if (argc != 2)
    {
        printf("invalid value\n");
        return 1;
    }
    string final = argv[1];
    // this was used to have a string of all the letters
    char alpha[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
                    'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                   };
    // the first two letters the hashed input is equal to the salt that is
    // needed for the crypt function
    char salt[] = {final[0], final[1], '\0'};

    // this for loop gives all the one letter keys
    for (int i = 0; i < ('z' - 'a' + 'Z' - 'A'); i++)
    {
        char solution[] = {alpha[i], '\0'};
        string code = crypt(solution, salt);
        // compare every hashed code with the given hashcode
        if (strcmp(argv[1], code) == 0)
        {
            printf("nice job, the key is: %s\n", solution);
            return 0;
        }
    }

    // this for loop gives all the two letter keys
    // the following for loops will have a different amount of letters for keys
    // this is equal to the amount of for loops.
    for (int i = 0; i < ('z' - 'a' + 'Z' - 'A'); i++)
    {
        for (int j = 0; j < ('z' - 'a' + 'Z' - 'A'); j++)
        {
            char solution[] = {alpha[i], alpha[j], '\0'};
            string code = crypt(solution, salt);
            if (strcmp(argv[1], code) == 0)
            {
                printf("nice job, the key is: %s\n", solution);
                return 0;
            }
        }
    }

    for (int i = 0; i < ('z' - 'a' + 'Z' - 'A'); i++)
    {
        for (int j = 0; j < ('z' - 'a' + 'Z' - 'A'); j++)
        {
            for (int k = 0; k < ('z' - 'a' + 'Z' - 'A'); k++)
            {
                char solution[] = {alpha[i], alpha[j], alpha[k], '\0'};
                string code = crypt(solution, salt);
                if (strcmp(argv[1], code) == 0)
                {
                    printf("nice job, the key is: %s\n", solution);
                    return 0;
                }
            }
        }
    }
    for (int i = 0; i < ('z' - 'a' + 'Z' - 'A'); i++)
    {
        for (int j = 0; j < ('z' - 'a' + 'Z' - 'A'); j++)
        {
            for (int k = 0; k < ('z' - 'a' + 'Z' - 'A'); k++)
            {
                for (int l = 0; l < ('z' - 'a' + 'Z' - 'A'); l++)
                {
                    char solution[] = {alpha[i], alpha[j], alpha[k], alpha[l], '\0'};
                    string code = crypt(solution, salt);
                    if (strcmp(argv[1], code) == 0)
                    {
                        printf("nice job, the key is: %s\n", solution);
                        return 0;
                    }
                }
            }
        }
    }

    for (int i = 0; i < ('z' - 'a' + 'Z' - 'A'); i++)
    {
        for (int j = 0; j < ('z' - 'a' + 'Z' - 'A'); j++)
        {
            for (int k = 0; k < ('z' - 'a' + 'Z' - 'A'); k++)
            {
                for (int l = 0; l < ('z' - 'a' + 'Z' - 'A'); l++)
                {
                    for (int m = 0; m < ('z' - 'a' + 'Z' - 'A'); m++)
                    {
                        char solution[] = {alpha[i], alpha[j], alpha[k], alpha[l], alpha[m], '\0'};
                        string code = crypt(solution, salt);
                        if (strcmp(argv[1], code) == 0)
                        {
                            printf("nice job, the key is: %s\n", solution);
                            return 0;
                        }
                    }
                }
            }
        }

    }
    printf("there is no key\n");
    return 1;
}