#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from classes.braco  import Braco
from classes.base   import Base
# from classes.sensor import Sensor
import json
import time

PRESO = True
SOLTO = False
HORARIO = 'horario'
ANTIHORARIO = 'antihorario'

#arquivo = 'algoritmoDeSolucao/cubos/movimentos_cuboConfigEx1.json'
# Create your objects here.

ev3 = EV3Brick()

# Inicializa as partes do jorginho

braco =  Braco(Motor(Port.A, Direction.CLOCKWISE, None))
base =  Base(Motor(Port.B, Direction.CLOCKWISE, None), ev3)
#sensor =  Sensor(Motor(Port.C, Direction.CLOCKWISE, None))

def verificaSentido (movimento):
    if len(movimento) == 1:
        return HORARIO
    elif len(movimento) == 2:
        return ANTIHORARIO
 
def verificaMovimento(movimento):

    direcao = verificaDirecao(movimento)
    sentido = verificaSentido(movimento)

    return direcao, sentido

def verificaDirecao(movimento):
    
    if movimento == 'Fi' or movimento == 'F':
        direcao = 'frente'
        
    elif movimento == 'Ri' or movimento == 'R':
        direcao = 'direita'
        
    elif movimento == 'Ui' or movimento == 'U':
        direcao = 'cima'
        
    elif movimento == 'Li' or movimento == 'L':
        direcao = 'esquerda'
        
    elif movimento == 'Bi' or movimento == 'B':
        direcao = 'costas'
        
    elif movimento == 'Di' or movimento == 'D':
        direcao = 'baixo'
        
    elif movimento == 'Xi' or movimento == 'X':
        direcao = 'rotacionaX'
    
    elif movimento == 'Yi' or movimento == 'Y':
        direcao = 'rotacionaY'
        
    elif movimento == 'Zi' or movimento == 'Z':
        direcao = 'rotacionaZ'
        
    elif movimento == 'Mi' or movimento == 'M':
        direcao = 'meridiano'
        
    elif movimento == 'Si' or movimento == 'S':
        direcao = 'meridiano Y'
        
    elif movimento == 'Ei' or movimento == 'E':
        direcao = 'equador'
        
    return direcao
 
   
def giraBase180(direcao, estado):
    if direcao == HORARIO:
        base._movDireita(estado)
        base._movDireita(estado)
    
    elif direcao == ANTIHORARIO:
        base._movEsquerda(estado)
        base._movEsquerda(estado)

def giraCuboEixoX(direcao):
    # X
    if direcao == HORARIO:
        base._movEsquerda(SOLTO)
        braco.set_movimenta()
        base._movDireita(SOLTO)
    
    elif direcao == ANTIHORARIO:
        base._movDireita(SOLTO)
        braco.set_movimenta()
        base._movEsquerda(SOLTO)
        
def giraCuboEixoY(direcao):
    # Y
    if direcao == HORARIO:
        base._movDireita(SOLTO)
    
    elif direcao == ANTIHORARIO:
        base._movEsquerda(SOLTO)

def giraCuboEixoZ(direcao):
    # Z
    if direcao == HORARIO:
        giraBase180(HORARIO, SOLTO)
        braco.set_movimenta()
        giraBase180(HORARIO, SOLTO)

    elif direcao == ANTIHORARIO:
        braco.set_movimenta()

def movimentaFace(direcao):
    #face esquerda
    # L
    if direcao == HORARIO:
        braco.set_movimenta()
        braco._segurarCubo()
        base._movEsquerda(PRESO)
        braco._voltarPosicaoOriginal()
        giraBase180(HORARIO, SOLTO)
        braco.set_movimenta()
        giraBase180(HORARIO, SOLTO)

    elif direcao == ANTIHORARIO:
        braco.set_movimenta()
        braco._segurarCubo()
        base._movDireita(PRESO)
        braco._voltarPosicaoOriginal()
        giraBase180(ANTIHORARIO, SOLTO)
        braco.set_movimenta()
        giraBase180(ANTIHORARIO, SOLTO)

def movimentaFaceTras(direcao):
    # B
    if direcao == HORARIO:
        base._movEsquerda(SOLTO)
        movimentaFace(HORARIO)
        base._movDireita(SOLTO)
    
    elif direcao == ANTIHORARIO:
        base._movEsquerda(SOLTO)
        movimentaFace(ANTIHORARIO)
        base._movDireita(SOLTO)

def movimentaFaceFrente(direcao):
    # F
    if direcao == HORARIO:
        base._movDireita(SOLTO)
        movimentaFace(HORARIO)
        base._movEsquerda(SOLTO)
    
    elif direcao == ANTIHORARIO:
        base._movDireita(SOLTO)
        movimentaFace(ANTIHORARIO)
        base._movEsquerda(SOLTO)

