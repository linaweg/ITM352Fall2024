# Create a list of even numbers from 1 to 50 using a while loop
even_numbers = []
num = 1

while num <= 50:
    if num % 2 == 0:
        even_numbers.append(num)
    num += 1

# Convert the list to a tuple
even_numbers_tuple = tuple(even_numbers)

# Try to append to the tuple
try:
    even_numbers_tuple.append(52)  # This will raise an error
except AttributeError:
    print("Error: Tuples are immutable, and an attempt was made to append a value to the tuple.")
