import random

from context.abstract_context import AbstractObjectiveContext


class BaseObjectiveContext(AbstractObjectiveContext):

    # Traffic volumes
    TRAFFIC_LOW = 'Low'
    TRAFFIC_HIGH = 'High'
    TRAFFIC_RANDOM = 'Random'
    TRAFFIC_MEDIUM = 'Medium'  # More meaningful name for TRAFFIC_RANDOM

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
        rand = random.random()
        if self.traffic_density == 'High':
            # One in every six hours
            return True if rand < (1.0 / 360) else False
        elif self.traffic_density == 'Low':
            # One in every 24 hours
            return True if rand < (1.0 / 1440) else False
        elif self.traffic_density in ('Random', 'Medium'):
            # One in every 12 hours
            return True if rand < (1.0 / 720) else False

    def set_traffic_density(self, value):
        self.traffic_density = value

    def get_arrived(self):
        return self.ships_arrived


