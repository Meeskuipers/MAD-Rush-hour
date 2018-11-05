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
int main(void)
{
    // int frequency(string note)
    // {
        string note = "Bb5";
        char notes = note[0];
        float hz = 440.0;
        float num = 1.0 / 12.0;
        int no;

        if (notes == 'A')
        {
            no = hz * pow(2, (num * 0.0));
        }
        else if (notes == 'B')
        {
            no = hz * pow(2.0, (num * 2.0));
        }
        else if (notes == 'C')
        {
            no = hz / pow(2.0, (num * 9.0));
        }
        else if (notes == 'D')
        {
            no = hz / pow(2.0, (num * 7.0));
        }
        else if (notes == 'E')
        {
            no = hz / pow(2.0, (num * 5.0));
        }
        else if (notes == 'F')
        {
            no = hz / pow(2.0, (num * 4.0));
        }
        else if (notes == 'G')
        {
            no = hz / pow(2.0, (num * 2.0));
        }
        else
        {
            printf("invalid input");
            return 1;
        }

        char octaaf = note[1];
        char octaaf2 = note[2];

        if (isdigit(octaaf))
        {
            int oct = octaaf - '0' - 4.0;
            no = round(no * pow(2.0, oct));
            printf("1: %i", no);
            return no;
        }
        else if (octaaf == '#')
        {
            int oct = octaaf2 - '0' - 4.0;
            no = roundf(no * pow(2.0, (oct + num)));
            printf("2: %i", no);
            return no;
        }
        else if (octaaf == 'b')
        {
            int oct = octaaf2 - '0' - 4.0;
            no = round(no * pow(2.0, (oct - num)));
            printf("3: %i", no);
            return no;
        }
        else
        {
            return 1;
        }
}