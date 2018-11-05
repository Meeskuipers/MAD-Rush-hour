#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int values[] = {27, 28, 29, 30};
    int n = 4;
    int value = 28;
    int left = 0;
    int right = n;
    int middle = (right + left) / 2;
    while (values[middle] != value)
    {
        if (right - left == 0)
        {
            return 0;
            printf("nice3");
        }
        if (value < values[middle])
        {
            right = middle - 1;
            printf("nice1");
        }
        else if (value > values[middle])
        {
             left = middle + 1;
             printf("nice2");
        }
        else
        {
            printf("invalid input");
            return 0;
        }
        middle = (right + left) / 2;
    }
    return 1;
    printf("nice4");
}