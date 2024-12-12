import requests
import pandas as pd

# URL URL file 
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    # Send the GET request with SSL verification disabled
    response = requests.get(url, verify=False)

    # Write the response content to a local CSV file
    with open('sales_data.csv', 'wb') as f:
        f.write(response.content)

    # Read the CSV file while skipping bad lines
    df = pd.read_csv('sales_data.csv', on_bad_lines='skip')

    # Print the first 5 rows of the DataFrame
    print(df.head())

except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: There was a problem parsing the CSV file.")
except Exception as e:
    print(f"An error occurred: {e}")

