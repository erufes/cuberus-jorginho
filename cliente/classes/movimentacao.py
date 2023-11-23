#!/usr/bin/env pybricks-micropython
PRESO = True
SOLTO = False
HORARIO = 'Horario'
ANTIHORARIO = 'Antihorario'

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
    sentido = ""
    if direcao == ANTIHORARIO:
        sentido = "i"
    # D
    return ["PV", sentido + "PH", "SV"]

def movimentaMeridiano(direcao):
    sentido = ""
    if direcao == ANTIHORARIO:
        sentido = "i"
    
    # M
    mov = movimentaFace(direcao) + giraBase180(HORARIO,SOLTO)
    
    mov += ["V", "PV", sentido+"PH", "SV", "iSH", "V"]
    
    return mov

def movimentaEquador(direcao):
    sentido1 = ""
    sentido2 = ""
    
    if direcao == HORARIO:
        sentido2 = "i"
        
    if direcao == ANTIHORARIO:
        sentido1 = "i"
    
    # E
    mov = ["PV", sentido1+"PH", "SV", "V", "V", "PV", sentido2+"PH", "SV", sentido1+"PH", "V", "V"]
    return mov

def movimentaMeridianoY(direcao):
    # S
    mov = ["SH"] + movimentaMeridiano(direcao) + ["iSH"]

    if direcao == ANTIHORARIO:
        mov += ["V", "V"]
        
    return mov