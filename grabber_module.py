#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)

class Grabber:
    
    def __init__(self, motor): 
        self.motor = motor
        self.GRAB_DUTY_LIMIT = 50
        self.GRAB_SPEED = 500
        self.GRAB_HOLD_ACTION = Stop.COAST
        
    def open(self):
        start_angle = self.motor.angle()
        self.motor.run_until_stalled(-self.GRAB_SPEED, self.GRAB_HOLD_ACTION, self.GRAB_DUTY_LIMIT)
        stop_angle = self.motor.angle()
        print("motor rotated at ", stop_angle - start_angle)

    def close(self):
        start_angle = self.motor.angle()
        self.motor.run_until_stalled(self.GRAB_SPEED, self.GRAB_HOLD_ACTION, self.GRAB_DUTY_LIMIT)
        stop_angle = self.motor.angle()
        print("motor rotated at ", stop_angle - start_angle)


