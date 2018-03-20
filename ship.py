import random

class Ship: #AgentCoopa(Agent):
    def __init__(self, unique_id):#, model):
        #super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.distance = random.randrange(100);
        self.size = random.randrange(60,180); # indirectly represents the time to unload
        self.wait = 0
        self.max_speed_kmh = random.randrange(16,25) #kilometers per hour
        
        #Learning, relationship between size and cost
            #personal drived fromt he size
            #cost per minute when waiting 