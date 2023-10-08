import numpy as np
import cv2
import os
import json

boundaries = [                                                    #LISTA PARAMETRO DAS CORES
    ([50, 180, 210], [90, 210, 240]),      # amarelo 0
    ([0, 153, 0], [110, 255, 102]),        # verde 1
    ([0, 102, 230], [102, 178, 255]),      # laranja 2
    ([30, 30, 200], [90, 80, 230]),        # vermelho 3
    ([100, 90, 90], [255, 255, 255]),      # branco 
    ([86, 31, 4], [220, 135, 70]),         # azul  5
]
listaCoordenadas = [                                              #LISTA DAS COORDENADAS DE CADA PARTE DO CUBO
    [169, 50],          # coordenada 0,0      
    [165, 111],         # coordenada 0,1      
    [165, 171],         # coordenada 0,2      
    [219, 51],          # coordenada 1,0      
    [217, 112],         # coordenada 1,1           CENTRO
    [216, 178],         # coordenada 1,2      
    [280, 47],          # coordenada 2,0      
    [280, 116],         # coordenada 2,1      
    [275, 182],         # coordenada 2,2      
]

lista = ["Amarelo", "Verde", "Laranja", "Vermelho", "Branco", "Azul"]

def giraFace(face, sentido="antiorario", n=1):
    
    if sentido == "antiorario":
        for _ in range(n):
            # Transformar as linhas em colunas
            face = list(map(list, zip(*[list(reversed(linha)) for linha in face])))
    else:
        for _ in range(n):
            # Transformar as linhas em colunas sem inverter
            face = [list(linha) for linha in zip(*face[::-1])]

    return face

def ordena(cubo, ordem_leitura):
    for i, item in enumerate(ordem_leitura):
        if(i == 0 and item == "Amarelo"):
            cubo["Amarelo"] = giraFace(cubo["Amarelo"],  "antiorario")
        elif(i == 1 and item == "Vermelho"):
            pass
        elif(i == 2 and item == "Branco"):
            cubo["Branco"] = giraFace(cubo["Branco"],  "horario")
        elif(i == 3 and item == "Laranja"):
            cubo["Laranja"] = giraFace(cubo["Laranja"], "horario", 2)
        elif(i == 4 and item == "Verde"):
            cubo["Verde"] = giraFace(cubo["Verde"],  "antiorario")
        elif(i == 5 and item == "Azul"):
            cubo["Verde"] = giraFace(cubo["Verde"],  "antiorario")
        else:
            print("Cubo fora de posição")
    return cubo

def getCor(rgb):
    for parametroCor, (lower, upper) in enumerate(boundaries):
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            if ((lower[0] <= rgb[0]) and (rgb[0] <= upper[0])):
                if ((lower[1] <= rgb[1]) and (rgb[1] <= upper[1])):
                    if ((lower[2] <= rgb[2]) and (rgb[2] <= upper[2])):
                        return lista[parametroCor]

def getCorFace(image):
    face, linha  = [], []
    
    for (y, x) in listaCoordenadas:
        rgb = image[y, x]
        linha.append(getCor(rgb))
        if len(linha) == 3:
            face.append(linha)
            linha = []
    return face

def getCubo():
    cubo = {}
    ordem_leitura=[]
    
    for i in range(6):
        arquivo = "face"+str(i+1)+".png"
        
        image = cv2.imread(arquivo)
        (h, w) = image.shape[:2]
        
        face = getCorFace(image)
        cubo[face[1][1]] = face
        ordem_leitura.append(face[1][1])
        
        # os.remove(arquivo)
    return ordena(cubo, ordem_leitura)

if __name__ == '__main__':
    
    with open('cubo.json', 'w') as json_file:
        json.dump(getCubo(), json_file, indent=2)