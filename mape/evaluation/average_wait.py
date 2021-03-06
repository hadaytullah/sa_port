from mape.evaluation.abstract_evaluation import AbstractEvaluation
from mape.evaluation.meta_data import EvaluationMetaData
import operator


class AverageWait(AbstractEvaluation):

    def __init__(self):
        super().__init__()
        self.evaluation_name = "Average Wait Time"
        self.evaluation_unit = "Minute"
        self.maximize = False
        self.meta_data = EvaluationMetaData(10, operator.le)

    def evaluate_(self, ships):
        average_wait_time = 0
        if len(ships) > 0:
            print("WAIT TIMES")
            average_wait_time = 0
            wait_sum = 0

            for index, current_ship in enumerate(ships):
                print(" Ship %i served in %i minutes" % (current_ship.unique_id, current_ship.wait))
                wait_sum += current_ship.wait

            #calculating average
            average_wait_time = wait_sum/(60*len(ships))
            print("Average Wait: %f hours" % average_wait_time)
        #else:
        #    print ('No average, no ship served.')
        return average_wait_time

    def evaluate(self, terminal):
        ships = terminal.served_ships
        ships_count = len(ships)

        if ships_count == 0:
            return 0.0

        wait_sum = 0
        for index, current_ship in enumerate(ships):
            wait_sum += current_ship.wait

        average_wait_time = wait_sum/ships_count
        print('Ships served: {}'.format(ships_count))
        return average_wait_time
