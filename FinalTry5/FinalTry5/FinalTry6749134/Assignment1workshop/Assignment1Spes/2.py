# Step 2: Simple quiz game with two questions using a list of tuples
def quiz_game():
    # List of tuples for questions and correct answers
    questions = [
        ("How was Columbus' ship called in 1492?", "Santa Maria"),
        ("What is 2 + 2?", "4")
    ]

    # Iterate 
    for question, correct_answer in questions:
        # Ask  question
        user_answer = input(question + " ")

        # Check  answer is correct
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

# Run 
quiz_game()
