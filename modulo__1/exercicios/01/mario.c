#include <stdio.h>
#include <stdbool.h>

int montanhaSimples(int tamanho)
{
    int contador = tamanho;
    for (int i = 1; i <= tamanho; i++)
    {
        for (int j = 1; j <= tamanho; j++)
        {
            if (j >= contador)
            {
                printf("#");
            }
            else
            {
                printf(".");
            }
        }
        printf("\n");
        contador--;
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

    montanhaSimples(tamanho);
}
