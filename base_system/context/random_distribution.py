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
                self.ships_arrived.append(ShipFactory.factory('Large'))
            elif random.choice([True, False]): #faster solution bool(random.getrandbits(1))
                self.ships_arrived.append(ShipFactory.factory('Medium'))
            elif random.choice([True, False]): #faster solution bool(random.getrandbits(1))
                self.ships_arrived.append(ShipFactory.factory('Small'))
            else:
                self.ships_arrived.append(ShipFactory.factory('Any'))

    def finish_step(self, **kwargs):
        pass




