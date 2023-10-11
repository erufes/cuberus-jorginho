import os
from PIL                    import Image


def ajustaIMG(rotate=False):
    for i in range(6):
        arquivo = "face"+str(i+1)+".png"

        # creating a object 
        image = Image.open(r"solucao/fotos/"+arquivo)

        MAX_SIZE = (500, 500)
        image.thumbnail(MAX_SIZE)

        image_rotated = image
        if rotate:
            image_rotated = image.rotate(-90, expand=True)

        # Crie o diretório de saída, se não existir
        os.makedirs("solucao/fotos/adjusted/", exist_ok=True)

        # creating thumbnail
        image_rotated.save("solucao/fotos/adjusted/"+arquivo)
        os.remove("solucao/fotos/"+arquivo)