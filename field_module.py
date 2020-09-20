

class Field:
    def __init__(self):
        self.line_border_reflection = 30  # calibrate_line_side(left_line_sensor)
        self.white_reflection = 70
        self.black_reflection = 11
        self.max_white_reflection = self.line_border_reflection + (self.line_border_reflection - self.black_reflection)

