from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from models.user import User
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

auth = Blueprint("auth", __name__)


# -----------------------------
# User Registration
# -----------------------------
@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check if all fields are provided
    if not username or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({
            "message": "Email already exists"
        }), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


# -----------------------------
# User Login
# -----------------------------
@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # Check if user exists
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    # Verify password
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    # Generate JWT Token
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "username": user.username
    }), 200


# -----------------------------
# Protected Profile Route
# -----------------------------
@auth.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    return jsonify({
        "message": "Protected Route Accessed Successfully",
        "user_id": current_user
    }), 200