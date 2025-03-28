import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const styles = {
    navbar: {
      backgroundColor: '#f8f9fa',
      padding: '10px 20px',
      borderBottom: '1px solid #ddd',
    },
    navLinks: {
      listStyle: 'none',
      padding: 0,
      margin: 0,
      display: 'flex',
      gap: '20px',
    },
    navItem: {
      margin: 0,
    },
    link: {
      textDecoration: 'none',
      color: '#333',
      fontWeight: 'bold',
    },
  };

  return (
    <nav style={styles.navbar}>
      <ul style={styles.navLinks}>
        <li style={styles.navItem}>
          <Link to="/" style={styles.link}>
            Home
          </Link>
        </li>
        <li style={styles.navItem}>
          <Link to="/create" style={styles.link}>
            Create Note
          </Link>
        </li>
        <li style={styles.navItem}>
          <Link to="/login" style={styles.link}>
            Login
          </Link>
        </li>
        <li style={styles.navItem}>
          <Link to="/signup" style={styles.link}>
            Sign Up
          </Link>
        </li>
        {/* You can add more navigation links here */}
      </ul>
    </nav>
  );
};

export default Navbar;