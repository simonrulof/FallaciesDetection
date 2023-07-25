%%%%%%%%%%%%%%%%%%%%%%%%%
%% Some usage examples %%
%%%%%%%%%%%%%%%%%%%%%%%%%

%% extract_schema([s2, a, [s1, [s5, h], [s6, u]], [s3, [s4, g]]], L).
%% is_plausible(rain, L).
%% prove(wet, L).
%% plausible([wet, not(wet)], L), get_fallacies(L, LL).
%% plausibly_sound(arg7, L).
%% sound(arg7, L).
%% is_plausible(humidity, L).
%% prove(humidity, L).


%%%%%%%%
%% KB %%
%%%%%%%%

%% %% % Facts
%% fact(cause(rain, wet)).
%% fact(cause(wet, humidity)).
%% fact(expert(drWho)).
%% fact(expert(alf)).
%% fact(expert(hal)).
%% fact(claim(drWho, sunny)).
%% fact(claim(alf, rain)).
%% fact(claim(hal, not(wet))).
%% fact(expert(groucho)).
%% 				fact(claim(groucho,sunny)).

%% %% % Schemas (and fallacies)
%% schema(s1, [expert(X), claim(X, Y)], Y).
%% schema(s2, [X, cause(X, Y)], Y).

%% %% % List of fallacies
%% %% (for demonstration purposes only...)
%% fallacy(s1).
%% fallacy(s2).

%% % Arguments
%% A valid and sound argument
%% argument(arg1, [expert(drWho), claim(drWho, sunny)], sunny).
%% %% Another valid and sound argument (because sunny and rain are not contradictory)
%% argument(arg2, [expert(alf), claim(alf, rain)], rain).
%% %% Another valid and sound argument that uses arg1 as "premise"
%% argument(arg3, [rain, cause(rain, wet)], wet).
%% %% A valid but not (plausibly) sound argument (expert(groucho) is not a fact not supported by an arg)
%% argument(arg4, [expert(groucho), claim(groucho, sunny)], sunny).
%% %% An invalid (and thus unsound) argument (it does not respect any schema of the base)
%% argument(arg5, [claim(drWho, sunny)], sunny).
%% %% A sound argument (that is sound even is its conclusion contradict arg3s conclusion)
%% argument(arg6, [expert(hal), claim(hal, not(wet))], not(wet)).
%% %% A plausibly sound but not strictly sound argument (it uses a formula, "wet" (arg3), that is not proven (because of arg6))
%% argument(arg7, [wet, cause(wet, humidity)], humidity).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Proofs and (argumentative) inferences %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Plausible (plausibly inferred)
is_plausible(X, L) :- plausible([X], L).

plausible([fail], []) :- fail.
%% plausible([not(not(X))], L) :- plausible([X], L).
plausible([], []).
plausible([H|T], [fact(H)|TS]) :-
    fact(H),
    plausible(T, TS).
plausible([H|T], [LS|TS]) :-
    argument(Arg, _, H),
    plausibly_sound(Arg, LS),
    plausible(T, TS).

valid(Arg, S) :-
    argument(Arg, PremsA, ConcA),
    schema(S, PremsS, ConcS),
    permutation(PremsS, PremsA),
    permutation([ConcS], [ConcA]).

valid_no_fallacy(Arg, S) :-
    argument(Arg, PremsA, ConcA),
    schema(S, PremsS, ConcS),
    \+ fallacy(S),
    permutation(PremsS, PremsA),
    permutation([ConcS], [ConcA]).

valid_fallacy(Arg, S) :-
    argument(Arg, PremsA, ConcA),
    schema(S, PremsS, ConcS),
    fallacy(S),
    permutation(PremsS, PremsA),
    permutation([ConcS], [ConcA]).

plausibly_sound(Arg, R) :-
    argument(Arg, Prems, _),
    valid(Arg, S),
    plausible(Prems, LS),
    append([S], LS, R).

%% Proven (certainly inferred)
prove(X, L) :- proven([X], L).

proven([fail], []) :- fail.
%% proven([not(not(X))], L) :- proven([X], L).
proven([], []).
proven([H|T], [fact(H)|TS]) :-
    \+ plausible([not(H)], _),
    fact(H),
    proven(T, TS).
proven([H|T], [LS|TS]) :-
    \+ plausible([not(H)], _),
    argument(Arg, _, H),
    sound(Arg, LS),
    proven(T, TS).

sound(Arg, R) :-
    argument(Arg, Prems, _),
    valid(Arg, S),
    proven(Prems, LS),
    append([S], LS, R).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Detection of schemas and fallacies %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fallacious(X, F) :- prove(X, L), get_fallacies(L, F).

get_fallacies(L, F) :- extract_schemas(L, LL), findall(S, (fallacy(S), member(S, LL)), F).

extract_schemas([],[]).
extract_schemas([H|T], R) :- extract_schema(H, R1), extract_schemas(T, R2), append(R1, R2, R).

extract_schema(S, []) :- \+ is_list(S).
extract_schema([S|T], [S|T2]) :- extract_schemas(T, T2).
