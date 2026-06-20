from flask import Blueprint
from flask import request
from flask import jsonify

from database.db import db

from models.processing_log import ProcessingLog

logs_bp = Blueprint(
    "logs",
    __name__,
    url_prefix="/logs"
)


@logs_bp.route("", methods=["GET"])
def get_logs():

    logs = ProcessingLog.query.order_by(
        ProcessingLog.processed_at.desc()
    ).all()

    result = []

    for log in logs:

        result.append({
            "id": log.id,
            "invoice_id": log.invoice_id,
            "user_id": log.user_id,
            "status": log.status,
            "result": log.result,
            "processed_at": log.processed_at
        })

    return jsonify(result)