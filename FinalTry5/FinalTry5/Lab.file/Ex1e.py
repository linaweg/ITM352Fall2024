with open('/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/names.txt', 'r') as name_file:
    names = name_file.readlines()  # Reads all lines into a list
    
    # Remove newlines and extra spaces
    names = [name.strip() for name in names]
    
    # Print each name
    for name in names:
        print(name)
    
    # Print the total number of names
    print(f"There are {len(names)} names")
