# Sample of fares
sample_fares = [8.60, 5.75, 13.25, 21.21]

# Iterate through each fare in the list
for fare in sample_fares:
    if fare > 12:
        print(f"{fare}: This fare is high!")
    else:
        print(f"{fare}: This fare is low")
