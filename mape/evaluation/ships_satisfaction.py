from mape.evaluation.abstract_evaluation import AbstractEvaluation
from mape.evaluation.meta_data import EvaluationMetaData
import operator


class ShipsSatisfaction(AbstractEvaluation):
    """Measures satisfaction of the ships. Percentage of ships whose goals and constraints were satisfied.
    """
    def __init__(self):
        super().__init__()
        self.evaluation_name = "Ships Satisfaction"
        self.evaluation_unit = "%"
        self.maximize = True
        self.meta_data = EvaluationMetaData(10, operator.ge)

    def evaluate(self, terminal):
        ships = terminal.served_ships
        ships_count = len(ships)

        if len(ships) == 0:
            return 0.0

        satisfied_ships = 0
        for index, current_ship in enumerate(ships):
            if current_ship.wait <= current_ship.max_wait:
                satisfied_ships += 1

        satisfaction = (satisfied_ships/ships_count) * 100
        return satisfaction
