import random

from context.base_context import BaseObjectiveContext
from context.ship import ShipFactory


class MajoritySmallShipsObjectiveContext (BaseObjectiveContext):
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


