from flask import Blueprint, request, jsonify
from app.models.note import Note
from bson import ObjectId
from datetime import datetime

note_bp = Blueprint('notes', __name__, url_prefix='/api/notes')

@note_bp.route('', methods=['POST', 'GET'])
def handle_notes():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({"error": "Content is required"}), 400

        content = data['content']
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        location_name = data.get('location_name')
        updated_at = datetime.now()
        
        new_note = Note(content=content, latitude=latitude, longitude=longitude, location_name=location_name, updated_at=updated_at)
        saved_id = new_note.save()
        
        if saved_id:
            return jsonify({"message": "Note created successfully",
                            "note_id": str(saved_id)}), 201
        else:
            return jsonify({"error": "Failed to create note"}), 500       
        
    elif request.method == 'GET':
        notes = Note.find_all()
        return jsonify([note.to_dict() for note in notes]), 200

@note_bp.route('/<note_id>', methods=['GET', 'PATCH', 'DELETE'])
def handle_single_notes(note_id):
    note_id = ObjectId(note_id)
    if request.method == "GET":
        note = Note.find_by_id(note_id)
        if note:
            return jsonify(note.to_dict()), 200
        else:
            return jsonify({"error": f"Note with id {note_id} not found"}), 404
    elif request.method == "PATCH":
        data = request.get_json()
        if not data or not "content" in data:
            return jsonify({"error": "No update detected"}), 400
        else:          
            updated_at = datetime.now()
            data["updated_at"] = updated_at
            updated_note = Note.update(note_id=note_id, update_operation=data)
            if updated_note:
                return jsonify({"message": "Note updated successfully", "updated_note": updated_note.to_dict()}), 200            

            else:
                return jsonify({"error": "Failed to update note"}), 500
            
    elif request.method == "DELETE":
        note = Note.find_by_id(note_id)
        if note:
            note.delete()
            return jsonify({"message": f"Note with id {note_id} deleted successfully"}), 200
        else:
            return jsonify({"error": f"Note with id {note_id} not found"}), 404

@note_bp.route("/by_locname/<loc_name>", methods=["GET"])
def handle_notes_by_locname(loc_name):
    notes = Note.find_by_locname(loc_name)
    return jsonify([note.to_dict() for note in notes]), 200