"""Main functions for creating and executing simulations.
"""
import random

from base_system.port_model import PortModel

from mape.evaluation.average_wait import AverageWait


def main_step(ports, step, order, *args, **kwargs):
    """Main simulation step. Calls each ports :func:`step`.

    :param list ports:
        All ports in simulation
    :param int step:
        The iteration number.
    :param str order:
        If ``order == 'random```, shuffles ports in every step.
    """
    if order == 'random':
        random.shuffle(ports)

    for p in ports:
        p.step(step, *args, **kwargs)


def main_finish_step(ports, step, *args, **kwargs):
    """Callback to each port after main step has been executed (for logging, etc.).
    """
    for p in ports:
        p.finish_step(step, *args, **kwargs)


def create_ports(n_ports, *args, **kwargs):
    """Create ``n_ports`` with given args and kwargs.
    """
    ports = []
    for i in range(n_ports):
        port_name = "Port{:0>2}".format(i+1)
        ports.append(PortModel(name=port_name, **kwargs))
    return ports


def run(n_ports, steps, order, *args, **kwargs):
    """Main simulation creation and loop.
    """
    evaluation = kwargs.pop('evaluation', AverageWait())
    port_kwargs = kwargs.pop('port_kwargs', {})
    ports = create_ports(n_ports, **port_kwargs)

    for i in range(steps):
        main_step(ports, i, 'random')
        main_finish_step(ports, i)
        #evaluation.report(ports)

    for p in ports:
        print ('{}: {} minutes'.format(evaluation.evaluation_name, evaluation.evaluate(p)))
        print ('Ships still waiting: {}'.format(len(p.arriving)))
