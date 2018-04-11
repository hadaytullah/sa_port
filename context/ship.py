import math
import random


# Size in TEU: https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit
# Ships range from ~1000 to more than 14500: https://en.wikipedia.org/wiki/Container_ship#Size_categories
# Average ship size in 2015 was ~3700 TEU: https://www.usmma.edu/sites/usmma.edu/files/docs/CMA%20Paper%20Murray%201%20%282%29.pdf
SHIP_MIN_SIZE = 500
SHIP_MAX_SIZE = 16000

# minutes
SHIP_MIN_WAIT = 360  # 6 hours, could be more probably
SHIP_MAX_WAIT = 7200  # 5 days, could be more probably

# 23 knots seems to be "the standard" (in 2015) according to Murray's paper (see above)
SPEED_23_KNOTS = 42.596

# Tons of fuel per TEU to travel at 23 knots for a day, approximation from Murray's paper (p. 18)
FUEL_PER_TEU = 0.02

# Around 390 today according to: https://shipandbunker.com/prices
# Bunker price is price per tonne (of coal or oil, I think oil is what above link measures)
FUEL_BUNKER_PRICE = 390

#SHIP_LOAD_TYPE = {
#    'bio':{
#        'max_wait_time': 60
#    },
#    'metal':{
#        'max_wait_time': 420
#    },
#    'rock':{
#        'max_wait_time': 800
#    }
#}


class ShipFactory(object):

    # Unique ID of the next created ship.
    ship_id = 1

    @staticmethod
    def create(ship_type):
        """Create a new ship.

        :param ship_type:
            If ship type is ``Small``, ``Medium`` or ``Large``, creates a ship in that size category. If ship type is
            an integer, creates a ship with that exact size. Otherwise creates a random ship.
        """
        unique_id = ShipFactory.next_ship_id()
        return Ship(unique_id, ShipFactory.get_ship_size(ship_type))

    @staticmethod
    def get_ship_size(ship_type):
        """Get new ship size by ship type.
        """
        if ship_type == "Small":
            return random.randrange(500, 3000)  # Feeders
        if ship_type == "Medium":
            return random.randrange(3000, 10000)  # Panamax & Post-Panamax
        if ship_type == "Large":
            return random.randrange(10000, 16000)  # New Panamax & Ultra-large Cargo Vessel (ULCV)
        if type(ship_type) == int:
            return ship_type
        return random.randint(SHIP_MIN_SIZE, SHIP_MAX_SIZE)

    @staticmethod
    def next_ship_id():
        """Request next ship's unique id.
        """
        ship_id = ShipFactory.ship_id
        ShipFactory.ship_id += 1
        return ship_id


class Ship:

    def __init__(self, unique_id, size=None, max_wait=None):
        self.unique_id = unique_id

        # urgency indicate the cargo type, fruits and veggies needs to be transferred quickly
        # 1: less urgest, 20:most urgest
        self.cargo_type_urgency = random.randrange(1, 20)

        # The size in TEU: https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit
        if size is None:
            self.size = random.randrange(SHIP_MIN_SIZE, SHIP_MAX_SIZE)
        else:
            self.size = size

        if self.size <= (SHIP_MAX_SIZE + SHIP_MIN_SIZE) / 2:
            self.max_speed_kmh = random.randrange(38, 46)  # kilometers per
        else:
            self.max_speed_kmh = random.randrange(30, 38)

        # Atlantic ocean varies from ~2850 to 6400 km in width
        self.distance = random.randrange(3000)
        self.minutes_to_port = int((self.distance / self.max_speed_kmh) * 60)

        # Hand-wavy estimate: constant + cubic root of the ship size in TEU.
        # size=500: 18, size=14000: 33
        self.number_of_crew = int(10 + math.pow(self.size, 0.333))
        # 150 USD / day (low estimate probably)
        self.crew_average_salary = 150
        self.crew_cost_per_minute = (self.number_of_crew * self.crew_average_salary) / 1440

        # Tons of fuel per minute and its cost (FUEL_PER_TEU should be a function of the ship size)
        self.fuel_per_minute = (FUEL_PER_TEU * self.size) / 1440
        self.fuel_cost_per_minute = self.fuel_per_minute * FUEL_BUNKER_PRICE

        # cost per minute, waiting or travelling
        # cost = crew cost + fuel cost
        self.travelling_cost = self.fuel_cost_per_minute + self.crew_cost_per_minute
        self.waiting_cost = self.crew_cost_per_minute
        self.cost = self.travelling_cost

        # changing attributes, should not be here, it is not a property of the ship
        self.wait = 0

        #Constraints
        self.max_wait = random.randrange(SHIP_MIN_WAIT, SHIP_MAX_WAIT) if max_wait is None else max_wait

    def __str__(self):
        return "S{}(sz={}, ur={}, c={:.3f})".format(self.unique_id, self.size, self.cargo_type_urgency, self.cost)

