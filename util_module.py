#!/usr/bin/env pybricks-micropython

import sys

def exit():
    sys.exit(0)

def wait_start_keypress():
    brick.display.text("Line side: " + str(line_side))
    brick.display.text("Press any key to start")
    while not any(brick.buttons()):
        wait(10)

def on_junction_or_turn_90(main_sensor, add_sensor, line_side_reflection):
    main_sensor_deviation = 5
    return (add_sensor.reflection() < line_side_reflection) and (main_sensor.reflection() < line_side_reflection + main_sensor_deviation)

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

