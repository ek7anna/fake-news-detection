import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');
  const [prediction, setPrediction] = useState('');
  const [error, setError] = useState('');

  const handleCheckNews = async () => {
    setError('');
    setPrediction('');
    if (!title || !text) {
      setError('Please enter both title and content of the news.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:3000/predict', {
        title,
        text
      });
      setPrediction(response.data.prediction);
    } catch (err) {
      setError('Something went wrong while checking the news.');
    }
  };

  return (
    <div className="App">
      <h1 className="header">Truth Finder</h1>
      <p className="quote">"Then you will know the truth, and the truth will set you free." <br /><span>– John 8:32</span></p>

      <div className="form">
        <input
          type="text"
          placeholder="News Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="News Content"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button onClick={handleCheckNews}>Check News</button>

        {error && <p className="error">{error}</p>}
        {prediction && (
          <p className="result">
            Prediction: <strong>{prediction}</strong>
          </p>
        )}
      </div>
    </div>
  );
}

export default App