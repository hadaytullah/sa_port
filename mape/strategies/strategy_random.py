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
    def apply(self, arriving):
        let_inside_index = random.randrange(0,len(arriving))
        return arriving[let_inside_index], let_inside_index
