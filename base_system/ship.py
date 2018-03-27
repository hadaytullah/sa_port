import random

class ShipFactory(object):
    # Create based on class name:
    def factory(type):
        #return eval(type + "()")
        if type == "Small":
            ship = ship()
            ship.size = random.randrange(60,80)
            ship.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
            return ship

        elif type == "Medium":
            ship = ship()
            ship.size = random.randrange(120,140)
            ship.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
            return ship

        elif type == "Large":
            ship = ship()
            ship.size = random.randrange(150,180)
            ship.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)
            return ship

        else:
            ship = ship()
            return ship

    factory = staticmethod(factory)

class Ship: #AgentCoopa(Agent):
    def __init__(self, unique_id):#, model):
        #super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.distance = random.randrange(100);

        self.max_speed_kmh = random.randrange(16,25) #kilometers per hour

        #urgency indicate the cargo type, fruits and vegies needs to be transfered quickly
        #1: less urgest, 20:most urgest
        self.cargo_type_urgency = random.randrange(1,20)

        # The size indicates the ship size, unable to identify suitable scale
        self.size = random.randrange(60,180)
        #self.cost = 0

        #self.random_size()

        #random.randrange(60,180) # indirectly represents the time to unload

        #cost per minute, waiting or travelling
        #cost = crew cost + fuel cost
        self.cost = (abs (self.size/10))*(30) * abs(self.size*0.05)

        #changing attributes, should not be here, it is not a property of the ship
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
