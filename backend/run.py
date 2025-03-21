from app import create_app
from app.models.note import Note

app = create_app()

if __name__ == '__main__':
    # with app.app_context():  # Push an application context for accessing current_app
    #     # Test creating and saving a note
    #     new_note = Note(content="This is a test note from the model!", latitude=1.23, longitude=4.56)
    #     saved_id = new_note.save()
    #     print(f"Saved note ID: {saved_id}")

    #     if saved_id:
    #         # Test finding the note by ID
    #         retrieved_note = Note.find_by_id(saved_id)
    #         if retrieved_note:
    #             print("Retrieved note:")
    #             print(retrieved_note.to_dict())
    #         else:
    #             print("Failed to retrieve the note.")

    #         # Test finding all notes
    #         all_notes = Note.find_all()
    #         print("\nAll notes:")
    #         for note in all_notes:
    #             print(note.to_dict())
    #     else:
    #         print("Failed to save the note.")

    app.run(debug=True, host='0.0.0.0', port=5000)