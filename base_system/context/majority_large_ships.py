
#from base_system.context.abstract_context import AbstractContext

from base_system.ship import ShipFactory
from base_system.context.base_context import BaseContext
import random


class MajorityLargeShipsContext (BaseContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Majority of the ships are large"
        #self.ships_arrived = []
        #self.ship_unique_id = 1

    def step(self, **kwargs):
        #if random.choice([True, False]): #may or may not arrive #faster solution bool(random.getrandbits(1))
        if self.add_new_ship(): #traffic density dictates this choice
            isLarge = True if random.randrange(0,100) < 90 else False # less probability for larger ships
            if isLarge:
                self.ships_arrived.append(ShipFactory.factory('Large'))
            else:
                self.ships_arrived.append(ShipFactory.factory('Small'))

    def finish_step(self, **kwargs):
        pass


