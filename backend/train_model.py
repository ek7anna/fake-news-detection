import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_fake_news_model():
    # Step 1: Load the training data CSV file
    train_df = pd.read_csv('train.csv')

    # Step 2: Drop rows with missing 'title' or 'text' columns
    train_df = train_df.dropna(subset=['title', 'text'])

    # Step 3: Combine 'title' and 'text' columns to create a single text feature 'content'
    train_df['content'] = train_df['title'] + ' ' + train_df['text']

    # Step 4: Create TF-IDF vectors from 'content'
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = vectorizer.fit_transform(train_df['content'])

    # Step 5: Extract target labels (make sure they are integers)
    y = train_df['label'].astype(int)

    # Step 6: Split data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Step 7: Initialize and train the Logistic Regression classifier
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Step 8: Predict on test data
    y_pred = model.predict(X_test)

    # Step 9: Print accuracy and detailed classification report
    print(f"Accuracy on test set: {accuracy_score(y_test, y_pred):.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Step 10: Save the trained model and vectorizer to disk
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    print("Model and vectorizer saved as 'model.pkl' and 'vectorizer.pkl'")

if __name__ == "__main__":
    train_fake_news_model()
