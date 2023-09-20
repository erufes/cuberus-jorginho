#!/usr/bin/env pybricks-micropython
#from pybricks.hubs import EV3Brick
#from pybricks.ev3devices import Motor
#from pybricks.parameters import Port, Direction

#from classes.movimento import Movimento
#from classes.braco  import Braco
#from classes.base   import Base
#from classes.sensor import Sensor
import json

arquivo = './../algoritmoDeSolucao/cubos/movimentos_cuboConfigEx1.json'
# Create your objects here.

#ev3 = EV3Brick()

# Inicializa as partes do jorginho

#braco =  Braco(Motor(Port.A, Direction.CLOCKWISE, None))
#base =  Base(Motor(Port.A, Direction.CLOCKWISE, None), ev3)
#sensor =  Sensor(Motor(Port.A, Direction.CLOCKWISE, None))
def verifica_sentido(movimento):

        if movimento == 'Fi' or movimento == 'Ri' or movimento == 'Ui' or movimento == 'Li' or movimento == 'Bi' or movimento == 'Di' or movimento == 'Xi' or movimento == 'Yi' or movimento == 'Zi' or movimento == 'Mi'or movimento == 'Si' or movimento == 'Ei':
            sentido = 'anti horario'
        else:
            sentido = 'horario'
        return sentido

f = open(arquivo,"r")
movimentos = json.loads(f.read())

for i in movimentos:
    sentido = verifica_sentido(i)
   #direcao, sentido = verifica_movimento(i)


f.close()

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