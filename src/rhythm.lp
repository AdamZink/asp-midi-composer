%#include "grid.lp".

% TODO trying to reduce ground program size by inlining relevant facts after solving grid.lp
end_ticks(960). grid(1,1,0,2). grid(1,2,0,2). grid(1,3,0,2). grid(1,4,0,2). grid(2,1,0,2). grid(2,2,0,2). grid(2,3,0,2). grid(2,4,0,2). grid(3,1,0,2). grid(3,2,0,2). grid(3,3,0,2). grid(3,4,0,2). grid(4,1,0,2). grid(4,2,0,2). grid(4,3,0,2). grid(4,4,0,2). grid(1,1,1,2). grid(1,2,1,2). grid(1,3,1,2). grid(1,4,1,2). grid(2,1,1,2). grid(2,2,1,2). grid(2,3,1,2). grid(2,4,1,2). grid(3,1,1,2). grid(3,2,1,2). grid(3,3,1,2). grid(3,4,1,2). grid(4,1,1,2). grid(4,2,1,2). grid(4,3,1,2). grid(4,4,1,2). grid_ticks(1,1,0,2,0). grid_ticks(1,2,0,2,60). grid_ticks(1,3,0,2,120). grid_ticks(1,4,0,2,180). grid_ticks(1,1,1,2,30). grid_ticks(1,2,1,2,90). grid_ticks(1,3,1,2,150). grid_ticks(1,4,1,2,210). grid_ticks(2,1,0,2,240). grid_ticks(2,2,0,2,300). grid_ticks(2,3,0,2,360). grid_ticks(2,4,0,2,420). grid_ticks(2,1,1,2,270). grid_ticks(2,2,1,2,330). grid_ticks(2,3,1,2,390). grid_ticks(2,4,1,2,450). grid_ticks(3,1,0,2,480). grid_ticks(3,2,0,2,540). grid_ticks(3,3,0,2,600). grid_ticks(3,4,0,2,660). grid_ticks(3,1,1,2,510). grid_ticks(3,2,1,2,570). grid_ticks(3,3,1,2,630). grid_ticks(3,4,1,2,690). grid_ticks(4,1,0,2,720). grid_ticks(4,2,0,2,780). grid_ticks(4,3,0,2,840). grid_ticks(4,4,0,2,900). grid_ticks(4,1,1,2,750). grid_ticks(4,2,1,2,810). grid_ticks(4,3,1,2,870). grid_ticks(4,4,1,2,930). grid_order(1,1,0,2,1). stress(1,3,"slightly stressed"). stress(2,3,"slightly stressed"). stress(3,3,"slightly stressed"). stress(4,3,"slightly stressed"). stress(1,1,"stressed"). stress(2,1,"stressed"). stress(3,1,"stressed"). stress(4,1,"stressed"). grid_order(1,2,0,2,3). grid_order(1,3,0,2,5). grid_order(1,4,0,2,7). grid_order(1,1,1,2,2). grid_order(1,2,1,2,4). grid_order(1,3,1,2,6). grid_order(1,4,1,2,8). grid_order(2,1,0,2,9). grid_order(2,2,0,2,11). grid_order(2,3,0,2,13). grid_order(2,4,0,2,15). grid_order(2,1,1,2,10). grid_order(2,2,1,2,12). grid_order(2,3,1,2,14). grid_order(2,4,1,2,16). grid_order(3,1,0,2,17). grid_order(3,2,0,2,19). grid_order(3,3,0,2,21). grid_order(3,4,0,2,23). grid_order(3,1,1,2,18). grid_order(3,2,1,2,20). grid_order(3,3,1,2,22). grid_order(3,4,1,2,24). grid_order(4,1,0,2,25). grid_order(4,2,0,2,27). grid_order(4,3,0,2,29). grid_order(4,4,0,2,31). grid_order(4,1,1,2,26). grid_order(4,2,1,2,28). grid_order(4,3,1,2,30). grid_order(4,4,1,2,32).
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
