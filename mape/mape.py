from mape.trend import Trend
from abc import ABC, abstractmethod
import random


class Mape(ABC):
    average_wait_time_list = []

    def __init__(self, strategy_list, evaluation_list):
        self._monitoring_data = None
        self._strategy_list = strategy_list
        self._evaluation_list = evaluation_list
        #self.id = random.randrange(22,90) #temporary fix, have to merge with terminal id
        self.clock = 0
        self._evaluation = 0

    def step(self):



        self.clock += 1
        if self.clock % (60*6) == 0: #every six hours
            self._analyse()


        #print ('Monitoring data {}'.format(self.id))

    @abstractmethod
    def _get_monitoring_data(self):
        pass

    @abstractmethod
    def _set_strategy(self, strategy):
        pass

    @abstractmethod
    def _get_id(self):
        pass


    def _monitor(self):
        pass

    def _analyse(self):
        self._evaluation = self._get_monitoring_data()
        #self.average_wait_time_list.append(average_wait)
        evaluation_sum = 0
        for evaluation in self._evaluation_list:
            evaluation_value = evaluation.evaluate(self)
            evaluation_sum += evaluation_value
            print('{} {}: {} {}'.format(self.name, evaluation.evaluation_name, evaluation_value, evaluation.evaluation_unit))


        print('Analysing..{}'.format(evaluation_sum))
        self._plan()
        # looking for a trend, increasing, decreasing.
        # decreasing is good, increasing will need adaptation
#        trend_neutral = 0
#        trend_increasing = 0
#        trend_decreasing = 0
#
#        if len(self.average_wait_time_list) > 0:
#            previous_wait_time = self.average_wait_time_list[0]
#            for current_wait_time in self.average_wait_time_list:
#                if current_wait_time == previous_wait_time:
#                    trend_neutral +=1
#                elif current_wait_time > previous_wait_time:
#                    trend_increasing +=1
#                elif current_wait_time < previous_wait_time:
#                    trend_decreasing +=1
#            print (self.average_wait_time_list)
#            if trend_increasing > trend_decreasing:
#                print('Adapt the base system, call plan')
#                self.plan()
#            else:
#                print('No need for adaptation, keep monitoring.')

    def _plan(self):
        print('MAPE: Plan- a new strategy.')
        new_strategy = random.choice(self._strategy_list)

        self._execute(new_strategy)

    def _execute(self, new_strategy):
        print('MAPE: execute- the new strategy.')
        print('ID {}, Clock is {}, Mape changing strategy to:{}'.format(self._get_id(),self.clock, new_strategy.name))
            #self._analyse()
            #self._set_strategy(new_strategy)
