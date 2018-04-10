import random

from knowledge_base import DictKB

from mape.trend import Trend


class Mape:
    average_wait_time_list = []

    def __init__(self, strategy_list, evaluation_list):
        self._monitoring_data = None
        self._strategy_list = strategy_list
        self._evaluation_list = evaluation_list
        self._kb = DictKB()
        #self.id = random.randrange(22,90) #temporary fix, have to merge with terminal id
        self.clock = 0
        self._evaluation = 0

    def step(self):
        self.clock += 1
        if self.clock % (60*6) == 0:  # every six hours
            self._analyse()
        # print ('Monitoring data {}'.format(self.id))

    def _get_monitoring_data(self):
        raise NotImplementedError

    def _get_id(self):
        raise NotImplementedError

    def _monitor(self):
        pass

    def _analyse(self):
        self._evaluation = self._get_monitoring_data()
        evals = {}
        #self.average_wait_time_list.append(average_wait)
        evaluation_sum = 0
        for evaluation in self._evaluation_list:
            evaluation_value = evaluation.evaluate(self)
            evaluation_sum += evaluation_value
            evals[evaluation] = evaluation_value
            print('{} {}: {} {}'.format(self.name, evaluation.evaluation_name, evaluation_value, evaluation.evaluation_unit))

        print('Analysing..{}'.format(evaluation_sum))
        self._plan(evals)
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

    def _plan(self, evaluations):
        print('MAPE: Plan- a new strategy.')

        eval_within_threshold = {}
        for func, eval in evaluations.items():
            eval_within_threshold[func] = func.meta_data.within_threshold(eval)

        new_strategy = random.choice(self._strategy_list)
        self._execute(new_strategy)

    def _execute(self, new_strategy):
        print('MAPE: execute- the new strategy.')
        print('ID {}, Clock is {}, Mape changing strategy to: {}'.format(self._get_id(), self.clock, new_strategy.name))
        # self._analyse()
        # self.strategy = new_strategy

    def prestep(self, func, *args, **kwargs):
        pass
        #self.log("Prestep!")

    def poststep(self, result, func, *args, **kwargs):
        #self.log("Poststep wrapped!")
        self.clock += 1
        if self.clock % (60*6) == 0:  # every six hours
            self._analyse()

