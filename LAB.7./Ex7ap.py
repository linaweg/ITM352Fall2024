# Define the tuples
years_tuple = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
respondents_tuple = (17, 35, 26, 26, 25, 27, 35, 21, 19)

# Initialize empty lists
years_list = []
respondents_list = []

# Iterate through indices of tuples
for i in range(len(years_tuple)):
    years_list.append(years_tuple[i])
    respondents_list.append(respondents_tuple[i])

# Store data in dic 
survey_data = {
    "years": years_list,
    "respondents": respondents_list
}

# print
print(survey_data)
