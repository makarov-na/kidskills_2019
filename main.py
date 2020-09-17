#!/usr/bin/env pybricks-micropython

from util_module import *
import csv
import math
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from util_module import *
from truck_module import *
import math
import time


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
line_border_reflection = 30  # calibrate_line_side(left_line_sensor)
white_reflection = 70
black_reflection = 11
speed_down_error = line_border_reflection - black_reflection
max_white_reflection = line_border_reflection + (line_border_reflection - black_reflection)

KP = 2
KD = 2
KI = 0.1
pid_regulator = PidRegulator(line_border_reflection, KP, KD, KI)

# Настройка скорости и стартовых значений тележки
max_speed = 200  # mm/sec
min_speed = 150
speed_delta_down = 10
speed_delta_up = 3
speed = min_speed

steering = 0
steering_direction_for_left_sensor = -1
steering_direction_for_right_sensor = 1

metrics_data = []
# Пауза перед началом работы
# wait(1000)

# Проезд по линии до первого поворота 90
main_line_sensor = left_line_sensor
add_line_sensor = right_line_sensor
steering_direction = steering_direction_for_left_sensor

def change_speed(current_error, current_speed):
    new_speed = current_speed
    if (abs(current_error) >= (speed_down_error)):
        new_speed = current_speed - speed_delta_down
        if (new_speed < min_speed):
            new_speed = min_speed
    else:
        new_speed = current_speed + speed_delta_up
        if (new_speed > max_speed):
            new_speed = max_speed
    return new_speed



start_time = time.time()
while (time.time()-start_time < 200):

    reflection = main_line_sensor.reflection()
    # Нормализуем значение для устранения перекоса управляющего воздействия
    # if reflection > max_white_reflection:
    #    reflection = max_white_reflection

    steering = pid_regulator.get_output(reflection) * steering_direction
    speed = change_speed(pid_regulator.get_current_error(), speed)
    truck.drive(speed, steering)


    #metrics_data.append([time, error, sum_out, p_out, d_out, i_out, motor_a_speed, motor_b_speed])
    time = current_milli_time()
    error = pid_regulator.current_err
    sum_out = steering
    p_out = pid_regulator.current_err*pid_regulator.k
    i_out = pid_regulator.integr_err*pid_regulator.ki
    d_out = pid_regulator.diff_err*pid_regulator.kd
    motor_a_speed = 0
    motor_b_speed = 0
    metrics_data.append([time, error, sum_out, p_out, d_out, i_out, motor_a_speed, motor_b_speed])

    print("TV:", pid_regulator.target_value,
          ";CV:", reflection,
          ";CERR:", pid_regulator.current_err,
          ";PERR:", pid_regulator.prevent_err,
          ";PV:", pid_regulator.current_err*pid_regulator.kp,
          ";IV:", pid_regulator.integr_err*pid_regulator.ki,
          ";DV:", pid_regulator.diff_err*pid_regulator.kd,
          ";SV:", steering * steering_direction,
          ";SP:", speed)

    wait(10)

    if (on_junction_or_turn_90(main_line_sensor, add_line_sensor, line_border_reflection)):
        truck.stop()
        print("###################")
        break

write_metrics_to_file(metrics_data)
exit()

# Проезд по короткому пути от старта до объекта в зоне 3, возврат на базу и выход на второй круг
# Основным выступает правый датчик, кторый работает по правой стороне линии
right_angle_count = 1
main_line_sensor = right_line_sensor
add_line_sensor = left_line_sensor
steering_direction = steering_direction_for_right_sensor

while not any(brick.buttons()):

    # Вычисляем управляющее воздействие для следования по линии и передаем его на вход тележки
    steering = pid_regulator.get_output(main_line_sensor.reflection()) * steering_direction
    speed = change_speed(pid_regulator.get_current_error(), speed)
    truck.drive(max_speed, steering)

    # Отдельный алгоритм для прохода пряых углов и зон с объектами при проходе против часовой стрелки
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

while not any(brick.buttons()):

    # Вычисляем управляющее воздействие для следования по линии и передаем его на вход тележки
    steering = pid_regulator.get_output(main_line_sensor.reflection()) * steering_direction
    speed = change_speed(pid_regulator.get_current_error(), speed)
    truck.drive(speed, steering)

    # Отдельный алгоритм для прохода пряых углов и зон с объектами при проходе по часовой стрелке
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
