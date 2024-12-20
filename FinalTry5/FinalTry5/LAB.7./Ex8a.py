even_numbers = []
num = 1

while num <= 50:
    if num % 2 == 0:
        even_numbers.append(num)
    num += 1

print(even_numbers)

# Convert the list to a tuple
even_numbers_tuple = tuple(even_numbers)

# Try to append to the tuple (error?)
try:
    even_numbers_tuple.append(52)
except AttributeError as e:
    print(f"Error: {e}")
