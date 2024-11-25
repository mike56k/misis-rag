import React from 'react';
import FillDatabase from './FillDatabase';
import GenerateResponse from './GenerateResponse';
import './App.css'; // Import global styles
import ChatWidget from './ChatWidget';

function App() {
    return (
        <div className="App">
            <ChatWidget />
            {/* <h1>НИТУ МИСИС ИНФОРМАТОР</h1>
            <div className="chat-container">
                <GenerateResponse />
            </div>
            <div className="additional-options">
                <FillDatabase />
            </div> */}
        </div>
    );
}

export default App;