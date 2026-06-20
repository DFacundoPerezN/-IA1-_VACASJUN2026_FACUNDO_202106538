from database.db import db
#registro de procesamiento

class ProcessingLog(db.Model):

    __tablename__ = "processing_logs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoices.id")
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id" )
    )

    status = db.Column(
        db.String(32)
    )

    result = db.Column(
        db.Text
    )

    processed_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )