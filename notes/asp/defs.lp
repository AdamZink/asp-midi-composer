% bars(4).
def_predicate("bars", "arity", 1).
def_predicate("bars", "description", "Number of bars in the phrase").

def_term("bars", 1, "name", "Bars").
def_term("bars", 1, "type", "Number").
def_term("bars", 1, "min", 1).


% ticks_per_beat(60).
def_predicate("ticks_per_beat", "arity", 1).
def_predicate("ticks_per_beat", "description", "Number of ticks per beat").

def_term("ticks_per_beat", 1, "name", "TicksPerBeat").
def_term("ticks_per_beat", 1, "type", "Number").
def_term("ticks_per_beat", 1, "min", 1).
def_term("ticks_per_beat", 1, "notes", "Higher value allows for more granularity of note positions").


% min_pitch(48).
def_predicate("min_pitch", "arity", 1).
def_predicate("min_pitch", "description", "Lowest pitch to allow in the phrase").

def_term("min_pitch", 1, "name", "MinPitch").
def_term("min_pitch", 1, "type", "Number").
def_term("min_pitch", 1, "min", 1).
def_term("min_pitch", 1, "max", 120).


% key_root_pitch(60).
def_predicate("key_root_pitch", "arity", 1).
def_predicate("key_root_pitch", "description", "Pitch representing the root of the phrase's key").

def_term("key_root_pitch", 1, "name", "KeyRootPitch").
def_term("key_root_pitch", 1, "type", "Number").
def_term("key_root_pitch", 1, "min", 1).
def_term("key_root_pitch", 1, "max", 120).


% max_pitch(67).
def_predicate("max_pitch", "arity", 1).
def_predicate("max_pitch", "description", "Highest pitch to allow in the phrase").

def_term("max_pitch", 1, "name", "MaxPitch").
def_term("max_pitch", 1, "type", "Number").
def_term("max_pitch", 1, "min", 1).
def_term("max_pitch", 1, "max", 120).


% note_number(GridNumber)
def_predicate("note_number", "arity", 1).
def_predicate("note_number", "description", "Note index referenced in other atoms").

def_term("note_number", 1, "name", "GridNumber").
def_term("note_number", 1, "type", "Number").


% note_ticks_start(GridNumber,Start_Grid_Ticks)
def_predicate("note_ticks_start", "arity", 2).
def_predicate("note_ticks_start", "description", "Number of ticks at the start of the note").

def_term("note_ticks_start", 1, "name", "GridNumber").
def_term("note_ticks_start", 1, "type", "Number").
def_term("note_ticks_start", 2, "name", "Start_Grid_Ticks").
def_term("note_ticks_start", 2, "type", "Number").


% note_ticks_duration(GridNumber,Ticks_Duration)
def_predicate("note_ticks_duration", "arity", 2).
def_predicate("note_ticks_duration", "description", "The note's duration in ticks").

def_term("note_ticks_duration", 1, "name", "GridNumber").
def_term("note_ticks_duration", 1, "type", "Number").
def_term("note_ticks_duration", 2, "name", "Ticks_Duration").
def_term("note_ticks_duration", 2, "type", "Number").


% note_stress(GridNumber,Stress)
def_predicate("note_stress", "arity", 2).
def_predicate("note_stress", "description", "The level of stress to apply to the note").

def_term("note_stress", 1, "name", "GridNumber").
def_term("note_stress", 1, "type", "Number").
def_term("note_stress", 2, "name", "Stress").
def_term("note_stress", 2, "type", "String").


% note_pitch(GridNumber,Pitch)
def_predicate("note_pitch", "arity", 2).
def_predicate("note_pitch", "description", "The level of stress to apply to the note").

def_term("note_pitch", 1, "name", "GridNumber").
def_term("note_pitch", 1, "type", "Number").
def_term("note_pitch", 2, "name", "Pitch").
def_term("note_pitch", 2, "type", "Number").
