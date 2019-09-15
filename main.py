#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from grabber_module import Grabber


grabber = Grabber(Motor(Port.A))

grabber.close()
brick.sound.beep()
grabber.open()
brick.sound.beep()

'''
line_sensor = ColorSensor(Port.S1)

while not any(brick.buttons()):
    color = line_sensor.color()
    print(" colour:", color)

    wait(100)
'''





