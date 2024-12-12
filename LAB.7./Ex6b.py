# Function to classify fares (for testing purposes)
def classify_fare(fare):
    if fare > 12:
        return f"{fare}: This fare is high!"
    else:
        return f"{fare}: This fare is low"

# Function to classify and print fares (using classify_fare function)
def classify_and_print_fares(fares):
    for fare in fares:
        print(classify_fare(fare))

# Test cases function
def run_tests():
    # List test cases: (input, expected_output)
    test_cases = [
        (21.21, "21.21: This fare is high!"),
        (13.25, "13.25: This fare is high!"),
        (8.60, "8.6: This fare is low"),
        (5.75, "5.75: This fare is low"),
    ]

    # Run 
    for i, (fare, expected) in enumerate(test_cases):
        result = classify_fare(fare)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed")

# Call the function to classify and print 
sample_fares = [8.60, 5.75, 13.25, 21.21]
classify_and_print_fares(sample_fares)

# Run
run_tests()

