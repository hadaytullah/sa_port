import random

from base_system.context.abstract_context import AbstractContext
from base_system.ship import Ship


class BernoulliDistribution (AbstractContext):
    """Context creating ships using Bernoulli distribution with given p.
    """
    def __init__(self, p=0.5):
        super().__init__()
        self.context_name = "CTX Bernoulli distribution"
        self.p = p
        self.ships_arrived = []
        self.ship_unique_id = 1

    def step(self, **kwargs):
        if random.random() < self.p:
            self.ships_arrived.append(Ship(self.ship_unique_id))
            self.ship_unique_id += 1

    def finish_step(self, **kwargs):
        pass

    def get_arrived(self):
        return self.ships_arrived
