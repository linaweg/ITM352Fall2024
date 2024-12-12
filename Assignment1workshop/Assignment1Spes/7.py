import random

# Function to get the quiz questions with their options and correct answers
def get_questions():
    return {
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

# Function to randomize the order of questions
def randomize_questions(questions):
    question_list = list(questions.items())
    random.shuffle(question_list)
    return question_list

# Function to randomize the answer options for each question
def randomize_options(options):
    options_list = list(options.items())
    random.shuffle(options_list)
    return options_list

# Function to display the question and its options
def ask_question(question, options):
    print("\n" + question)  # Display the question
    for label, option in options:  # Display the randomized answer options
        print(f"{label}) {option}")

# Function to get the user's answer
def get_user_answer():
    return input("Enter the letter of your choice: ").strip().upper()

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Main quiz game function
def quiz_game():
    # Get the questions
    questions = get_questions()

    # Randomize the order of the questions
    question_list = randomize_questions(questions)

    # Initialize score
    correct_answers = 0

    # Iterate through the randomized questions
    for question, details in question_list:
        correct = False  # Flag to track if the user has answered correctly

        # Randomize the answer options for this question
        options = randomize_options(details["options"])

        # Loop until the user provides the correct answer
        while not correct:
            # Display the question and options
            ask_question(question, options)

            # Get the user's answer
            user_answer = get_user_answer()

            # Check if the user's answer is correct
            if check_answer(user_answer, details["correct"]):
                print("Correct!\n")
                correct_answers += 1  # Increment score
                correct = True  # Break the loop once the correct answer is given
            else:
                print(f"Wrong! Please try again.\n")

    # Final score summary
    print(f"Quiz finished! You got {correct_answers} out of {len(questions)} correct.")

# Run the quiz game
quiz_game()
