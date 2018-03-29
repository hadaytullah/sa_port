from mape.evaluation.abstract_evaluation import AbstractEvaluation

class ShipsSatisfaction(AbstractEvaluation):
    """Measures satisfaction of the ships. Percentage of ships whose goals and constraints were satisfied.
    """
    def __init__(self):
        super().__init__()
        self.evaluation_name = "Ships Satisfaction"
        self.evaluation_unit = "%"
        self.maximize = True


    def evaluate(self, terminal):
        average_wait_time = 0
        ships_count = 0

        ships = terminal.served_ships
        ships_count = len(ships)

        if ships_count > 0:
            #print("WAIT TIMES")
            satisfied_ships = 0
            wait_sum = 0

            for index, current_ship in enumerate(ships):
                #print (" Ship %i served in %i minutes" % (current_ship.unique_id, current_ship.wait))
                if current_ship.wait <= current_ship.max_wait:
                    satisfied_ships += 1

        #
        satisfaction = (satisfied_ships/ships_count) * 100
        #print ('Ships satisfied : %i ' %satisfaction)
        return satisfaction
