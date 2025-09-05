import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load dataset (replace with your dataset path)
# Example assumes a CSV with columns: 'text' and 'label' ('spam' or 'ham')
df = pd.read_csv(r'C:\Users\Karthik HS\Desktop\Ml-project\spam.csv', encoding='latin1')
print(df.columns)
# Preprocessing
X = df['v2']  # message text
y = df['v1'].map({'ham': 0, 'spam': 1})  # label

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to numerical features
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['ham', 'spam']))

# Display confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['ham', 'spam'])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

# Predict on new email
def predict_email(email_text):
    email_vec = vectorizer.transform([email_text])
    pred = model.predict(email_vec)[0]
    return 'spam' if pred == 1 else 'ham'

# Example usage
print(predict_email('Is that seriously how you spell his name?'))
