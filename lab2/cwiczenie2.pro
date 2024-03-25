rodzic(jan,karol).
rodzic(karol,darek).
rodzic(amelia,ania).
rodzic(amelia,karol).
rodzic(jan,ania).
rodzic(mateusz,karol).
rodzic(mateusz,julia).
rodzic(ania,kacper).
rodzic(karol,goha).
rodzic(ania,emilia).

mezczyzna(jan).
mezczyzna(karol).
mezczyzna(mateusz).
mezczyzna(adrian).
mezczyzna(darek).
mezczyzna(kacper).

osoba(jan).
osoba(karol).
osoba(mateusz).
osoba(adrian).
osoba(darek).
osoba(kacper).
osoba(ania).
osoba(amelia).
osoba(julia).
osoba(goha).
osoba(emilia).




kobieta(X):-
    (
    	(osoba(X)),
        (\+ mezczyzna(X))
    ).

ojciec(X, Y):-
    (
    	(            
       	    (mezczyzna(X)),
            (osoba(Y)),
            (rodzic(Y, X)),
            (X \= Y)
        )
    ).

matka(X,Y):-
    (   
    	(   
        	(kobieta(X)),
            (osoba(Y)),
            (rodzic(Y,X)),
            ((X \= Y)) 
        )        	   
    ).

corka(X, Y):-
    (
    	(
            (osoba(Y)),
            (osoba(X)),
            (kobieta(X)),
            (rodzic(X, Y)),
        	(X \= Y)
        )
    ).

brat_rodzony(X, Y):-
    (
    	(
            (mezczyzna(X)),
            (ojciec(A, X)),
            (matka(B, X))
        ),
        (
            (osoba(Y)),
            (ojciec(A, Y)),
            (matka(B, Y))
        ),
        (
	    	(A \= X),
            (A \= Y),
            (A \= B),
            (B \= X),
            (B \= Y),
            (X \= Y)
        )
    ).

brat_przyrodni(X, Y):-
    (
    	(
    	    (mezczyzna(X)),
            (rodzic(X, A)),
            (rodzic(X, B)),
            (\+ brat_rodzony(X, Y))
    	),
        (
            (osoba(Y)),
            (rodzic(Y, A)),
            (rodzic(Y, C))
        ),
    	(
            (A \= X),
            (A \= Y),
            (A \= B),
            (A \= C),
            (B \= X),
            (B \= Y),
            (B \= C),
            (C \= X),
            (C \= Y),
            (X \= Y)
        )
    ).

dziadek_od_strony_ojca(X, Y):-
    (
    	(
            (ojciec(A, Y)),
            (rodzic(A, X)),
            (A \= X),
            (A \= Y),
            (X \= Y)
        )
    ).

dziadek_od_strony_matki(X,Y):-
    (
    	(
            (matka(A, Y)),
            (rodzic(A, X)),
            (A \= X),
            (A \= Y),
            (X \= Y)
        )
    ).

dziadek(X, Y):-
    (
    	(
            (mezczyzna(X)),
            (rodzic(A, X)),
            (rodzic(Y, A)),
            (A \= X),
            (A \= Y),
            (X \= Y)
        )
    ).
babcia(X, Y):-
    (
    	(
            (kobieta(X)),
            (rodzic(A, X)),
            (rodzic(Y, A)),
            (A \= X),
            (A \= Y),
            (X \= Y)
        )
    ).

wnuczka(X,Y):-
     (
    	(
            (kobieta(Y)),
            (X \= Y)
        ),
        (   
        	(dziadek(X,Y)); 
        	(babcia(X,Y)) 
        )
    ).



