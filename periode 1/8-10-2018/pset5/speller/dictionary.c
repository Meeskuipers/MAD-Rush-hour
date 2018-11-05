/**
 * Mees Kuipers
 * 11288477
 *
 * Implements a dictionary's functionality.
 *
 */

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#include "dictionary.h"

// is the struct that is used called node
typedef struct node
{
    bool is_word;
    struct node *alpha[27];
} node;

void free_node(node *current);
node *head;
int counter = 0;
int place;



//Returns true if word is in dictionary else false.
bool check(const char *word)
{

    node *current = NULL;
    current = head;
    int n = strlen(word);
    // checks every letter of the word
    for (int i = 0; i < n; i++)
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
        // Checks if the letter is in one of the arrays if not return false
        if (current->alpha[place] == NULL)
        {
            return false;
        }
        // move the current to a new pointer
        else
        {
            current = current->alpha[place];
        }
    }

    // returns true if word does exist
    return (current->is_word);
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    FILE *dictio = fopen(dictionary, "r");

    if (dictio == NULL)
    {
        printf("Could not open dictionary.\n");
        unload();
        return 2;
    }

    char LENG[47];

    head = calloc(1, sizeof(node));
    node *current = NULL;

    // This loop goes one to the eld of the dictionary. Every word in the
    // dictionary is called LENG
    while (fgets(LENG, 47, dictio) != NULL)
    {

        // every begin of the word the current start by the head
        current = head;
        counter++;

        // checks every letter of the word
        int n = strlen(LENG);
        for (int i = 0; i < n - 1; i++)
        {
            int letter = LENG[i];
            if (letter == '\'')
            {
                place = 26;
            }
            else
            {
                place = letter - 'a';
            }

            // if het path did not excist a new pad is mad by this statement
            if (current->alpha[place] == NULL)
            {
                node *new_node = calloc(1, sizeof(node));
                current->alpha[place] = new_node;
            }

            // The current goes to the new place that is made on line 107 or
            // already excist
            current = current->alpha[place];

        }
        current->is_word = true;
    }
    fclose(dictio);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// This function uses the function free_node to free every space
bool unload(void)
{
    free_node(head);
    return true;

}

// Unloads dictionary from memory, returning true if successful else false
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