import pandas as pd

# get CSV file 
df = pd.read_csv('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.pandas/homes_data.csv')

# Step 1: Check current data types
print("Data types before cleaning:")
print(df.dtypes)

# Step 2: Coerce columns to the correct data types

df['units'] = pd.to_numeric(df['units'], errors='coerce')  
df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')  



# Step 3: Check data types again to confirm changes
print("\nData types after cleaning:")
print(df.dtypes)

# Step 4: Print the cleaned data
print("\nCleaned Data (first 10 rows):")
print(df.head(10))
