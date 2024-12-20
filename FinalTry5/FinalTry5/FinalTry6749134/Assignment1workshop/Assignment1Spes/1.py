# Step 1: Simple quiz game with two questions
def quiz_game():
    # Dictionary for questions and their answers
    questions = {
        "How was Columbus ship called 1492?": "Santa Maria",
        "What is 2 + 2?": "4"
    }

    # Iterate the
    for question, correct_answer in questions.items():
        # Ask the user
        user_answer = input(question + " ")

        # Check if the user's answer is correct
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

# Run 
quiz_game()