def movimentaFaceDireita(direcao):
    # R
    if direcao == HORARIO:
        giraBase180(HORARIO,SOLTO)
        movimentaFace(HORARIO)
        giraBase180(HORARIO, SOLTO)
    
    elif direcao == ANTIHORARIO:
        giraBase180(ANTIHORARIO, SOLTO)
        movimentaFace(ANTIHORARIO)
        giraBase180(ANTIHORARIO, SOLTO)

def movimentaFaceSuperior(direcao):
    # U
    if direcao == HORARIO:
        giraCuboEixoZ(ANTIHORARIO)
        braco.set_movimenta()
        braco._segurarCubo()
        base._movEsquerda(PRESO)
        braco._voltarPosicaoOriginal()
        giraBase180(HORARIO, SOLTO)
        braco.set_movimenta()
        braco.set_movimenta()
        giraBase180(HORARIO, SOLTO)

    elif direcao == ANTIHORARIO:
        giraCuboEixoZ(ANTIHORARIO)
        braco.set_movimenta()
        braco._segurarCubo()
        base._movDireita(PRESO)
        braco._voltarPosicaoOriginal()
        giraBase180(HORARIO, SOLTO)
        braco.set_movimenta()
        braco.set_movimenta()
        giraBase180(HORARIO, SOLTO)

def movimentaFaceInferior(direcao):
    # D
    if direcao == HORARIO:
        braco._segurarCubo()
        base._movEsquerda(PRESO)
        braco._voltarPosicaoOriginal()
    
    elif direcao == ANTIHORARIO:
        braco._segurarCubo()
        base._movDireita(PRESO)
        braco._voltarPosicaoOriginal

def movimentaMeridiano(direcao):
    # M
    if direcao == HORARIO:
        movimentaFace(ANTIHORARIO)
        giraBase180(HORARIO,SOLTO)
        braco.set_movimenta()
        braco._segurarCubo()
        base._movEsquerda(PRESO)
        braco._voltarPosicaoOriginal()
        base._movEsquerda(SOLTO)
        braco.set_movimenta()
        

    elif direcao == ANTIHORARIO:
        movimentaFace(HORARIO)
        giraBase180(HORARIO,SOLTO)
        braco.set_movimenta()
        braco._segurarCubo()
        base._movDireita(PRESO)
        braco._voltarPosicaoOriginal()
        base._movEsquerda(SOLTO)
        braco.set_movimenta()

def movimentaEquador(direcao):
    # E
    if direcao == HORARIO:
        giraCuboEixoZ(HORARIO)
        movimentaMeridiano(HORARIO)
        giraCuboEixoZ(ANTIHORARIO)

    elif direcao == ANTIHORARIO:
        giraCuboEixoZ(HORARIO)
        movimentaMeridiano(ANTIHORARIO)
        giraCuboEixoZ(ANTIHORARIO)

def movimentaMeridianoY(direcao):
    # S
    if direcao == HORARIO:
        base._movDireita(SOLTO)
        movimentaMeridiano(HORARIO)
        base._movEsquerda(SOLTO)
    
    elif direcao == ANTIHORARIO:
        base._movDireita(SOLTO)
        movimentaMeridiano(ANTIHORARIO)
        base._movEsquerda(SOLTO)
        braco.set_movimenta()
        braco.set_movimenta()
        
# f = open(arquivo,"r")
# movimentos = json.loads(f.read())

# for i in movimentos:
#     direcao, sentido = verificaMovimento(i)

direcao = 'meridiano'
sentido = ANTIHORARIO
      
if direcao == 'rotacionaX':
    giraCuboEixoX(sentido)

elif direcao == 'rotacionaY':
    giraCuboEixoY(sentido)

elif direcao == 'rotacionaZ':
    giraCuboEixoZ(sentido)

elif direcao == 'esquerda':
    movimentaFace(sentido)

elif direcao == 'direita':
    movimentaFaceDireita(sentido)
    
elif direcao == 'cima':
    movimentaFaceSuperior(sentido)

elif direcao == 'baixo':
    movimentaFaceInferior(sentido)

elif direcao == 'frente':
    movimentaFaceFrente(sentido)
    
elif direcao == 'costas':
    movimentaFaceTras(sentido)
    
elif direcao == 'meridiano':
    movimentaMeridiano(sentido)
    
elif direcao == 'meridiano Y':
    movimentaMeridianoY(sentido)

elif direcao == 'equador':
    movimentaEquador(sentido)
    
print(direcao)
print(sentido)

#f.close()