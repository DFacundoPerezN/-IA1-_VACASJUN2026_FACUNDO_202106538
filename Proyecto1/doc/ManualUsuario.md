# Manual de Usuario

En este manual se desribira elfuncionamiento de las paginas html con la cual el usuario cliente y el usuaroio administrador podran interactauar para ejecutar las funciones del sistema.

## Dashboard principal

![imagen del dashboard principal](/Proyecto1/doc/img/dashboard_main.jpg)

En esta agina es que se desplieguan las opciones para los pacientes

### 1- Selección de sintomas

En la parte media a la izquierda se alcanza a ver una lista desplegada con todas los sintomas que están cargados en el sistema, esto para elegir los que se presentan en el equipo del cliente.
Por dar un ejemplo tenemos a:

* Instalar modulo bluetooth
* Instalar modulo wifi
* Analizar sistema con antivirus
...

### 2- Resultado

En esta parte de la zon aderecha de la pagina podemos observar los resultados que nos dan de diagnostico.
Se incluyen los apartados de:
**Falla detectada;** que es el nombre de la falla atribuida a los sintomas presentados.

**Recomendaciones;** la cual es una lista de recomnedacions a hacer para solventar la falla resultante del analisis con los sintomas.
Por dar un ejemplo tenemos a:

* Sin conexión red
* Wifi caído
* Bluetooth caido

### 3- Switch de envio de notificación

Ubicado en la parte media a la izquierda tenemos el label y switch para selecionar si se quiere que se notifique por medio del bot de telegram al chat.

### 4- histoial de diagnositcos

Finalemente en la parte de abajo tenemos el historial de diagnosticos realziados, el cual guarda información en el navegador. El historial guarda la fecha y hroa de cada consulta asi como los sintomas presentados y la falla conluida causante de esos sintomas.

Eso en un enlistamiento de los últimos diagnositcos realizados.

También se presenta un botón para limpiar el historial.

## Dashboard administrador

![imagen del dashboard administrador](/Proyecto1/doc/img/dashboard_admin.jpg)

En esta agina es que se desplieguan las opciones para el administrador.

### 1- Admin sintomas

En la parte arriba a la izquierda se alcanza a ver una lista desplegada con todas los sintomas que están cargados en el sistema; esta lista muestra opciones de editar y eliminar para cada uno de los sintomas. Arriba de la lista se esncuentra un espacio para cargar un nuevo sintoma.
Por dar un ejemplo tenemos a:

* Instalar modulo bluetooth
* Instalar modulo wifi
* Analizar sistema con antivirus
...

### 2- Admin Fallas

En la parte arriba a en medio se alcanza a ver una lista desplegada con todas las fallas que están cargadas en el sistema; esta lista muestra opciones de editar y eliminar para cada uno de llas fallas. Arriba de la lista se esncuentra un espacio para cargar una nueva falla.
Por dar un ejemplo tenemos a:

* Sin modulo bluetooth
* Sin modulo wifi
* Fuente de poder inestable
...

### 3- Admin Relación sintoma-falla

Ubicado en la parte arriba a la derecha tenemos el espacio para asignar una nueva relacion entre falla y sintoma, aqui se despliegan opciones de las barras y con esto elegimos al sintoma y a la falla.

### 4- Admin recomendaciones

En la parte media a en la izquierda se alcanza a ver una lista desplegada con todas las recomendaciones que están cargadas en el sistema; esta lista muestra opciones de editar y eliminar para cada uno de estas recomendaciones. Arriba de la lista se esncuentra un espacio para cargar una nueva recomendacion.
Por dar un ejemplo tenemos a:

* Instalar modulo bluetooth
* Instalar modulo wifi
* Cambiar pasta
...

### 5- Admin Relación falla-recomendacion

Ubicado en la parte arriba a la derecha tenemos el espacio para asignar una nueva conexión entre falla y recomendación, aqui se despliegan opciones de las barras y con esto elegimos a la falla y a la recomendación.

### 6- Admin Cambiar id del chat del bot

En la parte de abajo tenemos una barra donde esta el espacio para cambiar el id del bot, este funciona con un boton a la derecha el cual envia el cambio de id.
