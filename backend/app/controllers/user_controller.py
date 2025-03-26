from flask import Blueprint, request, jsonify, current_app, make_response
from app.models.user import User
from datetime import datetime, timedelta
import bcrypt
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from flask_wtf.csrf import generate_csrf

user_bp = Blueprint('users', __name__, url_prefix='/api/users')

# New CSRF Token Route
@user_bp.route('/csrf-token', methods=['GET'])
def get_csrf_token():
    token = generate_csrf()
    response = make_response(jsonify({"csrf_token": token}), 200)
    return response

# Register Route
@user_bp.route('/register', methods=['POST'])
def handle_register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    elif ('username' not in data) and ('email' not in data):
        return jsonify({"error": "Username or email is required"}), 400
    if 'password' not in data:
        return jsonify({"error": "Password is required"}), 400
   
    # Hash the password
    pw_salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), pw_salt)
   
    # Prepare user data
    username = data["username"]
    email = data["email"]
    password = hashed_password
    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "created_at": datetime.now(),
    }
   
    # Save the user
    user = User(**user_data)
    new_user_id = user.save()
   
    if new_user_id:
        return jsonify({"message": "User created successfully", "user_id": str(new_user_id)}), 201
    else:
        return jsonify({"error": "Failed to create user"}), 500

# Login Route
@user_bp.route('/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    elif 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    elif 'password' not in data:
        return jsonify({"error": "Password is required"}), 400
    
    # Fetch user by username or email
    if "@" in data["username"]:
        user = User.find_by_email(data["username"])
    else:
        user = User.find_by_username(data["username"])
    
    # Validate password
    if user and bcrypt.checkpw(data["password"].encode('utf-8'), user.password):
        # Create an access token with the user's ID as the identity
        access_token = create_access_token(identity=str(user._id))
        
        # Create a response object
        response = jsonify({"message": "Logged in successfully", "user_id": str(user._id)})
        
        # Set the JWT access token in a secure HTTPOnly cookie
        set_access_cookies(response, access_token)
        
        return response, 200
    else:
        return jsonify({"error": "Invalid username/email or password"}), 401

# Logout Route
@user_bp.route('/logout', methods=['POST'])
def handle_logout():
    response = jsonify({"message": "Logged out successfully"})
    unset_jwt_cookies(response)
    return response, 200