#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    long long num;
    long long num1;
    long long num2;
    long long num3;
    long long modul;
    long long modul1;
    long long c;
    long long combound;
    long long combound1 = 0;
    long long combound2 = 0;
    long long combound3 = 0;

    do
    {
        num = get_long_long("creditcardnumber: ");
    }
    while (num / pow(10, 13) < 1.0 && num / pow(10, 17) > 1.0);

    num1 = num;
    num2 = num;
    num3 = num;
    num1 = num1 / 10;
    do
    {
        modul = (num1 % 10) * 2;
        num1 = num1 / 100;
        if (modul > 9)
        {
            modul1 = modul % 10;
            c = (modul - modul1) / 10;
            //combound1 is for every number that is higher then 9 when
            //multiplied
            combound1 = combound1 + modul1 + c;
        }
        else if (modul <= 9)
        {
            //combound 2 is for every number that is lower then 10 when
            //multiplied
            combound2 = combound2 + modul;
        }
        num2 = num % 10;
        combound3 = combound3 + num2;
        num = num / 100;
    }
    while (num >= 0.9);
    combound = combound1 + combound2 + combound3;
    if (combound % 10 == 0)
    {
        //gives all the creditcardnumber with 16 numbers
        if (num3 / pow(10, 15) >= 1)
        {
            if (num3 >= (51 * pow(10, 14)) && num3 < (56 * pow(10, 14)))
            {
                printf("MASTERCARD\n");
            }
            else if (num3 >= (4 * pow(10, 15)) && num3 < (5 * pow(10, 15)))
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        //gives all the creditcardnumber with 15 numbers
        else if (num3 / pow(10, 14) >= 1) //gives a
        {
            if ((num3 >= 34 * pow(10, 13) && num3 < 35 * pow(10, 13)) ||
                (num3 >= 37 * pow(10, 13) && num3 < 38 * pow(10, 13)))
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        //gives all the creditcardnumbers with 16 numbers
        else if (num >= 4 * pow(10, 12) && num < 5 * pow(10, 12))
        {
            printf("VISA\n");
            exit(0);
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
