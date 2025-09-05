from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load and train model (same as before)
df = pd.read_csv(r'C:\Users\Karthik HS\Desktop\Ml-project\spam.csv', encoding='latin1')
X = df['v2']
y = df['v1'].map({'ham': 0, 'spam': 1})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_vec, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    email_text = data['email']
    email_vec = vectorizer.transform([email_text])
    pred = model.predict(email_vec)[0]
    result = 'spam' if pred == 1 else 'ham'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)