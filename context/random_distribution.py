from context.base_context import BaseObjectiveContext
from context.ship import ShipFactory


class RandomDistributionObjectiveContext(BaseObjectiveContext):
    def __init__(self):
        super().__init__()
        self.context_name = "Randomly generated ships"

    def step(self, **kwargs):
        if self.add_new_ship():
            # All ships have random size.
            self.ships_arrived.append(ShipFactory.create('Any'))

    def finish_step(self, **kwargs):
        pass




