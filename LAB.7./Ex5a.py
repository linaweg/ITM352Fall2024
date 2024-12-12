tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

# counter for strings
string_count = 0

# Loop through the tuple
for element in tuple:
    # Check if the element is a string
    if type(element) == str:
        string_count += 1

# Print 
print(f"There are {string_count} strings in the tuple.")

