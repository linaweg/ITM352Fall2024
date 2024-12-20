# Dictionary with questions, answer options, and the correct answer
QUESTIONS = {
    "What is 5 + 7?": {
        "options": ["10", "11", "12", "13"],
        "correct": "12"
    },
    "What is the capital of Texas?": {
        "options": ["Houston", "Austin", "Dallas", "San Antonio"],
        "correct": "Austin"
    }
}

# Initialize score
score = 0

# Iterate through the questions dictionary
for question, details in QUESTIONS.items():
    print(question)  # Display the question
    for i, option in enumerate(details["options"], 1):  # Display answer options
        print(f"{i}. {option}")
    
    # Get the user's answer (choosing the option number)
    answer_index = int(input("Enter the number of your choice: "))
    
    # Check if the chosen option is the correct answer
    if details["options"][answer_index - 1] == details["correct"]:
        score += 1  # Increment score if correct

# Print the final score
print(f"Your score is {score}")
