import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load data from spam-data.csv
data = pd.read_csv('spam-data.csv')

# Split data into features (X) and target labels (y)
X = data.drop(columns=['label'])
y = data['label']

# Build and train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Load email content from emails.txt
with open('emails.txt', 'r') as file:
    email_content = file.read()

# Extract email features using CountVectorizer
vectorizer = CountVectorizer(vocabulary=X.columns)
email_features = vectorizer.fit_transform([email_content])

# Classify email as spam or not spam
prediction = model.predict(email_features)
if prediction[0] == 1:
    print("The email is predicted to be spam.")
else:
    print("The email is predicted not to be spam.")

# Analyze feature importance
feature_importance = pd.Series(model.coef_[0], index=X.columns)
print("Feature Importance:")
print(feature_importance)
