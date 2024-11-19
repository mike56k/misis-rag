import React, { useState } from 'react';
import axios from 'axios';
import styles from './GenerateResponse.module.css';
import LoadingSpinner from './LoadingSpinner'; // Import the loading spinner component

const GenerateResponse = () => {
    const [question, setQuestion] = useState('');
    const [responses, setResponses] = useState([]);
    const [loading, setLoading] = useState(false); // State to manage loading

    const handleGenerateResponse = async () => {
        setLoading(true);
        try {
            const result = await axios.post('/generate_response', { question });
            setResponses([...responses, { question, answer: result.data.result }]);
            setQuestion(''); // Clear input after submission
        } catch (error) {
            console.error("Error generating response:", error);
            alert("Failed to generate response");
        }
        finally {
            setLoading(false);
        }
    };

    return (
        <div className={styles.container}>
            <div className={styles.chatBox}>
                {responses.map((item, index) => (
                    <div key={index} className={styles.message}>
                        <p><strong>You:</strong> {item.question}</p>
                        <p><strong>Bot:</strong> {item.answer}</p>
                    </div>
                ))}
            </div>
            <input 
                type="text" 
                value={question} 
                onChange={(e) => setQuestion(e.target.value)} 
                placeholder="Введите свой вопрос..." 
            />
            {loading ? (<LoadingSpinner /> ) : (<button onClick={handleGenerateResponse}>Отправить</button>)}
        </div>
    );
};

export default GenerateResponse;