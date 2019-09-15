#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

GRAB_DEGREE = 400
GRAB_SPEED = 500
GRAB_HOLD_ACTION = Stop.BRAKE
GRAB_DUTY_LIMIT = 30

grab_motor = Motor(Port.A)

def open_grab():
    angle = grab_motor.angle() 
    print(angle)
    grab_motor.run_target(GRAB_SPEED, -GRAB_DEGREE, GRAB_HOLD_ACTION)
    angle = grab_motor.angle() 
    print(angle)

def close_grab():
    angle = grab_motor.angle() 
    print(angle)
    grab_motor.run_target(GRAB_SPEED, GRAB_DEGREE, GRAB_HOLD_ACTION)
    angle = grab_motor.angle() 
    print(angle)

def open_grab_until_stop():
    grab_motor.run_until_stalled(GRAB_SPEED, GRAB_HOLD_ACTION, GRAB_DUTY_LIMIT)

def close_grab_until_stop():
    grab_motor.run_until_stalled(-GRAB_SPEED, GRAB_HOLD_ACTION, GRAB_DUTY_LIMIT)




