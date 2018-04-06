import random


# May be called Berths? https://en.wikipedia.org/wiki/Berth_(moorings)
class Terminal:
    """Terminal which serves ships by unloading their cargo.
    """
    def __init__(self, strategy, ctx, name=None):
        self._name = 'T00' if name is None else name
        self.ctx = ctx
        self.strategy = strategy
        self._neighbors = {}
        # per minute load processing
        self.processing_capacity = 5
        self._capacity = self.processing_capacity * (24*60) * 0.75
        self.served_ships = []
        # self.resources = 0  # staff

        # Cranes part of the terminal. It could be objects, but lets see if more properties for cranes become desirable.
        self.cranes_count = random.randrange(1, 4)
        self.ship_on_dock = None
        self.docked_ship_processed = 0

    @property
    def name(self):
        """Name of the agent.

        All agent names should be unique.
        """
        return self._name

    @property
    def capacity(self):
        """Ideal number of ships the terminal can process in 24hrs

        Set at the 75% of the whole processing capacity, rest of the time goes into maintenance, breaks etc.
        """
        return self._capacity

    @property
    def neighbors(self):
        """Dictionary of the peers this agent has contact to.

        Keys are the peer names and values are dictionaries of information about the peers. Each value has at least
        key 'agent' which is a reference to the neighbor itself.
        """
        return self._neighbors

    def add_neighbor(self, nb_name, agent, meta_information=None):
        """Add neighbor for the agent with given dictionary of meta information.

        :param str nb_name: Name of the neighbor
        :param obj agent:
            Reference to the agent, it is added to the meta information with the key 'agent'. This replaces current
            key 'agent' from meta information, if such exists.
        :param dict meta_information:
            Dictionary of meta information about the agent. If the parameter is ``None`` a new dictionary is created.

        :raises: :py:exc:`KeyError` if the name of the new neighbor is already in the neighbors.
        """
        if nb_name in self.neighbors:
            raise KeyError("{}: Name {} already in neighbors".format(self.name, nb_name))
        if meta_information is None:
            meta_information = {}
        meta_information['agent'] = agent
        self.neighbors[nb_name] = meta_information

    def step(self, **kwargs):
        """Base function for the agent to execute some actions during one simulation step.
        """
        if self.ship_on_dock is not None:
            return self.process()

        arrived = self.ctx.get_arrived()
        if len(arrived) > 0:
            let_inside_ship, let_inside_index = self.strategy.apply(arrived)

            self.ship_on_dock = let_inside_ship
            self.docked_ship_processed = self.ship_on_dock.size + (self.ship_on_dock.distance * 60/self.ship_on_dock.max_speed_kmh)

            self.log('Serving ship: {}'.format(self.ship_on_dock))
            self.broadcast("Let inside ship: {}".format(self.ship_on_dock))
            self.served_ships.append(arrived.pop(let_inside_index))

            for index, waiting_ship in enumerate(arrived):
                waiting_ship.wait += 1
                # current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
                # print('Sever Ships:%d' %len(self.served_ships))

    def process(self):
        if self.ship_on_dock is not None:
            if self.docked_ship_processed > 0:
                self.log('Still Serving {}'.format(self.ship_on_dock))
                self.docked_ship_processed -= self.processing_capacity
            else:
                self.ship_on_dock = None
                self.docked_ship_processed = 0

    def finish_step(self, **kwargs):
        """Called on each simulation step after all agents in the simulation have acted.

        Suitable for, e.g., logging internal parameters, interaction between agents, etc.
        """
        pass

    def log(self, msg):
        """Base logging behavior.
        """
        print("{}: {}".format(self.name, msg))

    def broadcast(self, msg):
        """Broadcast a message to all neighbors.
        """
        rets = {}
        for nb in self.neighbors:
            rets[nb] = self.send(nb, msg)
        return rets

    def send(self, agent_name, msg):
        """Send a message to an agent

        Agent name must be in `neighbors`.

        :returns: Message (if any) returned by the agent.
        """
        self.log("SND -> {}: {}".format(agent_name, msg))
        return self.neighbors[agent_name]['agent'].rcv(self.name, msg)

    def rcv(self, agent_name, msg):
        """Receive message from an agent.
        """
        self.log("RCV <- {}: {}".format(agent_name, msg))
        return {'agent': self.name, 'status': 'OK', 'msg': msg}





