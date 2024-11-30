import React from 'react';
import FillDatabase from './FillDatabase';
import './App.css'; // Import global styles
import ChatWidget from './ChatWidget';

function App() {
    return (
        <div className="App">
            <ChatWidget />
            {/*  <FillDatabase /> */}
        </div>
    );
}

export default App;