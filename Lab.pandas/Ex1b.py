import numpy as np

# List of percentiles and household incomes
Percentile = [
    (10, 14629), 
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]

# Convert the list to a numpy array
percentile_array = np.array(Percentile)

# Print table header
print(f"{'Percentile':<15}{'Household Income'}")

# Print each row of the array
for row in percentile_array:
    print(f"{row[0]:<15}{row[1]}")
