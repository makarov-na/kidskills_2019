#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from grabber_module import Grabber

class Truck:

    def __init__ (self, left_motor, right_motor, grabber_motor, front_sensor):
        self.TRUCK_SPEED = 500;
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.grabber = Grabber(grabber_motor)
        self.front_sensor = front_sensor

    def run_forward(self):
        self.left_motor.run(self.TRUCK_SPEED)
        self.right_motor.run(self.TRUCK_SPEED)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def run_backward(self):
        self.left_motor.run(-self.TRUCK_SPEED)
        self.right_motor.run(-self.TRUCK_SPEED)

    def rotate_180_by_gyro(self):
        gyro_sensor = GyroSensor(Port.S4)
        gyro_sensor.reset_angle(0)
        self.left_motor.run(self.TRUCK_SPEED)
        self.right_motor.run(-self.TRUCK_SPEED)
        while (gyro_sensor.angle()<135):
            print("Angle: ",gyro_sensor.angle())
            wait(1)
        self.stop()
        wait(4000)
    
    def take_object(self):
        self.grabber.open()
        self.run_forward()
        while (self.front_sensor.distance()>40):
            print("Distance to object: ",self.front_sensor.distance())
            wait(1)
        self.stop()
        self.grabber.close()
        

    def open_grubber(self):
        self.grabber.open()

