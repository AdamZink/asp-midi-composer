% Stress patterns
% S = stressed
% s = slightly stressed
% u = unstressed

% {meter_stressed|meter_slightly_stressed}(BeatsPerBar,MeterId,Beat)

% TODO these are the starting rules, but can be broken (e.g., syncopation). Use cascading constraints to override default stress pattern)

% 2 beats per bar = S, u
meter_stressed(2,1,1).

% 3 beats per bar = S, u, u
meter_stressed(3,1,1).

% 4 beats per bar = S, u, s, u
meter_stressed(4,1,1).
meter_slightly_stressed(4,1,3).

% 5 beats per bar = S, u, s, u, u, or
% 5 beats per bar = S, u, u, s, u
meter_stressed(5,1,1).
meter_stressed(5,1,3).
%meter_stressed(5,2,1).
%meter_stressed(5,2,4).


% Do not allow slightly stressed beat without stressed beat
:- meter_slightly_stressed(BeatsPerBar,MeterId,_),
    not meter_stressed(BeatsPerBar,MeterId,_).


% {stressed|slightly_stressed}(Bar,Beat)
1 { bar_stress_pattern(Bar,StressPatternId) : meter_stressed(BeatsPerBar,StressPatternId,_) } 1 :- meter(Bar,BeatsPerBar).

stress(Bar,Beat,"stressed") :-
    meter(Bar,BeatsPerBar),
    bar_stress_pattern(Bar,StressPatternId),
    meter_stressed(BeatsPerBar,StressPatternId,Beat).

stress(Bar,Beat,"slightly stressed") :-
    meter(Bar,BeatsPerBar),
    bar_stress_pattern(Bar,StressPatternId),
    meter_slightly_stressed(BeatsPerBar,StressPatternId,Beat).


bar(Bar) :- bars(Bars), Bar=1..Bars.

meter(Bar,BeatsPerBar) :-
    bar(Bar),
    meter_change(Bar,BeatsPerBar).

meter(Bar+1,BeatsPerBar) :-
    bar(Bar),
    bar(Bar+1),
    meter(Bar,BeatsPerBar),
    not meter_change(Bar+1,_).

bar_ticks(Bar+1,PriorTicks+TicksPerBeat*BeatsPerBar) :-
    bar(Bar),
    bar(Bar+1),
    bar_ticks(Bar,PriorTicks),
    ticks_per_beat(TicksPerBeat),
    meter(Bar,BeatsPerBar).
