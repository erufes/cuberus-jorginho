from base import Base
from braco import Braco

class Movimento():
    def verifica_sentido(movimento):

        if movimento == 'Fi' or movimento == 'Ri' or movimento == 'Ui' or movimento == 'Li' or movimento == 'Bi' or movimento == 'Di' or movimento == 'Xi' or movimento == 'Yi' or movimento == 'Zi' or movimento == 'Mi'or movimento == 'Si' or movimento == 'Ei':
            sentido = 'anti horario'
        else:
            sentido = 'horario'
        return sentido

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
            
        
    def verifica_movimento(movimento):

        direcao = verifica_direcao(movimento)
        sentido = verifica_sentido(movimento)

        return direcao, sentido

    def movimenta_esquerda(sentido):
        if sentido == 'horario':

        else:

    def movimenta_direita(sentido):
        if sentido == 'horario':

        else:

    def movimenta_baixo(sentido):
        if sentido == 'horario':

        else:

    def movimenta_cima(sentido):
        if sentido == 'horario':

        else:

    def movimenta_frente(sentido):
        if sentido == 'horario':

        else:

    def movimenta_tras(sentido):
        if sentido == 'horario':

        else:

    def roda_eixoX(sentido):
        if sentido == 'horario':

        else:

    def roda_eixoY(sentido):
        if sentido == 'horario':

        else:
    def roda_eixoZ(sentido):
        if sentido == 'horario':

        else: