# models/rpa_record.py

from database.db import db

class RPARecord(db.Model):

    __tablename__ = "rpa_records"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    invoice_number = db.Column(
        db.String(100)
    )

    supplier = db.Column(
        db.String(255)
    )

    nit = db.Column(
        db.String(50)
    )

    subtotal = db.Column(
        db.Numeric(10,2)
    )

    tax = db.Column(
        db.Numeric(10,2)
    )

    total = db.Column(
        db.Numeric(10,2)
    )