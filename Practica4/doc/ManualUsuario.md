# Manual de Usuario

En este manual se desribira elfuncionamiento de la pagina html con la cual el usuario podra interactauar para ejecutar las funciones del sistema.

## Dashboard

![imagen del dashboard con matriz y botones](/Practica4/doc/Dashboard.png)

En una sola pagiona se despliegan todas la funciones de la pagina web.

### 1- Tamaño del laberinto

En la parte superior izquierda empezamos con el apartado de modificar el tamaño del laberinto, esto desde una matriz 4x4 a una 15x20, cuando se modifica el tramañao se borra todo lo que habia.

### 2- Matriz

La matriz representa el tablero donde se seleciona donde estará el inicio (S), el destino (G) y las celdas de obstaculos (muro) que se configuran.

El muro es opcional.

### 3- Modo de edición

En este apartado se selecciona por medio de botones el despliegue de los elementos de la matriz.

* inicio (S)
* el destino (G)
* celdas de obstaculos (muro)
* eliminar; para borrar las celdas ya dispuestas

### 4- Ejecutar algoritmo

Se elige el algoritmo de busqueda según las tres eleciones que hay:

* Breath First Search (BFS)
* Deep First Search (DBFS)
* A star (A*)

### 5- Resultados

Despues de ejecutar el algoritmo de busqueda sale el cuadro de resultados.

![imagen de resultados de la busqueda con algoritmo](/Practica4/doc/Resultados.png)
