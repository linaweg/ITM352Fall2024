import pandas as pd

# Load the JSON file into DataFrame
df = pd.read_json('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.pandas/Taxi_Trips.json')

# Print summary statistics
print("Summary Statistics:")
print(df.describe())

# Calculate and print median values for numeric columns only
print("\nMedian Values (for numeric columns):")
print(df.select_dtypes(include='number').median())

