def computer_score(word:str, POINTERS:list):
    sum:int = 0

    for i in range(len(word)):
        letter:str = word[i]

        if letter == 'a':
            sum += POINTERS[0]
        elif letter == 'b':
            sum += POINTERS[1]
        elif letter == 'c':
            sum += POINTERS[2]
        elif letter == 'd':
            sum += POINTERS[3]
        elif letter == 'e':
            sum += POINTERS[4]
        elif letter == 'f':
            sum += POINTERS[5]
        elif letter == 'g':
            sum += POINTERS[6]
        elif letter == 'h':
            sum += POINTERS[7]
        elif letter == 'i':
            sum += POINTERS[8]
        elif letter == 'j':
            sum += POINTERS[9]
        elif letter == 'k':
            sum += POINTERS[10]
        elif letter == 'l':
            sum += POINTERS[11]
        elif letter == 'm':
            sum += POINTERS[12]
        elif letter == 'n':
            sum += POINTERS[13]
        elif letter == 'o':
            sum += POINTERS[14]
        elif letter == 'p':
            sum += POINTERS[15]
        elif letter == 'q':
            sum += POINTERS[16]
        elif letter == 'r':
            sum += POINTERS[17]
        elif letter == 's':
            sum += POINTERS[18]
        elif letter == 't':
            sum += POINTERS[19]
        elif letter == 'u':
            sum += POINTERS[20]
        elif letter == 'v':
            sum += POINTERS[21]
        elif letter == 'w':
            sum += POINTERS[22]
        elif letter == 'x':
            sum += POINTERS[23]
        elif letter == 'y':
            sum += POINTERS[24]
        elif letter == 'z':
            sum += POINTERS[25]

        return sum


def main():
    POINTERS:list = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    
    # Solicitar ao usuário duas palavras
    player1:str = str(input("Player 1: ")).strip().lower()
    player2:str = str(input("Player 2: ")).strip().lower()

    # Calcular os pontos de cada palavra
    pontosPlayer1:int = computer_score(player1, POINTERS)
    pontosPlayer2:int = computer_score(player2, POINTERS)

    # Imprimir o vencedor
    if (pontosPlayer1 > pontosPlayer2) :
        print("Player 1 wins!")
    elif (pontosPlayer2 > pontosPlayer1):
        print("Player 2 wins!")
    else:
        print("Tie!")


if __name__=='__main__':
    main()