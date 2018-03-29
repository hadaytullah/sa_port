import random

from base_system.context.base_context import BaseContext
from base_system.ship import ShipFactory


class RandomDistributionContext(BaseContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Randomly generated ships"

    def step(self, **kwargs):
        if self.add_new_ship():
            # All ships have random size.
            self.ships_arrived.append(ShipFactory.create('Any'))

    def finish_step(self, **kwargs):
        pass




