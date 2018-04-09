"""Base agent class implementing some of the very basic functions.
"""


class Agent:
    """Base agent class.

    An agent has a name and some neighbors it can communicate with.
    """
    def __init__(self, name):
        self._name = name
        self._neighbors = {}

    @property
    def name(self):
        """Name of the agent.

        All agent names should be unique.
        """
        return self._name

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
        pass

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
