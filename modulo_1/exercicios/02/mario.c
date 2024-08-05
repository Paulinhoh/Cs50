#include <stdio.h>

int montanhaDupla(int tamanho)
{
    int contador1 = tamanho;
    int contador2 = 1;
    for (int i = 1; i <= tamanho; i++)
    {
        for (int j = 1; j <= tamanho; j++)
        {
            if (j >= contador1)
            {
                printf("#");
            }
            else
            {
                printf(".");
            }
        }

        for (int i = 1; i <= 2; i++)
        {
            printf(" ");
        }

        for (int j = 1; j <= tamanho; j++)
        {
            if (j <= contador2)
            {
                printf("#");
            }
            else
            {
                printf(".");
            }
        }

        printf("\n");
        contador1--;
        contador2++;
    }
}

int main(void)
{
    montanhaDupla(4);
}
