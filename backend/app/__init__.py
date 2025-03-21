from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

def create_app():
    load_dotenv()  # Load environment variables from .env file
    app = Flask(__name__)
    CORS(app)       # Enable CORS for all origins (you might want to restrict this later)

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
    # from .controllers.user_controller import user_bp  # You might add this later

    # Register your Blueprints
    app.register_blueprint(note_bp)
    # app.register_blueprint(user_bp) # You'll register this later

    return app