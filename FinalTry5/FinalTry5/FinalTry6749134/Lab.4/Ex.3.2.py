first_name = input("First name:")
middle_name = input("Middle name:")
last_name = input("Last name:")

##Ex1a

###Ex1b
##full_name = f"{first_name} {middle_name[0]}. {last_name}"

##Ex1c
###full_name ="%s %s. %s"%(first_name, middle_name[0], last_name)

##Ex1d
###full_name = "{} {}. {}".format(first_name, middle_name[0], last_name)

##Ex1e
###full_name = ' '.join([first_name, middle_name[0], last_name])

##Ex1f - homework 
###name_list = [first_name, middle_name[0], last_name]

##full_name = "{} {} {}".format(*name_list)

##print(full_name)


# Create a list of the name parts
name_list = [first_name, {middle_name[0]}, last_name]

# Use the format() method and unpack the list with * operator
full_name = "{} {} {}".format(*name_list)

# Print the formatted string
print(full_name)



