import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Import the CSS file for styling

function HomePage() {
    return (
        <div className="home-page">
            <div className="content">
                <h1>Welcome to Health Insurance</h1>
                <section>
                    <h2>What is Health Insurance?</h2>
                    <p>Information about health insurance...</p>
                </section>
                <section>
                    <h2>Why Health Insurance?</h2>
                    <p>Reasons for health insurance...</p>
                </section>
                <section>
                    <h2>Our Health Solutions</h2>
                    <p>Currently offering personal health plans...</p>
                </section>
                <Link to="/quote" className="quote-link">Get a Quote</Link>
                <Link to="/login" className="login-link">Login</Link>
            </div>

            {/* Sidebar for navigation */}
            <div className="sidebar">
                <Link to="/health-and-wellbeing">Health & Wellbeing</Link>
                <Link to="/contact-us">Contact Us</Link>
                <Link to="/about-us">About Us</Link>
                <Link to="/login">Login</Link>
            </div>
        </div>
    );
}

export default HomePage;
