import random

from base_system.ship import ShipFactory
from base_system.context.base_context import BaseContext


class MajorityLargeShipsContext(BaseContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Majority of the ships are large"

    def step(self, **kwargs):
        if self.add_new_ship():  # traffic density dictates this choice
            large_ship = True if random.randrange(0, 100) < 90 else False  # less probability for larger ships
            if large_ship:
                self.ships_arrived.append(ShipFactory.create('Large'))
            else:
                self.ships_arrived.append(ShipFactory.create('Small'))

    def finish_step(self, **kwargs):
        pass


