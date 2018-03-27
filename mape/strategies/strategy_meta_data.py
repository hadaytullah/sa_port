
class StrategyMetaData:
    def __init__(self):
        # there can be positive and negative incluences between 0 and 1
        self.influence_wait_time = 0
        self.influence_cost = 0
        self.influence_overload = 0
        self.influence_underload = 0
