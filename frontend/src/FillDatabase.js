import React from 'react';
import axios from 'axios';

const FillDatabase = () => {
    const handleFillDatabase = async () => {
        try {
            const response = await axios.get('/fill_database');
            alert(response.data);
        } catch (error) {
            console.error("Error filling database:", error);
            alert("Failed to populate database");
        }
    };

    return (
        <div>
            <h2>Populate Database</h2>
            <button onClick={handleFillDatabase}>Fill Database</button>
        </div>
    );
};

export default FillDatabase;