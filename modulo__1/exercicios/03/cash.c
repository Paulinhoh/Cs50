#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    float valor = 0;
    int quantidade = 0;

    while (true)
    {
        printf("Troca devida: ");
        scanf("%f", &valor);

        valor = valor * 100;

        if (valor > -1)
        {
            break;
        }
        else
        {
            printf("Valor invalido! Tente novamente.\n");
        }
    }

    while (true)
    {
        if (valor >= 25)
        {
            valor = valor - 25;
            quantidade++;
        }
        else if (valor >= 10 && valor < 25)
        {
            valor = valor - 10;
            quantidade++;
        }
        else if (valor >= 5 && valor < 10)
        {
            valor = valor - 5;
            quantidade++;
        }
        else if (valor >= 1 && valor < 5)
        {
            valor = valor - 1;
            quantidade++;
        }
        else
        {
            break;
        }
    }

    printf("%i", quantidade);
}