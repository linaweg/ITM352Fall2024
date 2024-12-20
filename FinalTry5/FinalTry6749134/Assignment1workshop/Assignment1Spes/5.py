# Step 5: Improved quiz game with better usability and correct answer tracking
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

    # Initialize score
    correct_answers = 0

    # Iterate through 
    for question, details in questions.items():
        correct = False  

        # Loop until the user provides the correct answer
        while not correct:
            # Display 
            print("\n" + question)  # \n for spacing
            
            # Display answer options 
            for label, option in details["options"].items():
                print(f"{label}) {option}")
            
            # Ask for the user's answer by label
            user_answer = input("Enter the letter of your choice: ").strip().upper()

            # Check if the user's answer is correct
            if user_answer == details["correct"]:
                print("Correct!\n")
                correct_answers += 1  
                correct = True  
            else:
                print(f"Wrong! Please try again.\n")

    # Final score summary
    print(f"Quiz finished! You got {correct_answers} out of {len(questions)} correct.")

# Run 
quiz_game()
