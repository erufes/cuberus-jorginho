#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

#from classes.movimento import Movimento
from classes.braco  import Braco
from classes.base   import Base
from classes.sensor import Sensor
import json
import time

#arquivo = 'algoritmoDeSolucao/cubos/movimentos_cuboConfigEx1.json'
# Create your objects here.

ev3 = EV3Brick()

# Inicializa as partes do jorginho

braco =  Braco(Motor(Port.A, Direction.COUNTERCLOCKWISE, None))
base =  Base(Motor(Port.B, Direction.CLOCKWISE, None), ev3)
#sensor =  Sensor(Motor(Port.C, Direction.CLOCKWISE, None))
def movimenta_esquerda(sentido):
    if sentido == 'horario':
        base._movEsquerda()
        braco.set_movimenta()
        braco._segurarCubo()
        #time.sleep(1)
        braco._segurarCubo()
        base._movEsquerda()
        braco._voltarPosicaoOriginal()
        braco._voltarPosicaoOriginal()
        base.ajeitadinha()
        time.sleep(1)
        # braco.set_movimenta()
        # base.ajeitadinha()
        # braco.set_movimenta()
        # base.ajeitadinha()
        # base._movEsquerda()
        # braco._girarCubo()
        # braco._voltarPosicaoOriginal()
        # base._movDireita()
        


def movimenta_direita(sentido):
     if sentido == 'horario':
        braco._segurarCubo()
        braco._girarCubo()
        braco._voltarPosicaoOriginal()
        base._movDireita()
        braco._segurarCubo()
        braco._girarCubo()
        time.sleep(1)
        braco._segurarCubo()
        base._movEsquerda()
        braco._girarCubo()
        braco._voltarPosicaoOriginal()
        base._movEsquerda()


# def movimenta_baixo(sentido):
#     if sentido == 'horario':

#     else:

<<<<<<< Updated upstream:main.py
def movimenta_cima(sentido):
    if sentido == 'horario':

    else:
=======
# def movimenta_cima(sentido):
#     if sentido == 'horario':
#         braco._segurarCubo()
#         braco._girarCubo()
        
#     else:
>>>>>>> Stashed changes:collector/main.py

# def movimenta_frente(sentido):
#     if sentido == 'horario':

#     else:

def roda_eixoX(sentido):
    
    if sentido == 'horario':
        base._movDireita()
        base._movDireita()
        braco._segurarCubo()
        braco._girarCubo()
<<<<<<< Updated upstream:main.py
=======
        braco._voltarPosicaoOriginal()
        base._movDireita()
        base._movDireita()
>>>>>>> Stashed changes:collector/main.py
        
    else:
        braco._segurarCubo()
        braco._girarCubo()

def roda_eixoY(sentido):
    
    if sentido == 'horario':
        base._movDireita()
    else:
        base._movEsquerda()
        
def roda_eixoZ(sentido):
    
    if sentido == 'horario':
        base._movDireita()
        braco._segurarCubo()
        braco._girarCubo()
<<<<<<< Updated upstream:main.py
        base_hor._movEsquerda()
=======
        braco._voltarPosicaoOriginal()
        base._movEsquerda()
>>>>>>> Stashed changes:collector/main.py
        
    else:
        base._movEsquerda()
        braco._segurarCubo()
        braco._girarCubo()
<<<<<<< Updated upstream:main.py
        base_hor._movDireita()
=======
        braco._voltarPosicaoOriginal()
        base._movDireita()
>>>>>>> Stashed changes:collector/main.py

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
    
<<<<<<< Updated upstream:main.py
    if direcao == 'rotacionaX':
        
    elif direcao == 'rotacionaY':
        
    elif direcao == 'rotacionaZ':
    
    elif direcao == 'rotacionaX':
=======
#     if direcao == 'rotacionaX':
#         roda_eixoX(sentido)
        
#     elif direcao == 'rotacionaY':
#         roda_eixoY(sentido)
        
#     elif direcao == 'rotacionaZ':
#         roda_eixoZ(sentido)
direcao = 'esquerda'
sentido = 'horario'


if direcao == 'rotacionaX':
    roda_eixoX(sentido)
        
elif direcao == 'rotacionaY':
    roda_eixoY(sentido)
        
elif direcao == 'rotacionaZ':
    roda_eixoZ(sentido)
elif direcao == 'esquerda':
    movimenta_esquerda(sentido)
>>>>>>> Stashed changes:collector/main.py
        
    # elif direcao == 'rotacionaX':
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