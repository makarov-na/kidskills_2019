
class PidRegulator:

    def __init__(self, target_value, kp, kd, ki):
        self.target_value = target_value
        self.err = 0
        self.diff_err = 0
        self.integr_err = 0
        self.prevent_err = 0
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.integral_value_max = 20

        self.last_output = 0

    def get_error(self):
        return self.err

    def get_output(self, current_value):
        self.input = current_value
        self.err = self.target_value - current_value
        self.integr_err = self.integr_err + self.err
        if (self.integr_err > 0 and self.integr_err > self.integral_value_max):
            self.integr_err = self.integral_value_max
        if (self.integr_err < 0 and self.integr_err < - self.integral_value_max):
            self.integr_err = -self.integral_value_max
        self.diff_err = self.err - self.prevent_err
        # if (abs(self.err) < 19):
        #    self.integr_err = 0
        # if (abs(self.err) == 19 and abs(self.prevent_err) == 19):
        #    self.diff_err = self.err
        output_val = self.kp*self.err + self.kd*self.diff_err + self.ki*self.integr_err
        self.output = output_val
        self.prevent_err = self.err
        return output_val