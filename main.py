#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from grabber_module import Grabber
from truck_module import Truck

#Инициализация
grabber = Grabber(Motor(Port.A))
truck = Truck(Motor(Port.B),Motor(Port.C))
front_sensor = UltrasonicSensor(Port.S1)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)


#Работа

def takeObject:
    grabber.open()
    truck.run_forward()
    while (front_sensor.distance()>40):
        print(front_sensor.distance())
        wait(10)
    grabber.close()


takeObject()
truck.rotate180()
truck.run_forward()
wait(5000)

truck.stop()
grabber.open()

brick.sound.beep()






