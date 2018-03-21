#Authors: Hadaytullah
import random

#a port can hold one or more service points to serve the ships with varying traits
# for example, capacity, staff, etc.

class Terminal:
    def __init__(self,strategy):

        self.strategy = strategy
        #per minute load processing
        self.processing_capacity = random.randrange(2,3)

        #ideal number of ships it can process in 24hrs (one run)
        # set at the 75%, rest of the time goes into maintainenance, breaks etc.
        self.capacity = self.processing_capacity * (24*60) * 0.75

        #the serving strategy
        #self.strategy = strategy

        self.served_ships = []
        #self.ship_unique_id = 1

        #self.resources = 0  #staff
        self.ship_on_dock = None
        self.docked_ship_processed = 0

    def step(self, arrived):
        if self.ship_on_dock is None:
            if len(arrived) > 0:
                let_inside_ship, let_inside_index = self.strategy.apply(arrived);

                self.ship_on_dock = let_inside_ship
                self.docked_ship_processed = self.ship_on_dock.size

                print ('Serving the ship %i of size %i at %i km with speed of %i kmh' %(self.ship_on_dock.unique_id,
                                                                                        self.ship_on_dock.size, self.ship_on_dock.distance, self.ship_on_dock.max_speed_kmh));
                self.process()
                self.served_ships.append(arrived.pop(let_inside_index));

                for index, waiting_ship in enumerate(arrived):
                    waiting_ship.wait += 1
                    #current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
                    #print('Sever Ships:%d' %len(self.served_ships))
        else:
            self.process()

    def process(self):
        #print ('Serving the ship %i of size %i at %i km with speed of %i kmh' %(ship.unique_id, ship.size, ship.distance, ship.max_speed_kmh));
        if self.ship_on_dock is not None:
            if self.docked_ship_processed > 0:
                print ('Still Serving %i' %self.ship_on_dock.unique_id)
                self.docked_ship_processed -= self.processing_capacity
            else:
                self.ship_on_dock  = None
                self.docked_ship_processed = 0




