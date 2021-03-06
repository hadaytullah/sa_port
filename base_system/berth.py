import random

from util import add_callbacks
from base_system.agent import Agent
from mape.mape import Mape
from context.subjective_context import SubjectiveContext


class Berth(Mape, Agent):
    """Berth which serves ships by unloading their cargo.
    """
    def __init__(self, strategy, objective_context, evaluation, perceived_attributes, name=None):
        super().__init__()
        self._name = 'T00' if name is None else name
        self.objective_ctx = objective_context
        self.subjective_ctx = SubjectiveContext(perceived_attributes)
        #self._knowledge_base = DictKB()
        #self._strategy = strategy_list[0] if len(strategy_list) > 0 else None
        self._strategy = strategy
        self._neighbors = {}

        # Unload speed for each crane. TEU / minute, i.e. approx 2 minutes per unloading, 2 TEUs at a time.
        self.crane_speed = 1
        # Cranes part of the berth. It could be objects, but lets see if more properties for cranes become desirable.
        self.cranes_count = random.randrange(1, 4)
        self.processing_capacity = self.crane_speed * self.cranes_count
        # Processing capacity per day.
        # TODO: Verify value of this. Are cargo ports operational 24/7?
        self._capacity = self.processing_capacity * (24*60) * 0.75

        # Current ship on berth, its processing time and previously served ships
        self.ship = None
        self.ship_processed = 0
        self.served_ships = []

        # Initialize knowledge base
        #self._knowledge_base.create('neighbors', {})

    def _get_monitoring_data(self):
        return 23  # TODO

    def _get_id(self):
        return self._name

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy):
        self._strategy = new_strategy

    @property
    def capacity(self):
        """Ideal number of ships the berth can process in 24hrs

        Set at the 75% of the whole processing capacity, rest of the time goes into maintenance, breaks etc.
        """
        return self._capacity

    def add_neighbor(self, nb_name, agent, meta_information=None):
        """Add neighbor for the agent with given dictionary of meta information.

        **Adds the neighbor also into the knowledge base.**

        :param str nb_name: Name of the neighbor
        :param obj agent:
            Reference to the agent, it is added to the meta information with the key 'agent'. This replaces current
            key 'agent' from meta information, if such exists.
        :param dict meta_information:
            Dictionary of meta information about the agent. If the parameter is ``None`` a new dictionary is created.

        :raises: :py:exc:`KeyError` if the name of the new neighbor is already in the neighbors.
        """
        super().add_neighbor(nb_name, agent, meta_information)
        if meta_information is None:
            meta_information = {}
        meta_information['agent'] = agent
        #kb_neighbors = self._knowledge_base.read('neighbors')
        #kb_neighbors[nb_name] = meta_information

    @add_callbacks('prestep', 'poststep')
    def step(self, **kwargs):
        """Base function for the agent to execute some actions during one simulation step.
        """
        if self.ship is not None:
            self.process()
        else:
            ctx = self.subjective_ctx.get_perceived_context(self.objective_ctx)
            arrived = ctx['ships_arrived']
            if len(arrived) > 0:
                let_inside_ship, let_inside_index = self.strategy.apply(arrived)

                self.ship = let_inside_ship
                self.ship_processed = self.ship.size + (self.ship.distance * 60 / self.ship.max_speed_kmh)

                self.log('Serving ship: {}'.format(self.ship))
                self.broadcast("Let inside ship: {}".format(self.ship))
                self.served_ships.append(arrived.pop(let_inside_index))

                for index, waiting_ship in enumerate(arrived):
                    waiting_ship.wait += 1
                    # current_ship.wait + let_inside_ship.size + (let_inside_ship.distance* 60/let_inside_ship.max_speed_kmh)
                    # print('Sever Ships:%d' %len(self.served_ships))
        # super(Terminal, self).step()

    def process(self):
        if self.ship is not None:
            if self.ship_processed > 0:
                #self.log('Still Serving {}'.format(self.ship_on_dock))
                self.ship_processed -= self.processing_capacity
            else:
                self.ship = None
                self.ship_processed = 0

    def finish_step(self, **kwargs):
        """Called on each simulation step after all agents in the simulation have acted.

        Suitable for, e.g., logging internal parameters, interaction between agents, etc.
        """
        pass
