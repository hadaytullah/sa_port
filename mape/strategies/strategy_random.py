import random
#def strategy(arriving):
#    let_inside_ship = arriving[0];
#    let_inside_index = 0;
#    for index, current_ship in enumerate(arriving):
#        if current_ship.distance < let_inside_ship.distance:
#            let_inside_ship = current_ship
#            let_inside_index = index
#    return let_inside_ship, let_inside_index

class Strategy:
    def __init__(self):
        self.meta_data = StrategyMetaData()
        self.meta_data.influence_wait_time = 0 #don't know,
        self.meta_data.influence_cost = 0 #don't know,
        self.meta_data.influence_overload = 0 #don't know,
        self.meta_data.influence_underload = 0 #don't know,

    def apply(self, arriving):
        let_inside_index = random.randrange(0,len(arriving))
        return arriving[let_inside_index], let_inside_index
