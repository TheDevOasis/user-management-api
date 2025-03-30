# __init__.py (Flask App Factory)
from flask import Flask, jsonify  # 🔹 Asegúrate de que jsonify esté aquí
from app.config import Config
from app.db import db
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "¡Welcome to User Management API!"}), 200  

    return app
