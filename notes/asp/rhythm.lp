% rhythm(Bar,Beat,Start_Numerator,Start_Denominator,End_Numerator,End_Demonmiator,RhythmNumber)
% Repesents a rhythm event taking place at an available grid point in the music

max_grid_per_rhythm(2).

% TODO design rule(s) to use up 2 or more grid events when making a rhythm event
% Maybe assign rhythm_number first, then do the rest?

% TODO runtime noticeably increased - split into 3 steps? (grid, rhythm, and pitches?)

grid_number(GridNumber) :- grid_order(_,_,_,_,GridNumber).

grid_rhythm_size_option(G,1) :- grid_number(G).

grid_rhythm_size_option(G+1,S+1) :-
    grid_rhythm_size(G,_,S),
    max_grid_per_rhythm(M),
    S < M,
    grid_number(G+1).

1 { selected_grid_rhythm_size_option(G,S) : grid_rhythm_size_option(G,S) } 1 :-
    grid_number(G).

grid_rhythm_size(G,1,S) :-
    selected_grid_rhythm_size_option(G,S),
    G == 1.

grid_rhythm_size(G+1,R+1,S) :-
    grid_rhythm_size(G,R,_),
    selected_grid_rhythm_size_option(G+1,S),
    S == 1.

grid_rhythm_size(G+1,R,S) :-
    grid_rhythm_size(G,R,_),
    selected_grid_rhythm_size_option(G+1,S),
    S > 1.

grid_rhythm_lookup(G,R) :-
    grid_rhythm_size(G,R,_).

rhythm_number(RhythmNumber) :- grid_rhythm_lookup(_,RhythmNumber).


2 {
    rhythm_ticks_start(RhythmNumber,Start_Grid_Ticks);
    rhythm_ticks_duration(RhythmNumber,Ticks_Duration)
} 2 :-
    rhythm_number(RhythmNumber),
    grid_rhythm_size(Start_GridNumber,RhythmNumber,Start_S),
    Start_S == 1,
    grid_rhythm_size(End_GridNumber,RhythmNumber+1,End_S),
    End_S == 1,
    grid(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator),
    grid_order(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_GridNumber),
    grid_ticks(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_Grid_Ticks),
    grid(End_Bar,End_Beat,End_Numerator,End_Denominator),
    grid_order(End_Bar,End_Beat,End_Numerator,End_Denominator,End_GridNumber),
    grid_ticks(End_Bar,End_Beat,End_Numerator,End_Denominator,End_Grid_Ticks),
    Ticks_Duration = End_Grid_Ticks - Start_Grid_Ticks.

2 {
    rhythm_ticks_start(RhythmNumber,Start_Grid_Ticks);
    rhythm_ticks_duration(RhythmNumber,Ticks_Duration)
} 2 :-
    rhythm_number(RhythmNumber),
    grid_rhythm_size(Start_GridNumber,RhythmNumber,Start_S),
    Start_S == 1,
    grid(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator),
    grid_order(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_GridNumber),
    grid_ticks(Start_Bar,Start_Beat,Start_Numerator,Start_Denominator,Start_Grid_Ticks),
    not grid_rhythm_size(_,RhythmNumber+1,_),
    end_ticks(End_Ticks),
    Ticks_Duration = End_Ticks - Start_Grid_Ticks.

%#show rhythm_ticks_start/2.
%#show rhythm_ticks_duration/2.

2 {
    rhythm_order(Bar,Beat,Numerator,Denominator,RhythmNumber);
    rhythm_ticks(Bar,Beat,Numerator,Denominator,GridTicks)
} 2 :-
    grid_rhythm_size(GridNumber,RhythmNumber,Size),
    Size == 1,
    grid_order(Bar,Beat,Numerator,Denominator,GridNumber),
    grid_ticks(Bar,Beat,Numerator,Denominator,GridTicks).


% TODO choose a meter id

rhythm_stress(RhythmNumber,Stress) :-
    rhythm_number(RhythmNumber),
    rhythm_order(Bar,Beat,Numerator,_,RhythmNumber),
    Numerator == 0,
    stress(Bar,Beat,Stress).

rhythm_stress(RhythmNumber,"unstressed") :-
    rhythm_number(RhythmNumber),
    rhythm_order(Bar,Beat,Numerator,_,RhythmNumber),
    Numerator == 0,
    not stress(Bar,Beat,_).

rhythm_stress(RhythmNumber,"unstressed") :-
    rhythm_number(RhythmNumber),
    rhythm_order(Bar,Beat,Numerator,_,RhythmNumber),
    Numerator > 0.

%#show rhythm_stress/2.
