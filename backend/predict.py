import joblib

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_news(title, text):
    content = title + ' ' + text
    vect_content = vectorizer.transform([content])
    prediction = model.predict(vect_content)
    return prediction[0]  # 0 or 1

# For testing
if __name__ == "__main__":
    sample_title = "Some news headline"
    sample_text = "Some news body text here..."
    pred = predict_news(sample_title, sample_text)
    if pred == 0:
        print("Real news")
    else:
        print("Fake news")
