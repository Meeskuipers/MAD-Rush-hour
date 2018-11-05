/**
 * Mees Kuipers
 * 11288477
 *
 * This program gives all the initials of the name that was given by the user
 *
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
long long getal;


int main(void)
{
    string name = get_string("Name: \n");
    // if the input value do not begin with a letter, the first letter
    // should not be printed
    if (name[0] != ' ' && isalpha(name[0]))
    {
        printf("%c", toupper(name[0]));
    }
    else
    {
        printf("invalid input\n");
        return 1;
    }
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        // this means that every letter that comes after a space, that
        // letter should be printed
        if (name[i] == ' ' && (name[i + 1] != ' ')
        {
            // makes sure that every input value is a alphabetic letter
            if (isalpha(name[i + 1]))
            {
                printf("%c", toupper(name[i + 1]));
            }
            else
            {
                printf("invalid input\n");
                return 1;
            }
        }
    }
    printf("\n");
}
