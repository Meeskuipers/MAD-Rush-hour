/**
 * Mees Kuipers
 * 11288477
 *
 * This file can inlarge a bmp file
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdlib.h>
#include <cs50.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 1;
    }

    // remember filenames
    int inlarge = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    if (isdigit(inlarge) && inlarge >= 1 && inlarge <= 100)
    {
        fprintf(stderr, "should be a number between 0 and 100");
        return 2;
    }
    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    int oldHeight = bi.biHeight;
    bi.biHeight = bi.biHeight * inlarge;

    // determine padding for scanlines
    int oudpadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int oldWidth = bi.biWidth;
    bi.biWidth = bi.biWidth * inlarge;

    // determine padding for scanlines
    int newpadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + newpadding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(oldHeight); i < biHeight; i++)
    {
        int counter = 0;
        RGBTRIPLE line[bi.biWidth];
        // iterate over pixels in scanline
        for (int j = 0; j < oldWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // write RGB triple to outfile
            for (int k = 0; k < inlarge; k++)
            {
                line[counter] = triple;
                counter++;
            }
        }

        // skip over padding, if any
        fseek(inptr, oudpadding, SEEK_CUR);

        // then add it back (to demonstrate how)
        for (int l = 0; l < inlarge; l++)
        {
            fwrite(line, sizeof(RGBTRIPLE) * bi.biWidth, 1, outptr);
            for (int m = 0; m < newpadding; m++)
            {
                fputc(0x00, outptr);
            }

        }

    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
