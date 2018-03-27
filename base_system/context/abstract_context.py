from abc import ABC, abstractmethod
from base_system.ship import Ship

class AbstractContext(ABC):

    def __init__(self):
        #self.value = value
        super().__init__()

    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def getShips(self):
        pass

    #factory method to create different kind of ships
    #def factory_large_ship():
    #    ship = new
    #    if type == 'large'


