#include "notes/asp/rhythm.lp".

% note(Bar,Beat,Start_Numerator,Start_Denominator,End_Numerator,End_Demonmiator,Pitch)
% Repesents a rhythm event taking place at an available grid point in the music

% TODO have note and rest atoms, or use note with pitch = 0 as a rest?

pitch(60;62;64;65;67;69;71;72).

4 { note_number(GridNumber);
    note_ticks_start(GridNumber,Start_Grid_Ticks);
    note_ticks_duration(GridNumber,Ticks_Duration);
    note_stress(GridNumber,Stress)
} 4 :-
    rhythm_number(GridNumber),
    rhythm_ticks_start(GridNumber,Start_Grid_Ticks),
    rhythm_ticks_duration(GridNumber,Ticks_Duration),
    rhythm_stress(GridNumber,Stress).

1 { note_pitch(GridNumber,Pitch) : pitch(Pitch) } 1 :- rhythm_number(GridNumber).

% No consecutive pitches
:- no_consecutive_pitches,
    note_number(First_GridNumber),
    note_number(Second_GridNumber),
    First_GridNumber + 1 == Second_GridNumber,
    note_pitch(First_GridNumber,Pitch),
    note_pitch(Second_GridNumber,Pitch).

% No intervals larger than perfect fifth
:- no_large_intervals,
    note_number(First_GridNumber),
    note_number(Second_GridNumber),
    First_GridNumber + 1 == Second_GridNumber,
    note_pitch(First_GridNumber,First_Pitch),
    note_pitch(Second_GridNumber,Second_Pitch),
    |First_Pitch - Second_Pitch| > 7.


#show note_number/1.
#show note_ticks_start/2.
#show note_ticks_duration/2.
#show note_stress/2.
#show note_pitch/2.
