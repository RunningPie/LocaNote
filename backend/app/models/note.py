from flask import current_app
from datetime import datetime

class Note:
    def __init__(self, content, latitude=None, longitude=None, location_name=None, created_at=None, user_id=None, _id=None, updated_at=None):
        self.content = content
        self.latitude = latitude
        self.longitude = longitude
        self.location_name = location_name
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at
        self.user_id = user_id
        self._id = _id  # MongoDB's unique identifier

    def to_dict(self):
        return {
            "content": self.content,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "location_name": self.location_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user_id": self.user_id,
        }

    @staticmethod
    def get_collection():
        db = current_app.mongo_client["LocaNoteDB"]  # Assuming you've set up the MongoDB client in your app
        return db["notes"]

    def save(self):
        notes_collection = self.get_collection()

        # Insert new note
        result = notes_collection.insert_one(self.to_dict())
        self._id = result.inserted_id
        return self._id
    
    def delete(self):
        notes_collection = self.get_collection()

        # Delete old note
        result = notes_collection.delete_one({"_id": self._id})
        return result.acknowledged
    
    @staticmethod #this has to be a static method
    def update(note_id, update_operation):
        # Update existing note
        notes_collection = Note.get_collection()
        notes_collection.update_one({"_id": note_id}, {"$set": update_operation})
        note_data = notes_collection.find_one({"_id": note_id})
        if note_data:
            return Note(**note_data)
        return None

    @staticmethod
    def find_by_id(note_id):
        notes_collection = Note.get_collection()
        note_data = notes_collection.find_one({"_id": note_id})
        if note_data:
            return Note(**note_data)
        return None

    @staticmethod
    def find_all(user_id=None):
        notes_collection = Note.get_collection()
        notes = []
        if user_id:
            res = notes_collection.find({"user_id": user_id})
        else:
            res = notes_collection.find()
        for note_data in res:
            notes.append(Note(**note_data))
        return notes

    @staticmethod
    def find_by_locname(loc_name, user_id):
        # print(f"loc_name: {loc_name}")
        notes_collection = Note.get_collection()
        notes = []
        for note_data in notes_collection.find({"location_name": loc_name, "user_id": user_id}):
            notes.append(Note(**note_data))
        return notes