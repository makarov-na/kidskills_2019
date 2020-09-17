#!/usr/bin/env pybricks-micropython

import sys
import time

def current_milli_time():
    return int(round(time.time() * 1000))

def exit():
    sys.exit(0)

def write_metrics_to_file(data):
    with open('pid.csv', mode='w') as pid_out_file:
        for row_data in data:
            pid_out_file.write(','.join(map(str, row_data))  + "\n")


def wait_start_keypress():
    brick.display.text("Line side: " + str(line_side))
    brick.display.text("Press any key to start")
    while not any(brick.buttons()):
        wait(10)

def on_junction_or_turn_90(main_sensor, add_sensor, line_side_reflection):
    main_sensor_deviation = 5
    return (add_sensor.reflection() < line_side_reflection) and (main_sensor.reflection() < line_side_reflection + main_sensor_deviation)

def calibrate_line_side(sensor):
    brick.display.clear()
    brick.display.text("Position left sensor")
    brick.display.text("to left line border ")
    brick.display.text("and press any key")
    while not any(brick.buttons()):
        wait(10)
    wait(1000)
    line_side = sensor.reflection()
    return line_side

def test_max_speed():
    while True:
        truck.drive(320, 320)
        print("speed: " + str(steering), "L motor speed: ", left_wheel_motor.speed(), "R motor speed: ", right_wheel_motor.speed())
        steering = steering + 1 
        wait(10)
