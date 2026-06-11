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

## 5. POST Crear sintoma

/doctor/sintoma

request:

```json
{
    "sintoma": "wifi_caido"
}
```

response:

```json
{
  "success": true,
  "message": "El sintoma 'wifi_caido' fue agregado con exitoso.",
  "code": 201
}
```

## 6. POST Crear falla

/doctor/falla

request:

```json
{
    "falla": "sin_modulo_wifi"
}
```

response:

```json
{
  "success": true,
  "message": "La falla 'sin_modulo_wifi' fue agregado con exitos.",
  "code": 201
}
```

## 7. POST Crear Recomendacion

/doctor/recomendacion

request:

```json
{
    "recomendacion": "instalar_modulo_wifi"
}
```

response:

```json
{
  "success": true,
  "message": "La recomendacion 'instalar_modulo_wifi' fue agregado con exito.",
  "code": 201
}
```

## 8. POST Crear Conexión sintoma-fallo

/doctor/falla_sintoma

request:

```json
{
    "falla":"sin_modulo_wifi",
    "sintoma":"wifi_caido"
}
```

response:

```json
{
  "mensaje": "Relación falla sintoma actualizada",
  "falla": "sin_modulo_wifi",
  "sintoma": "wifi_caido"
}
```

## 9. POST Crear Conexión falla-RECOMENDACION

/doctor/recomendacion_falla

request:

```json
{
    "falla":"sin_modulo_wifi",
    "recomendacion": "instalar_modulo_wifi"
}
```

response:

```json
{
  "mensaje": "Relación falla sintoma actualizada",
  "falla": "sin_modulo_wifi",
  "sintoma": "instalar_modulo_wifi"
}
```

## 10. GET Para obtener todos las fallas

/doctor/all_fallas

response:

```json
[
  "sobrecalentamiento_procesador",
  //...
  "corto_circuito_usb",
  "sin_modulo_wifi"
]
```

## 11. GET Para obtener todos las recomendaciones

/doctor/all_recomendaciones

response:

```json
[
  "limpiar_ventiladores",
  "cambiar_pasta",
  //...
  "actualizar_sistema_operativo",
  "instalar_modulo_wifi"
]
```
