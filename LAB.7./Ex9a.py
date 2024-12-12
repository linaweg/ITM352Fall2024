for num in range(1, 11):
    if num == 5:
        continue  # Skip the number 5
    if num == 8:
        print("Reached 8, stopping the loop.")
        break  # Stop the loop when number is 8
    print(num)
