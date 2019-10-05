#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from util_module import *
from truck_module import *


# Инициализация оборудования
distance_sensor = UltrasonicSensor(Port.S1)
left_wheel_motor = Motor(Port.B)
right_wheel_motor = Motor(Port.C)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
grabber_motor = Motor(Port.A)
truck = Truck(left_wheel_motor, right_wheel_motor, grabber_motor, distance_sensor)
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, 43.2, 112)

# Настройка PID датчика
line_side = calibrate_line_side(left_sensor)
pid_regulator = PidRegulator(line_side, 2, 2, 0.1)

# Настройка скорости и стартовых значений тележки
max_speed = 150
steering = 0


wait(1000)

while not any(brick.buttons()):

    steering = - pid_regulator.get_output(left_sensor.reflection())
    # Если мы на белом, то otput отрицательный, нужно разогнать левое на максимум и тормозить правое колесо на значение output
    # Если мы на черном, то output положительный, нужно разогнать правое на максимум и тормозить левое колесо на значение output
    drive_base.drive(max_speed, steering)

    #Проверить нет ли угла 90 градусов
    #Если есть повернуть по отдельному алгоритму

    if (distance_sensor.distance() < 150):
        break
    wait(10)

brick.sound.beep()
