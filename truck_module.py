#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from grabber_module import Grabber
import math


class Truck:

    def __init__(self):
        self.MAX_SPEED = 500
        self.left_wheel_motor = Motor(Port.B)
        self.right_wheel_motor = Motor(Port.C)
        self.left_line_sensor = ColorSensor(Port.S2)
        self.right_line_sensor = ColorSensor(Port.S3)
        self.drive_base = DriveBase(self.left_wheel_motor, self.right_wheel_motor, 43.2, 112)


    def run_forward_mm(self):
        self.left_wheel_motor.run(self.MAX_SPEED)
        self.right_wheel_motor.run(self.MAX_SPEED)

    def run_backward_mm(self):
        self.left_wheel_motor.run(self.MAX_SPEED)
        self.right_wheel_motor.run(self.MAX_SPEED)

    def run_forward(self):
        self.left_wheel_motor.run(self.MAX_SPEED)
        self.right_wheel_motor.run(self.MAX_SPEED)

    def drive(self, max_speed, steering):
        self.drive_base.drive(max_speed, steering)

    def drive_time(self, speed, steereng, time):
        self.drive_base.drive_time(speed, steereng, time)

    def stop(self):
        self.drive_base.stop()
        self.left_wheel_motor.stop()
        self.right_wheel_motor.stop()

    def run_backward(self):
        self.left_wheel_motor.run(-self.MAX_SPEED)
        self.right_wheel_motor.run(-self.MAX_SPEED)

    def rotate_180_by_gyro(self):
        gyro_sensor = GyroSensor(Port.S4)
        gyro_sensor.reset_angle(0)
        self.left_wheel_motor.run(self.MAX_SPEED)
        self.right_wheel_motor.run(-self.MAX_SPEED)
        while (gyro_sensor.angle() < 135):
            print("Angle: ", gyro_sensor.angle())
            wait(1)
        self.stop()
        wait(4000)

    def turn_right_90(self):
        angle_for_90_degrees = 235
        self.left_wheel_motor.run_angle(self.MAX_SPEED, angle_for_90_degrees, Stop.COAST, False)
        self.right_wheel_motor.run_angle(-self.MAX_SPEED, angle_for_90_degrees, Stop.COAST, True)

    def turn_left_90(self):
        angle_for_90_degrees = 235
        self.left_wheel_motor.run_angle(-self.MAX_SPEED, angle_for_90_degrees, Stop.COAST, False)
        self.right_wheel_motor.run_angle(self.MAX_SPEED, angle_for_90_degrees, Stop.COAST, True)

    def turn_left_180(self):
        angle_for_180_degrees = 235*2
        self.left_wheel_motor.run_angle(-self.MAX_SPEED, angle_for_180_degrees, Stop.COAST, False)
        self.right_wheel_motor.run_angle(self.MAX_SPEED, angle_for_180_degrees, Stop.COAST, True)

    def turn_right_180(self):
        angle_for_180_degrees = 235*2
        self.left_wheel_motor.run_angle(self.MAX_SPEED, angle_for_180_degrees, Stop.COAST, False)
        self.right_wheel_motor.run_angle(-self.MAX_SPEED, angle_for_180_degrees, Stop.COAST, True)

    def take_object(self):
        self.grabber.open()
        self.run_forward()
        while (self.front_sensor.distance() > 40):
            print("Distance to object: ", self.front_sensor.distance())
            wait(1)
        self.stop()
        self.grabber.close()

    def open_grabber(self):
        self.grabber.open()
