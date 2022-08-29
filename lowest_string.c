// Find the minmum length of a word in sentence

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>



int main(void)
{
    char *phrase = "lets talk about Cj the best language X";
    int *array_lens = malloc(sizeof(int));
    int k = 0;
    int len = 0;
    
    for(int i = 0; phrase[i] != '\0' ; i++)
    {
        if (!isspace(phrase[i]))
        {
            len++;
        }
        else
        {
            array_lens[k] = len;
            k++;
            array_lens = realloc(array_lens,(k+1) * sizeof(int));
            len = 0;
        }
    }
    array_lens[k] = len;
    int min = array_lens[0];
    int size = sizeof(array_lens)/sizeof(int);
    for (int i = 0; i <= k; i++)
    {
        if (array_lens[i] < min)
        {
            min = array_lens[i];
        }
    }
    printf("%i\n",min);
}
