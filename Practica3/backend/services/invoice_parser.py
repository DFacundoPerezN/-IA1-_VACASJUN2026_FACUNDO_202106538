import re
#expresiones regulares

def extract_invoice_number(text):

    match = re.search(
        r'FAC-\d+',
        text,
        re.IGNORECASE
    )

    return match.group(0) if match else None

def extract_supplier(text):

    match = re.search(
        r'Proveedor:\s*(.+)',
        text
    )

    return match.group(1).strip() if match else None

def extract_nit(text):

    match = re.search(
        r'NIT:\s*([\d\-]+)',
        text
    )

    return match.group(1) if match else None

def extract_date(text):

    match = re.search(
        r'Fecha:\s*(\d{2}/\d{2}/\d{4})',
        text
    )

    return match.group(1) if match else None

def extract_subtotal(text):

    match = re.search(
        r'Subtotal:\s*Q?\s*([\d\.]+)',
        text,
        re.IGNORECASE
    )

    return match.group(1) if match else None

def extract_tax(text):

    match = re.search(
        r'IVA\s*[\d]+%?:\s*Q.?\s*([\d\.]+)',
        text,
        re.IGNORECASE
    )
    #print(match)
    if match:
        return match[1]

    return None

def extract_total(text):

    matches = re.findall(
        r'TOTAL:\s*Q?\s*([\d\.]+)',
        text,
        re.IGNORECASE
    )

    if matches:
        return matches[-1]

    return None

def extract_invoice_data(text):

    return {
        "invoice_number":
            extract_invoice_number(text),

        "supplier":
            extract_supplier(text),

        "nit":
            extract_nit(text),

        "date":
            extract_date(text),

        "subtotal":
            extract_subtotal(text),

        "tax":
            extract_tax(text),

        "total":
            extract_total(text)
    }