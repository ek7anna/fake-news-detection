# Truth Finder — Fake News Detection

A small full-stack project that trains a TF-IDF + Logistic Regression model to classify news as real or fake.
Includes a Flask ML API, a Node proxy server, and a React frontend.

---

## Quick Links

| Component            | Description                               | File                                               |
| -------------------- | ----------------------------------------- | -------------------------------------------------- |
| Model Training       | Training logic (saves model & vectorizer) | `backend/train_model.py`                           |
| ML API               | Flask API exposing `/predict` endpoint    | `backend/api.py`                                   |
| Prediction Helper    | Local test prediction script              | `backend/predict.py`                               |
| Node Proxy           | Forwards frontend requests to Flask API   | `backend/server.js`                                |
| Dataset              | Training data for model                   | `backend/train.csv`                                |
| Backend Dependencies | Python & Node backend dependencies        | `backend/requirements.txt`, `backend/package.json` |
| Frontend App         | Main React component                      | `frontend/src/App.js`                              |
| Frontend Styles      | CSS styles                                | `frontend/src/App.css`                             |
| Frontend Entry       | HTML entry file                           | `frontend/public/index.html`                       |
| Frontend Tests       | Unit tests                                | `frontend/src/App.test.js`                         |
| Frontend Config      | Package configuration                     | `frontend/package.json`                            |

---

## Prerequisites

* Python 3.8+ (for backend)
* Node.js and npm (for frontend and optional Node proxy)

---

## Backend — Train and Run ML API

### 1. Create Virtual Environment and Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train Model

Trains on `train.csv` and saves `model.pkl` and `vectorizer.pkl`:

```bash
python train_model.py
```

### 3. Start Flask API

```bash
python api.py
```

Notes:

* Training uses `train_fake_news_model` in `train_model.py`.
* The helper script `predict.py` loads the trained model for quick local predictions via `predict_news`.

---

## Node Proxy (Optional)

You can run a Node proxy to forward frontend requests to the Flask API.

### Start Proxy

```bash
cd backend
node server.js
```

Important:

* The proxy listens on the port defined in `server.js`.
* If the React development server uses the same port, change one of them or set a custom React port in a `.env` file.

---

## Frontend — React App

### 1. Install and Run

```bash
cd frontend
npm install
npm start
```

### 2. Open in Browser

Default: [http://localhost:3000](http://localhost:3000)

The React app (`App.js`) posts to `http://localhost:3000/predict` by default.
Ensure the Flask API or Node proxy is running on the corresponding port.

---

## Testing

### Frontend Unit Tests

```bash
cd frontend
npm test
```

### Backend Quick Prediction Test

```bash
python backend/predict.py
```

---

## File Map (High Level)

```
backend/
├── train_model.py          # Training script and model save
├── api.py                  # Flask API exposing /predict
├── predict.py              # Helper for local prediction
├── server.js               # Node proxy server
├── requirements.txt
├── package.json
└── train.csv

frontend/
├── src/
│   ├── App.js
│   ├── App.css
│   └── App.test.js
├── public/
│   └── index.html
└── package.json
```

---

## Tips

* If ports conflict between React and Node proxy, change the port in `server.js` or define a React port in `.env`.
* Retrain the model if data or labels change:

  ```bash
  python backend/train_model.py
  ```
* The trained model and vectorizer are stored as `model.pkl` and `vectorizer.pkl`.

---

## License

MIT License

---

Made using Flask, React, and Machine Learning.
