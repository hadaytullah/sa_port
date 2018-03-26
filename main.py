#from cargo_ship_port import CargoShipPort
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

mape = Mape()
steps = 24*60
#cargo_ship_port = PortModel(StrategyRandom())
cargo_ship_port = PortModel(StrategyClosest())
evaluation = AverageWait()

for i in range(steps):
    cargo_ship_port.step()

#print ("Average Wait: %f hours" %average_wait_time)

print ('%s: %i minutes' %(evaluation.evaluation_name, evaluation.evaluate(cargo_ship_port)))
print ('ships still waiting: %i' %len(cargo_ship_port.arriving))


    #cargo_ship_port = CargoShipPort(StrategyRandom(), AverageWait())
    #cargo_ship_port = CargoShipPort(StrategyRandom(), Cost())
    #average_wait_time = 0
    
    #for i in range(runs):
    #average_wait_time += cargo_ship_port.step()
    
#print('Average wait time in %i runs is %i' %(runs,average_wait_time/runs))
#mape.monitor(average_wait_time)
