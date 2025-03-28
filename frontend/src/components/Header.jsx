import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  const styles = {
    header: {
      backgroundColor: '#333',
      color: 'white',
      padding: '15px 20px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
    },
    logo: {
      fontSize: '1.5em',
      fontWeight: 'bold',
      textDecoration: 'none',
      color: 'white',
    },
  };

  return (
    <header style={styles.header}>
      <Link to="/" style={styles.logo}>
        LocaNote
      </Link>
      {/* You can add more elements to the header here if needed */}
    </header>
  );
};

export default Header;