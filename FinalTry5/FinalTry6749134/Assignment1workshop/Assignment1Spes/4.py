# Step 4: Simple quiz game allowing the user to select the answer by its label
def quiz_game():
    # Dictionary of questions, answer options, and correct answer labels
    questions = {
        "How was Columbus' ship called in 1492?": {
            "options": {"A": "Santa Maria", "B": "Santa Nina", "C": "Santa Pinta"},
            "correct": "A"
        },
        "What is 2 + 2?": {
            "options": {"A": "3", "B": "4", "C": "5"},
            "correct": "B"
        }
    }

    # Iterate through questions
    for question, details in questions.items():
        # Display tquestion 
        print(question)
        
        # Display the answer options
        for label, option in details["options"].items():
            print(f"{label}) {option}")
        
        # Ask for user's answer by label
        user_answer = input("Enter the letter of your choice: ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == details["correct"]:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {details['correct']} ({details['options'][details['correct']]})")

# Run 
quiz_game()
