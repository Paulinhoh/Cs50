def main():
    pai:str = str(input("Digite o tipo sanguineo do pai: "))
    mae:str = str(input("Digite o tipo sanguineo da mãe: "))
    
    filho:list = []
    
    for i in range(len(pai)):
        for j in range(len(mae)):
            filho.append(pai[i] + mae[j])
            
    for i in range(len(filho)):
            print(filho[i])
            


if __name__ == "__main__":
    main()
