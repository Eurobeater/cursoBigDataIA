% Sistema experto para diagnosticar por qué un ordenador no se enciende.

% Hechos iniciales (desconocidos)
:- dynamic(suministro_electrico/1).
:- dynamic(fuente_alimentacion/1).
:- dynamic(boton_power/1).
:- dynamic(cable_video/1).

% Reglas para diagnosticar el problema
diagnostico :-
    comprobar_suministro,
    comprobar_fuente,
    comprobar_boton,
    comprobar_cable,
    write('Todo parece estar en orden, el ordenador debería encender.'), nl.

diagnostico :-
    write('Revisa el diagnóstico de los componentes.'), nl.

% Reglas para comprobar cada componente
comprobar_suministro :-
    suministro_electrico(esta_bien), !,
    write('El suministro eléctrico está bien.'), nl.
comprobar_suministro :-
    write('Comprueba el suministro eléctrico, parece que está fallando.'), nl, fail.

comprobar_fuente :-
    fuente_alimentacion(esta_bien), !,
    write('La fuente de alimentación está funcionando correctamente.'), nl.
comprobar_fuente :-
    write('La fuente de alimentación podría estar fallando.'), nl, fail.

comprobar_boton :-
    boton_power(esta_bien), !,
    write('El botón de encendido está bien.'), nl.
comprobar_boton :-
    write('El botón de encendido no está funcionando correctamente.'), nl, fail.

comprobar_cable :-
    cable_video(esta_bien), !,
    write('El cable de vídeo está correctamente conectado.'), nl.
comprobar_cable :-
    write('El cable de vídeo no está conectado o está defectuoso.'), nl, fail.

% Preguntas interactivas para conocer el estado de cada componente
main :-
    write(''),nl,
    write('Sistema experto para evaluar el funcionamiento de un ordenador'), nl,
    write('--------------------------------------------------------------'), nl,
    preguntar_suministro,
    preguntar_fuente,
    preguntar_boton,
    preguntar_cable,
    diagnostico.

preguntar_suministro :-
    write('¿El suministro eléctrico está bien? (si/no): '),
    read(Respuesta),
    (Respuesta == si -> assertz(suministro_electrico(esta_bien));
     assertz(suministro_electrico(no_funciona))).

preguntar_fuente :-
    write('¿La fuente de alimentación está funcionando correctamente? (si/no): '),
    read(Respuesta),
    (Respuesta == si -> assertz(fuente_alimentacion(esta_bien));
     assertz(fuente_alimentacion(no_funciona))).

preguntar_boton :-
    write('¿El botón de encendido está funcionando? (si/no): '),
    read(Respuesta),
    (Respuesta == si -> assertz(boton_power(esta_bien));
     assertz(boton_power(no_funciona))).

preguntar_cable :-
    write('¿El cable de vídeo del monitor está conectado correctamente? (si/no): '),
    read(Respuesta),
    (Respuesta == si -> assertz(cable_video(esta_bien));
     assertz(cable_video(no_funciona))).
