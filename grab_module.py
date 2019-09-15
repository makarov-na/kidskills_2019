#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

GRAB_DEGREE = 400

def open_grab():
    grab_motor = Motor(Port.A)
    angle = grab_motor.angle() 
    print(angle)
    grab_motor.run_target(500, -GRAB_DEGREE, Stop.BRAKE)
    angle = grab_motor.angle() 
    print(angle)

def close_grab():
    grab_motor = Motor(Port.A)
    angle = grab_motor.angle() 
    print(angle)
    grab_motor.run_target(500, GRAB_DEGREE, Stop.BRAKE)
    angle = grab_motor.angle() 
    print(angle)



