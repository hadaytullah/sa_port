
from base_system.context.abstract_context import AbstractContext
from base_system.ship import Ship
import random

class MajorityLargeShipsContext (AbstractContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Majority of the ships are large"
        self.ships_arrived = []
        self.ship_unique_id = 1

    def step(self):
        if random.choice([True, False]): #faster solution bool(random.getrandbits(1))
            ship = Ship(self.ship_unique_id).large_size()
            self.ships_arrived.append(ship)
            self.ship_unique_id += 1

    def getShips(self):
        return self.ships_arrived


