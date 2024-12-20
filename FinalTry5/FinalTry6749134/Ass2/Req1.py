import requests
import pandas as pd
import time
import warnings

# I got warnings...--> to avoid that 
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# URL of the CSV file
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

# showing that file is loading
print("Loading sales data...")

try:
    # Send the GET request with SSL verification 
    response = requests.get(url, verify=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the file locally and load it into a DataFrame
        with open('sales_data.csv', 'wb') as f:
            f.write(response.content)
        
        # Start timing the loading process
        start_time = time.time()
        
        # Load the CSV file into pandas DataFrame
        df = pd.read_csv('sales_data.csv')
        
        # Replace missing data with zeros
        df.fillna(0, inplace=True)
        
        # Calculate load time
        load_time = time.time() - start_time
        
        # Display data info
        print("Data loaded successfully.")
        print(f"Time taken: {load_time:.2f} seconds")
        print(f"Rows of data: {df.shape[0]}")
        print("Available columns:", list(df.columns))
        
        # Required columns for analytics
        required_columns = ['column1', 'column2', 'column3']  # Replace with actual required columns
        
        # Check for missing columns
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print("Warning: Missing columns for analytics:", missing_columns)
            print("Some analytics may not work due to missing data.")
    else:
        print("Error: Failed to download the file. Please check the URL or internet connection.")

except Exception as e:
    print("An error occurred while loading the data:", e)






