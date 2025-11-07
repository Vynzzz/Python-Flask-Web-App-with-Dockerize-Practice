from flask import Blueprint, jsonify
from app.auth import require_token

bp = Blueprint("main", __name__)

@bp.route("/public")
def public_route():
    return jsonify({"message":"This route is public"}), 200

@bp.route("/private")
@require_token
def private_route():
    return jsonify({"message":"You accessed a protected route"}), 200