from flask import Blueprint, request, jsonify, current_app
from app.models.note import Note
from bson import ObjectId
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint('notes', __name__, url_prefix='/api/notes')

@note_bp.route('', methods=['POST', 'GET'])
@jwt_required()
def handle_notes():
    current_user_id = get_jwt_identity() # Get the identity (user ID) from the JWT
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({"error": "Content is required"}), 400

        content = data['content']
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        location_name = data.get('location_name')
        updated_at = datetime.now()
        
        new_note = Note(content=content, latitude=latitude, longitude=longitude, location_name=location_name, updated_at=updated_at, user_id=current_user_id)
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
@jwt_required()
def handle_single_notes(note_id):
    current_user_id = get_jwt_identity()

    try:
        note_id_obj = ObjectId(note_id)
    except Exception:
        return jsonify({"error": "Invalid note ID format"}), 400

    note = Note.find_by_id(note_id_obj)

    if not note:
        return jsonify({"error": f"Note with id {note_id} not found"}), 404

    if note.user_id != current_user_id:
        return jsonify({"error": "Unauthorized to access this note"}), 403

    if request.method == "GET":
        return jsonify(note.to_dict()), 200
    elif request.method == "PATCH":
        data = request.get_json()
        if not data or not "content" in data:
            return jsonify({"error": "No update detected"}), 400
        else:
            updated_at = datetime.now()
            data["updated_at"] = updated_at
            updated_note = Note.update(note_id=note_id_obj, update_operation=data)
            if updated_note:
                return jsonify({"message": "Note updated successfully", "updated_note": updated_note.to_dict()}), 200
            else:
                return jsonify({"error": "Failed to update note"}), 500

    elif request.method == "DELETE":
        note.delete()
        return jsonify({"message": f"Note with id {note_id} deleted successfully"}), 204

@note_bp.route("/by_locname/<loc_name>", methods=["GET"])
@jwt_required()
def handle_notes_by_locname(loc_name):
    current_user_id = get_jwt_identity()
    notes = Note.find_by_locname(loc_name, user_id=current_user_id)
    return jsonify([note.to_dict() for note in notes]), 200