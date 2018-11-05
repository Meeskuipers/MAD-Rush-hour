/**
 * Mees Kuipers
 * 11288477
 *
 * find lost pictures in card.raw
 *
 */


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdlib.h>
#include <cs50.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: copy infile\n");
        return 1;
    }

    // argv[1] == "card.raw"
    // dictionary == "dictionaries/large"
    char *file = argv[1];
    FILE *infile = fopen(file, "r");

    // open input file
    if (file == NULL)
    {
        fprintf(stderr, "Could not find file\n");
        return 2;
    }

    unsigned char buffer[512];
    int counter = 0;

    FILE *img = NULL;
    // Checks if the beginning of 512 bites is the start of a jpeg file
    while (fread(buffer, 1, 512, infile) == 512)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            char store[8];
            // Makes for every new jpeg file a new jpg file
            sprintf(store, "%03i.jpg", counter);
            counter++;
            img = fopen(store, "w");
        }

        if (img != NULL)
        {
            // Write down the storted values
            fwrite(buffer, 1, 512, img);
        }
    }

    // close infile
    fclose(img);

    // close outfile
    fclose(infile);

    // success
    return 0;
}