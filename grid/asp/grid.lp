#include "grid/asp/meter.lp".

% grid(Bar,Beat,Numerator,Denominator)
% Repesents a possible point in the music timeline to have a rhythm event

#const denominator = 2.

% E.g., numbered beats
use_numbered_beats_in_bar(Bar) :- use_numbered_beats, bar(Bar).

grid(Bar,Beat,0,denominator) :-
    use_numbered_beats_in_bar(Bar),
    bar(Bar),
    meter(Bar,BeatsPerBar),
    Beat=1..BeatsPerBar.

% E.g., "and" beats
use_and_beats_in_bar(Bar) :- use_and_beats, bar(Bar).

grid(Bar,Beat,1,denominator) :-
    use_and_beats_in_bar(Bar),
    bar(Bar),
    meter(Bar,BeatsPerBar),
    Beat=1..BeatsPerBar.

grid(Bar,Beat,Numerator,Denominator) :-
    use_grid(Bar,Beat,Numerator,Denominator),
    Bar != "*",
    Beat != "*",
    Numerator != "*",
    Denominator != "*".

Bars { grid(Bar,Beat,Numerator,Denominator) : Bar=1..Bars } Bars :-
    use_grid(WildcardBar,Beat,Numerator,Denominator),
    WildcardBar == "*",
    Beat != "*",
    Numerator != "*",
    Denominator != "*",
    bars(Bars).

BeatsPerBar { grid(Bar,Beat,Numerator,Denominator) : Beat=1..BeatsPerBar } BeatsPerBar :-
    use_grid(Bar,WildcardBeat,Numerator,Denominator),
    Bar != "*",
    WildcardBeat == "*",
    Numerator != "*",
    Denominator != "*",
    meter(Bar,BeatsPerBar).

% grid_ticks(Beat,Bar,Numerator,Denominator,Ticks)
% Calculated ticks for grid event
grid_ticks(Bar,Beat,Numerator,Denominator,Grid_Ticks) :-
    grid(Bar,Beat,Numerator,Denominator),
    bar_ticks(Bar,Bar_Ticks),
    ticks_per_beat(TicksPerBeat),
    Grid_Ticks = Bar_Ticks + (Beat-1)*TicksPerBeat + (Numerator*TicksPerBeat)/Denominator.

end_ticks(End_Ticks) :-
    bars(FinalBar),
    bar_ticks(FinalBar,Ticks),
    ticks_per_beat(TicksPerBeat),
    meter(FinalBar,BeatsPerBar),
    End_Ticks = Ticks + TicksPerBeat*BeatsPerBar.


grid_count(GridCount) :- GridCount = #count { Grid_Ticks : grid_ticks(_,_,_,_,Grid_Ticks) }.

sorted_ticks_candidate(Grid_Ticks,1) :- grid_ticks(_,_,_,_,Grid_Ticks).

grid_number(GridNumber) :- sorted_ticks_candidate(_,GridNumber).

1 { sorted_ticks(Grid_Ticks,GridNumber) :
    sorted_ticks_candidate(Grid_Ticks,GridNumber)
} 1 :-
    grid_number(GridNumber).

:- sorted_ticks(Grid_Ticks,GridNumber),
    sorted_ticks_candidate(Unsorted_Grid_Ticks,GridNumber),
    Unsorted_Grid_Ticks < Grid_Ticks.

sorted_ticks_candidate(Grid_Ticks,GridNumber+1) :-
    grid_number(GridNumber),
    sorted_ticks_candidate(Grid_Ticks,GridNumber),
    not sorted_ticks(Grid_Ticks,GridNumber),
    grid_count(GridCount),
    GridNumber < GridCount.

% grid_order(Beat,Bar,Numerator,Denominator,GridNumber)
% Represents numeric ordering of grid events (to be used by rhythm generator for ending numerator/denominator)
grid_order(Bar,Beat,Numerator,Denominator,GridNumber) :-
    grid_ticks(Bar,Beat,Numerator,Denominator,Grid_Ticks),
    sorted_ticks(Grid_Ticks,GridNumber).


#show ticks_per_beat/1.
#show grid/4.
#show grid_order/5.
#show grid_ticks/5.
#show end_ticks/1.
#show stress/3.
