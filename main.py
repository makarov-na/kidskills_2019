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

#Калибровка левого датчика
'''brick.display.clear()
brick.display.text("Position left sensor")
brick.display.text("to line side ")
brick.display.text("and press any key")
while not any(brick.buttons()):
    wait(10)
wait(1000)
line_side = left_sensor.reflection()'''
line_side = 40
brick.display.text("Line side: " + str(line_side))
brick.display.text("Press any key to start")
while not any(brick.buttons()):
    wait(10)

wait(1000)
target_value = line_side
kp=2
kd=1
ki=0
err = 0
diff_err = 0
integr_err = 0
prevent_err = 0


drive_base = DriveBase(Motor(Port.B),Motor(Port.C), 43.2, 112)

speed = 50;
steering = 0;
#включаем оба мотора на полную
while not any(brick.buttons()):
    current_value = left_sensor.reflection()
    current_err = target_value - current_value
    integr_err = integr_err + current_err
    diff_err = current_err- prevent_err
    output_val = kp*current_err + kd*diff_err + ki*integr_err
    prevent_err = current_err
    output_val = kp*current_err + kd*diff_err + ki*integr_err
    print("target_value: ", target_value, " current_value: ", current_value, " current_err: ", current_err, "prevent_err: ", prevent_err ," integr_err: ", integr_err, "diff_err: ", diff_err, "optput: ", output_val)
    steering = -output_val
    drive_base.drive (speed, steering)
    #Если мы на белом, то otput отрицательный, нужно разогнать левое на максимум и тормозить правое колесо на значение output
    #Если мы на черном, то output положительный, нужно разогнать правое на максимум и тормозить левое колесо на значение output
    wait(1)



#Старт по линии

#Получить показание левого датчика

#Работа

'''
while (True):
    print("LR: ", left_sensor.reflection(), "RR: ", right_sensor.reflection())
    wait(1000)
truck.rotate_180()

truck.take_object()
truck.rotate_180()
truck.run_forward()
truck.stop()
truck.open_grubber()
'''
brick.sound.beep()






