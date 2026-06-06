% Hechos
% datos ciudades

ciudad(berlin).
ciudad(hamburgo).
ciudad(munich).
ciudad(colonia).
ciudad(francfort_del_meno).
ciudad(stuttgart).
ciudad(dusseldorf).
ciudad(dortmund).
ciudad(leipzig).
ciudad(essen).
ciudad(bremen).
ciudad(nuremberg).

% datos conexiones entre ciudades

ruta(berlin, hamburgo, 289).
ruta(hamburgo, bremen, 125).
ruta(berlin, leipzig, 194).
ruta(leipzig, nuremberg, 292).
ruta(nuremberg, munich, 169).
ruta(munich, stuttgart, 231).
ruta(stuttgart, francfort_del_meno, 203).
ruta(francfort_del_meno, colonia, 172).
ruta(colonia, dusseldorf, 40).
ruta(dortmund, colonia, 94).
ruta(essen, dusseldorf, 37).
ruta(essen, dortmund, 36).
ruta(dortmund, bremen, 235).

% reglas

distancia(Ciudad1, Ciudad2, Distancia):- ruta(Ciudad1, Ciudad2, Distancia).
distancia(Ciudad1, Ciudad2, Distancia):- ruta(Ciudad2, Ciudad1, Distancia).

get_ciudades(Lista):- findall(Ciudad, ciudad(Ciudad), Lista).

% regla para encontrar una ruta directa entre dos ciudades

recorrido/4.

% Inicializa la lista de Visitadas con la ciudad de Origen.
recorrido(Origen, Destino, ListaCiudades, Distancia) :-
    recorrido_aux(Origen, Destino, [Origen], ListaCiudades, Distancia).

% Base: Una ruta directa entre el Origen y el Destino.
recorrido_aux(Origen, Destino, Visitadas, ListaCiudades, Distancia) :-
    distancia(Origen, Destino, Distancia),

    % Construr lista final append al destino
    append(Visitadas, [Destino], ListaCiudades)
    % ,write('Ruta encontrada: '), write(ListaCiudades), write(' con distancia: '), write(Distancia), nl
    .

% Recursion: No hay ruta directa, buscamos una ciudad intermedia (Siguiente).
recorrido_aux(Origen, Destino, Visitadas, ListaCiudades, Distancia) :-
    distancia(Origen, Siguiente, D1),

    % Evitamos ciclos al confirmar que Siguiente no haya sido visitada antes
    \+ member(Siguiente, Visitadas),
    % Evitamos pasar dos veces por el Destino
    \+ member(Destino, Visitadas),

    % Añadimos la ciudad intermedia a los Visitadas
    append(Visitadas, [Siguiente], NuevosVisitadas),

    % Buscamos el resto del camino desde 'Siguiente' hasta el 'Destino'
    recorrido_aux(Siguiente, Destino, NuevosVisitadas, ListaCiudades, D2),
    % Sumar distancias
    Distancia is D1 + D2.

% recorrido(essen, dortmund, ListaCiudades, Distancia)

% consult('citys.pl')