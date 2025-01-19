def checkFlag(numberCard:str)->None:
    checkDigits:str
    
    if numberCard[0] == '4':
        checkDigits = numberCard[0:1]
    else:
        checkDigits = numberCard[0:2]
        
    if (checkDigits == '34' or checkDigits == '37') and len(numberCard) == 15:
        print("AMEX")
    elif (checkDigits == '51' or checkDigits == '52' or checkDigits == '53' or checkDigits == '54' or checkDigits == '55') and len(numberCard) == 16:
        print("MASTERCARD")
    elif checkDigits == '4' and (len(numberCard) == 13 or len(numberCard) == 16 or len(numberCard) ==19):
        print("VISA")
    else:
        print("INVALID")


def checkCreditCard(numberCard:str)->bool:
    checkDigit:int = int(numberCard[-1])
    reverseNumbersWithoutCheckDigit:str = numberCard[slice(0,-1)][::-1]
    
    vector:list = []
    sum:int = 0
    for i in reverseNumbersWithoutCheckDigit:
        vector.append(int(i))
    
    for i in range(len(vector)):    
        if (i+1)%2 != 0:
            vector[i] = (vector[i]*2)-9 if (vector[i]*2 > 9) else vector[i]*2

    for i in range(len(vector)):
        sum += vector[i]

    if (sum + checkDigit)%10 == 0:
        return True
    else:
        return False


def main():
    while(True):
        numberCard:str = str(input("Digite os numeros do Cartão: ")).strip().replace("-"," ").replace(" ", "")
        if numberCard.isnumeric():
            break
        else:
            print("Invalid Input")

    if checkCreditCard(numberCard):
        checkFlag(numberCard)
    else:
        print("INVALID")


if __name__=='__main__':
    main()

# Test: 378282246310005