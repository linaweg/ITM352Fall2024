import requests
from bs4 import BeautifulSoup


url = "https://www.hicentral.com/hawaii-mortgage-rates.php"


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    rate_table = soup.find('table')  

    if rate_table:
        
        rates = []

        
        rows = rate_table.find_all('tr')[1:]  
        
        
        for row in rows:
            columns = row.find_all('td')
            
            
            bank_name = columns[0].get_text(strip=True)  
            current_rate = columns[1].get_text(strip=True)  

           
            rates.append((bank_name, current_rate))

        
        print("Bank Name and Current Mortgage Rates:")
        for bank, rate in rates:
            print(f"{bank}: {rate}")
    else:
        print("Could not find the rate table on the page.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
