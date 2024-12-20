with open('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/names.txt', 'r') as name_file:
    name = name_file.readline()  # Read the first line
    num_names = 0

    # Loop through until no more names (empty string)
    while name != '':
        print(name.strip())  # Print the name and remove any extra newline characters
        num_names += 1
        name = name_file.readline()  # Read the next line

# Print the total number of names
print(f"There are {num_names} names")


