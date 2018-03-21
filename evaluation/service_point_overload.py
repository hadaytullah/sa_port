from evaluation.abstract_evaluation import AbstractEvaluation


class ServicePointOverLoad(AbstractEvaluation):

    def __init__(self):
        super().__init__()
        self.evaluation_name = "Service Point Overload"
        self.maximize = False


    def evaluate(self, service_point):
        print('PointOverLoad, not implemented.')
        overload = 0
#        if len(ships) > 0:
#            #print("Cost")
#            average_cost = 0
#            cost_sum = 0
#
#            for index, current_ship in enumerate(ships):
#                #print (" Ship %i served in %i minutes" %(current_ship.unique_id, current_ship.wait))
#                cost_sum += (current_ship.cost * current_ship.wait)
#
#            #calculating average
#            average_cost = cost_sum/(60*len(ships))
#            print ("Average Cost: %f €" %average_cost)
#        #else:
#        #    print ('No average, no ship served.')
        return overload
