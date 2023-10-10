from classes.ordenacao  import *
from PIL import Image
import numpy as np
import cv2

boundaries = [
	([0, 173, 192], [90, 220, 242]),      #amarelo
	([0, 153, 0], [110, 255, 102]),        #verde
	([0, 102, 230], [102, 178, 255]),      #laranja
	([20, 14, 180], [90, 80, 240]),        #vermelho
	([165, 170, 170], [210, 225, 220]),    #branco
	([86, 31, 4], [220, 155, 70]),         #azul 
]

listaCoordenadas = [                                              #LISTA DAS COORDENADAS DE CADA PARTE DO CUBO
    [37, 37],          # coordenada 0,0      
    [110, 37],         # coordenada 0,1      
    [183, 37],         # coordenada 0,2      
    [31, 103],          # coordenada 1,0      
    [114, 103],         # coordenada 1,1           CENTRO
    [188, 103],         # coordenada 1,2      
    [40, 179],          # coordenada 2,0      
    [125, 179],         # coordenada 2,1      
    [190, 165],         # coordenada 2,2      
]

lista = [
    ("Y", "Amarelo"),
    ("G", "Verde"), 
    ("O", "Laranja"), 
    ("R", "Vermelho"), 
    ("W", "Branco"), 
    ("B", "Azul")  
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
        for dy in range(-2, 3):  # Altere o alcance de dy
            for dx in range(-2, 3):  # Altere o alcance de dx
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < image.shape[0] and 0 <= new_x < image.shape[1]:
                    rgb = image[new_y, new_x]
                    cor = getCor(rgb)
                    if cor is not None:
                        cores_proximas.append(cor)
                    else:
                        cores_proximas.append("N")
        
        # Encontrar a cor mais frequente na área maior
        if cores_proximas:
            cor_mais_frequente = max(set(cores_proximas), key=cores_proximas.count)
            linha.append(cor_mais_frequente)
            
        if len(linha) == 3:
            face.append(linha)
            linha = []
    return face

def getCorCubo():
    cubo = {}
    ordem_leitura=[]

    for i in range(6):
        arquivo = "fotos/face"+str(i+1)+".png"
        
        img = cv2.imread(arquivo)
        
        face = getCorFace(img)
        print(face)
        
        cv2.imshow("Face - "+str(i+1), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        centro = list(filter(lambda x: x[0] == face[1][1], lista))[0][1]
        
        cubo[centro] = face
        ordem_leitura.append(centro)
        # os.remove(arquivo)
    
    cubo = ordena(cubo, ordem_leitura)
    return getSTRCubo(cubo, ordem_leitura)