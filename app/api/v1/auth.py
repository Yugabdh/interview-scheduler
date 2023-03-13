from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.db.models.User import User
from app.util.hasher import check_password_hash
from datetime import timedelta


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    print(email, password)
    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.find_by_email(email)

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # jwt = api_v1.config['jwt']
    access_token = create_access_token(
        identity=user.email,
        expires_delta=timedelta(hours=1),
    )
    return jsonify({'access_token': access_token, 'user': user.to_user_data()}), 200
