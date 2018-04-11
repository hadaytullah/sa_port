import argparse


import context
from knowledge_base import DictKB
import simulation
from mape.evaluation.average_wait import AverageWait
from mape.evaluation.cost import Cost
from mape.evaluation.ships_satisfaction import ShipsSatisfaction

from mape.strategies.closest_first import ClosestFirstStrategy
from mape.strategies.closest_smallest_first import ClosestSmallestFirstStrategy
from mape.strategies.smallest_first import SmallestFirstStrategy
from mape.strategies.random_first import RandomFirstStrategy

if __name__ == "__main__":
    desc = "Command line script to run self-adaptive terminals simulations."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-a', metavar='agents', type=int, dest='agents',
                        help="Number of agents.", default=4)
    parser.add_argument('-s', metavar='steps', type=int, dest='steps',
                        help="Number of simulation steps (minute of simulated time / step).", default=24*60*50)
    args = parser.parse_args()

    n_agents = args.agents
    steps = args.steps

    ctx = context.FlexibleObjectiveContext(context.FLEXIBLE_ALL_SHIPS_EVENLY)
    ctx.set_traffic_density(context.TRAFFIC_HIGH)

    shared_knowledge_base = DictKB()

    shared_knowledge_base.create('strategy_list',
                                 [RandomFirstStrategy(),
                                  ClosestFirstStrategy(),
                                  ClosestSmallestFirstStrategy(),
                                  SmallestFirstStrategy()])

    shared_knowledge_base.create('evaluation_list',
                                 [AverageWait(),
                                  Cost(),
                                  ShipsSatisfaction()])

#    agent_kwargs = {'strategy_list': [RandomFirstStrategy(),
#                                      ClosestFirstStrategy(),
#                                      ClosestSmallestFirstStrategy(),
#                                      SmallestFirstStrategy()],
#                    'objective_context': ctx,
#                    'evaluation_list': [AverageWait(),
#                                        Cost(),
#                                        ShipsSatisfaction()],
#                    'perceived_attributes': ['ships_arrived', 'traffic_density']
#                    }
    agent_kwargs = {'strategy': RandomFirstStrategy(),
                    'objective_context': ctx,
                    'evaluation': AverageWait(),
                    'perceived_attributes': ['ships_arrived', 'traffic_density']
                    }
    agents = simulation.create_terminals(n_agents, **agent_kwargs)

    for a in agents:
        a.enable_mape(True)

    #evaluation = AverageWait()
    evaluation = ShipsSatisfaction()
    sim = simulation.Simulation(agents, ctx, evaluation)
    sim.run(steps, 'random')
    sim.end()

