%:- consult('fallacies.pl').
:- consult('fallacies_diff_version.pl').

%% # %% %% % Schemas (and fallacies)
schema(modusponens, [X, implies(X,Y) | H], Y).
%% # schema(notmodusponens, [X, implies(X,Y)], Y).
schema(hilbertK, [], implies(X,implies(Y,X))).
schema(hilbertS, [], implies(implies(X,implies(Y,Z)),implies(implies(X,Y),implies(X,Z)))).
schema(hilbertnot,[],implies(not(not(X)),X)).
schema(hilbertnot2,[],implies(X,not(not(X)))).
schema(contrap,[], implies(implies(not(Y),not(X)),implies(X,Y))).
schema(contrap2,[], implies(implies(Y,X),implies(not(X),not(Y)))).


schema(badImplication,[implies(A, B), B | H], A).

%% # %% %% % List of fallacies
	
%% # schema(notTest, [X, implies(Y, X)], Y).
%% # schema(test, [X, implies(Y, X)], Y).

fallacy(test).

%% # %% % Arguments
%% # argument(arg0, [], implies(a,not(not(a)))).
%% # argument(arg0b, [a,implies(a,not(not(a)))], not(not(a))).
%% # argument(arg1, [], implies(a,implies(b,a))).
%% # argument(arg2, [a, implies(a,implies(b,a))], implies(b,a)).
%% # argument(arg3, [], implies(implies(b,a), implies(not(a),not(b)))).
%% # argument(arg4, [implies(b,a), implies(implies(b,a), implies(not(a),not(b)))], implies(not(a), not(b))).
%% # argument(arg5, [], implies(not(not(a)),implies(not(b),not(not(a))))).
%% # argument(arg6, [not(not(a)), implies(not(not(a)), implies(not(b),not(not(a))))], implies(not(b),not(not(a)))).
%% # argument(arg7, [], implies(implies(not(b),not(not(a))), implies(not(a),b))).
%% # argument(arg8, [implies(not(b),not(not(a))), implies(implies(not(b),not(not(a))), implies(not(a),b))], implies(not(a),b)).
%% # argument(arg9, [not(a), implies(not(a),b)], b).


%% # fact(a).l
%% # fact(not(a)).


%%     # schema(modusponens, [X, implies(X,Y)], Y).
%%     # schema(hilbertK, [], implies(X,implies(Y,X))).
%%     # schema(hilbertS, [], implies(implies(X,implies(Y,Z)),implies(implies(X,Y),implies(X,Z)))).
%%     # schema(hilbertnot, [], implies(implies(not(Y),not(X)),implies(implies(not(Y),X),Y))).

%% # fact(implies(rain,take(umbrella))).
%% # fact(rain).
%% # fact(conc).
%% # fact(implies(pre, conc)).

%% # argument(arg1, [rain,implies(rain,take(umbrella))], take(umbrella)).

%% # argument(arg2, [conc, implies(pre, conc)], pre).
fact([A, B, C, D]) :-
	fact(A),
	fact(B),
	fact(C),
	fact(D).
	
fact([A]) :-
	fact(A).
	
	
	
%%# fact(object(a,card,countable,na,eq,1)).	

%%# fact(object(b,bear,countable,na,eq,1)).

%%# fact(property(c,thrown,pos)).

%%# fact(predicate(d,be,a,c)).

%%# fact(implies([property(c,thrown,pos), predicate(d,be,a,c)], predicate(g,die,b))).

%%#fact(object(a,ground,countable,na,eq,1)).
%%#fact(object(b,weather,countable,na,eq,1)).
%%#fact(property(c,wet,pos)).
%%#fact(predicate(d,be,a,c)).
%%#fact(implies(predicate(e,rain,b),predicate(d,be,a,c))).

%%#argument(jenaimarre, [object(a,ground,countable,na,eq,1), object(b,weather,countable,na,eq,1), property(c,wet,pos), predicate(d,be,a,c), implies(predicate(e,rain,b),predicate(d,be,a,c))], predicate(e,rain,b)).



