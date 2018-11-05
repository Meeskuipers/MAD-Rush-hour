/**
 * Mees Kuipers
 * 11288477
 *
 * Helper functions for music
 * This vile gives three function that is used in music.
 * The duration function give the duration for the note (how long)
 * The frequency function give the right frequency to the note
 * The rest function can distinguish a blank space and makes sure there
 * is a rest period
 *
 */

#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int teller = atoi(&fraction[0]);
    int noemer = atoi(&fraction[2]);
    int number = 8 / noemer;
    int frac = teller * number;
    return frac;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    char notes =  note[0];
    float num = 1.0 / 12.0;
    float num1 = 440.0;
    float no;

    if (notes == 'A')
    {
        no = num1 * pow(2.0, (num * 0.0));
    }

    else if (notes == 'B')
    {
        no = num1 * pow(2.0, (num * 2.0));
    }

    else if (notes == 'C')
    {
        no = num1 / pow(2.0, (num * 9.0));
    }

    else if (notes == 'D')
    {
        no = num1 / pow(2.0, (num * 7.0));
    }

    else if (notes == 'E')
    {
        no = num1 / pow(2.0, (num * 5.0));
    }

    else if (notes == 'F')
    {
        no = num1 / pow(2.0, (num * 4.0));
    }

    else if (notes == 'G')
    {
        no = num1 / pow(2.0, (num * 2.0));
    }

    else
    {
        printf("invalid input");
        return 1;
    }

    char octaaf = note[1];
    char octaaf2 = note[2];
    // distinguish in a normal note, a sharp note (#) and a flat note (d)
    if (isdigit(octaaf))
    {
        // -0 needs te be done because it is the ascii value
        int oct = octaaf - '0' - 4.0;
        no = round(no * pow(2.0, oct));
        return no;
    }
    else if (octaaf == '#')
    {
        int oct = octaaf2 - '0' - 4.0;
        no = roundf(no * pow(2.0, (oct + num)));
        return no;
    }
    else if (octaaf == 'b')
    {
        int oct = octaaf2 - '0' - 4.0;
        no = round(no * pow(2.0, (oct - num)));
        return no;
    }
    else
    {
        return 1;
    }
}
// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s, "") == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}