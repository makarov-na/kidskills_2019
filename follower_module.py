

class Follower:

    STEERING_DIRECTION_FOR_LEFT_SENSOR = -1
    STEERING_DIRECTION_FOR_RIGHT_SENSOR = 1
    MAIN_SENSOR_DEVIATION = 5
    CHECK_TIME_MS = 10
    MIN_SPEED = 150

    def __init__(self, main_sensor, add_sensor, steering_direction, line_side_reflection):
        self.main_sensor = main_sensor
        self.add_sensor = add_sensor
        self.steering_direction = steering_direction
        self.line_side_reflection = line_side_reflection
        self.prev_time = 0
    

    @classmethod
    def left_sensor_follower(cls, truck, line_side_reflection):
        return cls(truck.left_line_sensor,truck.right_line_sensor, cls.STEERING_DIRECTION_FOR_LEFT_SENSOR, line_side_reflection)

    @classmethod
    def right_sensor_follower(cls, truck, line_side_reflection):
        return cls(truck.right_line_sensor, truck.left_line_sensor, cls.STEERING_DIRECTION_FOR_RIGHT_SENSOR, line_side_reflection)

    def on_junction_or_turn_90(self):
        return (self.add_sensor.reflection() < self.line_side_reflection) and (self.main_sensor.reflection() < self.line_side_reflection + self.MAIN_SENSOR_DEVIATION)
