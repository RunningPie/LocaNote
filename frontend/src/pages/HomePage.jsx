import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const HomePage = () => {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const backendURL = process.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    const fetchNotes = async () => {
      try {
        const response = await axios.get(`${backendURL}/api/notes`,
          {withCredentials: true}
        ); // Assuming your backend runs on the same domain or you've configured a proxy
        setNotes(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message || 'Failed to fetch notes');
        setLoading(false);
      }
    };

    fetchNotes();
  }, []); // Empty dependency array means this effect runs once after the initial render

  if (loading) {
    return <div>Loading notes...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Your Notes</h1>
      <Link to="/create-note">Create New Note</Link>

      {notes.length === 0 ? (
        <p>No notes yet. Click "Create New Note" to add one.</p>
      ) : (
        <ul>
          {notes.map(note => (
            <li key={note._id}>
              <strong>{note.content}</strong>
              {note.location_name && <p>Location: {note.location_name}</p>}
              {note.latitude && note.longitude && <p>Coordinates: {note.latitude}, {note.longitude}</p>}
              {/* You can add Edit and Delete buttons here later */}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default HomePage;