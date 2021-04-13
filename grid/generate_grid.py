import clingo
from .atom_classes import *


def get_grid(config_json):
    prg = clingo.Control()
    prg.configuration.solve.models = 1
    # TODO figure out if relative imports work for python imports, clingo includes, and python open statements (like below)
    with open('grid/asp/grid.lp', 'r') as f:
        prg.add('base', [], f.read())
        prg.add('base', [], f'''
    bars({config_json['bars']}).
    
    bar_ticks(1,0).
    
    ticks_per_beat(60).
    
    meter_change(1,{config_json['beatsPerBar']}).
    
    use_numbered_beats.
    use_and_beats.
    ''')
    # TODO ^^^ add more of these facts to config_json (i.e., config_4_bars.json)

    prg.ground([('base', [])])

    atom_map = None
    with prg.solve(yield_=True) as handle:
        for model in handle:
            atom_map = get_atom_map(model.symbols(atoms=True))

    return atom_map
