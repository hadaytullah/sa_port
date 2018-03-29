import random

from base_system.context.base_context import BaseContext
from base_system.ship import ShipFactory


class FlexibleContext(BaseContext):
    """Flexible context which may change its distribution of ships.

    :param tuple distribution:
        Distribution of different ship types. Should be a 2-tuple of floats (in [0, 1]) defining the intervals from
        which to draw the different the ship types. Small ships are drawn with probability distribution[0], medium
        ships with probability distribution[1] - distribution[0] and large ships with probability 1 - distribution[1].
    """
    def __init__(self, distribution):
        super().__init__()
        self.context_name = "Flexible context"
        self._distribution = distribution

    @property
    def distribution(self):
        return self._distribution

    @distribution.setter
    def distribution(self, dist):
        self._distribution = dist

    def step(self, **kwargs):
        if self.add_new_ship():
            r = random.random()
            if r < self.distribution[0]:
                self.ships_arrived.append(ShipFactory.create('Small'))
            elif r < self.distribution[1]:
                self.ships_arrived.append(ShipFactory.create('Medium'))
            else:
                self.ships_arrived.append(ShipFactory.create('Large'))




