# Endpoints del Backend

## 1. POST login

/auth/login

request:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

response:

```json
{
  "token": "eyJhbG.....cuECxip7I5rUete9RbDapRJgxIsEIym55rtNuZzeWJE"
}
```

## 2. POST Crear Proveedor

/suppliers

request:

```json
{
  "name":"Nintendo",
  "nit": "251795376",
  "email": "non@email.com",
  "phone": "+502 88899977"
}
```

response:

```json
{
  "message": "Proveedor creado"
}
```

## 3. GET ver proveedores

/suppliers

response:

```json
[
  {
    "email": "non@email.com",
    "id": 1,
    "name": "Nintendo",
    "nit": "251795376",
    "phone": "+502 88899977"
  },
  {
  "name": "Intelaf",
  "nit": "1234567-8",
  "email": "ventas@intelaf.com",
  "phone": "2222-2222"
  }
  //...
]
```

## 4. GET un proveedor

/suppliers/<id>

response:

```json
{
    "email": "non@email.com",
    "id": 1,
    "name": "Nintendo",
    "nit": "251795376",
    "phone" : "+502 88899977"
}

```

## 5. PUT Editarroveedor

/suppliers

request:

```json
{
  "name":"Nintendo of Gt",
  "nit": "251795376",
  "email": "nintendogt@email.com",
  "phone": "+502 88899977"
}
```

response:

```json
{
  "message": "Proveedor actualizado"
}
```

## 6. DELETE un proveedor

/suppliers/<id>

response:

```json
{
  "message": "Proveedor eliminado"
}
```
