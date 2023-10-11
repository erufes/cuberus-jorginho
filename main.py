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

preso = True
#arquivo = 'algoritmoDeSolucao/cubos/movimentos_cuboConfigEx1.json'
# Create your objects here.

ev3 = EV3Brick()

# Inicializa as partes do jorginho

braco =  Braco(Motor(Port.A, Direction.CLOCKWISE, None))
base =  Base(Motor(Port.B, Direction.CLOCKWISE, None), ev3)
#sensor =  Sensor(Motor(Port.C, Direction.CLOCKWISE, None))

def roda_eixoZ(sentido):
    
    if sentido == 'horario':
        base._movDireita(not preso)
        base._movDireita(not preso)
        braco.set_movimenta()
        base._movDireita(not preso)
        base._movDireita(not preso)
        
    else:
        braco.set_movimenta()

def roda_eixoY(sentido):
    
    if sentido == 'horario':
        base._movDireita(not preso)
    else:
        base._movEsquerda(not preso)
        
def roda_eixoX(sentido):
    
    if sentido == 'horario':
        base._movEsquerda(not preso)
        braco.set_movimenta()
        base._movDireita(not preso)
        
    else:
        base._movDireita(not preso)
        braco.set_movimenta()
        base._movEsquerda(not preso)

def movimenta_esquerda(sentido):
    
    if sentido == 'horario':
        braco.set_movimenta()
        time.sleep(0.02)
        braco._segurarCubo()
        base._movEsquerda(preso)
        braco._voltarPosicaoOriginal()
        time.sleep(1)
        base._movEsquerda(not preso)
        base._movEsquerda(not preso)
        braco.set_movimenta()
        base._movEsquerda(not preso)
        base._movEsquerda(not preso)
    else:
        braco.set_movimenta()
        time.sleep(0.02)
        braco._segurarCubo()
        base._movDireita(preso)
        braco._voltarPosicaoOriginal()
        time.sleep(1)
        base._movEsquerda(not preso)
        base._movEsquerda(not preso)
        braco.set_movimenta()
        base._movEsquerda(not preso)
        base._movEsquerda(not preso)

def movimenta_direita(sentido):
    
    if sentido == 'horario':
        roda_eixoZ(sentido)
        time.sleep(0.02)
        braco._segurarCubo()
        braco._segurarCubo()
        base._movDireita(preso)
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        time.sleep(1)
        
    else:
        roda_eixoZ('horario')
        time.sleep(0.02)
        braco._segurarCubo()
        braco._segurarCubo()
        base._movEsquerda(preso)
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        time.sleep(1)
        


def movimenta_cima(sentido):
    
    if sentido == 'horario':
        braco.set_movimenta()
        braco.set_movimenta()
        braco._segurarCubo()
        braco._segurarCubo()
        base._movEsquerda(preso)
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
    
    else:
        braco.set_movimenta()
        braco.set_movimenta()
        braco._segurarCubo()
        braco._segurarCubo()
        base._movDireita(preso)
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()

def movimenta_frente(sentido):
    if sentido == 'horario':
        base._movEsquerda(not preso)
        movimenta_esquerda('horario')
        base._movDireita(not preso)

    else:
        base._movEsquerda(not preso)
        movimenta_esquerda('anti horario')
        base._movDireita(not preso)

def movimenta_costas(sentido):
    if sentido == 'horario':
        base._movDireita(not preso)
        movimenta_esquerda('horario')
        base._movEsquerda(not preso)

    else:
        base._movDireita(not preso)
        movimenta_esquerda('anti horario')
        base._movEsquerda(not preso)

def movimenta_baixo(sentido):
    if sentido == 'horario':
        braco._segurarCubo()
        braco._segurarCubo()
        base._movEsquerda(preso)
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
        braco.set_movimenta()
        braco.set_movimenta()
    else:
        braco._segurarCubo()
        braco._segurarCubo()
        base._movDireita(preso)
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
        braco.set_movimenta()
        braco.set_movimenta()
        
def roda_meio_em_pe(sentido):
    if sentido == 'horario':
        braco.set_movimenta()
        braco._segurarCubo()
        base._movEsquerda(preso)
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
        braco.set_movimenta()
        braco._segurarCubo()
        base._movDireita(preso)
        braco._voltarPosicaoOriginal()
        base._movEsquerda(not preso)
        braco.set_movimenta()
        
        
    else:
        braco.set_movimenta()
        braco._segurarCubo()
        base._movDireita(preso)
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
        braco.set_movimenta()
        braco._segurarCubo()
        base._movEsquerda(preso)
        braco._voltarPosicaoOriginal()
        
def verifica_direcao(movimento):
    
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
        direcao = 'roda meio em pe'
        
    elif movimento == 'Si' or movimento == 'S':
        direcao = 'roda meio de lado'
        
    elif movimento == 'Ei' or movimento == 'E':
        direcao = 'roda meio deitado'
        
    return direcao
    
def verifica_sentido(movimento):

    if movimento == 'Fi' or movimento == 'Ri' or movimento == 'Ui' or movimento == 'Li' or movimento == 'Bi' or movimento == 'Di' or movimento == 'Xi' or movimento == 'Yi' or movimento == 'Zi' or movimento == 'Mi'or movimento == 'Si' or movimento == 'Ei':
        sentido = 'anti horario'
    else:
        sentido = 'horario'
    return sentido

def verifica_movimento(movimento):

    direcao = verifica_direcao(movimento)
    sentido = verifica_sentido(movimento)

    return direcao, sentido

# f = open(arquivo,"r")
# movimentos = json.loads(f.read())

# for i in movimentos:
#     direcao, sentido = verifica_movimento(i)
    
direcao = 'roda meio em pe'
sentido = 'horario'

if direcao == 'rotacionaX':
    roda_eixoX(sentido)

elif direcao == 'rotacionaY':
    roda_eixoY(sentido)

elif direcao == 'rotacionaZ':
    roda_eixoZ(sentido)

elif direcao == 'esquerda':
    movimenta_esquerda(sentido)

elif direcao == 'direita':
    movimenta_direita(sentido)
    
elif direcao == 'cima':
    movimenta_cima(sentido)

elif direcao == 'baixo':
    movimenta_baixo(sentido)

elif direcao == 'frente':
    movimenta_frente(sentido)
    
elif direcao == 'costas':
    movimenta_costas(sentido)
    
elif direcao == 'roda meio em pe':
    roda_meio_em_pe(sentido)
    
print(direcao)
print(sentido)



#f.close()

# # Movimento braço
# # braco =  Braco(Motor(Port.A, Direction.CLOCKWISE, None))
# # braco.set_sentido(1)
#
# # ev3.speaker.beep()
#
# # braco.set_movimenta()

# # Movimento Base
# # base =  Base(Motor(Port.A, Direction.CLOCKWISE, None), ev3)
# # base.set_qtdMovimentos(4)
# # base.set_Direcao('d')
#
# # base.set_movimenta()
#     
# # ev3.speaker.beep()

# # Movimento sensor
# # sensor =  Sensor(Motor(Port.A, Direction.CLOCKWISE, None))
# # sensor.set_TimerLeituraCentro(2)
# # sensor.set_TimerLeituraAresta(16)
#
# # sensor.set_movimenta()
#
# # ev3.speaker.beep()