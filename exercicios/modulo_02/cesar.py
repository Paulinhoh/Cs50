from os import system
from time import sleep

def cesarCipherEncryption(plaintext:str, key:int):
    encoded:str = ""
    
    for i in plaintext:
        if i.isalpha() and i.islower():
            if ord(i)+key > 122:
                encoded += chr(ord(i)+key -26)
            else:
                encoded += chr(ord(i)+key)
        elif i.isalpha() and i.isupper():
            if ord(i)+key > 90:
                encoded += chr(ord(i)+key -26)
            else:
                encoded += chr(ord(i)+key)
        else:
            encoded += i
    return encoded


def cesarCipherDecryption(plaintext:str, key:int):
    decryptedMessage:str = ""
    
    for i in plaintext:
        if i.isalpha() and i.islower():
            if ord(i)-key < 97:
                decryptedMessage += chr(ord(i)-key +26)
            else:
                decryptedMessage += chr(ord(i)-key)
        elif i.isalpha() and i.isupper():
            if ord(i)-key < 65:
                decryptedMessage += chr(ord(i)-key +26)
            else:
                decryptedMessage += chr(ord(i)-key)
        else:
            decryptedMessage += i
    return decryptedMessage


def main():
    while True:
        print("\nDeseja Encriptar ou Desencriptar um msg:")
        print("[1] -> Encriptar")
        print("[2] -> Desencriptar")
        choice:str = str(input("-> "))
        print("-----------------------------------------")
        
        if choice == "1":
            key:int = int(input("key: "))
            plaintext:str = str(input("text: "))
            ciphertext:str = cesarCipherEncryption(plaintext, key)
            print(f"ciphertext: {ciphertext}\n")
            sleep(0.5)
            break
        
        elif choice == "2":
            key:int = int(input("key: "))
            ciphertext:str = str(input("text: "))
            plaintext:str = cesarCipherDecryption(ciphertext, key)
            print(f"plaintext: {plaintext}\n")
            sleep(0.5)
            break
        
        else:
            print("Entrada invalida! Tente novamente")
            sleep(0.8)
            system('cls')


if __name__=='__main__':
    main()