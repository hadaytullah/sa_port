import random

from context.base_context import BaseObjectiveContext
from context.ship import ShipFactory


class MajorityLargeShipsObjectiveContext(BaseObjectiveContext):
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


