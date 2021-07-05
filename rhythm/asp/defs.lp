% rhythm_number(RhythmNumber)
def_predicate("rhythm_number", "arity", 1).
def_predicate("rhythm_number", "description", "Rhythm index referenced in other atoms").

def_term("rhythm_number", 1, "name", "RhythmNumber").
def_term("rhythm_number", 1, "type", "Number").


% rhythm_ticks_start(RhythmNumber,Start_Rhythm_Ticks)
def_predicate("rhythm_ticks_start", "arity", 2).
def_predicate("rhythm_ticks_start", "description", "Number of ticks at the start of the rhythm event").

def_term("rhythm_ticks_start", 1, "name", "RhythmNumber").
def_term("rhythm_ticks_start", 1, "type", "Number").
def_term("rhythm_ticks_start", 2, "name", "Start_Rhythm_Ticks").
def_term("rhythm_ticks_start", 2, "type", "Number").


% rhythm_ticks_duration(RhythmNumber,Ticks_Duration)
def_predicate("rhythm_ticks_duration", "arity", 2).
def_predicate("rhythm_ticks_duration", "description", "The rhythm event's duration in ticks").

def_term("rhythm_ticks_duration", 1, "name", "RhythmNumber").
def_term("rhythm_ticks_duration", 1, "type", "Number").
def_term("rhythm_ticks_duration", 2, "name", "Ticks_Duration").
def_term("rhythm_ticks_duration", 2, "type", "Number").


% rhythm_stress(RhythmNumber,Stress)
def_predicate("rhythm_stress", "arity", 2).
def_predicate("rhythm_stress", "description", "The level of stress to apply to the rhythm event").

def_term("rhythm_stress", 1, "name", "RhythmNumber").
def_term("rhythm_stress", 1, "type", "Number").
def_term("rhythm_stress", 2, "name", "Stress").
def_term("rhythm_stress", 2, "type", "String").
