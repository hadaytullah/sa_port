
from base_system.context.abstract_context import AbstractContext
from base_system.ship import Ship
import random


class MajoritySmallShipsContext (AbstractContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Majority of the ships are small"
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

