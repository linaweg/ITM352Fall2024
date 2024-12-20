import warnings
import pandas as pd
import requests

# my warnings again 
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Load data
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
response = requests.get(url, verify=False)
with open('sales_data.csv', 'wb') as f:
    f.write(response.content)
df = pd.read_csv('sales_data.csv').fillna(0)

# Display column names for structure
print("Available columns:", df.columns)

# Function for Sales Data Preview
def sales_data_preview():
    """Show the first n rows of the sales data based on user input."""
    total_rows = len(df)
    print(f"\nTotal rows available: {total_rows}")
    n = input("Enter rows to display:\n- Enter a number from 1 to {0}\n- To see all rows, enter 'all'\n- To skip preview, press Enter\n".format(total_rows))
    
    if n.strip().lower() == "all":
        print(df)
    elif n.isdigit() and 1 <= int(n) <= total_rows:
        print(df.head(int(n)))
    elif n.strip() == "":
        print("No preview selected.")
    else:
        print("Invalid input. Please enter a valid number within range or 'all'.")

# Function for Sales by Customer Type and Order Type by State
def sales_by_customer_type_and_order_type_by_state():
    """Show sales by customer type and order type, grouped by state."""
    pivot_table = pd.pivot_table(df, values='quantity', index=['customer_state', 'customer_type'], columns='order_type', aggfunc='sum', fill_value=0)
    print("\nSales by customer type and order type by state:")
    print(pivot_table)

# Function for Number of Unique Employees by Region
def unique_employees_by_region():
    """Show the number of unique employees by sales region."""
    pivot_table = df.pivot_table(index='sales_region', values='employee_id', aggfunc=pd.Series.nunique)
    pivot_table.columns = ['unique_employees']
    print("\nNumber of unique employees by sales region:")
    print(pivot_table)

# Main loop
def main_menu():
    print("\n--- Sales Data Dashboard ---")
    print("1. Sales Data")
    print("2. Sales by Customer Type and Order Type by State")
    print("3. Number of Employees by Region")
    
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        sales_data_preview()
    elif choice == "2":
        sales_by_customer_type_and_order_type_by_state()
    elif choice == "3":
        unique_employees_by_region()
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")

# Run 
main_menu()


