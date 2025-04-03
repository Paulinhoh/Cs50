def main():
    dinheiro:float = float(input('Digite o valor em dinheiro: ')) * 100
    moedas:int = 0
    
    while(True):
        if(dinheiro >= 25):
            dinheiro -= 25
            moedas += 1
        elif(dinheiro >= 10 and dinheiro < 25):
            dinheiro -= 10
            moedas += 1
        elif(dinheiro >= 5 and dinheiro < 10):
            dinheiro -= 5
            moedas += 1
        elif(dinheiro >= 1 and dinheiro < 5):
            dinheiro -= 1
            moedas += 1
        else:
            break
    
    print(f'{moedas} moedas')
    


if __name__ == '__main__':
    main()