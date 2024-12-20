import requests

# Define the URL with the query
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"


response = requests.get(url)


records = response.json()


print("API Response:")
print(records)
