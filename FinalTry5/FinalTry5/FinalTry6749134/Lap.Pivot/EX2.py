import pandas as pd
import pyarrow  # Good practice, as noted
import numpy as np

# The correct Google Drive download link
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Set display option to show all columns
pd.set_option('display.max_columns', None)

try:
    # First, download the file using requests
    import requests
    response = requests.get(url, verify=False)
    
    # Save the content to a file
    with open('sales_data.csv', 'wb') as f:
        f.write(response.content)
    
    # Now read the file locally with pandas
    sales_data = pd.read_csv('sales_data.csv', dtype_backend='pyarrow', on_bad_lines='skip')

    # Parse the order_date field (without 'format="mixed"')
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], errors='coerce')

    # Print the first 5 rows
    print(sales_data.head())

    # Ensure quantity and unit_price are numeric
    sales_data['quantity'] = pd.to_numeric(sales_data['quantity'], errors='coerce')
    sales_data['unit_price'] = pd.to_numeric(sales_data['unit_price'], errors='coerce')

    # Calculate total sales
    sales_data['sales'] = sales_data['quantity'] * sales_data['unit_price']

    # Create a pivot table aggregating sales by sales_region, with columns defined by order_type
    sales_pivot = sales_data.pivot_table(
        index='sales_region', 
        columns='order_type', 
        values='sales', 
        aggfunc=np.sum,
        fill_value=0,  # Fill missing values with 0
        margins=True, 
        margins_name="Totals"
    )

    print(sales_pivot)

except Exception as e:
    print(f"An error occurred: {e}")

