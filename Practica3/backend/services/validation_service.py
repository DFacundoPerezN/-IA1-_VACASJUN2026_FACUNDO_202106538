def validate_invoice(data):

    errors = []

    if not data.get("invoice_number"):
        errors.append(
            "Número de factura no encontrado"
        )

    if not data.get("nit"):
        errors.append(
            "NIT no encontrado"
        )

    if not data.get("total"):
        errors.append(
            "Total no encontrado"
        )

    try:

        subtotal = float(
            data["subtotal"]
        )

        tax = float(
            data["tax"]
        )

        total = float(
            data["total"]
        )

        if round(subtotal + tax, 2) != round(total, 2):

            errors.append(
                "La suma subtotal + impuesto no coincide con el total"
            )

    except:

        errors.append(
            "Error validando montos"
        )

    return errors