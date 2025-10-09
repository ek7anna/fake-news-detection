const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.post('/predict', async (req, res) => {
    const { title, text } = req.body;

    if (!title || !text) {
        return res.status(400).json({ error: 'Title and text are required' });
    }

    try {
        const response = await axios.post('http://127.0.0.1:5000/predict', { title, text });
        res.json(response.data);
    } catch (error) {
        console.error('Error calling Flask API:', error.message);
        res.status(500).json({ error: 'Error getting prediction from ML API' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
