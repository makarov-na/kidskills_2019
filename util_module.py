#!/usr/bin/env pybricks-micropython

import sys


def exit():
    sys.exit(0)


def wait_start_keypress():
    brick.display.text("Line side: " + str(line_side))
    brick.display.text("Press any key to start")
    while not any(brick.buttons()):
        wait(10)


def calibrate_line_side(sensor):
    return 30
    brick.display.clear()
    brick.display.text("Position left sensor")
    brick.display.text("to line side ")
    brick.display.text("and press any key")
    while not any(brick.buttons()):
        wait(10)
    wait(1000)
    line_side = sensor.reflection()
    return line_side


def take_object_and_run():
    while (True):
        print("LR: ", left_sensor.reflection(), "RR: ", right_sensor.reflection())
        wait(1000)
    truck.rotate_180()

    truck.take_object()
    truck.rotate_180()
    truck.run_forward()
    truck.stop()
    truck.open_grubber()

