#!/usr/bin/env pybricks-micropython

import sys
import time

def current_milli_time():
    return int(round(time.time() * 1000))

def exit():
    sys.exit(0)

def wait_start_keypress():
    brick.display.text("Line side: " + str(line_side))
    brick.display.text("Press any key to start")
    while not any(brick.buttons()):
        wait(10)


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
