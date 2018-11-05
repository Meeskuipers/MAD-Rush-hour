#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height:");
    }
    while (h < 0 || h > 23);

    for (int i = 0; i < h; i++)
    {
        for (int s = i; s < h - 1; s++)
        {
            printf(" ");
            //print spaces
        }
        for (int a = 0; a < i + 2; a++)
        {
            printf("#");
            //print hashtags
        }
        printf("\n");
        //print enter
    }
}

