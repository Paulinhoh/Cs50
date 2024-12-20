#include <stdio.h>
#include <string.h>

int checkFlag(char numberCard)
{
    char visa[2] = "4";
    char checkDigits[3] = "";
    size_t num1 = 1;
    size_t num2 = 2;

    if (strncmp(visa, numberCard, num1))
    {
        strncpy(checkDigits, numberCard, num1);
    }
    else
    {
        strncpy(checkDigits, numberCard, num2);
    }

    if (checkDigits == "34" || checkDigits == "37")
        &&(strlen(numberCard) == 15)
        {
            printf("AMEX");
        }
    else if (checkDigits == "51" || checkDigits == "52" || checkDigits == "53" || checkDigits == "54" || checkDigits == "55")
        &&(len(numberCard) == 16)
        {
            printf("MASTERCARD");
        }
    else if (checkDigits == "4")
        &&(len(numberCard) == 13 || len(numberCard) == 16 || len(numberCard) == 19)
        {
            print("VISA");
        }
    else
    {
        print("INVALID");
    }
}

int checkCreditCard(char numberCart)
{
    char checkDigit[3] = "";
    strncpy(checkDigit, numberCart, -1);

    char reverseNumbersWithoutCheckDigit[20] = "";
    strncpy(reverseNumbersWithoutCheckDigit, numberCart, strlen(numberCart) - 1);
}

int main(void)
{
    char numberCard[20] = "";
    printf("Digite o numero do cartao (sem espacos): ");
    fgets(numberCard, 20, stdin);
    // scanf("%19[^\n]s", &numberCard);
    // fflush(stdin);

    if (checkCreditCard(numberCard))
    {
        checkFlag(numberCard);
    }
    else
    {
        printf("Cartão Invalido");
    }
}

//  Test: 378282246310005
