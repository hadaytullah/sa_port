from mape.trend import Trend


class Mape:
    average_wait_time_list = []

    def monitor(self, average_wait):
        self.average_wait_time_list.append(average_wait)
        self.analyse()

    def analyse(self):
        # looking for a trend, increasing, decreasing.
        # decreasing is good, increasing will need adaptation
        trend_neutral = 0
        trend_increasing = 0
        trend_decreasing = 0

        if len(self.average_wait_time_list) > 0:
            previous_wait_time = self.average_wait_time_list[0]
            for current_wait_time in self.average_wait_time_list:
                if current_wait_time == previous_wait_time:
                    trend_neutral +=1
                elif current_wait_time > previous_wait_time:
                    trend_increasing +=1
                elif current_wait_time < previous_wait_time:
                    trend_decreasing +=1
            print (self.average_wait_time_list)
            if trend_increasing > trend_decreasing:
                print('Adapt the base system, call plan')
                self.plan()
            else:
                print('No need for adaptation, keep monitoring.')

    def plan(self):
        print('MAPE: Plan- a new strategy.')
        self.execute()

    def execute(self):
        print('MAPE: execute- the new strategy.')
