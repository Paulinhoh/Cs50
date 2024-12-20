def substituicao(alfabeto:str, text:str):
    codificado:str = ""
    
    upperAlfabeto:str = alfabeto.upper()
    lowerAlfabeto:str = alfabeto.lower()
    
    for i in text:
        if i.islower():
            if i == "a":
                codificado += lowerAlfabeto[0]
            elif i == "b":
                codificado += lowerAlfabeto[1]
            elif i == "c":
                codificado += lowerAlfabeto[2]
            elif i == "d":
                codificado += lowerAlfabeto[3]
            elif i == "e":
                codificado += lowerAlfabeto[4]
            elif i == "f":
                codificado += lowerAlfabeto[5]
            elif i == "g":
                codificado += lowerAlfabeto[6]
            elif i == "h":
                codificado += lowerAlfabeto[7]
            elif i == "i":
                codificado += lowerAlfabeto[8]
            elif i == "j":
                codificado += lowerAlfabeto[9]
            elif i == "k":
                codificado += lowerAlfabeto[10]
            elif i == "l":
                codificado += lowerAlfabeto[11]
            elif i == "m":
                codificado += lowerAlfabeto[12]
            elif i == "n":
                codificado += lowerAlfabeto[13]
            elif i == "o":
                codificado += lowerAlfabeto[14]
            elif i == "p":
                codificado += lowerAlfabeto[15]
            elif i == "q":
                codificado += lowerAlfabeto[16]
            elif i == "r":
                codificado += lowerAlfabeto[17]
            elif i == "s":
                codificado += lowerAlfabeto[18]
            elif i == "t":
                codificado += lowerAlfabeto[19]
            elif i == "u":
                codificado += lowerAlfabeto[20]
            elif i == "v":
                codificado += lowerAlfabeto[21]
            elif i == "w":
                codificado += lowerAlfabeto[22]
            elif i == "x":
                codificado += lowerAlfabeto[23]
            elif i == "w":
                codificado += lowerAlfabeto[24]
            elif i == "z":
                codificado += lowerAlfabeto[25]
        
        elif i.isupper():
            if i == "A":
                codificado += upperAlfabeto[0]
            elif i == "B":
                codificado += upperAlfabeto[1]
            elif i == "C":
                codificado += upperAlfabeto[2]
            elif i == "D":
                codificado += upperAlfabeto[3]
            elif i == "E":
                codificado += upperAlfabeto[4]
            elif i == "F":
                codificado += upperAlfabeto[5]
            elif i == "G":
                codificado += upperAlfabeto[6]
            elif i == "H":
                codificado += upperAlfabeto[7]
            elif i == "I":
                codificado += upperAlfabeto[8]
            elif i == "J":
                codificado += upperAlfabeto[9]
            elif i == "K":
                codificado += upperAlfabeto[10]
            elif i == "L":
                codificado += upperAlfabeto[11]
            elif i == "M":
                codificado += upperAlfabeto[12]
            elif i == "N":
                codificado += upperAlfabeto[13]
            elif i == "O":
                codificado += upperAlfabeto[14]
            elif i == "P":
                codificado += upperAlfabeto[15]
            elif i == "Q":
                codificado += upperAlfabeto[16]
            elif i == "R":
                codificado += upperAlfabeto[17]
            elif i == "S":
                codificado += upperAlfabeto[18]
            elif i == "T":
                codificado += upperAlfabeto[19]
            elif i == "U":
                codificado += upperAlfabeto[20]
            elif i == "V":
                codificado += upperAlfabeto[21]
            elif i == "W":
                codificado += upperAlfabeto[22]
            elif i == "X":
                codificado += upperAlfabeto[23]
            elif i == "Y":
                codificado += upperAlfabeto[24]
            elif i == "Z":
                codificado += upperAlfabeto[25]
            
        else:
            codificado += i
    
    return codificado


def main():
    alfabeto:str = "VCHPRZGJNTLSKFBDQWAXEUYMOI"
    texto:str = "hello, world"
    
    codificado:str = substituicao(alfabeto, texto)
    print(f"Codificado: {codificado}")


if __name__=='__main__':
    main()