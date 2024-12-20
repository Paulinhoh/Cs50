def colemanLiau(text:str):
    letters:int = checkLetters(text)
    words:int = checkWords(text)
    sentences:int = checkSenetences(text)
    
    L:float = (letters * 100) / words
    S:float = (sentences * 100) / words
    indice:float = 0.0588 * L - 0.296 * S - 15.8
    
    return indice


def checkLetters(text:str):
    letters:int = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
    return letters


def checkWords(text:str):
    words:int = 0
    for i in range(len(text)):
        if text[i].isspace():
            words += 1
    return words + 1


def checkSenetences(text:str):
    sentences:int = 0
    organizedText:str = text.replace(" ", "1").replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")
    for i in range(len(organizedText)):
        if organizedText[i].isspace():
            sentences += 1
    return sentences


def main():
    text:str = str(input("Text: ")).strip()

    result:float = colemanLiau(text).__round__()
    
    if result <= 1:
        print("Before Grade 1")
    elif result >= 16:
        print("Grade 16+")
    else:
        print(f"Grade: {result}")

if __name__=='__main__':
    main()
