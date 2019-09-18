#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)

class Truck:

    def __init__ (self, left_motor, right_motor):
        self.TRUCK_SPEED = 500;
        self.left_motor = left_motor
        self.right_motor = right_motor

    def run_forward(self):
        self.left_motor.run(self.TRUCK_SPEED)
        self.right_motor.run(self.TRUCK_SPEED)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def run_backward(self):
        self.left_motor.run(-self.TRUCK_SPEED)
        self.right_motor.run(-self.TRUCK_SPEED)

    def rotate180(self):
        ROTATE_ANGLE = 490
        self.left_motor.run_angle(500, ROTATE_ANGLE, Stop.COAST, False)
        self.right_motor.run_angle(500, -ROTATE_ANGLE, Stop.COAST, False)
        wait(4000)

