#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
base = Motor(Port.A, Direction.CLOCKWISE, None)
qtdMovimentos = 4
direcao = 'd'

def movEsquerda(vezes, base):
    base.run_angle(500, -270*vezes, Stop.HOLD, True)
    ev3.speaker.beep()

def movDireita(vezes, base):
    base.run_angle(500, 270*vezes, Stop.HOLD, True)
    ev3.speaker.beep()

if direcao == 'e': 
    movEsquerda(qtdMovimentos, base)

else:
    if direcao == 'd':
        movDireita(qtdMovimentos, base)
ev3.speaker.beep()