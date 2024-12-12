# Step 3: Simple quiz game with answer options and correct choice
def quiz_game():
    # Dictionary of questions, answer options, and correct answer
    questions = {
        "How was Columbus' ship called in 1492?": {
            "options": ["A) Santa Maria", "B) Santa Nina", "C) Santa Pinta"],
            "correct": "A"
        },
        "What is 2 + 2?": {
            "options": ["A) 3", "B) 4", "C) 5"],
            "correct": "B"
        }
    }

    # Iterate through the questions
    for question, details in questions.items():
        # Display the question
        print(question)
        
        # Display the answer options
        for option in details["options"]:
            print(option)
        
        # Ask for the user's answer
        user_answer = input("Enter the letter of your choice: ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == details["correct"]:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {details['correct']}")

# Run 
