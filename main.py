#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from util_module import *
from truck_module import *
import math


# Инициализация оборудования
grabber_sensor = UltrasonicSensor(Port.S1)
grabber_motor = Motor(Port.A)
left_wheel_motor = Motor(Port.B)
right_wheel_motor = Motor(Port.C)
left_line_sensor = ColorSensor(Port.S2)
right_line_sensor = ColorSensor(Port.S3)
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, 43.2, 112)
truck = Truck(left_wheel_motor, right_wheel_motor, grabber_motor, grabber_sensor, drive_base)

# Настройка PID регулятора
line_border_reflection = calibrate_line_side(left_line_sensor)
KP = 2
KD = 2
KI = 0.1
pid_regulator = PidRegulator(line_border_reflection, KP, KD, KI)

# Настройка скорости и стартовых значений тележки
max_speed = 150  # mm/sec
steering = 0
steering_direction_for_left_sensor = -1
steering_direction_for_right_sensor = 1

# Пауза перед началом работы
wait(1000)

# Проезд по короткому пути от старта до объекта в зоне 3, возврат на базу и выход на второй круг
# Основным выступает правый датчик, кторый работает по правой стороне линии
right_angle_count = 1
main_line_sensor = right_line_sensor
add_line_sensor = left_line_sensor
steering_direction = steering_direction_for_right_sensor

while not any(brick.buttons()):

    #Вычисляем управляющее воздействие для следования по линии и передаем его на вход тележки
    steering = pid_regulator.get_output(main_line_sensor.reflection()) * steering_direction
    truck.drive(max_speed, steering)

    #Отдельный алгоритм для прохода пряых углов и зон с объектами при проходе против часовой стрелки
    if (on_junction_or_turn_90(main_line_sensor, add_line_sensor, line_border_reflection)):
        truck.stop()
        if (right_angle_count == 1):
            truck.take_object()
            truck.turn_right_180()
            # TODO Заменить на drive_time
            truck.run_forward()
            wait(500)
        else:
            truck.stop()
            truck.drive_time(100, 0, 700)
            truck.open_grabber()
            truck.drive_time(-100, 0, 700)
            truck.turn_right_90()
            # TODO Заменить на drive_time
            truck.run_forward()
            wait(500)
            break
        right_angle_count += 1
    wait(10)

# Проезд от старта до финиша с забором объекта из зоны 1
right_angle_count = 1
zone_1_2_right_angle = 1
zone_3_4_right_angle = 2
main_line_sensor = left_line_sensor
add_line_sensor = right_line_sensor
steering_direction = steering_direction_for_left_sensor
KSPEED = 0.1
KBLACK = 1.5

while not any(brick.buttons()):

    #Вычисляем управляющее воздействие для следования по линии и передаем его на вход тележки
    steering = pid_regulator.get_output(main_line_sensor.reflection()) * steering_direction
    if (steering < 0):
        steering = steering * KBLACK
    speed = max_speed * (1 - abs(steering) * KSPEED)
    truck.drive(speed, steering)

    #Отдельный алгоритм для прохода пряых углов и зон с объектами при проходе по часовой стрелке 
    if (on_junction_or_turn_90(main_line_sensor, add_line_sensor, line_border_reflection)):
        truck.stop()
        if (right_angle_count == zone_1_2_right_angle):
            truck.turn_left_90()
            truck.take_object()
            truck.turn_right_180()
            # TODO Заменить на drive_time
            truck.run_forward()
            wait(500)
        elif (right_angle_count == zone_3_4_right_angle):
            truck.turn_right_90()
            # TODO Заменить на drive_time
            truck.run_forward()
            wait(500)
        else:
            truck.stop()
            truck.open_grabber()
            break
        right_angle_count += 1
    wait(10)

brick.sound.beep()
