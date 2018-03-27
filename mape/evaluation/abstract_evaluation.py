from abc import ABC, abstractmethod

class AbstractEvaluation(ABC):

    def __init__(self):
        #self.value = value
        super().__init__()

    @abstractmethod
    def evaluate(self):
        pass

