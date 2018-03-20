import random
import datetime, threading
from ship import Ship
from strategy import strategy
from mape import Mape


mape_loop = Mape()


#-----------------------
served_ships = [];
def on_arrival(arriving):
    while len(arriving) != 0:
        
        let_inside_ship, let_inside_index = strategy(arriving);
        
#        for index, current_ship in enumerate(arriving):
#            if current_ship.distance < let_inside_ship.distance:
#                let_inside_ship = current_ship
#                let_inside_index = index

        print ('Letting in the near by ship %i of size %i at %i km with speed of %i kmh' %(let_inside_ship.unique_id, let_inside_ship.size, let_inside_ship.distance, let_inside_ship.max_speed_kmh));
        #print (let_inside_index)


        #print('Serving')
        served_ships.append(arriving.pop(let_inside_index));

        for index, current_ship in enumerate(arriving):
            current_ship.wait = current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
    print('Sever Ships:%d' %len(served_ships))

#------ evaluation / goal function --------
def calculate_average():
    print("WAIT TIMES")
    average_wait_time = 0
    wait_sum = 0
    for index, current_ship in enumerate(served_ships):
        print (" Ship %i served in %i minutes" %(current_ship.unique_id, current_ship.wait))
        wait_sum += current_ship.wait
    
    #calculating average
    average_wait_time = wait_sum/(60*len(served_ships))
    print ("Average Wait: %f hours" %average_wait_time)
    
    #simulating monitoring of the objective
    mape_loop.monitor(average_wait_time)
    
#------------------ main -------------------
steps = 2;
next_ship_id = 1;
def simulate_arrival():
    global steps
    global next_ship_id
    print (datetime.datetime.now())
    arriving = []
    for i in range(1,random.randrange(2, 7)):#2 to 7 ships arriving #range (1,20):
        arriving.append(Ship(next_ship_id))
        next_ship_id += 1
    
    threading.Timer(1, on_arrival, [arriving]).start()
    
    if steps != 0:
        threading.Timer(random.randrange(3, 6), simulate_arrival).start()
        steps-=1
    else:
        calculate_average()

simulate_arrival()
simulate_arrival()
simulate_arrival()

