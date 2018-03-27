import random

from base_system.context.abstract_context import AbstractContext
from base_system.ship import Ship


class RandomDistributionContext (AbstractContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Randomly generated ships"
        self.ships_arrived = []
        self.ship_unique_id = 1

    def step(self, **kwargs):
        if random.choice([True, False]): #faster solution bool(random.getrandbits(1))
            self.ships_arrived.append(Ship(self.ship_unique_id))
            self.ship_unique_id += 1

    def finish_step(self, **kwargs):
        pass

    def get_arrived(self):
        return self.ships_arrived


