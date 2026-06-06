# Endpoints del Backend

## 1. GET Para obtener todas las ciudades /ciudades/

response:

```json
[
  "berlin",
  "hamburgo",
  "munich",
  "colonia",
  "francfort_del_meno",
  "stuttgart",
  "dusseldorf",
  "dortmund",
  "leipzig",
  "essen",
  "bremen",
  "nuremberg"
]
```

## 2. POST Guardar ciudad /ciudades/

request:

````json
{
    "city": "spares"
}
```
response:

````json
{
  "success": true,
  "message": "La ciudad 'spares' fue agregada exitosamente.",
  "code": 201
}
```

## 3. POST Guardar ruta /ciudades/ruta

request:

````json
{
  "city1": "spares",
  "city2": "francfort_del_meno",
  "distance": 50
}
```
response:

````json
{
  "success": true,
  "message": "La ciudad 'spares' fue agregada exitosamente.",
  "code": 201
}
```
