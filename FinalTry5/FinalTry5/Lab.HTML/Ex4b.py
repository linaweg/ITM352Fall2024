from sodapy import Socrata
import pandas as pd

client = Socrata("data.cityofchicago.org", None)

results = client.get("rr23-ymwb", limit=500)


df = pd.DataFrame.from_records(results)


print("Available columns:", df.columns)


if 'vehicle_make' in df.columns and 'vehicle_fuel_source' in df.columns:
    print("\nVehicle Makes and Fuel Sources:")
    print(df[['vehicle_make', 'vehicle_fuel_source']])
else:
    print("The columns 'vehicle_make' and/or 'vehicle_fuel_source' were not found in the dataset.")
