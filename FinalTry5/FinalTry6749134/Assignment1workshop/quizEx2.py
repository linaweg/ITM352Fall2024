# List of tuples with questions and correct answers
qa_pairs = [
    ("What is 5 + 7", "12"),
    ("What is the capital of Texas", "Austin")
]

# Initialize score
score = 0

# Iterate through the list of question-answer pairs
for question, correct_answer in qa_pairs:
    answer = input(question + "? ")  
    if answer == correct_answer:     
        score += 1                   
# Print the final score
print(f"Your score is {score}")
