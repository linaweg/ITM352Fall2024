filename = '/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/names.txt'

#  Append the name "Port, Dan" to the file
try:
    with open(filename, 'a') as name_file:
        name_file.write("\nPort, Dan")  # at end of file 

    print("The name 'Port, Dan' has been added to the file.")

except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Step 2: Reopen the file 
try:
    with open(filename, 'r') as name_file:
        names = name_file.readlines()

        # Print 
        print("The entire contents of the file are:")
        for name in names:
            print(name.strip())

except Exception as e:
    print(f"An error occurred while reading the file: {e}")
