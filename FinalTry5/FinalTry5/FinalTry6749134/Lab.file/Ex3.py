import csv

# Initialize variables for calculations
total_fare = 0
fare_count = 0
max_trip_miles = 0

# Path to CSV file
csv_file_path = '/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/taxi_1000.csv'  

# Read the CSV file and process fare and trip miles
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            # Get the fare and trip miles, converting to float for calculations
            fare = float(row['Fare'])
            trip_miles = float(row['Trip Miles'])

            # Update total fare and count
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

# print/ output the results 
print(f"Total Fares: {total_fare}")
print(f"Average Fare: {average_fare}")
print(f"Maximum Trip Distance: {max_trip_miles} miles")
