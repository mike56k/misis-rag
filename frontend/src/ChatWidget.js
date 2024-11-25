import React, { useState } from 'react';
import axios from 'axios';
import './ChatWidget.css'; // Ensure this is updated with new styles
import LoadingSpinner from './LoadingSpinner'; // Import the loading spinner component

const ChatWidget = () => {
  const [responses, setResponses] = useState([]);
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async () => {
    if (!question.trim()) return; // Prevent sending empty messages

    setResponses([...responses, { question, answer: '...' }]); // Show loading state
    setLoading(true);
    setQuestion('');

    try {
      const result = await axios.post('/generate_response', { question });
      setResponses([...responses, { question, answer: result.data.result }]);
    } catch (error) {
      console.error('Error fetching response:', error);
      setResponses([...responses, { question, answer: 'Error fetching response' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-widget">
      <div className="chat-window">
        <div className="messages">
          {responses.map((msg, index) => (
            <div key={index} className={`message ${msg.answer === '...' ? 'loading' : ''}`}>
              <p><strong>Вы:</strong> {msg.question}</p>
              <p><strong>Бот:</strong> {msg.answer}</p>
            </div>
          ))}
        </div>
        <div className="input-area">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ваш вопрос о НИТУ МИСИС..."
          />
            {loading ? (<LoadingSpinner />) : (<button onClick={handleSendMessage} disabled={loading}>
            Отправить
          </button>)}
        </div>
      </div>
    </div>
  );
};

export default ChatWidget;