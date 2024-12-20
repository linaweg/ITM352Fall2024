import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.pandas/homes_data.csv')

# Print the dimensions
print(f"DataFrame dimensions: {df.shape}")

# Show the first 10 rows of the DataFrame
print("\nFirst 10 rows:")
print(df.head(10))
