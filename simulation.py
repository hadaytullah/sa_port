"""Main functionality for creating and executing simulations.
"""
import random

from base_system.berth import Berth


def create_berths(n_terminals, add_neighbors=True, **kwargs):
    """Convenience function to create a number of berths with given kwargs.
    """
    agents = []
    for i in range(n_terminals):
        agent_name = "T{:0>2}".format(i + 1)
        agents.append(Berth(name=agent_name, **kwargs))
    if add_neighbors:
        for a in agents:
            for b in agents:
                if a.name != b.name:
                    a.add_neighbor(b.name, b, None)
    return agents


class Simulation():
    """Main simulation implementation.

    Holds agents, context and evaluation and is responsible for calling the context's and each
    agent's :func:`step` and :func:`finish_step`.

    Usage:
        n_steps = 1000
        sim = Simulation(agents, context, evaluation)
        sim.run(n_steps, *args, **kwargs)
        # do some analysis
        sim.run(n_steps, *args, **kwargs)
        # etc.
    """

    def __init__(self, agents, context, evaluation, **kwargs):
        """Create simulation with given agents, context and evaluation.

        Arbitrary keyword arguments are added as attributes.
        """
        self.ctx = context
        self.agents = agents
        self.evaluation = evaluation
        self.clock = 0

        # Set some arbitrary values given by kwargs if needed
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _init_step(self):
        """Initialize simulation step.
        """
        self.clock += 1

    def _step(self, order='random', **kwargs):
        """Main simulation step. Calls each agent's :func:`step`.

        :param str order:
            If ``order == 'random'``, shuffles agents in every step.
        """
        if order == 'random':
            random.shuffle(self.agents)

        for a in self.agents:
            a.step(**kwargs)

    def _finish_step(self, **kwargs):
        """Callback to each agent after main step has been executed (for logging, etc.).
        """
        self.ctx.finish_step(**kwargs)
        for a in self.agents:
            a.finish_step(**kwargs)

    def run(self, steps, order='random', **kwargs):
        """Main simulation run loop which advances the simulation ``steps`` iterations.

        Additional keyword arguments are passed for agents the context and the agents
        at each time step. Context's step function is called before any agent's step function.

        :param int steps:
            Number of steps to advance the simulation.
        :param str order:
            If ``order == 'random'``, shuffles agents in every step.
        """
        for i in range(steps):
            self._init_step()
            self.ctx.step(**kwargs)
            self._step(order, **kwargs)
            self._finish_step(**kwargs)
            #evaluation.report(ports)

        #for a in self.agents:
        #    print('{} {}: {} {}'.format(a.name, self.evaluation.evaluation_name, self.evaluation.evaluate(a), self.evaluation.evaluation_unit))
        print('Ships still waiting: {}'.format(len(self.ctx.ships_arrived)))

    def end(self, *args, **kwargs):
        """Perform last book-keeping, logging, etc. in order to end the simulation.
        """
        pass
