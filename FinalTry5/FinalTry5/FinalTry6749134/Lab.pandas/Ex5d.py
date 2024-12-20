import pandas as pd

# get CSV file 
df = pd.read_csv('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.pandas/homes_data.csv')

# Step 1: Drop rows with null values
df_cleaned = df.dropna()

# Step 2: Drop duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Step 3: Print the cleaned data (after removing null values and duplicates)
print("Data after dropping null values and duplicates (first 10 rows):")
print(df_cleaned.head(10))

# NOt neccessary: Print the shape of the DataFrame to see how many rows/columns remain
print(f"\nDataFrame shape after cleaning: {df_cleaned.shape}")
