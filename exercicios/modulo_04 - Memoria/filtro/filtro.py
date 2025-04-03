import sys
from PIL import Image, ImageFilter # type: ignore

def main(argv):
    # abrindo imagem
    img = Image.open(argv[1])
    
    escolha = int(input("Escolha um filtro: \n1 - Blur\n2 - Cinza\n3 - Espelhar\n-> "))
    
    match escolha:
        case 1:
            img_blur = img.filter(ImageFilter.BLUR)
            img_blur.show()
            img_blur.save(argv[2])
        case 2:
            img_cinza = img.convert("L")
            img_cinza.show()
            img_cinza.save(argv[2])
        case 3:
            img_espelhada = img.transpose(Image.FLIP_LEFT_RIGHT)
            img_espelhada.show()
            img_espelhada.save(argv[2])

        
    # convertendo para escala de cinza
    img_cinza = img.convert("L")

if __name__ == "__main__":
    main(sys.argv)
