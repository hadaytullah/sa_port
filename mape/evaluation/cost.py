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
        ships = terminal.served_ships
        ships_count = len(ships)

        if ships_count == 0:
            return 0.0

        cost_sum = 0
        for index, current_ship in enumerate(ships):
            cost_sum += (current_ship.cost * current_ship.wait)

        average_cost = cost_sum/(60 * ships_count)
        return average_cost
