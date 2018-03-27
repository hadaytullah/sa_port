from abc import ABC, abstractmethod

class AbstractContext(ABC):

    def __init__(self):
        #self.value = value
        super().__init__()

    @abstractmethod
    def step(self):
        pass
