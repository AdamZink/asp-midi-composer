% ticks_per_beat/1.
def_predicate("ticks_per_beat", "arity", 1).
def_predicate("ticks_per_beat", "description", "Number of ticks per beat").

def_term("ticks_per_beat", 1, "name", "TicksPerBeat").
def_term("ticks_per_beat", 1, "type", "Number").
def_term("ticks_per_beat", 1, "min", 1).
def_term("ticks_per_beat", 1, "notes", "Higher value allows for more granularity of note positions").


% stress/3.
def_predicate("stress", "arity", 3).
def_predicate("stress", "description", "Stress on a possible grid event with numerator of 0").

def_term("stress", 1, "name", "Bar").
def_term("stress", 1, "type", "Number").
def_term("stress", 2, "name", "Beat").
def_term("stress", 2, "type", "Number").
def_term("stress", 3, "name", "Stress").
def_term("stress", 3, "type", "String").


% grid/4.
def_predicate("grid", "arity", 4).
def_predicate("grid", "description", "Position of a possible note").

def_term("grid", 1, "name", "Bar").
def_term("grid", 1, "type", "Number").
def_term("grid", 2, "name", "Beat").
def_term("grid", 2, "type", "Number").
def_term("grid", 3, "name", "Numerator").
def_term("grid", 3, "type", "Number").
def_term("grid", 4, "name", "Denominator").
def_term("grid", 4, "type", "Number").


% grid_ticks/5.
def_predicate("grid_ticks", "arity", 5).
def_predicate("grid_ticks", "description", "Number of ticks at the start of the grid event").

def_term("grid_ticks", 1, "name", "Bar").
def_term("grid_ticks", 1, "type", "Number").
def_term("grid_ticks", 2, "name", "Beat").
def_term("grid_ticks", 2, "type", "Number").
def_term("grid_ticks", 3, "name", "Numerator").
def_term("grid_ticks", 3, "type", "Number").
def_term("grid_ticks", 4, "name", "Denominator").
def_term("grid_ticks", 4, "type", "Number").
def_term("grid_ticks", 5, "name", "GridTicks").
def_term("grid_ticks", 5, "type", "Number").


% end_ticks/1.
def_predicate("end_ticks", "arity", 1).
def_predicate("end_ticks", "description", "Total number of ticks containing all grid events").

def_term("end_ticks", 1, "name", "EndTicks").
def_term("end_ticks", 1, "type", "Number").


% grid_order/5.
def_predicate("grid_order", "arity", 5).
def_predicate("grid_order", "description", "Order of the grid event").

def_term("grid_order", 1, "name", "Bar").
def_term("grid_order", 1, "type", "Number").
def_term("grid_order", 2, "name", "Beat").
def_term("grid_order", 2, "type", "Number").
def_term("grid_order", 3, "name", "Numerator").
def_term("grid_order", 3, "type", "Number").
def_term("grid_order", 4, "name", "Denominator").
def_term("grid_order", 4, "type", "Number").
def_term("grid_order", 5, "name", "GridNumber").
def_term("grid_order", 5, "type", "Number").
