import clingo
import random
from .atom_classes import *


def get_notes(config_json, grid_facts_list):
    prg = clingo.Control()
    prg.configuration.solve.models = 1
    prg.configuration.solver.rand_freq = random.random()
    prg.configuration.solver.seed = int(random.random() * 4294967295)
    print(f'Rand_freq: {prg.configuration.solver.rand_freq}')
    print(f'Seed: {prg.configuration.solver.seed}')
    # TODO figure out if relative imports work for python imports, clingo includes, and python open statements (like below)
    with open('notes/asp/notes.lp', 'r') as f:
        prg.add('base', [], f.read())
        prg.add('base', [], '\n'.join(grid_facts_list))
        prg.add('base', [], f'''
    no_consecutive_pitches.
    no_large_intervals.
    ''')
    # TODO ^^^ add more of these facts to config_json (i.e., config_4_bars.json)

    prg.ground([('base', [])])

    class_map = None
    with prg.solve(yield_=True) as handle:
        for model in handle:
            class_map = get_class_map(model.symbols(atoms=True))

    return class_map
