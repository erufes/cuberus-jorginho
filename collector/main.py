#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

from classes.braco  import Braco
from classes.base   import Base
from classes.sensor import Sensor

# Create your objects here.
ev3 = EV3Brick()

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