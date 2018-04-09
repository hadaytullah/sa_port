import argparse

from context.flexible import FlexibleObjectiveContext

import simulation
from mape.evaluation.average_wait import AverageWait
from mape.evaluation.ships_satisfaction import ShipsSatisfaction
from mape.strategies.closest_first import ClosestFirstStrategy
from mape.strategies.closest_smallest_first import ClosestSmallestFirstStrategy
from mape.strategies.random_first import RandomFirstStrategy

if __name__ == "__main__":
    desc = "Command line script to run self-adaptive terminals simulations."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-a', metavar='agents', type=int, dest='agents',
                        help="Number of agents.", default=4)
    parser.add_argument('-s', metavar='steps', type=int, dest='steps',
                        help="Number of simulation steps.", default=24*60)
    args = parser.parse_args()

    n_agents = args.agents
    steps = args.steps

    ctx = FlexibleObjectiveContext([0.3, 0.3])
    ctx.set_traffic_density(ctx.TRAFFIC_LOW)
    agent_kwargs = {'strategy_list': [RandomFirstStrategy(), ClosestFirstStrategy(), ClosestSmallestFirstStrategy()],
                    'objective_context': ctx,
                    'evaluation_list': [AverageWait(), ShipsSatisfaction()]
                    }
    agents = simulation.create_terminals(n_agents, **agent_kwargs)
    #evaluation = AverageWait()
    evaluation = ShipsSatisfaction()
    sim = simulation.Simulation(agents, ctx, evaluation)
    sim.run(steps, 'random')
    sim.end()

