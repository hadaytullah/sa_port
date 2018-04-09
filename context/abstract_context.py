from abc import ABC, abstractmethod


class AbstractObjectiveContext(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def step(self, **kwargs):
        pass

    @abstractmethod
    def finish_step(self, **kwargs):
        pass

    @abstractmethod
    def get_arrived(self):
        pass

    @abstractmethod
    def set_traffic_density(self, value):
        pass
