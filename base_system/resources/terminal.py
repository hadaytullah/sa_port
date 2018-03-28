import random


class Terminal:
    """Terminal which serves ships by unloading their cargo.
    """
    def __init__(self, strategy, ctx, name=None):
        self.name = 'T00' if name is None else name
        self.ctx = ctx
        self.strategy = strategy
        # per minute load processing
        self.processing_capacity = 5

        # ideal number of ships it can process in 24hrs (one run)
        # set at the 75%, rest of the time goes into maintainenance, breaks etc.
        self.capacity = self.processing_capacity * (24*60) * 0.75

        self.served_ships = []

        # self.resources = 0  # staff
        self.ship_on_dock = None
        self.docked_ship_processed = 0

    def step(self, **kwargs):
        if self.ship_on_dock is not None:
            return self.process()

        arrived = self.ctx.get_arrived()
        if len(arrived) > 0:
            let_inside_ship, let_inside_index = self.strategy.apply(arrived)

            self.ship_on_dock = let_inside_ship
            self.docked_ship_processed = self.ship_on_dock.size + (self.ship_on_dock.distance * 60/self.ship_on_dock.max_speed_kmh)

            self.log('Serving ship: {}'.format(self.ship_on_dock))
            self.served_ships.append(arrived.pop(let_inside_index))

            for index, waiting_ship in enumerate(arrived):
                waiting_ship.wait += 1
                #current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
                #print('Sever Ships:%d' %len(self.served_ships))

    def process(self):
        if self.ship_on_dock is not None:
            if self.docked_ship_processed > 0:
                self.log('Still Serving {}'.format(self.ship_on_dock))
                self.docked_ship_processed -= self.processing_capacity
            else:
                self.ship_on_dock = None
                self.docked_ship_processed = 0

    def finish_step(self, **kwargs):
        pass

    def log(self, msg):
        print("{}: {}".format(self.name, msg))




