from flask import current_app
from datetime import datetime

class User:
    def __init__(self, username, email, password, created_at=None, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at if created_at else datetime.now()
        self._id = _id
    
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
        }
    
    @staticmethod
    def get_collection():
        db = current_app.mongo_client["LocaNoteDB"]  # Assuming you've set up the MongoDB client in your app
        return db["users"]

    def save(self):
        users_collection = self.get_collection()
        
        # Insert new user
        result = users_collection.insert_one(self.to_dict())
        self._id = result.inserted_id
        return self._id
    
    def delete(self):
        users_collection = self.get_collection()
        
        # Delete old user
        result = users_collection.delete_one({"_id": self._id})
        return result.acknowledged
    
    @staticmethod
    def find_all():
        users_collection = User.get_collection()
        users = []
        for user_data in users_collection.find():
            users.append(User(**user_data))
        return users

    @staticmethod
    def find_by_username(username):
        users_collection = User.get_collection()
        user_data = users_collection.find_one({"username": username})
        if user_data:
            return User(**user_data)
    
    @staticmethod
    def find_by_email(email):
        users_collection = User.get_collection()
        user_data = users_collection.find_one({"email": email})
        if user_data:
            return User(**user_data)

    @staticmethod
    def find_by_id(user_id):
        users_collection = User.get_collection()
        user_data = users_collection.find_one({"_id": user_id})
        if user_data:
            return User(**user_data)