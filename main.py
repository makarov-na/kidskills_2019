#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from grabber_module import Grabber

#Инициализация
grabber = Grabber(Motor(Port.A))

grabber.open()

left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)
front_sensor = UltrasonicSensor(Port.S1)


TRUCK_SPEED = 500;
left_wheel.run(TRUCK_SPEED)
right_wheel.run(TRUCK_SPEED)

while (front_sensor.distance()>40):
    print(front_sensor.distance())
    wait(10)
left_wheel.stop()
right_wheel.stop()
grabber.close()

left_wheel.run(-TRUCK_SPEED)
right_wheel.run(-TRUCK_SPEED)
wait(5000)

left_wheel.stop()
right_wheel.stop()

grabber.open()


brick.sound.beep()

'''
line_sensor = ColorSensor(Port.S1)

while not any(brick.buttons()):
    color = line_sensor.color()
    print(" colour:", color)

    wait(100)
'''





