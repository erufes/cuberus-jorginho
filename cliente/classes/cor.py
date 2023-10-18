from classes.ordenacao  import *
from PIL import Image
import numpy as np
import cv2

boundaries = [
    ([144, 32, 0], [255, 220, 136]),     # azul 
    ([60, 173, 36], [202, 255, 155]),    # verde
    
	([18, 89, 245], [112, 211, 255]),   # laranja
	([59, 157, 201], [169, 255, 255]),  # amarelo
	([7, 8, 176], [120, 148, 255]),       # vermelho
 
	([175, 140, 144], [255, 255, 255]), # branco
]

lista = [
    ("B", "Azul"),
    ("G", "Verde"), 
    
    ("O", "Laranja"), 
    ("Y", "Amarelo"),
    ("R", "Vermelho"), 
    
    ("W", "Branco"), 
]

listaCoordenadas = [                                              #LISTA DAS COORDENADAS DE CADA PARTE DO CUBO
    [58, 28],          # coordenada 0,0      
    [155, 26],          # coordenada 0,1      
    [239, 31],          # coordenada 0,2      
    [53, 82],           # coordenada 1,0      
    [146, 89],          # coordenada 1,1           CENTRO
    [250, 91],          # coordenada 1,2      
    [54, 158],          # coordenada 2,0      
    [147, 160],         # coordenada 2,1      
    [249, 166],         # coordenada 2,2      
]


def getSTRCubo(cubo, ordem_leitura):
    ordem_str = [ordem_leitura[0], ordem_leitura[3], ordem_leitura[5],ordem_leitura[1],ordem_leitura[4],ordem_leitura[2]]
    
    # transforma em string face 1
    str_concatenada = ''.join([elemento for linha in cubo[ordem_str[0]] for elemento in linha])
    
    # transforma em string faces de 2 a 5
    str_concatenada += ''.join([elemento for i in range(3) for face in ordem_str[1:-1] for elemento in cubo[face][i]])
    
    # transforma em string face 6
    str_concatenada += ''.join([elemento for linha in cubo[ordem_str[-1]] for elemento in linha])
    
    return str_concatenada

def getCor(rgb):
    for parametroCor, (lower, upper) in enumerate(boundaries):
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            if ((lower[0] <= rgb[0]) and (rgb[0] <= upper[0])):
                if ((lower[1] <= rgb[1]) and (rgb[1] <= upper[1])):
                    if ((lower[2] <= rgb[2]) and (rgb[2] <= upper[2])):
                        return lista[parametroCor][0]

def getCorFace(image):
    face, linha = [], []
    
    for (x, y) in listaCoordenadas:
        # Coletar cores em uma área maior ao redor do ponto
        cores_proximas = []
        for dy in range(-3, 4):  # Altere o alcance de dy
            for dx in range(-3, 4):  # Altere o alcance de dx
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < image.shape[0] and 0 <= new_x < image.shape[1]:
                    rgb = image[new_y, new_x]
                    cor = getCor(rgb)
                    if cor is not None:
                        cores_proximas.append(cor)
        
        # Encontrar a cor mais frequente na área maior
        if len(cores_proximas) == 0:
            linha.append("N")
        elif cores_proximas:
            cor_mais_frequente = max(set(cores_proximas), key=cores_proximas.count)
            linha.append(cor_mais_frequente)
            
        if len(linha) == 3:
            face.append(linha)
            linha = []
    return face

def getCorCubo(debug = False):
    cubo = {}
    ordem_leitura=[]

    for i in range(6):
        arquivo = "fotos/recortados/face"+str(i+1)+".png"
        # arquivo = "fotos/adjusted/face"+str(i+1)+".png"
        img = cv2.imread(arquivo)
        
        face = getCorFace(img)
        
        print(face)
        if debug:
            print(face)
            cv2.imshow("Face - "+str(i+1), img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        centro = list(filter(lambda x: x[0] == face[1][1], lista))[0][1]
        
        cubo[centro] = face
        ordem_leitura.append(centro)
    
    cubo = ordena(cubo, ordem_leitura)
    print(getSTRCubo(cubo, ordem_leitura))
    return getSTRCubo(cubo, ordem_leitura)