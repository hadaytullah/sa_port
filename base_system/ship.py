import random


class ShipFactory(object):

    # Unique ID of the next created ship.
    ship_id = 1

    @staticmethod
    def factory(ship_type):
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
        return random.randint(Ship.min_size, Ship.max_size)

    @staticmethod
    def next_ship_id():
        ship_id = ShipFactory.ship_id
        ShipFactory.ship_id += 1
        return ship_id


class Ship:

    # TODO: remove constants, add variables, shared ones
    # shared among all ship objects
    min_size = 60
    max_size = 180

    def __init__(self, unique_id, size=None):
        self.unique_id = unique_id
        self.distance = random.randrange(100)

        self.max_speed_kmh = random.randrange(16, 25)  # kilometers per hour

        # urgency indicate the cargo type, fruits and veggies needs to be transferred quickly
        # 1: less urgest, 20:most urgest
        self.cargo_type_urgency = random.randrange(1, 20)

        # The size indicates the ship size, unable to identify suitable scale
        if size is None:
            self.size = random.randrange(60, 180)
        else:
            self.size = size

        # cost per minute, waiting or travelling
        # cost = crew cost + fuel cost
        self.cost = (self.size ** 2) * 0.15

        # changing attributes, should not be here, it is not a property of the ship
        self.wait = 0

        #Learning, relationship between size and cost
            #personal drived fromt he size
            #cost per minute when waiting
#    @classmethod
#    def init_for_factory(cls, filename):
#        "Initialize MyData from a file"
#        data = open(filename).readlines()
#        return cls(data)

#    def small_size(self):
#        self.size = random.randrange(60,80)
#        self.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
#        return self
#
#    def large_size(self):
#        self.size = random.randrange(150,180)
#        self.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
#        return self
#
#    def medium_size(self):
#        self.size = random.randrange(120,140)
#        self.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
#        return self
#
#    def random_size(self):
#        self.size = random.randrange(60,180)
#        self.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
#        return self
