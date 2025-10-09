from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer once at startup
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validate input fields
    title = data.get('title', '')
    text = data.get('text', '')
    if not title or not text:
        return jsonify({'error': 'Both title and text are required.'}), 400

    content = title + ' ' + text
    vect_content = vectorizer.transform([content])
    pred = model.predict(vect_content)[0]

    label = 'Fake news' if pred == 1 else 'Real news'

    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
