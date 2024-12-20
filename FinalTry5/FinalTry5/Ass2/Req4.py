import warnings
import pandas as pd
import requests

# my warnings 
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# get data 
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
response = requests.get(url, verify=False)
with open('sales_data.csv', 'wb') as f:
    f.write(response.content)
df = pd.read_csv('sales_data.csv').fillna(0)

# Function to display data summary
def display_data_summary():
    """Display a summary of the data to guide users."""
    print("\n--- Data Summary ---")
    summary = {}
    
    # Total orders
    summary["Total orders"] = len(df)
    
    # Number of employees
    if 'employee_id' in df.columns:
        summary["Number of employees"] = df['employee_id'].nunique()
    
    # Sales regions
    if 'sales_region' in df.columns:
        summary["Sales regions"] = df['sales_region'].nunique()
    
    # Date range of orders
    if 'order_date' in df.columns:
        summary["Date range"] = f"{df['order_date'].min()} to {df['order_date'].max()}"
    
    # Number of unique customers
    if 'customer_name' in df.columns:
        summary["Unique customers"] = df['customer_name'].nunique()
    
    # Product categories
    if 'product_category' in df.columns:
        summary["Product categories"] = df['product_category'].nunique()
    
    # Unique states
    if 'customer_state' in df.columns:
        summary["Unique states"] = df['customer_state'].nunique()
    
    # Total sales amount
    if 'unit_price' in df.columns and 'quantity' in df.columns:
        df['total_sales'] = df['unit_price'] * df['quantity']
        summary["Total sales amount"] = df['total_sales'].sum()
    
    # Total quantities of products sold
    if 'quantity' in df.columns:
        summary["Total quantities sold"] = df['quantity'].sum()
    
    # Print summary
    for key, value in summary.items():
        print(f"{key}: {value}")

# Custom Pivot Table Generator with Export Option
def custom_pivot_table():
    """Generate a custom pivot table based on user selections, with an option to export to Excel."""
    # Display data summary
    display_data_summary()
    
    # 1. select rows 
    print("\nSelect rows:")
    row_options = {
        "1": "employee_name",
        "2": "sales_region",
        "3": "product_category"
    }
    for key, value in row_options.items():
        print(f"{key}. {value}")
    row_selection = input("Enter the number(s) of your choice(s), separated by commas: ")
    rows = [row_options[num.strip()] for num in row_selection.split(",") if num.strip() in row_options]

    # 2, select colums 
    print("\nSelect columns (optional):")
    column_options = {
        "1": "order_type",
        "2": "customer_type"
    }
    for key, value in column_options.items():
        print(f"{key}. {value}")
    column_selection = input("Enter the number(s) of your choice(s), separated by commas (press Enter for no grouping): ")
    columns = [column_options[num.strip()] for num in column_selection.split(",") if num.strip() in column_options]

    # 3, select values 
    print("\nSelect values:")
    value_options = {
        "1": "quantity",
        "2": "unit_price"
    }
    for key, value in value_options.items():
        print(f"{key}. {value}")
    value_selection = input("Enter the number(s) of your choice(s), separated by commas: ")
    values = [value_options[num.strip()] for num in value_selection.split(",") if num.strip() in value_options]

    # 4, select function 
    print("\nSelect aggregation function:")
    agg_options = {
        "1": "sum",
        "2": "mean",
        "3": "count"
    }
    for key, value in agg_options.items():
        print(f"{key}. {value}")
    agg_selection = input("Enter the number of your choice: ").strip()
    agg_func = agg_options.get(agg_selection, "sum")  # Default to 'sum' if invalid

    # Create the pivot table
    try:
        pivot_table = pd.pivot_table(df, 
                                     values=values, 
                                     index=rows, 
                                     columns=columns if columns else None, 
                                     aggfunc=agg_func)
        print("\nGenerated Pivot Table:")
        print(pivot_table)
        
        # Option to export to Excel
        export = input("\nDo you want to export the result to an Excel file? (yes/no): ").strip().lower()
        if export == "yes":
            filename = input("Enter the filename (without extension): ").strip()
            if not filename:
                filename = "custom_pivot_table"
            pivot_table.to_excel(f"{filename}.xlsx", index=True)
            print(f"Data exported to {filename}.xlsx successfully.")
            
    except KeyError as e:
        print(f"Error: One of the selected fields is not available in the data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# pivot table 
custom_pivot_table()

