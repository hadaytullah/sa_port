from mape.evaluation.abstract_evaluation import AbstractEvaluation

class Cost(AbstractEvaluation):

    def __init__(self):
        super().__init__()
        self.evaluation_name = "Average Cost"
        self.maximize = False


    def evaluate(self, ships):
        average_cost = 0
        ships_count = 0
        for terminal in port_model.terminals:
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
        print ("Average Cost: %f €" %average_cost)
        #else:
        #    print ('No average, no ship served.')
        return average_cost