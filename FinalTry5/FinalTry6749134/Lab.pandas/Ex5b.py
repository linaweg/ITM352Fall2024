import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.pandas/homes_data.csv')

# Filter properties with 500 or more units
df_filtered = df[df['units'] >= 500]

# Print the first 10 rows of the filtered DataFrame
print("Filtered Data (first 10 rows):")
print(df_filtered.head(10))




