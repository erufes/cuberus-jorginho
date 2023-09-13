#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.port import LegoPort

from classes.braco  import Braco
from classes.base   import Base

from pybricks.iodevices import I2CDevice
from pybricks.iodevices import  AnalogSensor
from pybricks.iodevices import UARTDevice
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import Font

import os
import sys
import time

from nxtcam.i2c import *
from nxtcam.mindsensorsPYB import NXTCAM

NXTCAM_ADDRESS = 0x02
ev3 = EV3Brick()
ev3.speaker.beep()
# Set LEGO port for Pixy on input port 1
#in1 = LegoPort(INPUT_1)
#in1.mode = 'auto'
# Wait 2 secs for the port to get ready

time.sleep(2)

# Connect Pixy camera
#pixy = Sensor(INPUT_1)

#initialize nxtcam
cam = NXTCAM(Port.S1,NXTCAM_ADDRESS)

cam.startTracking()
cam.trackObject()

b = cam.getBlobs(1)
print("Color: " + str(b.color))
print("Left: " + str(b.left))
print("Top: " + str(b.top))
print("Right: " + str(b.right))
print("Bottom: " + str(b.bottom))




