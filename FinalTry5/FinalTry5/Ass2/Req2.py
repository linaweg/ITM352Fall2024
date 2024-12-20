#I got warnings, to avaid that 
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")



import pandas as pd
import requests
import time

# Load the data as before
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
response = requests.get(url, verify=False)
with open('sales_data.csv', 'wb') as f:
    f.write(response.content)
df = pd.read_csv('sales_data.csv').fillna(0)

# Define functions for each dashboard operation
def show_first_n_rows():
    n = int(input("Enter the number of rows to display: "))
    print(df.head(n))

def total_sales_by_region_and_order_type():
    result = df.groupby(['region', 'order_type'])['sales'].sum()
    print(result)

def average_sales_by_region_state_sale_type():
    result = df.groupby(['region', 'state', 'sale_type'])['sales'].mean()
    print(result)

def sales_by_customer_type_and_order_type_by_state():
    result = df.groupby(['customer_type', 'order_type', 'state'])['sales'].sum()
    print(result)

def total_sales_quantity_price_by_region_product():
    result = df.groupby(['region', 'product'])[['quantity', 'price']].sum()
    print(result)

def total_sales_quantity_price_by_customer_type():
    result = df.groupby('customer_type')[['quantity', 'price']].sum()
    print(result)

def max_min_sales_price_by_category():
    max_price = df.groupby('category')['price'].max()
    min_price = df.groupby('category')['price'].min()
    print("Max sales price by category:\n", max_price)
    print("Min sales price by category:\n", min_price)

def unique_employees_by_region():
    result = df.groupby('region')['employee_id'].nunique()
    print("Number of unique employees by region:\n", result)

def create_custom_pivot_table():
    print("Create a custom pivot table")
    index_col = input("Enter the index column for pivot table: ")
    columns_col = input("Enter the columns for pivot table: ")
    values_col = input("Enter the values column for pivot table: ")
    aggfunc = input("Enter the aggregation function (e.g., sum, mean): ")
    try:
        pivot = pd.pivot_table(df, index=index_col, columns=columns_col, values=values_col, aggfunc=aggfunc)
        print(pivot)
    except KeyError:
        print("Invalid columns selected. Please check column names.")

def exit_program():
    print("Exiting the program.")
    exit()

# Create menu items as tuples of 
menu_items = [
    ("Show the first n rows of sales data", show_first_n_rows),
    ("Total sales by region and order_type", total_sales_by_region_and_order_type),
    ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_sale_type),
    ("Sales by customer type and order type by state", sales_by_customer_type_and_order_type_by_state),
    ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
    ("Total sales quantity and price by customer type", total_sales_quantity_price_by_customer_type),
    ("Max and min sales price by category", max_min_sales_price_by_category),
    ("Number of unique employees by region", unique_employees_by_region),
    ("Create a custom pivot table", create_custom_pivot_table),
    ("Exit", exit_program)
]

# Main loop
def main_menu():
    while True:
        print("\n--- Sales Data Dashboard ---")
        for i, (desc, _) in enumerate(menu_items, start=1):
            print(f"{i}. {desc}")
        
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= len(menu_items):
                # Execute the chosen function
                menu_items[choice - 1][1]()
            else:
                print("Invalid choice. Please select a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run 
main_menu()
