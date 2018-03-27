#from cargo_ship_port import CargoShipPort
import random
import argparse

from base_system.port_model import PortModel
from mape.mape import Mape
from mape.evaluation.average_wait import AverageWait
from mape.evaluation.cost import Cost
#from strategy import strategy

#TODO: define abstract interface and change the names in the strategies files
from mape.strategies.strategy_random import Strategy as StrategyRandom
from mape.strategies.strategy_closest_first import Strategy as StrategyClosest
from mape.strategies.strategy_smallest_first import Strategy as StrategySmallest
from mape.strategies.strategy_closest_smallest_first import Strategy as StrategyClosestSmallest
#from mape import Mape

import simulation


#mape = Mape()
#runs = 20
#for i in range(runs):
#    #cargo_ship_port = CargoShipPort(StrategyClosestSmallest(), AverageWait())
#    cargo_ship_port = CargoShipPort(StrategyClosestSmallest(), Cost())
#    average_wait_time = 0
#
#    #for i in range(runs):
#    average_wait_time += cargo_ship_port.step()
#
#print('Average wait time in %i runs is %i' %(runs,average_wait_time/runs))
#mape.monitor(average_wait_time)

if __name__ == "__main__":
    desc = "Command line script to run self-adaptive terminals simulations."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-a', metavar='agents', type=int, dest='agents',
                        help="Number of agents.", default=4)
    parser.add_argument('-s', metavar='steps', type=int, dest='steps',
                        help="Number of simulation steps.", default=24*60)
    args = parser.parse_args()

    n_agents = args.agents
    steps = args.steps
    port_kwargs = {'strategy': StrategyClosest()}
    simulation.run(n_agents, steps, order='random', port_kwargs=port_kwargs)

    #mape = Mape()
    #cargo_ship_port = PortModel(StrategyRandom())
    #cargo_ship_port = PortModel(StrategyClosest())
    #evaluation = AverageWait()

    #for i in range(steps):
    #    cargo_ship_port.step()

    #print ("Average Wait: %f hours" %average_wait_time)

    #print ('%s: %i minutes' %(evaluation.evaluation_name, evaluation.evaluate(cargo_ship_port)))
    #print ('ships still waiting: %i' %len(cargo_ship_port.arriving))


        #cargo_ship_port = CargoShipPort(StrategyRandom(), AverageWait())
        #cargo_ship_port = CargoShipPort(StrategyRandom(), Cost())
        #average_wait_time = 0

        #for i in range(runs):
        #average_wait_time += cargo_ship_port.step()

    #print('Average wait time in %i runs is %i' %(runs,average_wait_time/runs))
    #mape.monitor(average_wait_time)
