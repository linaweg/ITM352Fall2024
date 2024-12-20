import requests
from bs4 import BeautifulSoup

# URL 
url = "https://shidler.hawaii.edu/itm/people"

# Fetch t
response = requests.get(url)
page_content = response.content

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Print 
print(soup.prettify()[:500])  
