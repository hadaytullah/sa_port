#Authors: Hadaytullah
import random

#a port can hold one or more service points to serve the ships with varying traits
# for example, capacity, staff, etc.

class ServicePoint:
    def __init__(self):
        self.capacity = random.randrange(120,180); #max size consumer that it can serve
        #self.resources = 0  #staff

