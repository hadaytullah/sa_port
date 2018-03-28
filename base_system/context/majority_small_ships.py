
#from base_system.context.abstract_context import AbstractContext
from base_system.context.base_context import BaseContext
from base_system.ship import Ship
from base_system.ship import ShipFactory
import random


class MajoritySmallShipsContext (BaseContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Majority of the ships are small"

    def step(self, **kwargs):

        #if random.choice([True, False]): #may or may not arrive #faster solution bool(random.getrandbits(1))
        if self.add_new_ship(): #traffic density dictates this choice
            isSmall = True if random.randrange(0,100) < 90 else False # less probability for larger ships

            if isSmall:
                self.ships_arrived.append(ShipFactory.factory('Small'))
            else:
                self.ships_arrived.append(ShipFactory.factory('Large'))

    def finish_step(self, **kwargs):
        pass


