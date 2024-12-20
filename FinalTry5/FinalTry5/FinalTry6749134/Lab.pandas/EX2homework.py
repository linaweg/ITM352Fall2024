import pandas as pd

# List of individuals' ages, names, and genders
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# Create a dictionary
data = {
    'Name': names,
    'Age': ages,
    'Gender': gender 
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate average age by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()

# Print DataFrame and average age by gender
print(df)
print("\nAverage age by gender:")
print(average_age_by_gender)

