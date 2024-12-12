import random

# Step 6: Quiz game with randomized question and answer order
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
        },
        "What is the capital of France?": {
            "options": {"A": "Rome", "B": "Madrid", "C": "Paris"},
            "correct": "C"
        },
        "Who wrote 'Hamlet'?": {
            "options": {"A": "Shakespeare", "B": "Hemingway", "C": "Tolkien"},
            "correct": "A"
        }
    }

    # Convert dictionary keys into a list to randomize question order
    question_list = list(questions.items())
    random.shuffle(question_list)  # Shuffle the list of questions

    # Initialize score
    correct_answers = 0

    # Iterate through the randomized questions
    for question, details in question_list:
        correct = False  # Flag to track if the user has answered correctly

        # Randomize the order of answer options
        options = list(details["options"].items())
        random.shuffle(options)

        # Loop until the user provides the correct answer
        while not correct:
            # Display the question
            print("\n" + question)  # \n for spacing
            
            # Display the randomized answer options
            for label, option in options:
                print(f"{label}) {option}")
            
            # Ask for the user's answer by label
            user_answer = input("Enter the letter of your choice: ").strip().upper()

            # Check if the user's answer is correct
            if user_answer == details["correct"]:
                print("Correct!\n")
                correct_answers += 1  # Increment score
                correct = True  # Break the loop once the correct answer is given
            else:
                print(f"Wrong! Please try again.\n")

    # Final score summary
    print(f"Quiz finished! You got {correct_answers} out of {len(questions)} correct.")

# Run the quiz game
quiz_game()
