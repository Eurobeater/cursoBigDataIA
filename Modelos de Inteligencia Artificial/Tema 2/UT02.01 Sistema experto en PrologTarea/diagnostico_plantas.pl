:- dynamic(hojas_amarillas/1).
:- dynamic(manchas_negras/1).
:- dynamic(hojas_caidas/1).
:- dynamic(tierra_humeda/1).
:- dynamic(plantas_dañadas/1).

diagnostico :-
    comprobar_hojas_amarillas,
    comprobar_manchas_negras,
    comprobar_hojas_caidas,
    comprobar_tierra_humeda,
    comprobar_plantas_dañadas,
    (hojas_amarillas(no), manchas_negras(no), hojas_caidas(no), tierra_humeda(no), plantas_dañadas(no) ->
        write('La planta parece estar en buen estado.'), nl
    ; 
        write('La planta tiene algunos problemas. Revisa los síntomas y actúa en consecuencia.'), nl
    ).

comprobar_hojas_amarillas :-
    hojas_amarillas(si), !,
    write('Las hojas están amarillas: La planta podría necesitar más nutrientes o estar sobreexpuesta al sol.'), nl.
comprobar_hojas_amarillas :-
    assertz(hojas_amarillas(no)),
    write('Las hojas no están amarillas.'), nl.

comprobar_manchas_negras :-
    manchas_negras(si), !,
    write('Manchas negras en las hojas: Podría ser un signo de hongos o infecciones.'), nl.
comprobar_manchas_negras :-
    assertz(manchas_negras(no)),
    write('No hay manchas negras en las hojas.'), nl.

comprobar_hojas_caidas :-
    hojas_caidas(si), !,
    write('Las hojas están cayendo: Podría ser una señal de falta de agua o estrés en la planta.'), nl.
comprobar_hojas_caidas :-
    assertz(hojas_caidas(no)),
    write('Las hojas no están cayendo.'), nl.

comprobar_tierra_humeda :-
    tierra_humeda(si), !,
    write('La tierra está húmeda: No riegues la planta por ahora.'), nl.
comprobar_tierra_humeda :-
    assertz(tierra_humeda(no)),
    write('La tierra está seca: La planta podría necesitar agua.'), nl.

comprobar_plantas_dañadas :-
    plantas_dañadas(si), !,
    write('Algunas partes de la planta están dañadas: Podría ser causado por plagas o condiciones extremas.'), nl.
comprobar_plantas_dañadas :-
    assertz(plantas_dañadas(no)),
    write('La planta no tiene daños visibles.'), nl.

preguntar :-
    write('¿Las hojas están amarillas? (si/no): '),
    read(Respuesta1),
    (Respuesta1 == si -> assertz(hojas_amarillas(si)); assertz(hojas_amarillas(no))),
    
    write('¿Hay manchas negras en las hojas? (si/no): '),
    read(Respuesta2),
    (Respuesta2 == si -> assertz(manchas_negras(si)); assertz(manchas_negras(no))),
    
    write('¿Las hojas están cayendo? (si/no): '),
    read(Respuesta3),
    (Respuesta3 == si -> assertz(hojas_caidas(si)); assertz(hojas_caidas(no))),
    
    write('¿La tierra está húmeda? (si/no): '),
    read(Respuesta4),
    (Respuesta4 == si -> assertz(tierra_humeda(si)); assertz(tierra_humeda(no))),
    
    write('¿La planta tiene partes dañadas? (si/no): '),
    read(Respuesta5),
    (Respuesta5 == si -> assertz(plantas_dañadas(si)); assertz(plantas_dañadas(no))),
    
    diagnostico.

?- preguntar.
