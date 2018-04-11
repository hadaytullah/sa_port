import random

from context.base_context import BaseObjectiveContext
from context.ship import ShipFactory


class FlexibleObjectiveContext(BaseObjectiveContext):
    """Flexible context which may change its distribution of ships.

    :param tuple distribution:
        Distribution of different ship types. Should be a 2-tuple of floats (in [0, 1]) defining the intervals from
        which to draw the different the ship types. Small ships are drawn with probability distribution[0], medium
        ships with probability distribution[1] - distribution[0] and large ships with probability 1 - distribution[1].
    """

    # Predefined distributions
    FLEXIBLE_ONLY_SMALL_SHIPS = (1.0, 1.0)
    FLEXIBLE_ONLY_MEDIUM_SHIPS = (0.0, 1.0)
    FLEXIBLE_ONLY_LARGE_SHIPS = (0.0, 0.0)
    FLEXIBLE_ALL_SHIPS_EVENLY = (0.333, 0.666)

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




