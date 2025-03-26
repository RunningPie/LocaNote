from datetime import timedelta
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    # Use a single secret key for JWT
    secret_key = os.getenv('SECRET_KEY', 'your_default_secret_key')
    app.config['JWT_SECRET_KEY'] = secret_key

    # CORS Configuration
    CORS(app, supports_credentials=True)

    # JWT Configuration
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SECURE'] = True
    app.config['JWT_COOKIE_SAMESITE'] = 'Strict'

    # Initialize JWT
    jwt = JWTManager(app)
    
    # Configure your database connection here using environment variables
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.mongo_client = MongoClient(app.config['MONGO_URI'], server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        app.mongo_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Import your models and controllers (Blueprints)
    from .models import note, user
    from .controllers.note_controller import note_bp
    from .controllers.user_controller import user_bp

    # Register your Blueprints
    app.register_blueprint(note_bp)
    app.register_blueprint(user_bp)

    return app