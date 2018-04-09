import random

from context.abstract_context import AbstractObjectiveContext


class BaseObjectiveObjectiveContext(AbstractObjectiveContext):

    #Traffic volumes
    TRAFFIC_LOW = 'Low'
    TRAFFIC_HIGH = 'High'
    TRAFFIC_RANDOM = 'Random'

    def __init__(self):
        super().__init__()
        self.context_name = 'Base context'
        self.ships_arrived = []
        self.traffic_density = self.TRAFFIC_LOW

    def step(self, **kwargs):
        pass

    def finish_step(self, **kwargs):
        pass

    def add_new_ship(self):
        if self.traffic_density == 'High':
            return True if random.randrange(0, 100) < 75 else False
        elif self.traffic_density == 'Low':
            return False if random.randrange(0, 100) < 75 else True
        elif self.traffic_density == 'Random':
            return False if random.randrange(0, 100) < 50 else True

    def set_traffic_density(self, value):
        self.traffic_density = value

    def get_arrived(self):
        return self.ships_arrived


