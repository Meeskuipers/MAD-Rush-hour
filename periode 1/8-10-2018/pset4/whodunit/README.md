# Questions

## What's `stdint.h`?

Makes sure that every integer has a specific width

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Gives the amount of bytes in all the different data types

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1 bytes
DWORD: 4 bytes
LONG: 4 bytes
WORD: 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x4d42

## What's the difference between `bfSize` and `biSize`?

biSize is the number of bytes that is needed for the header
bfSize is the number of bytes that is needed for the whole image include all the headers

## What does it mean if `biHeight` is negative?

The origin of the bitam is in de upper left corner

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

RGBTRIPLE

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

If you pass a file name that does not excist it gives a value of NULL

## Why is the third argument to `fread` always `1` in our code?

Cause there need to be read one byte

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

fseek is the ´cursur´. You set the file position indicator.

## What is `SEEK_CUR`?

This determine the flag position of the origin
