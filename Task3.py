import numpy as np
import pandas as pd

# Load data from the text file
data = np.loadtxt('spam-data.csv')

# Display the shape and first few rows of the loaded data
print("Shape of the data:", data.shape)
print("First few rows of the data:\n", data[:5])



# Load data from the text file into a DataFrame
df = pd.read_csv('spam-data.txt', delimiter='\t')  # Assuming the data is tab-separated

# Display the shape and first few rows of the loaded data
print("Shape of the data:", df.shape)
print("First few rows of the data:\n", df.head())

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained logistic regression model
# Assuming model is already trained and available
model = LogisticRegression()
model.coef_ = np.array([[-0.5]])  # Example coefficients, replace with actual values
model.intercept_ = np.array([-0.1])  # Example intercept, replace with actual values

# Load the email data from the "emails.txt" file
with open('emails.txt', 'r') as file:
    email_content = file.read()

# Preprocess the email data (e.g., extract features)
# Assuming we use simple Bag-of-Words representation
vectorizer = CountVectorizer()
email_features = vectorizer.fit_transform([email_content])

# Predict whether the email is spam or not
prediction = model.predict(email_features)

# Print the prediction result on the console
if prediction[0] == 1:
    print("The first email is predicted to be spam.")
else:
    print("The first email is predicted not to be spam.")
