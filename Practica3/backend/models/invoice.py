from database.db import db

class Invoice(db.Model):

    __tablename__ = "invoices"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    invoice_number = db.Column(
        db.String(100)
    )

    date = db.Column(
        db.Date
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "suppliers.id"
        )
    )

    nit = db.Column(
        db.String(50)
    )

    subtotal = db.Column(
        db.Numeric(10, 2)
    )

    tax = db.Column(
        db.Numeric(10, 2)
    )

    total = db.Column(
        db.Numeric(10, 2)
    )

    file_path = db.Column(
        db.String(500)
    )

    status = db.Column(
        db.String(50),
        default="PENDING"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )