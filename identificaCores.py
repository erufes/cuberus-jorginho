import numpy as np
import argparse
import cv2
import os

boundaries = [                                                    #LISTA PARAMETRO DAS CORES
    ([50, 180, 210], [90, 210, 240]),      # amarelo 0
    ([0, 153, 0], [110, 255, 102]),        # verde 1
    ([0, 102, 230], [102, 178, 255]),      # laranja 2
    ([30, 30, 200], [90, 80, 230]),        # vermelho 3
    ([180, 180, 204], [255, 255, 255]),    # branco 4
    ([86, 31, 4], [220, 135, 70]),         # azul  5
]

listaCoordenadas = [                                              #LISTA DAS COORDENADAS DE CADA PARTE DO CUBO
    ([169, 50]),          # coordenada 0,0      0
    ([219, 51]),          # coordenada 0,1      1
    ([280, 47]),          # coordenada 0,2      2
    ([165, 111]),         # coordenada 1,0      3
    ([217, 112]),         # coordenada 1,1      4     CENTRO
    ([280, 116]),         # coordenada 1,2      5
    ([165, 171]),         # coordenada 2,0      6
    ([216, 178]),         # coordenada 2,1      7
    ([275, 182]),         # coordenada 2,2      8
]

partesCubo = [                                                    #LISTA DAS PARTES DO CUBO
    ([0, 0]),    # 0
    ([0, 1]),    # 1
    ([0, 2]),    # 2
    ([1, 0]),    # 3
    ([1, 1]),    # 4
    ([1, 2]),    # 5
    ([2, 0]),    # 6
    ([2, 1]),    # 7
    ([2, 2]),    # 8
]

lista = ["Amarelo", "Verde", "Laranja", "Vermelho", "Branco", "Azul"]

imagensIniciais = ["face1.png", "face2.png", "face3.png", "face4.png", "face5.png", "face6.png"]
imagensDefinidas = ["Amarelo.png", "Verde.png", "Laranja.png", "Vermelho.png", "Branco.png", "Azul.png"]


def DefinirCentroFace(posicaoCorEncontrada, posicaoCaminhoImg):          #FUNCAO PARA RENOMEAR AS IMAGENS DE ACORDO COM O CENTRO DU CUBO
    nomeAntigo = imagensIniciais[posicaoCaminhoImg]
    nomeNovo = imagensDefinidas[posicaoCorEncontrada]
    os.rename(nomeAntigo, nomeNovo)

#def MontarArquivo(imagens, j):                                           #FUNCAO QUE FAZ O ARQUIVO CUBO.JSON
   
imgCaminho, caminhoImg = 0, 0

for caminhoImg, caminho in enumerate(imagensIniciais):             #esse loop pega os caminhos de imagem da lista de imagens iniciais e 
    image = cv2.imread(caminho)                                    #define a cor do meio do cubo na foto, renomeando pra cor indicada
    (h, w) = image.shape[:2]
    cv2.imshow("Original", image)

    rgbCentro = image[217, 112]
    parametroCor = 0

    for parametroCor, (lower, upper) in enumerate(boundaries):
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        if ((lower[0] <= rgbCentro[0]) and (rgbCentro[0] <= upper[0])):
            if ((lower[1] <= rgbCentro[1]) and (rgbCentro[1] <= upper[1])):
                if ((lower[2] <= rgbCentro[2]) and (rgbCentro[2] <= upper[2])):
                    DefinirCentroFace(parametroCor, caminhoImg)
                    print("> Cor do centro do cubo:")
                    print(lista[parametroCor])
                    break

for imgCaminho, imagem in enumerate(imagensDefinidas):                   #esse loop pega os novos caminhos de imagem e define as cores em cada parte do cubo
    image = cv2.imread(imagem)
    (h, w) = image.shape[:2]
    cv2.imshow("Original", image)

    coordenda = 0

    for coordenada, (y, x) in enumerate(listaCoordenadas):
        rgb = image[y, x]
        coordenadaX, coordenadaY = partesCubo[coordenada]
        parametroCor = 0

        for parametroCor, (lower, upper) in enumerate(boundaries):
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")

            if ((lower[0] <= rgb[0]) and (rgb[0] <= upper[0])):
                if ((lower[1] <= rgb[1]) and (rgb[1] <= upper[1])):
                    if ((lower[2] <= rgb[2]) and (rgb[2] <= upper[2])):
                        #MontarArquivo(c, j)
                        print("> Cor na coordenada ({},{}) da parte {},{} do cubo:".format(x, y, coordenadaX, coordenadaY))
                        print(lista[parametroCor])
                        break
  
