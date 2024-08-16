import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css'; 


const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <p className="mb-2">© {new Date().getFullYear()} Issue Tracker. All rights reserved.</p>
        <p className="mb-0">
          <Link to="/" className="footer-link">Home</Link> | 
          <Link to="/create" className="footer-link"> Create Issue</Link> | 
          <Link to="/issues" className="footer-link"> Issue List</Link>
        </p>
      </div>
    </footer>
  );
};

export default Footer;
