import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.pandas/homes_data.csv')

# Step 1: Convert the 'sale_price' column to numeric
df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')

# Step 2: Filter out rows where the sale price is 0 
df_filtered = df[df['sale_price'] > 0]

# Step 3: Print the filtered results (first 10 rows)
print("Data after filtering out 0 sales (first 10 rows):")
print(df_filtered.head(10))

# Step 4: Compute and display average sale prices 
average_sales_price = df_filtered['sale_price'].mean()
print(f"\nAverage Sales Price: {average_sales_price}")
