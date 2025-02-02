def vote(candidatos:list, quantidade_votos:int) -> list:
    votos:dict = {}
    for candidato in candidatos:
        votos[candidato] = 0

    for i in range(quantidade_votos):
        voto:str = str(input("Vote: "))
        if voto in votos:
            votos[voto] += 1
        else:
            print("Invalid vote")
    
    maior:int = 0
    vencedor:list = []

    for candidato in votos:
        if votos[candidato] > maior:
            maior = votos[candidato]

    for candidato in votos:
        if votos[candidato] == maior:
            vencedor.append(candidato)
    
    return vencedor


def print_winner(vencedor:list) -> None:
    for candidato in vencedor:
        print(candidato)


def main():
    candidatos:str = str(input("-> ")).split(" ")
    quantidade_votos:int = int(input("Numero de eleitores:  "))

    vencedor:list = vote(candidatos, quantidade_votos)
    print_winner(vencedor)


if __name__ == '__main__':
    main()
