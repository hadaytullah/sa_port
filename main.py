from cargo_ship_port import CargoShipPort
from mape import Mape
#from strategy import strategy

#TODO: define abstract interface and change the names in the strategies files
from strategies.strategy_random import Strategy as StrategyRandom
from strategies.strategy_closest_first import Strategy as StrategyClosest
from strategies.strategy_smallest_first import Strategy as StrategySmallest
from strategies.strategy_closest_smallest_first import Strategy as StrategyClosestSmallest
#from mape import Mape


mape = Mape()
runs = 20
for i in range(runs):
    cargo_ship_port = CargoShipPort(StrategyClosestSmallest())
    average_wait_time = 0
    
    #for i in range(runs):
    average_wait_time += cargo_ship_port.step()
    
print('Average wait time in %i runs is %i' %(runs,average_wait_time/runs))
mape.monitor(average_wait_time)
