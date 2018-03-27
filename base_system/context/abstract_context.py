from abc import ABC, abstractmethod
from base_system.ship import Ship

class AbstractContext(ABC):

    def __init__(self):
        #self.value = value
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
