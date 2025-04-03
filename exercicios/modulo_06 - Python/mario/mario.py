def main():
    altura:int = int(input("Hight: "))
    
    for i in range(altura):
        print(" " * (altura - i - 1) + "#" * (i + 1))


if __name__ == '__main__':
    main()
