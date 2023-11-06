import json
from rubik.cube import Cube
from resolucaoCubo import *
from cubos import *

#Este programa serve para traduzir o json com a configuração do cubo
#de uma forma que seja legível para a lib, visando a resolução do 
#quebra-cabeça.
#A orientação do cubo deve ser com o amarelo como +Z, o azul como +X e o vermelho como +Y;
def leArquivo (arquivo):
    #Colocar o nome do .json com o arquivo desejado;
    with open (arquivo) as file:
        return json.load(file)
data = leArquivo()
#Define a ordem das cores lidas pela lib;
ordemMeio = ["Laranja", "Azul", "Vermelho", "Verde"]

#Realiza a tradução do modo como é escrito o json para o modo como a lib lê o cubo;
def traduz (cor):
    if cor == "Branco":
        return "W"
    if cor == "Vermelho":
        return "R"
    if cor == "Azul":
        return "B"
    if cor == "Laranja":
        return "O"
    if cor == "Verde":
        return "G"
    if cor == "Amarelo":
        return "Y"
    
#Adiciona uma linha de uma face para a string que será lida pela lib;
def leLinha (face, linha):
    line = traduz(data[face][linha][0])+traduz(data[face][linha][1])+traduz(data[face][linha][2])
    return line

#Adiciona uma face inteira para a string;
def leFace (face):
    line = leLinha(face, 0)+leLinha(face, 1)+leLinha(face, 2)
    return line

#Cria a string que será usada pela lib para montar o cubo;
def leCubo ():
    config = leFace("Amarelo")
    for n in range (3):
        for cor in ordemMeio:
            config += leLinha(cor, n)
    config += leFace("Branco")

    return config

resolveCubo(str(leCubo()))