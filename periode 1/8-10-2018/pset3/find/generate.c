// Generates pseudorandom numbers in [0,LIMIT), one per line

#define _XOPEN_SOURCE

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Constant
#define LIMIT 65536

int main(int argc, string argv[])
{
    // TODO: makes sure that the arc is never more then 4 and lower then 2.
    if (argc != 2 && argc != 3)
    {
        printf("Usage: generate n [s]\n");
        return 1;
    }

    // TODO: makes the first input and integer instead of a string
    int n = atoi(argv[1]);

    // TODO: srand48 only works when there are 3 inputs
    if (argc == 3)
    {
        srand48((long int) atoi(argv[2]));
    }
    else
    {
        srand48((long int) time(NULL));
    }

    // TODO: drand48 gives randum number for n times.
    for (int i = 0; i < n; i++)
    {
        printf("%i\n", (int) (drand48() * LIMIT));
    }

    // Success
    return 0;
}
