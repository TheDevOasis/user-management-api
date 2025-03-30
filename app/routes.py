# routes.py (User CRUD Routes)
from flask import Blueprint, request, jsonify
from app.models import User
from app.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")
    new_user = User(username=data["username"], email=data["email"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@user_bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{ "id": u.id, "username": u.username, "email": u.email } for u in users])
