/**
 * Mees Kuipers
 * 11288477
 *
 * Helper functions
 * This vile gives two function that is used in find.
 * The sort function give all the number in the right order
 * the search function search the right value in the list
 */

#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

// Returns true if value is in array of n values, else false
bool search(int value, int values[], int n)
{
    int left = 0;
    int right = n - 1;
    int middle = (right + left) / 2;
    // This loop will go on until the number is not in the array
    while (left <= right)
    {
        // This gives the true value when the number is
        if (values[middle] == value)
        {
            return true;
        }
        // There is a new boundry at the right side if value is to the left
        // to the middle
        else if (value < values[middle])
        {
            right = middle - 1;
        }
        // There is a new boundry at the left side if value is to the right
        // to the middle
        else if (value > values[middle])
        {
            left = middle + 1;
        }

        middle = (right + left) / 2;
    }
    return false;
}

// Sorts array of n values
void sort(int values[], int n)
{
    // Sort all the numbers from low to high
    for (int i = 0; i < n - 1; i++)
    {
        int smal = values[i];
        int j;
        int temp;
        for (j = i + 1; j < n; j++)
        {
            if (values[j] < smal)
            {
                smal = values[j];
                temp = j;
            }
        }
        // Swapt the values
        if (values[i] != smal)
        {
            values[temp] = values[i];
            values[i] = smal;
        }
    }
    return;
}
