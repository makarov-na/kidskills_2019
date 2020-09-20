#!/usr/bin/env pybricks-micropython

import csv
from pybricks.tools import print, wait
from truck_module import Truck
from pid_module import PidRegulator
from util_module import *
from field_module import Field
import time

field = Field()
truck = Truck()

KP = 2
KD = 2
KD = 0
KI = 0.1
KI = 0
pid_regulator = PidRegulator(field.line_border_reflection, KP, KD, KI)

# Настройка скорости и стартовых значений тележки
max_speed = 200  # mm/sec
min_speed = 150
speed = min_speed

steering = 0
steering_direction_for_left_sensor = -1
steering_direction_for_right_sensor = 1

metrics_data = []

# Проезд по линии до первого поворота 90
main_line_sensor = truck.left_line_sensor
add_line_sensor = truck.right_line_sensor
steering_direction = steering_direction_for_left_sensor


start_time = time.time()
loop_count = 0
while (time.time()-start_time < 200):

    reflection = main_line_sensor.reflection()
    steering = pid_regulator.get_output(reflection) * steering_direction
    truck.drive(speed, steering)

    #curr_time = current_milli_time()
    curr_time = loop_count
    error = pid_regulator.current_err
    sum_out = pid_regulator.get_output(reflection)
    p_out = pid_regulator.current_err*pid_regulator.kp
    i_out = pid_regulator.integr_err*pid_regulator.ki
    d_out = pid_regulator.diff_err*pid_regulator.kd
    motor_a_speed = truck.left_wheel_motor.speed()
    motor_b_speed = truck.right_wheel_motor.speed()
    metrics_data.append([curr_time, error, sum_out, p_out, d_out, i_out, motor_a_speed, motor_b_speed, reflection])

    wait(10)
    loop_count += 1
    if (on_junction_or_turn_90(main_line_sensor, add_line_sensor, field.line_border_reflection)):
        truck.stop()
        print("###################")
        break

write_metrics_to_file(metrics_data)
exit()

