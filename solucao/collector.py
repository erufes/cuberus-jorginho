import json
import os

from PIL                    import Image

from rubik.cube             import Cube
from rubik.solve            import Solver

from classes.recortaFace    import recortarall
from classes.cor            import getCorCubo

def ajustaIMG():
    for i in range(6):
        arquivo = "face"+str(i+1)+".png"

        # creating a object 
        image = Image.open(r"fotos/"+arquivo)

        MAX_SIZE = (500, 500)
        image.thumbnail(MAX_SIZE)

        image_rotated = image.rotate(-90, expand=True)

        # Crie o diretório de saída, se não existir
        os.makedirs("fotos/adjusted/", exist_ok=True)

        # creating thumbnail
        image_rotated.save("fotos/adjusted/"+arquivo)
        # os.remove("fotos/"+arquivo)

if __name__ == '__main__':
    ajustaIMG()
    recortarall()
    
    c = Cube(getCorCubo())
    print(c)
    solver = Solver(c)
    solver.solve()
    
    #trocar o nome do .json para o nome desejado;
    with open ("solucao.txt", "w") as file:
        file.write(json.dumps(solver.moves))
        file.close()