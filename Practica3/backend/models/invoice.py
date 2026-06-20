from database.db import db
class Invoice(db.Model):

    __tablename__ = "invoices"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    original_filename = db.Column(
        db.String(255)
    )

    invoice_number = db.Column(
        db.String(100)
    )

    date = db.Column(
        db.Date
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey( "suppliers.id")
    )

    supplier = db.relationship(
        "Supplier",
        backref="invoices"
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

    status = db.Column(
        db.String(50)
    )