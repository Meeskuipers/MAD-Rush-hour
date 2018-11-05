#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int m = get_int("minutes: ");

    int n = m*12;
    if (m < 0)
    {
        printf("you have an error\n");
    }
    else
    {
        printf("bottles: %i\n", n);
    }
}


