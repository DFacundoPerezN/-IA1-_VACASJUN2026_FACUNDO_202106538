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

## 4. POST Obtener recomendaciones segun sintomas

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

## 12. DELETE sintoma

/doctor/delete_sintoma

request:

```json
{
    "sintoma":"periferico_no_reconocido"
}
```

response:

```json
{
  "mensaje": "Sintoma borrado",
  "sintoma": "periferico_no_reconocido"
}
```

## 13. DELETE falla

/doctor/delete_falla

request:

```json
{
    "falla":"sin_modulo_wifi"
}
```

response:

```json
{
  "mensaje": "Falla borrada",
  "falla": "sin_modulo_wifi"
}
```

## 14. DELETE Recomendacion

/doctor/delete_recomendacion

request:

```json
{
    "recomendacion": "instalar_modulo_wifi"
}
```

response:

```json
{
  "mensaje": "Recomendacion borrada",
  "recomendacion": "instalar_modulo_wifi"
}
```

## 15. PUT Editar nombre de Sintoma

/doctor/sintoma

request:

```json
{
    "viejo":"wifi_caido",
    "nuevo":"sin_wifi"
}
```

response:

```json
{
  "mensaje": "Sintoma editado",
  "nombre_viejo": "wifi_caido",
  "nuevo_nombre": "sin_wifi"
}
```

## 16. PUT Editar nombre de Falla

/doctor/falla

request:

```json
{
    "nuevo":"falta_modulo_wifi",
    "viejo":"sin_modulo_wifi"
}
```

response:

```json
{
  "mensaje": "Falla editada",
  "nombre_viejo": "sin_modulo_wifi",
  "nombre_nuevo": "falta_modulo_wifi"
}
```

## 17. PUT Editar nombre de Recomendacion

/doctor/recomendacion

request:

```json
{
    "nuevo":"instalar_nuevo_modulo_wifi",
    "viejo":"instalar_modulo_wifi"
}
```

response:

```json
{
  "mensaje": "Recomendacion editada",
  "nombre_viejo": "instalar_modulo_wifi",
  "nombre_nuevo": "instalar_nuevo_modulo_wifi"
}
```

## 18. PUT Editar Id del chat

/doctor/chat_id

request:

```json
{
  "chat_id":"-5040561022"
}
```

response:

```json
{
  "message": "se cambio correcatemente el id del chat"
}
```
