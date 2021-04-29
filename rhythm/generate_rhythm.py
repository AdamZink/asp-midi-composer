import clingo
import random
from .atom_classes import *


def get_rhythm(config_json, grid_facts_list):
    prg = clingo.Control()
    prg.configuration.solve.models = 1
    prg.configuration.solver.rand_freq = random.random()
    prg.configuration.solver.seed = int(random.random() * 4294967295)
    print(f'Rand_freq: {prg.configuration.solver.rand_freq}')
    print(f'Seed: {prg.configuration.solver.seed}')

    # TODO figure out if relative imports work for python imports, clingo includes, and python open statements (like below)
    with open('rhythm/asp/rhythm.lp', 'r') as f:
        prg.add('base', [], f.read())
        prg.add('base', [], '\n'.join(grid_facts_list))
        prg.add('base', [], f'''
    max_grid_per_rhythm({config_json['rhythm']['max_grid_per_rhythm']}).
    ''')

    prg.ground([('base', [])])

    atom_map = None
    with prg.solve(yield_=True) as handle:
        for model in handle:
            atom_map = get_atom_map(model.symbols(atoms=True))

    return atom_map
