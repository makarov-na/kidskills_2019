#!/usr/bin/env pybricks-micropython

import csv
from pybricks.tools import print, wait
from truck_module import Truck
from pid_module import PidRegulator
from util_module import *
from metrics_module import *
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

metrics = Metrics(pid_regulator,truck)

# Настройка скорости и стартовых значений тележки
max_speed = 200  # mm/sec
min_speed = 150
speed = min_speed

steering = 0
steering_direction_for_left_sensor = -1
steering_direction_for_right_sensor = 1


# Проезд по линии до первого поворота 90
main_line_sensor = truck.left_line_sensor
add_line_sensor = truck.right_line_sensor
steering_direction = steering_direction_for_left_sensor


start_time = time.time()

while (time.time()-start_time < 200):

    reflection = main_line_sensor.reflection()
    steering = pid_regulator.get_output(reflection) * steering_direction
    truck.drive(speed, steering)

    #curr_time = current_milli_time()
    metrics.append_metrics_item([reflection])
    wait(10)
    
    if (on_junction_or_turn_90(main_line_sensor, add_line_sensor, field.line_border_reflection)):
        truck.stop()
        print("###################")
        break

metrics.write_metrics_to_file()
exit()

