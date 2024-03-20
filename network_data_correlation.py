import pandas as pd

# Read the generated data from CSV file
df = pd.read_csv('network_data.csv', header=None)

# Calculate correlation matrix using Pearson formula
correlation_matrix = df.corr(method='pearson')

# Display correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Save correlation matrix to CSV
correlation_matrix.to_csv('correlation_matrix.csv')
