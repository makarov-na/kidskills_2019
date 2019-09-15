#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import grab_module as grab


grab.close_grab()
brick.sound.beep()
grab.open_grab()

line_sensor = ColorSensor(Port.S1)

while not any(brick.buttons()):
    color = line_sensor.
    print(" colour:", color)

    wait(100)





