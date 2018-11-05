#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float m;
    int g = 0;
    int t = 0;
    int v = 0;
    int e = 0;
    int c = 0;
    do
    {
        m = get_float("change: ");
    }
    while (m < 0.009);
    float p = m * 100;
    int x = round(p);
    while (x >= 25)
    {
        x = x - 25;
        g = g + 1;          //count every single quarter
        c = c + 1;          //c is used to count the total amount of coins
    }
    while (x >= 10)
    {
        x = x - 10;
        t = t + 1;          //count every single dime
        c = c + 1;
    }
    while (x >= 5)
    {
        x = x - 5;
        v = v + 1;          //count every single nickel
        c = c + 1;
    }
    while (x >= 1)
    {
        x = x - 1;
        e = e + 1;          //count every single penny
        c = c + 1;
    }
    if (x == 0)
    {
        printf("The minimum amount of coins was: %i\n", c);
        printf("25 quarters: %i\n10 dimes: %i\n5 nickels: %i\n1 pennies: %i\n", g, t, v, e);
    }
}