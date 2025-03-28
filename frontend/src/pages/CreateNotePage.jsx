import React, { useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

const CreateNotePage = () => {
  const [content, setContent] = useState('');
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [locationName, setLocationName] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    setSuccessMessage('');
    setErrorMessage('');

    const noteData = {
      content,
      latitude: latitude ? parseFloat(latitude) : null,
      longitude: longitude ? parseFloat(longitude) : null,
      location_name: locationName || null,
    };

    try {
      const response = await axios.post('/api/notes', noteData);
      setSuccessMessage(response.data.message);
      setContent('');
      setLatitude('');
      setLongitude('');
      setLocationName('');
      // Optionally navigate back to the home page after successful creation
      setTimeout(() => {
        navigate('/');
      }, 1500);
    } catch (error) {
      setErrorMessage(error.response?.data?.error || 'Failed to create note');
    }
  };

  return (
    <div>
      <h1>Create New Note</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="content">Content:</label>
          <textarea
            id="content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="latitude">Latitude (Optional):</label>
          <input
            type="number"
            id="latitude"
            value={latitude}
            onChange={(e) => setLatitude(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="longitude">Longitude (Optional):</label>
          <input
            type="number"
            id="longitude"
            value={longitude}
            onChange={(e) => setLongitude(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="locationName">Location Name (Optional):</label>
          <input
            type="text"
            id="locationName"
            value={locationName}
            onChange={(e) => setLocationName(e.target.value)}
          />
        </div>
        <button type="submit">Save Note</button>
      </form>

      {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}

      <p>
        <Link to="/">Back to Home</Link>
      </p>
    </div>
  );
};

export default CreateNotePage;