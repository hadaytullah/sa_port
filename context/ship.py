import random


# K, KG
SHIP_MIN_SIZE = 60
SHIP_MAX_SIZE = 180

# minutes
SHIP_MIN_WAIT = 4
SHIP_MAX_WAIT = 20

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
            return random.randrange(60, 80)
        if ship_type == "Medium":
            return random.randrange(120, 140)
        if ship_type == "Large":
            return random.randrange(150, 180)
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
        self.distance = random.randrange(100)

        self.max_speed_kmh = random.randrange(16, 25)  # kilometers per hour

        # urgency indicate the cargo type, fruits and veggies needs to be transferred quickly
        # 1: less urgest, 20:most urgest
        self.cargo_type_urgency = random.randrange(1, 20)


        # The size indicates the ship size, unable to identify suitable scale
        if size is None:
            self.size = random.randrange(SHIP_MIN_SIZE, SHIP_MAX_SIZE)
        else:
            self.size = size

        # cost per minute, waiting or travelling
        # cost = crew cost + fuel cost
        self.cost = (self.size ** 2) * 0.15

        # changing attributes, should not be here, it is not a property of the ship
        self.wait = 0

        #Constraints
        self.max_wait = random.randrange(SHIP_MIN_WAIT, SHIP_MAX_WAIT) if max_wait is None else max_wait


    def __str__(self):
        return "S{}(sz={}, ur={}, c={:.3f})".format(self.unique_id, self.size, self.cargo_type_urgency, self.cost)

