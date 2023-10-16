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

def verificaMovimento (movimento):
    if len(movimento) == 1:
        return HORARIO
    elif len(movimento) == 2:
        return ANTIHORARIO
    
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
        base._movEsquerda()

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
        giraBase180(SOLTO)
        braco.set_movimenta()
        giraBase180(SOLTO)

    elif direcao == ANTIHORARIO:
        braco.set_movimenta()
        braco._segurarCubo()
        base._movDireita(PRESO)
        braco._voltarPosicaoOriginal()
        giraBase180(SOLTO)
        braco.set_movimenta()
        giraBase180(SOLTO)

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
        giraBase180(SOLTO)
        movimentaFace(HORARIO)
        giraBase180(SOLTO)
    
    elif direcao == ANTIHORARIO:
        giraBase180(SOLTO)
        movimentaFace(ANTIHORARIO)
        giraBase180(SOLTO)

def movimentaFaceSuperior(direcao):
    # U
    if direcao == HORARIO:
        giraCuboEixoZ(ANTIHORARIO)
        movimentaFace(HORARIO)

    elif direcao == ANTIHORARIO:
        giraCuboEixoZ(ANTIHORARIO)
        movimentaFace(ANTIHORARIO)

def movimentaFaceInferior(direcao):
    # D
    if direcao == HORARIO:
        giraCuboEixoZ(HORARIO)
        movimentaFace(HORARIO)
    
    elif direcao == ANTIHORARIO:
        giraCuboEixoZ(HORARIO)
        movimentaFace(ANTIHORARIO)

def movimentaMeridiano(direcao):
    # M
    if direcao == HORARIO:
        movimentaFace(ANTIHORARIO)
        movimentaFaceDireita(HORARIO)

    elif direcao == ANTIHORARIO:
        movimentaFace(HORARIO)
        movimentaFaceDireita(ANTIHORARIO)

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