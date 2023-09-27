import numpy as np
import argparse
import cv2
import os
import json

cores = { 
    "Branco": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ],
    "Vermelho": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ],
    "Azul": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ],
    "Verde": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ], 
    "Amarelo": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ], 
    "Laranja": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}

boundaries = [                                                    #LISTA PARAMETRO DAS CORES
    ([50, 180, 210], [90, 210, 240]),      # amarelo 0
    ([0, 153, 0], [110, 255, 102]),        # verde 1
    ([0, 102, 230], [102, 178, 255]),      # laranja 2
    ([30, 30, 200], [90, 80, 230]),        # vermelho 3
    ([100, 90, 90], [255, 255, 255]),      # branco 
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
imagensDefinidas = ["", "", "", "", "", ""]


def DefinirCentroFace(posicaoCorEncontrada, posicaoCaminhoImg):          #FUNCAO PARA RENOMEAR AS IMAGENS DE ACORDO COM O CENTRO DU CUBO
    if (posicaoCorEncontrada == 0):                                      #se a cor encontrada foi amarelo... (baseado nalista boundaries)
        novoNome = "Amarelo.png"
        imagensDefinidas[posicaoCaminhoImg] = "Amarelo.png"
    elif (posicaoCorEncontrada == 1):
        novoNome = "Verde.png"
        imagensDefinidas[posicaoCaminhoImg] = "Verde.png"
    elif (posicaoCorEncontrada == 2):
        novoNome = "Laranja.png"
        imagensDefinidas[posicaoCaminhoImg] = "Laranja.png"
    elif (posicaoCorEncontrada == 3):
        novoNome = "Vermelho.png"
        imagensDefinidas[posicaoCaminhoImg] = "Vermelho.png"
    elif (posicaoCorEncontrada == 4):
        novoNome = "Branco.png"
        imagensDefinidas[posicaoCaminhoImg] = "Branco.png"
    elif (posicaoCorEncontrada == 5):
        novoNome = "Azul.png"
        imagensDefinidas[posicaoCaminhoImg] = "Azul.png"

    nomeAntigo = imagensIniciais[posicaoCaminhoImg]
    nomeNovo = novoNome
    os.rename(nomeAntigo, nomeNovo)


def RetornarCorEncontrada(corEncontrada):
    if (corEncontrada == 0):                                                      
        return "Amarelo"
    elif (corEncontrada == 1):
        return "Verde"
    elif (corEncontrada == 2):
        return "Laranja"
    elif (corEncontrada == 3):
        return "Vermelho"
    elif (corEncontrada == 4):
        return "Branco"
    elif (corEncontrada == 5):
        return "Azul"
    

def RetornarDataFace(imagem):
    if (imagem == 'Vermelho.png'):
        return 'Vermelho'
    elif (imagem == 'Verde.png'):
        return 'Verde'
    elif (imagem == 'Laranja.png'):
        return 'Laranja'
    elif (imagem == 'Azul.png'):
        return 'Azul'
    elif (imagem == 'Branco.png'):
        return 'Branco'
    elif (imagem == 'Amarelo.png'):
        return 'Amarelo'


def ArmazenarCorEncontrada(corEncontrada, parteXcubo, parteYcubo, imagem):
    encontrouCor = RetornarCorEncontrada(corEncontrada)
    dataFace = RetornarDataFace(imagem)
    
    with open('cubo.json', 'r') as json_file:
        dados = json.load(json_file)

    for i in range(3):
        for j in range (3):
            if ((i == parteYcubo)and(j == parteXcubo)):
                dados[dataFace][i][j] = encontrouCor
    return dados
    

def DeletarRestoCores(excecao):
    for i, cor in enumerate(lista):
        if (cor != excecao):
            del cores[cor]

 
def IniciarArquivo(imgCaminho, arquivoPng): 
    if (imgCaminho == 0):                     #FUNCAO QUE INICIA O ARQUIVO CUBO.JSON
        if (arquivoPng == 'Vermelho.png'):                   #vai verificar em qual posicao 
            excecao = 'Vermelho'
        elif (arquivoPng == 'Verde.png'):
            excecao = 'Verde'
        elif (arquivoPng == 'Laranja.png'):
            excecao = 'Laranja'
        elif (arquivoPng == 'Azul.png'):
            excecao = 'Azul'
        elif (arquivoPng == 'Branco.png'):
            excecao = 'Branco'
        elif (arquivoPng == 'Amarelo.png'):
            excecao = 'Amarelo'
        DeletarRestoCores(excecao)
    
    else:
        if (arquivoPng == 'Vermelho.png'):                   #vai verificar em qual posicao 
            fazerFace = 'Vermelho'
        elif (arquivoPng == 'Verde.png'):
            fazerFace = 'Verde'
        elif (arquivoPng == 'Laranja.png'):
            fazerFace = 'Laranja'
        elif (arquivoPng == 'Azul.png'):
            fazerFace = 'Azul'
        elif (arquivoPng == 'Branco.png'):
            fazerFace = 'Branco'
        elif (arquivoPng == 'Amarelo.png'):
            fazerFace = 'Amarelo'
        cores[fazerFace] = [["","",""], ["","",""], ["","",""]]
    with open('cubo.json', 'w') as json_file:
        json.dump(cores, json_file, indent=2)


imgCaminho, caminhoImg, defCor, verificaJson = 0, 0, 0, 0

for caminhoImg, caminho in enumerate(imagensIniciais):             #esse loop pega os caminhos de imagem da lista de imagens iniciais e 
    image = cv2.imread(caminho)                                    #define a cor do meio do cubo na foto, renomeando pra cor indicada
    (h, w) = image.shape[:2]

    rgbCentro = image[217, 112]
    parametroCor = 0

    for parametroCor, (lower, upper) in enumerate(boundaries):
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        if ((lower[0] <= rgbCentro[0]) and (rgbCentro[0] <= upper[0])):
            if ((lower[1] <= rgbCentro[1]) and (rgbCentro[1] <= upper[1])):
                if ((lower[2] <= rgbCentro[2]) and (rgbCentro[2] <= upper[2])):
                    DefinirCentroFace(parametroCor, caminhoImg)
                    break

for imgCaminho, imagem in enumerate(imagensDefinidas):                   #esse loop pega os novos caminhos de imagem e define as cores em cada parte do cubo
    image = cv2.imread(imagem)
    (h, w) = image.shape[:2]

    if (defCor == 1):
        os.remove(imagensDefinidas[imgCaminho-1])
    
    IniciarArquivo(imgCaminho, imagem)  
    defCor=0
    coordenada = 0

    for coordenada, (y, x) in enumerate(listaCoordenadas):
        rgb = image[y, x]
        coordenadaX, coordenadaY = partesCubo[coordenada]
        parametroCor = 0

        for parametroCor, (lower, upper) in enumerate(boundaries):
            if (defCor==1):
                break
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")

            if ((lower[0] <= rgb[0]) and (rgb[0] <= upper[0])):
                if ((lower[1] <= rgb[1]) and (rgb[1] <= upper[1])):
                    if ((lower[2] <= rgb[2]) and (rgb[2] <= upper[2])):
                        dados = ArmazenarCorEncontrada(parametroCor, coordenadaX, coordenadaY, imagem)
                        with open('cubo.json', 'w') as json_file:
                            json.dump(dados, json_file, indent=2)
    if (imgCaminho == 5):
        os.remove(imagensDefinidas[imgCaminho])
    defCor=1
            