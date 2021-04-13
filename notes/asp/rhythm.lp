%#include "grid.lp".

% rhythm(Bar,Beat,Start_Numerator,Start_Denominator,End_Numerator,End_Demonmiator,RhythmNumber)
% Repesents a rhythm event taking place at an available grid point in the music

3 { rhythm_number(Start_GridNumber);
    rhythm_ticks_start(Start_GridNumber,Start_Grid_Ticks);
    rhythm_ticks_duration(Start_GridNumber,Ticks_Duration)
} 3 :-
    grid(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator),
    grid_order(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_GridNumber),
    grid_ticks(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_Grid_Ticks),
    grid(End_Bar,End_Beat,End_Numerator,End_Denominator),
    grid_order(End_Bar,End_Beat,End_Numerator,End_Denominator,End_GridNumber),
    grid_ticks(End_Bar,End_Beat,End_Numerator,End_Denominator,End_Grid_Ticks),
    Start_GridNumber + 1 == End_GridNumber,
    Ticks_Duration = End_Grid_Ticks - Start_Grid_Ticks.

3 { rhythm_number(Start_GridNumber);
    rhythm_ticks_start(Start_GridNumber,Start_Grid_Ticks);
    rhythm_ticks_duration(Start_GridNumber,Ticks_Duration)
} 3 :-
    grid(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator),
    grid_order(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_GridNumber),
    grid_ticks(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_Grid_Ticks),
%    grid_order(Other_Bar,Other_Beat,Other_Numerator,Other_Denominator,Other_GridNumber),
    not grid_order(_,_,_,_,Start_GridNumber+1),
    end_ticks(End_Ticks),
    Ticks_Duration = End_Ticks - Start_Grid_Ticks.

%#show rhythm_ticks_start/2.
%#show rhythm_ticks_duration/2.


% TODO choose a meter id

rhythm_stress(GridNumber,Stress) :-
    rhythm_number(GridNumber),
    grid_order(Bar,Beat,Numerator,_,GridNumber),
    Numerator == 0,
    stress(Bar,Beat,Stress).

rhythm_stress(GridNumber,"unstressed") :-
    grid_order(Bar,Beat,Numerator,_,GridNumber),
    Numerator == 0,
    not stress(Bar,Beat,_).

rhythm_stress(GridNumber,"unstressed") :-
    grid_order(Bar,Beat,Numerator,_,GridNumber),
    Numerator > 0.

%#show rhythm_stress/2.
