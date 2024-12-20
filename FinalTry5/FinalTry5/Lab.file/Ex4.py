import csv

# Initialize variables for calculations
total_fare = 0
fare_count = 0
max_trip_miles = 0

# Path to the CSV file
csv_file_path = '/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/taxi_1000.csv'  

# Read the CSV file and process fare and trip miles for records with fares > 10
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            # Get the fare and trip miles, converting to float (for calculations)
            fare = float(row['Fare'])
            trip_miles = float(row['Trip Miles'])

            # Only process records where the fare is greater than 10 dollars
            if fare > 10:
                total_fare += fare
                fare_count += 1

                # Update max trip miles if the current trip is longer
                if trip_miles > max_trip_miles:
                    max_trip_miles = trip_miles
        except (ValueError, KeyError):
            # Skip rows where fare or trip miles are missing or not a valid float
            continue

# Calculate average fare
average_fare = total_fare / fare_count if fare_count > 0 else 0

# Outpu/ print  the results
print(f"Total Fares (greater than $10): {total_fare}")
print(f"Average Fare (greater than $10): {average_fare}")
print(f"Maximum Trip Distance (for fares greater than $10): {max_trip_miles} miles")