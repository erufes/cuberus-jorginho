#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

from classes.braco  import Braco
from classes.base   import Base
from classes.sensor import Sensor

# Create your objects here.
ev3 = EV3Brick()


# Leitura cubo completo

def scam_cubo(braco, base, sensor, sentido_braco, sentido_base, qtd_base, time_leitura):
    # Setting
    braco.set_sentido(sentido_braco)
    
    base.set_qtdMovimentos(qtd_base)
    base.set_Direcao(sentido_base)
    
    sensor.set_TimerLeituraCentro(time_leitura)
    
    # Face 1
    sensor.set_movimenta()
    
    # Face 2
    braco.set_movimenta()
    sensor.set_movimenta()
    
    # Face 3
    braco.set_movimenta()
    sensor.set_movimenta()
    
    # Face 4
    braco.set_movimenta()
    sensor.set_movimenta()
    
    # Face 5
    base.set_movimenta()
    braco.set_movimenta()
    sensor.set_movimenta()
    
    # Face 6
    braco.set_movimenta()
    braco.set_movimenta()
    sensor.set_movimenta()

# Movimento braço
braco =  Braco(Motor(Port.A, Direction.CLOCKWISE, None))

# Movimento Base
base =  Base(Motor(Port.B, Direction.CLOCKWISE, None), ev3)

# Movimento sensor
sensor =  Sensor(Motor(Port.C, Direction.CLOCKWISE, None))

scam_cubo(braco, base, sensor, 1, 'd', 1, 2)

ev3.speaker.beep()