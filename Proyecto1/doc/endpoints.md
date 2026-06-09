# Endpoints del Backend

## 1. GET Para obtener todos los sintomas

/doctor/sintomas

response:

```json
[
  "pantalla_negra",
  "reinicio_inesperado",
  //...
  "desconexion_usb_constante"
]
```

## 2. POST Obtener falla

/doctor/obtener_falla

request:

```json
{
    "sintomas": ["pantalla_azul" , "reinicio_inesperado", "problema_arranque", "lentitud_del_sistema"
      ]
}
```

response:

```json
{
  "code": 201,
  "falla": "memoria_ram_defectuosa"
}
```

## 3. GET Para obtener recomendaciones según falla

/doctor/recomendaciones?fail=sobrecalentamiento_procesador

response:

```json
{
  "code": 201,
  "cities": [
    "limpiar_ventiladores",
    "cambiar_pasta"
  ]
}
```

## 4. POST Obtener recomendaciones segun sintoma

/doctor/recomendaciones

request:

```json
{
    "sintomas": ["pantalla_azul" , "reinicio_inesperado", "problema_arranque", "lentitud_del_sistema"
      ]
}
```

response:

```json
{
  "code": 201,
  "recommendations": [
    "ejecutar_diagnostico_ram",
    "limpiar_contactos"
  ]
}
```
