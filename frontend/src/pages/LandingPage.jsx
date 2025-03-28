import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  const styles = {
    container: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '100vh',
      padding: '20px',
      textAlign: 'center',
      backgroundColor: '#f4f4f4',
    },
    title: {
      fontSize: '2.5em',
      marginBottom: '20px',
      color: '#333',
    },
    subtitle: {
      fontSize: '1.2em',
      marginBottom: '30px',
      color: '#666',
    },
    buttonContainer: {
      display: 'flex',
      gap: '20px',
    },
    button: {
      padding: '10px 20px',
      fontSize: '1em',
      borderRadius: '5px',
      textDecoration: 'none',
      color: 'white',
      backgroundColor: '#007bff',
      border: 'none',
      cursor: 'pointer',
      transition: 'background-color 0.3s ease',
    },
    buttonSecondary: {
      backgroundColor: '#6c757d',
    },
    features: {
      marginTop: '50px',
      maxWidth: '600px',
      textAlign: 'left',
    },
    featureItem: {
      marginBottom: '10px',
      color: '#555',
    },
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>LocaNote</h1>
      <p style={styles.subtitle}>Your location-aware note-taking companion.</p>

      <div style={styles.buttonContainer}>
        <Link to="/login" style={{ ...styles.button }}>
          Log In
        </Link>
        <Link to="/signup" style={{ ...styles.button, ...styles.buttonSecondary }}>
          Sign Up
        </Link>
      </div>

      <div style={styles.features}>
        <h2>Key Features</h2>
        <ul>
          <li style={styles.featureItem}>Create notes associated with specific locations.</li>
          <li style={styles.featureItem}>Easily recall information based on where you are.</li>
          <li style={styles.featureItem}>Optionally add latitude, longitude, or a location name to your notes.</li>
          <li style={styles.featureItem}>Securely store and access your notes from anywhere.</li>
          {/* Add more features as you develop them */}
        </ul>
      </div>
    </div>
  );
};

export default LandingPage;