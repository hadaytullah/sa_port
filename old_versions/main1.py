import random
from ship import Ship
arriving = []

for i in range (1,20):
    arriving.append(Ship(i));

print (arriving)

#Port traffic control



served_ships = [];

while len(arriving) != 0:
    let_inside_ship = arriving[0];
    let_inside_index = 0;
    for index, current_ship in enumerate(arriving):
        if current_ship.distance < let_inside_ship.distance:
            let_inside_ship = current_ship
            let_inside_index = index
        
    print ('Letting in the near by ship %i of size %i at %i km with speed of %i kmh' %(let_inside_ship.unique_id, let_inside_ship.size, let_inside_ship.distance, let_inside_ship.max_speed_kmh));
    #print (let_inside_index)

    
    #print(arriving)
    served_ships.append(arriving.pop(let_inside_index));
    
    for index, current_ship in enumerate(arriving):
        current_ship.wait = current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
    
    

print("WAIT TIMES")
average_wait_time = 0
wait_sum = 0
for index, current_ship in enumerate(served_ships):
    print (" Ship %i served in %i minutes" %(current_ship.unique_id, current_ship.wait))
    wait_sum += current_ship.wait
    
print ("Average Wait: %f hours" %(wait_sum/(60*len(served_ships))))   