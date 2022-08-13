// review white's pieces from black's pov! --> white : a8 ; black : h1

// THIS CODE IS NOT HANDLING ENOUGH EXCEPTIONS !
#include <stdio.h>
#include <stdlib.h>

int len(char *word);

int main(int argc, char **argv)
{
    char *letters = "abcdefgh";
    char *digits = "12345678";
    char res[2];


    if (argc != 2)
    {
        printf("Invalid CMD\n");
        return 1;
    }

    for (int k = 0 ; k < 8 ; k++)
    {
        for (int i = 0 ; i < 2 ; i++)
        {
            if (letters[k] == argv[1][i]) // YOU CANNOT COMPARE TWO STRINGS LIKE THIS !!!
            {
                res[i] = letters[7-k];  
            } 
        }
        for (int i = 0 ; i < 2 ; i++)
        {
            if (digits[k] == argv[1][i])
            {
                res[i] = digits[7-k];  
            } 
        }
    }
    for (int j = 0 ; j < 2 ; j++)
    {
        printf("%c",res[j]);
    }
    printf("\n");
    return 0;
}

int len(char *word)
{
    int c = 0;
    for (int i = 0 ; *(word + i) != '\0' ; i++)
    {
        c += 1;
    }
    return c;
}
