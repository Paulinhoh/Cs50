#include <stdio.h>
#include <string.h>

int main(void)
{
    char numberCard[] = "5217-7299-1473-0884";

    // removendo o caracter "-"
    for (int i = 0; i < strlen(numberCard); i++)
    {
        if (numberCard[i] == '-')
        {
            numberCard[i] = ' ';
        }
    }

    // removendo os espaços
    char numberCardUpadate[50];
    int aux = 0;
    for (int i = 0; i < strlen(numberCard); i++)
    {
        if (numberCard[i] != ' ')
        {
            numberCardUpadate[aux] = numberCard[i];
            aux++;
        }
    }

    // pegando o ultimo numero
    char checkDigit[] = "a";
    checkDigit[0] = numberCardUpadate[strlen(numberCardUpadate) - 1];

    // excluindo o ultimo valor
    char lastNumberCard[50];
    aux = 0;
    for (int i = 0; i < strlen(numberCardUpadate) - 2; i++)
    {
        lastNumberCard[aux] = numberCardUpadate[i];
        aux++;
    }

    // invertendo a string
    int inicio, auxiliar, fim, tam = strlen(lastNumberCard);
    fim = tam - 1;
    for (inicio = 0; inicio < tam; inicio++)
    {
        auxiliar = lastNumberCard[inicio];
        lastNumberCard[inicio] = lastNumberCard[fim];
        lastNumberCard[fim] = auxiliar;
        fim--;
    }

    // multiplicando os numeros impares por 2 e diminuindo 9 se passar de 9

    // somando todos os digitos

    // verificando se o resultado junto com o primeiro digito retirado é multiplo de 10
}
