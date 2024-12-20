import requests
from bs4 import BeautifulSoup


url = "https://www.hicentral.com/hawaii-mortgage-rates.php"


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
   
    rate_table = soup.find('table')  
    
    
    rows = rate_table.find_all('tr')[1:]  
    print("Extracted rows:", rows)  
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
