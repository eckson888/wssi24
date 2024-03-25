lubi(jan,pawel).
lubi(pawel,krzysztof).
lubi(pawel,jan).
lubi(jan,bartek).
lubi(bartek,jan).
lubi(adrian,darek).
lubi(darek,adrian).

kobieta(jan).
kobieta(darek).
mezczyzna(adrian).
mezczyzna(pawel).

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
    (    	
        \+ (
               	(lubi(X, Z)),
                (Z \= Y)
           )
   	).    

truelove(X,Y):-
    loves(X,Y),
    (   mezczyzna(X),kobieta(Y);
      	kobieta(X), mezczyzna(Y)).
