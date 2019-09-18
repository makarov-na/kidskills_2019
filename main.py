#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from truck_module import Truck

#Инициализация

truck = Truck(Motor(Port.B),Motor(Port.C), Motor(Port.A), UltrasonicSensor(Port.S1))
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)


#Работа

'''
while (True):
    print("LR: ", left_sensor.reflection(), "RR: ", right_sensor.reflection())
    wait(1000)
'''
truck.rotate_180()

'''
truck.take_object()
truck.rotate_180()
truck.run_forward()
truck.stop()
truck.open_grubber()
'''
brick.sound.beep()






