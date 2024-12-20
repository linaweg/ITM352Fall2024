import requests
import pandas as pd

# URL of the CSV file
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Send the GET request with SSL verification disabled
response = requests.get(url, verify=False)

# Write the response content to a local CSV file
with open('sales_data.csv', 'wb') as f:
    f.write(response.content)

# Load the CSV file using pandas
df = pd.read_csv('sales_data.csv')

# Print the first 5 rows of the DataFrame
print(df.head())



