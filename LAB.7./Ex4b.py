even_numbers = [2]
number = 4  # start with the next even number after 2
while number <= 50:
    even_numbers.append(number)
    number += 2
print(even_numbers)