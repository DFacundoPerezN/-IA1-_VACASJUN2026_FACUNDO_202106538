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
