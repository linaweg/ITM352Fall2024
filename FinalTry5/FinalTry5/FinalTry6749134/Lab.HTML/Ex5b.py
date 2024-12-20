import requests
import pandas as pd


url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

response = requests.get(url)


if response.status_code == 200:
    
    records = response.json()
    
    
    print("Records:", records)
    
    
    if isinstance(records, list) and len(records) > 0:
       
        df = pd.DataFrame.from_records(records)
       
        df.columns = ['driver_type', 'count']
        
        df.set_index('driver_type', inplace=True)
        
       
        print("\nDataFrame with License Counts by Driver Type:")
        print(df)
    else:
        print("Error: Records are not in the expected list format or are empty.")
else:
    print(f"Error: {response.status_code} - {response.text}")

