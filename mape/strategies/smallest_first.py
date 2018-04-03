
#def strategy(arriving):
#    let_inside_ship = arriving[0];
#    let_inside_index = 0;
#    for index, current_ship in enumerate(arriving):
#        if current_ship.distance < let_inside_ship.distance:
#            let_inside_ship = current_ship
#            let_inside_index = index
#    return let_inside_ship, let_inside_index

class SmallestFirstStrategy:
    def __init__(self):
        self.meta_data = StrategyMetaData()
        self.meta_data.influence_wait_time = -1 #wait time decreasing, weight
        self.meta_data.influence_cost = -1 #cost reducing
        self.meta_data.influence_overload = 0 #don't know, learn and decide
        self.meta_data.influence_underload = 0

    def apply(self, arriving):
        let_inside_ship = arriving[0];
        let_inside_index = 0;
        for index, current_ship in enumerate(arriving):
            if current_ship.size < let_inside_ship.size:
                let_inside_ship = current_ship
                let_inside_index = index
        return let_inside_ship, let_inside_index
