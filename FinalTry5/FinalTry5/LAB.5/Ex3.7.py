trip ={'miles': [1.1, 0.8, 2.5, 2.6],
    'fares': ('$6.25', '$5.25', '$10.50', '$8.05')}

###b
#third_trip_miles = trip["miles"][2]
#third_trip_fare = trip["fares"][2]


# Dictionary of trips

#third_trip_miles = trip["miles"][2]  
#third_trip_fare = trip["fares"][2]   

# Printing out the 3rd trip's miles and fare
#print(f"3rd Trip: {third_trip_miles} miles, Cost: {third_trip_fare}")




###c
# Defining the dictionary with miles and fares
##trip = {
    #'miles': [1.1, 0.8, 2.5, 2.6],
    #'fares': ["$6.25", "$5.25", "$10.50", "$8.05"]
#}

# Using zip() 
##trip_dict = dict(zip(trip['miles'], trip['fares']))

# 3rd trip duration and cost
#third_trip_miles = trip['miles'][2]  
#third_trip_fare = trip_dict[third_trip_miles]  
# Printing 3rd triü
#print(f"Duration: {third_trip_miles} miles")
#print(f"Cost: {third_trip_fare}")

# List omiles and fares
#trip_miles = [1.1, 0.8, 2.5, 2.6]
#trip_fares = ["$6.25", "$5.25", "$10.50", "$8.05"]

# list dic using loop 
#trips_list = [{'miles': miles, 'fare': fare} for miles, fare in zip(trip_miles, trip_fares)]

# Print
#print(trips_list)


#third_trip = trips_list[2]
#print(f"Duration: {third_trip['miles']} miles")
#print(f"Cost: {third_trip['fare']}")

# List of trip and fare
trip_miles = [1.1, 0.8, 2.5, 2.6]
trip_fares_str = ["$6.25", "$5.25", "$10.50", "$8.05"]


import re

# Convert tfare strings to numbers (floats)
trip_fares = [float(re.sub(r'\$(.*)', r'\1', fare)) for fare in trip_fares_str]

# Creating list of dictionaries using a loop
trips_list = [{'miles': miles, 'fare': fare} for miles, fare in zip(trip_miles, trip_fares)]

# Printing 
print(trips_list)


third_trip = trips_list[2]
print(f"Duration: {third_trip['miles']} miles")
print(f"Cost: ${third_trip['fare']:.2f}")  # Formatting fare as currency (2 decimal places)





