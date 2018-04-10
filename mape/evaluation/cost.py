from mape.evaluation.abstract_evaluation import AbstractEvaluation
from mape.evaluation.meta_data import EvaluationMetaData
import operator

class Cost(AbstractEvaluation):

    def __init__(self):
        super().__init__()
        self.evaluation_name = "Cost"
        self.evaluation_unit = "€"
        self.maximize = False
        self.meta_data = EvaluationMetaData(300, operator.le)

    def evaluate(self, terminal):
        average_cost = 0
        ships_count = 0

        ships = terminal.served_ships
        ships_count += len(ships)

        if len(ships) > 0:
            #print("Cost")
            average_cost = 0
            cost_sum = 0

            for index, current_ship in enumerate(ships):
                #print (" Ship %i served in %i minutes" %(current_ship.unique_id, current_ship.wait))
                cost_sum += (current_ship.cost * current_ship.wait)

                #calculating average
        average_cost = cost_sum/(60 * ships_count)
        #print ("Average Cost: %f €" %average_cost)
        #else:
        #    print ('No average, no ship served.')
        return average_cost
