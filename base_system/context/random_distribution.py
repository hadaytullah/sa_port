import random
#from base_system.context.abstract_context import AbstractContext
from base_system.context.base_context import BaseContext
from base_system.ship import Ship
from base_system.ship import ShipFactory


class RandomDistributionContext(BaseContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Randomly generated ships"

    def step(self, **kwargs):

        if self.add_new_ship():
            if random.choice([True, False]): #faster solution bool(random.getrandbits(1))
                self.ships_arrived.append(ShipFactory.factory('Large', self.ship_unique_id))
                self.ship_unique_id += 1

            elif random.choice([True, False]): #faster solution bool(random.getrandbits(1))
                self.ships_arrived.append(ShipFactory.factory('Medium', self.ship_unique_id))
                self.ship_unique_id += 1

            elif random.choice([True, False]): #faster solution bool(random.getrandbits(1))
                self.ships_arrived.append(ShipFactory.factory('Small', self.ship_unique_id))
                self.ship_unique_id += 1

            else:
                self.ships_arrived.append(ShipFactory.factory('Any', self.ship_unique_id))
                self.ship_unique_id += 1

    def finish_step(self, **kwargs):
        pass




