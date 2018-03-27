import argparse

from mape.evaluation.average_wait import AverageWait
#TODO: define abstract interface and change the names in the strategies files
from mape.strategies.strategy_closest_first import Strategy as StrategyClosest
from base_system.context.cxt_random_distribution import RandomDistributionContext
from base_system.context.cxt_majority_small_ships import MajoritySmallShipsContext
from base_system.context.cxt_majority_large_ships import MajorityLargeShipsContext
import simulation


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

    #ctx = RandomDistributionContext()
    #ctx = MajorityLargeShipsContext()

    ctx = MajoritySmallShipsContext()

    ctx.set_traffic_density(ctx.TRAFFIC_LOW)
    agent_kwargs = {'strategy': StrategyClosest(), 'ctx': ctx}
    agents = simulation.create_terminals(n_agents, **agent_kwargs)
    evaluation = AverageWait()
    sim = simulation.Simulation(agents, ctx, evaluation)
    sim.run(steps, 'random')
