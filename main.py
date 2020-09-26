#!/usr/bin/env pybricks-micropython

import csv
import time
from pybricks.tools import print, wait
from truck_module import Truck
from pid_module import PidRegulator
from util_module import *
from metrics_module import Metrics
from field_module import Field
from follower_module import Follower


KP = 2
KD = 2
KD = 0
KI = 0.1
KI = 0


field = Field()
truck = Truck()
pid_regulator = PidRegulator(field.line_border_reflection, KP, KD, KI)
metrics = Metrics(pid_regulator, truck)
left_sensor_follower = Follower.left_sensor_follower(truck, field.line_border_reflection)


# Проезд по линии до первого поворота 90

speed = 150
CHECK_TIME_MS = 10
prev_time = 0
while not (left_sensor_follower.on_junction_or_turn_90()):
    curr_time = current_milli_time()
    if ((curr_time - prev_time) < CHECK_TIME_MS):
        continue
    prev_time = curr_time
    reflection = left_sensor_follower.main_sensor.reflection()
    steering = pid_regulator.get_output(reflection) * left_sensor_follower.steering_direction
    truck.drive(speed, steering)
    metrics.append_metrics_item()

truck.stop()
metrics.write_metrics_to_file()
exit()
