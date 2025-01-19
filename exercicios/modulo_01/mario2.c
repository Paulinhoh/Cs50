#include <stdio.h>
#include <stdbool.h>

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
    int tamanho = 0;
    while (true)
    {
        printf("Digite o tamanho entre 1 e 8: ");
        scanf("%d", &tamanho);

        if (tamanho >= 1 && tamanho <= 8)
        {
            break;
        }
        else
        {
            printf("Valor invalido! Tente novamente.\n");
        }
    }

    montanhaDupla(tamanho);
}
