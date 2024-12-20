import os

filename = '/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/names.txt_bad'

# Check if file exists 
if os.path.isfile(filename) and os.access(filename, os.R_OK):
    try:
        with open(filename, 'r') as name_file:
            names = name_file.readlines()  # Reads all lines into a list

            # Remove newlines and extra spaces
            names = [name.strip() for name in names]

            # Print 
            for name in names:
                print(name)

            # Print t
            print(f"There are {len(names)} names")

    except Exception as e:
        # Catch other potential errors
        print(f"An error occurred while reading the file: {e}")
else:
    # If file doesn't exist or isn't readable
    print(f"Error: The file '{filename}' does not exist or is not readable.")
