/**
 * Mees Kuipers
 * 11288477
 *
 * Implements a dictionary's functionality
 *
 */

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#include "dictionary.h"

int place = 0;
int counter;

typedef struct node
{
    bool is_word;
    struct node *alpha[27];
}
node;

bool check(const char *word)
{
    current = head;
    for (int i = 0; i < strlen(word); i++)
    {
        int letter = word[i];
        if (letter == '\'')
        {
            place = 26;
        }
        else
        {
            letter = tolower(word[i]);
            place = letter - 'a';
        }
        if (current -> alpha[place] == NULL)
        {
            return false;
        }
        current = current -> alpha[place];
    }
return (current -> is_word);
}

bool load(const char *dictionary)
{
    FILE *dictio = fopen(dictionary, "r");

    if (dictio == NULL)
    {
        fprintf(stderr, "Could not find file\n");
        return 2;
    }

    head = calloc(1, sizeof(node));
    if (head == NULL) //???????????
    {
        fprintf(stderr, "could not make more space");
        return 3;
    }

    char wordload[LENGTH + 1];
    while (fscanf(dictio, "%s", wordload) != EOF)
    {
        current = head;

        for (int i = 0; i < strlen(wordload); i++)
        {
            int letter = wordload[i];
            if (letter == '\'')
            {
                place = 26;
            }
            else
            {
                place = letter - 'a';
            }
            if (current -> alpha[place] == NULL)
            {
                current -> alpha[place] = calloc(1, sizeof(node));
                if (current -> alpha[place] == NULL) //?????????
                {
                    fprintf(stderr, "could not make more space");
                    return 3;
                }
            }
            current = current -> alpha[place];
        }
        current -> is_word = true;
        counter++;
    }
    fclose(dictio);
    return true;
}

unsigned int size(void)
{
    return counter;
}

bool unload(void)
{
     free_node(head);
    return true;
}

void free_node(node *current)
{
     for (int i = 0; i < 27; i++)
     {
         if (current->alpha[i] != NULL)
         {
             free_node(current->alpha[i]);
         }
     }
     free(current);
}