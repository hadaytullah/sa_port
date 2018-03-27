#Author: Hadaytullah
#This is a second version where each step indicates one minute in time

import random
import datetime, threading
from base_system.ship import Ship
from base_system.resources.terminal import Terminal


class PortModel:

    def __init__(self, name="Port", strategy=None):
        self.name = name
        self.terminals = [Terminal(strategy)]

        #self.served_ships = []
        #steps = 2;
        self.ship_unique_id = 1;
        #self.strategy = strategy
        self.clock = 0 #minutes

        #self.evaluation = evaluation
        self.arriving = []

#    def on_arrival_(self, arriving):
#        while len(arriving) != 0:
#            let_inside_ship, let_inside_index = self.strategy.apply(arriving);
#
#            print ('Letting in the near by ship %i of size %i at %i km with speed of %i kmh' %(let_inside_ship.unique_id, let_inside_ship.size, let_inside_ship.distance, let_inside_ship.max_speed_kmh));
#            #print (let_inside_index)
#
#
#            #print('Serving')
#            self.served_ships.append(arriving.pop(let_inside_index));
#
#            for index, current_ship in enumerate(arriving):
#                current_ship.wait = current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
#        print('Sever Ships:%d' %len(self.served_ships))

    def log(self, msg):
        print("{}: {}".format(self.name, msg))


    def step(self, *args, **kwargs):
        self.clock += 1
        self.log('Clock: {}'.format(self.clock))

        arriving = self.simulate_arrival()
        for terminal in self.terminals:
            terminal.step(self.arriving)

        #self.on_arrival(arriving)
        #return self.evaluation.evaluate(self.served_ships)
        #return self.calculate_average()

    def finish_step(self, *args, **kwargs):
        """Callback after each step for logging, etc.

        This is called after all ports (terminals) in the simulation have executed their step.
        """
        pass

    def simulate_arrival(self):
        #TODO: Context-awareness: Generate different traffic patterns for different dates

        #global steps
        #global ship_unique_id
        #print (datetime.datetime.now())
        if random.choice([True, False]): #faster solution bool(random.getrandbits(1))
            self.arriving.append(Ship(self.ship_unique_id))
            self.ship_unique_id += 1


        #arriving = []
        #for i in range(1,random.randrange(5, 10)):#2 to 7 ships arriving #range (1,20):
        #    arriving.append(Ship(self.ship_unique_id))
        #    self.ship_unique_id += 1

        #return arriving
        #self.on_arrival(arriving)
        #threading.Timer(1, on_arrival, [arriving]).start()

        #if steps != 0:
        #    threading.Timer(random.randrange(3, 6), simulate_arrival).start()
        #    steps-=1
        #else:
        #    calculate_average()

    #------ evaluation / goal function --------
#    def calculate_average_old(self):
#        average_wait_time = 0
#        if len(self.served_ships) > 0:
#            print("WAIT TIMES")
#            average_wait_time = 0
#            wait_sum = 0
#
#            for index, current_ship in enumerate(self.served_ships):
#                print (" Ship %i served in %i minutes" %(current_ship.unique_id, current_ship.wait))
#                wait_sum += current_ship.wait
#
#            #calculating average
#            average_wait_time = wait_sum/(60*len(self.served_ships))
#            print ("Average Wait: %f hours" %average_wait_time)
#        else:
#            print ('No average, no ship served.')
#        return average_wait_time
        #simulating monitoring of the objective
        #mape_loop.monitor(average_wait_time)

#    simulate_arrival()
#    simulate_arrival()
#    simulate_arrival()

