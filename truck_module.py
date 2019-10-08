#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from grabber_module import Grabber
import math


class Truck:

    def __init__(self, left_motor, right_motor, grabber_motor, front_sensor):
        self.TRUCK_SPEED = 500
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
        while (gyro_sensor.angle() < 135):
            print("Angle: ", gyro_sensor.angle())
            wait(1)
        self.stop()
        wait(4000)

    def turn_right(self):
        angle_for_90_degrees = 235
        self.left_motor.run_angle(self.TRUCK_SPEED, angle_for_90_degrees, Stop.COAST, False)
        self.right_motor.run_angle(-self.TRUCK_SPEED, angle_for_90_degrees, Stop.COAST, True)

    def turn_left(self):
        angle_for_90_degrees = 235
        self.left_motor.run_angle(-self.TRUCK_SPEED, angle_for_90_degrees, Stop.COAST, False)
        self.right_motor.run_angle(self.TRUCK_SPEED, angle_for_90_degrees, Stop.COAST, True)

    def turn_left_180(self):
        angle_for_180_degrees = 235*2
        self.left_motor.run_angle(-self.TRUCK_SPEED, angle_for_180_degrees, Stop.COAST, False)
        self.right_motor.run_angle(self.TRUCK_SPEED, angle_for_180_degrees, Stop.COAST, True)

    def turn_right_180(self):
        angle_for_180_degrees = 235*2
        self.left_motor.run_angle(self.TRUCK_SPEED, angle_for_180_degrees, Stop.COAST, False)
        self.right_motor.run_angle(-self.TRUCK_SPEED, angle_for_180_degrees, Stop.COAST, True)


    def take_object(self):
        self.grabber.open()
        self.run_forward()
        while (self.front_sensor.distance() > 40):
            print("Distance to object: ", self.front_sensor.distance())
            wait(1)
        self.stop()
        self.grabber.close()

    def open_grubber(self):
        self.grabber.open()


class PidRegulator:

    def __init__(self, target_value, kp, kd, ki):
        self.target_value = target_value
        self.err = 0
        self.diff_err = 0
        self.integr_err = 0
        self.prevent_err = 0
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.integral_value_max = 20

    def get_output(self, current_value):
        current_err = self.target_value - current_value
        self.integr_err = self.integr_err + current_err
        if (self.integr_err > 0 and self.integr_err > self.integral_value_max):
            self.integr_err = self.integral_value_max
        if (self.integr_err < 0 and self.integr_err < - self.integral_value_max):
            self.integr_err = -self.integral_value_max
        self.diff_err = current_err - self.prevent_err
        output_val = self.kp*current_err + self.kd*self.diff_err + self.ki*self.integr_err
        self.prevent_err = current_err
        print("target_value: ", self.target_value, " current_value: ", current_value, " current_err: ", current_err,
              "prevent_err: ", self.prevent_err, " integr_err: ", self.integr_err, "diff_err: ", self.diff_err, "optput: ", output_val)
        return output_val
