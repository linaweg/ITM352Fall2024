import csv

# Initialize variables for calculations
realinc_values = []

# Path to CV file 
csv_file_path = '/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/survey_1000.csv'

# Read the CSV file and collect REALINC values, greather than 0
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            # REALINC is the 5457th field, which is index 5456 in Python (0-indexed)
            realinc_value = float(row[5456])
            if realinc_value > 0:
                realinc_values.append(realinc_value)
        except (ValueError, IndexError):
            # Skip rows that can't be converted or don't have enough fields
            continue

# Calculate the statistics for REALINC values
if realinc_values:
    realinc_count = len(realinc_values)
    realinc_avg = sum(realinc_values) / realinc_count
    realinc_max = max(realinc_values)
    realinc_min = min(realinc_values)

    # Print the results
    print(f"Number of values greater than 0: {realinc_count}")
    print(f"Average REALINC: {realinc_avg}")
    print(f"Maximum REALINC: {realinc_max}")
    print(f"Minimum REALINC: {realinc_min}")
else:
    print("No valid REALINC values found.")
