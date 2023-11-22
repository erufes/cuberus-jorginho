#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

from classes.braco  import Braco
from classes.base   import Base

PRESO = True
SOLTO = False
HORARIO = 'Horario'
ANTIHORARIO = 'Antihorario'

ev3 = EV3Brick()

braco =  Braco(Motor(Port.A, Direction.CLOCKWISE, None))
base =  Base(Motor(Port.B, Direction.CLOCKWISE, None), ev3)
    
def giraBase180(direcao, estado):
    sentido = ""
    est     = "S"
    
    if direcao  == ANTIHORARIO:
        sentido = "i"
    if estado   == PRESO:
        est     = "P"
        
    return [sentido+est+"H",sentido+est+"H"]

def giraCuboEixoX(direcao):
    sentido1 = ""
    sentido2 = ""
    
    # X
    if direcao == HORARIO:
        sentido1 = "i"
    elif direcao == ANTIHORARIO:
        sentido2 = "i"
        
    return [sentido1+"SH", "V", sentido2+"SH"]
        
def giraCuboEixoY(direcao):
    sentido = ""
    # Y
    if direcao == ANTIHORARIO:
        sentido = "i"
        
    return [sentido+"SH"]

def giraCuboEixoZ(direcao):
    mov = []
    # Z
    if direcao == HORARIO:
        mov += giraBase180(HORARIO, SOLTO)
        mov += ["V"]
        mov += giraBase180(HORARIO, SOLTO)

    elif direcao == ANTIHORARIO:
        mov += ["V"]
    
    return mov

def movimentaFace(direcao):
    sentido = ""
    
    # face esquerda
    # L
    if direcao == ANTIHORARIO:
        sentido = "i"
    
    mov = ["V", "PV", sentido+"PH", "SV"] + giraBase180(direcao, SOLTO) + ["V"] + giraBase180(direcao, SOLTO)
    return mov
        
def movimentaFaceTras(direcao):
    # B
    mov = ["iSH"] + movimentaFace(direcao) + ["SH"]
    return mov

def movimentaFaceFrente(direcao):
    # F    
    mov = ["SH"] + movimentaFace(direcao) + ["iSH"]
    return mov

def movimentaFaceDireita(direcao):
    # R
    mov = giraBase180(direcao,SOLTO) + movimentaFace(direcao) + giraBase180(direcao, SOLTO)
    return mov

def movimentaFaceSuperior(direcao):
    # U
    mov = giraCuboEixoZ(ANTIHORARIO) + ["V", "PV"]
    
    sentido = ""
    if direcao == ANTIHORARIO:
        sentido = "i"
        
    mov += [sentido + "PH", "SV"] + giraBase180(HORARIO, SOLTO) + ["V", "V"] + giraBase180(HORARIO, SOLTO)
    
    return mov

def movimentaFaceInferior(direcao):
    # D
    if direcao == HORARIO:
        braco._segurarCubo()
        base._movAntHorario(PRESO)
        braco._voltarPosicaoOriginal()
    
    elif direcao == ANTIHORARIO:
        braco._segurarCubo()
        base._movHorario(PRESO)
        braco._voltarPosicaoOriginal()

def movimentaMeridiano(direcao):
    # M
    if direcao == HORARIO:
        movimentaFace(ANTIHORARIO)
        giraBase180(HORARIO,SOLTO)
        braco.set_movimenta()
        braco._segurarCubo()
        base._movAntHorario(PRESO)
        braco._voltarPosicaoOriginal()
        base._movAntHorario(SOLTO)
        braco.set_movimenta()
        

    elif direcao == ANTIHORARIO:
        movimentaFace(HORARIO)
        giraBase180(HORARIO,SOLTO)
        braco.set_movimenta()
        braco._segurarCubo()
        base._movHorario(PRESO)
        braco._voltarPosicaoOriginal()
        base._movAntHorario(SOLTO)
        braco.set_movimenta()

def movimentaEquador(direcao):
    # E
    if direcao == HORARIO:
        braco._segurarCubo()
        base._movHorario(PRESO)
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
        braco.set_movimenta()
        braco._segurarCubo()
        base._movAntHorario(PRESO)
        braco._voltarPosicaoOriginal()
        base._movHorario(SOLTO)
        braco.set_movimenta()
        braco.set_movimenta()

    elif direcao == ANTIHORARIO:
        braco._segurarCubo()
        base._movAntHorario(PRESO)
        braco._voltarPosicaoOriginal()
        braco.set_movimenta()
        braco.set_movimenta()
        braco._segurarCubo()
        base._movHorario(PRESO)
        braco._voltarPosicaoOriginal()
        base._movAntHorario(SOLTO)
        braco.set_movimenta()
        braco.set_movimenta()

def movimentaMeridianoY(direcao):
    # S
    if direcao == HORARIO:
        base._movHorario(SOLTO)
        movimentaMeridiano(HORARIO)
        base._movAntHorario(SOLTO)
    
    elif direcao == ANTIHORARIO:
        base._movHorario(SOLTO)
        movimentaMeridiano(ANTIHORARIO)
        base._movAntHorario(SOLTO)
        braco.set_movimenta()
        braco.set_movimenta()