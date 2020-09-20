

class Metrics:

    def __init__(self, pid_regulator, truck):
        self.metrics_data = []
        self.metric_count = 0
        self.pid_regulator = pid_regulator
        self.truck = truck

    def append_metrics_item(self, row_data):
        #[curr_time, error, sum_out, p_out, d_out, i_out, motor_a_speed, motor_b_speed, reflection]
        self.metric_count += 1
        error = self.pid_regulator.current_err
        sum_out = self.pid_regulator.last_output
        p_out = self.pid_regulator.current_err*self.pid_regulator.kp
        i_out = self.pid_regulator.integr_err*self.pid_regulator.ki
        d_out = self.pid_regulator.diff_err*self.pid_regulator.kd
        motor_a_speed = self.truck.left_wheel_motor.speed()
        motor_b_speed = self.truck.right_wheel_motor.speed()
        self.metrics_data.append([self.metric_count, error, sum_out, p_out, d_out, i_out, motor_a_speed, motor_b_speed] + row_data)



    def write_metrics_to_file(self):
        with open('pid.csv', mode='w') as pid_out_file:
            for row_data in self.metrics_data:
                pid_out_file.write(','.join(map(str, row_data))  + "\n")
