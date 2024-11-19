import React from 'react';
import './LoadingSpinner.css'; // Create this CSS file for styles

const LoadingSpinner = () => {
    return (
        <div className="spinner-container">
            <div className="spinner"></div>
        </div>
    );
};

export default LoadingSpinner;