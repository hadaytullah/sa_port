from mape.strategies.strategy_meta_data import StrategyMetaData

class ClosestSmallestFirstStrategy:
    #TODO: META data for decision making at Planning or META-SA layer
    #context = [ContextA, ContextB]
    #quality = [5,10,1]

    def __init__(self):
        self.name = 'ClosestSmallestFirstStrategy'

    def apply(self, arriving):
        #let_inside_ship = arriving[0];
        #let_inside_index = 0;

        closest_ship_index = 0;
        smallest_ship_index = 0;
        closest_let_inside_ship = arriving[0]
        smallest_let_inside_ship = arriving[0]

        for index, current_ship in enumerate(arriving):
            if current_ship.distance < closest_let_inside_ship.distance:
                closest_ship_index = index
                closest_let_inside_ship = current_ship
            if current_ship.size < smallest_let_inside_ship.size:
                smallest_ship_index = index
                smallest_let_inside_ship = current_ship

        if closest_ship_index == smallest_ship_index: #the same ship is smallest and closest, good
            let_inside_index = closest_ship_index
        elif abs(arriving[closest_ship_index].distance - arriving[smallest_ship_index].distance) < 10:
            # the difference in distance is less than 10 km then let the small ship go forward
            let_inside_index = smallest_ship_index
        else:
            let_inside_index = closest_ship_index

        return arriving[let_inside_index], let_inside_index
