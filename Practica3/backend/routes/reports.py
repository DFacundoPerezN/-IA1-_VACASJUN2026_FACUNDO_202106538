from flask import Blueprint

import csv
from io import StringIO

from flask import Response

from models.invoice import Invoice


reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports"
)

@reports_bp.route("/invoices/csv", methods=["GET"])
def export_invoices_csv():

    invoices = Invoice.query.all()

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Factura",
        "ProveedorID",
        "NIT",
        "Fecha",
        "Subtotal",
        "IVA",
        "Total",
        "Estado"
    ])

    for invoice in invoices:

        supplier_name = ""

        if invoice.supplier_id:
            supplier_name = invoice.supplier_id

        writer.writerow([
            invoice.id,
            invoice.invoice_number,
            supplier_name,
            invoice.nit,
            invoice.date,
            invoice.subtotal,
            invoice.tax,
            invoice.total,
            invoice.status
        ])

    output.seek(0)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=invoices_report.csv"
        }
    )