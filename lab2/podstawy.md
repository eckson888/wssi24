lubi(jan,pawel).
lubi(pawel,krzysztof).
lubi(pawel,jan).
lubi(jan,bartek).
lubi(bartek,jan).
lubi(adrian,darek).
lubi(darek,adrian).

kobieta(darek).
mezczyzna(adrian).

przyjazn(X,Y) :-
    lubi(X,Y),
    lubi(Y,X).

niby_przyjazn(X,Y) :-
    lubi(X,Y);
    lubi(Y,X).

nieprzyjazn(X,Y) :-
    \+lubi(X,Y),
    \+lubi(Y,X).

loves(X,Y) :-
    przyjazn(X,Y),
    (\+lubi(X,_\=Y),
    \+lubi(Y,_\=X)).
    

truelove(X,Y):-
    loves(X,Y),
    (   mezczyzna(X),kobieta(Y);
      	kobieta(X), mezczyzna(Y)).
