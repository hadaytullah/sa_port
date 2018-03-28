import random

from base_system.context.base_context import BaseContext
from base_system.ship import ShipFactory


class MajoritySmallShipsContext (BaseContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Majority of the ships are small"

    def step(self, **kwargs):
        if self.add_new_ship():  # traffic density dictates this choice
            small_ship = True if random.randrange(0, 100) < 90 else False  # less probability for larger ships
            if small_ship:
                self.ships_arrived.append(ShipFactory.create('Small'))
            else:
                self.ships_arrived.append(ShipFactory.create('Large'))

    def finish_step(self, **kwargs):
        pass


