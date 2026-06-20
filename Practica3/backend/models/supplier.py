from database.db import db

class Supplier(db.Model):

    __tablename__ = "suppliers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    nit = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(255)
    )

    phone = db.Column(
        db.String(50)
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )


def get_supplier_id(supplier_name: str, nit = "C/F"):
    supplier = Supplier.query.filter(Supplier.name.ilike(supplier_name)).first()

    if supplier:
        supplier_id = supplier.id
    else:
        supplier = Supplier(
            name=supplier_name,
            nit=nit 
        )

        db.session.add(supplier)
        db.session.flush()

        supplier_id = supplier.id

    return supplier_id