#include <stdio.h>
#include <string.h>
#include <ctype.h>

int POINTERS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(char word);

int main(void)
{
    // Solicitar ao usuário duas palavras
    char player1[20] = "";
    printf("Player 1: ");
    fgets(player1, 20, stdin);

    char player2[20] = "";
    printf("Player 2: ");
    fgets(player2, 20, stdin);

    // Calcular os pontos de cada palavra
    int pontosPlayer1 = compute_score(player1);
    int pontosPlayer2 = compute_score(player2);

    // Imprimir o vencedor
    if (pontosPlayer1 > pontosPlayer2)
    {
        printf("Player 1 wins!");
    }
    else if (pontosPlayer2 > pontosPlayer1)
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }

    return 0;
}

int compute_score(char word)
{
    // Computa e devolve os pontos de cada palavra
    word = tolower(word);
    char letter[5] = "";
    int sum = 0;
    int tamanho = strlen(word);

    for (int i = 0; i < tamanho; i++)
    {
        strcpy(letter, word[i]);

        if (letter == "a")
        {
            sum += POINTERS[0];
        }
        else if (letter == "b")
        {
            sum += POINTERS[1];
        }
        else if (letter == "c")
        {
            sum += POINTERS[2];
        }
        else if (letter == "d")
        {
            sum += POINTERS[3];
        }
        else if (letter == "e")
        {
            sum += POINTERS[4];
        }
        else if (letter == "f")
        {
            sum += POINTERS[5];
        }
        else if (letter == "g")
        {
            sum += POINTERS[6];
        }
        else if (letter == "h")
        {
            sum += POINTERS[7];
        }
        else if (letter == "i")
        {
            sum += POINTERS[8];
        }
        else if (letter == "j")
        {
            sum += POINTERS[9];
        }
        else if (letter == "k")
        {
            sum += POINTERS[10];
        }
        else if (letter == "l")
        {
            sum += POINTERS[11];
        }
        else if (letter == "m")
        {
            sum += POINTERS[12];
        }
        else if (letter == "n")
        {
            sum += POINTERS[13];
        }
        else if (letter == "o")
        {
            sum += POINTERS[14];
        }
        else if (letter == "p")
        {
            sum += POINTERS[15];
        }
        else if (letter == "q")
        {
            sum += POINTERS[16];
        }
        else if (letter == "r")
        {
            sum += POINTERS[17];
        }
        else if (letter == "s")
        {
            sum += POINTERS[18];
        }
        else if (letter == "t")
        {
            sum += POINTERS[19];
        }
        else if (letter == "u")
        {
            sum += POINTERS[20];
        }
        else if (letter == "v")
        {
            sum += POINTERS[21];
        }
        else if (letter == "w")
        {
            sum += POINTERS[22];
        }
        else if (letter == "x")
        {
            sum += POINTERS[23];
        }
        else if (letter == "y")
        {
            sum += POINTERS[24];
        }
        else if (letter == "z")
        {
            sum += POINTERS[25];
        }

        return sum;
    }
}
