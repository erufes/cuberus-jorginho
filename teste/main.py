#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.
ev3 = EV3Brick()
braco =  Motor (Port.A, Direction.CLOCKWISE, None)
sentido = 1


# Write your program here.

def SegurarCubo(braco):                                    #seria a posição inicial do braço, usa-se pra quando for girar ou segurar o cubo;
    braco.run_angle(1000, 100, Stop.HOLD, True)

def GirarCubo(braco):                                      #no caso, ele faz esse movimento antes da leitura e isso acontece 4 vezes, exceto na quinta vez que ele faz esse movimento 2 vezes direto;
    braco.run_angle(1000, 140, Stop.HOLD, True)            #para encaixar no cubo;
    braco.run_angle(1000, -140, Stop.HOLD, True)           #para puxar o cubo, ou seja, fazendo ele girar;

def VoltarPosicaoOriginal(braco):                          #volta para a posição original antes de segurar o cubo;
    braco.run_angle(1000, -100, Stop.HOLD, True)


ev3.speaker.beep()                                         #inicio do código

if sentido == 1:
    SegurarCubo(braco)
    GirarCubo(braco)
    VoltarPosicaoOriginal(braco)
