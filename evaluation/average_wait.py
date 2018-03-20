from evaluation.abstract_evaluation import AbstractEvaluation

class AverageWait(AbstractEvaluation):

    def __init__(self):
        super().__init__()

    def evaluate(self, ships):
        average_wait_time = 0
        if len(ships) > 0:
            print("WAIT TIMES")
            average_wait_time = 0
            wait_sum = 0

            for index, current_ship in enumerate(ships):
                print (" Ship %i served in %i minutes" %(current_ship.unique_id, current_ship.wait))
                wait_sum += current_ship.wait

            #calculating average
            average_wait_time = wait_sum/(60*len(ships))
            print ("Average Wait: %f hours" %average_wait_time)
        #else:
        #    print ('No average, no ship served.')
        return average_wait_time
