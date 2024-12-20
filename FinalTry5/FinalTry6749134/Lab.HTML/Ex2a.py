import pandas as pd
import ssl

# Set SSl
ssl._create_default_https_context = ssl._create_unverified_context

# URL 
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Read HTML tables from the URL
page_tables = pd.read_html(url)

# Access the first table from the list of tables
table = page_tables[0]

# Loop t
for index in range(len(table)):
    date = table.loc[index, 'Date']
    interest_rate_1mo = table.loc[index, '1 Mo']
    print(f"Index: {index}, On {date} the 1 Mo interest rate was {interest_rate_1mo}")

