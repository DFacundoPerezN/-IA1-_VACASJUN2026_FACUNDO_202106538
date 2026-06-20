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

## 5. PUT Editar proveedor

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

## 7. GET ver facturas

/invoices

response:

```json
[
  
  {
    "original_filename": "factura_007.png",
    "id": 1,
    "invoice_number": "FAC-00007",
    "status": "PROCESSED"
  },
  //...
]
```

## 8. POST processar factura

/invoices/process

request: 

form data: file: "ruta"

response:

```json
{
    "data": {
        "date": "24/10/2025",
        "invoice_number": "FAC-00007",
        "nit": "3542019-1",
        "subtotal": "5019.46",
        "supplier": "Manufacturas Amor S.Com.",
        "tax": "602.34",
        "total": "5621.80"
    },
    "invoice_id": 1,
    "status": "SUCCESS"
}
```

## 7. GET ver bitacora

/logs

response:

```json
[
  {
    "id": 2,
    "invoice_id": 3,
    "processed_at": "Fri, 19 Jun 2026 23:22:50 GMT",
    "result": "Factura procesada correctamente",
    "status": "SUCCESS",
    "user_id": 1
  },
  {
    "id": 1,
    "invoice_id": 2,
    "processed_at": "Fri, 19 Jun 2026 22:50:44 GMT",
    "result": "Factura procesada correctamente",
    "status": "SUCCESS",
    "user_id": 1
  },
  //...
]
```

## 9. GET un factura por

/suppliers/<id>

response:

```json
{
  "id": 1,
  "invoice_number": "FAC-00007",
  "nit": "3542019-1",
  "status": "PROCESSED",
  "subtotal": 5019.46,
  "tax": 602.34,
  "total": 5621.8
}
```

## 9. GET reporte csv

/reports/invoices/csv

response:

```csv
ID,Factura,ProveedorID,NIT,Fecha,Subtotal,IVA,Total,Estado
1,FAC-00007,1,3542019-1,,5019.46,602.34,5621.80,PROCESSED
2,FAC-00007,1,3542019-1,,5019.46,602.34,5621.80,PROCESSED
3,FAC-00007,1,3542019-1,,5019.46,602.34,5621.80,PROCESSED
```
