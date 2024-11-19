import React from 'react';
import FillDatabase from './FillDatabase';
import GenerateResponse from './GenerateResponse';
import './App.css'; // Import global styles

function App() {
    return (
        <div className="App">
            <h1>НИТУ МИСИС ИНФОРМАТОР</h1>
            <div className="chat-container">
                <GenerateResponse />
            </div>
            <div className="additional-options">
                <FillDatabase />
            </div>
        </div>
    );
}

export default App;