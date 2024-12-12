##import os and json
import os
import json  
print(f"Current working directory: {os.getcwd()}")

# Function to request answer from user
def get_answer():
    return input("Enter the letter of the right answer (or type 'HINT' for a hint): ").strip().upper()

# loading questions from the JSON file 
def load_quiz_questions():
    try:
        with open("quiz.questions.json", "r") as file:
            questions = json.load(file)  
        return questions
    except FileNotFoundError:
        print("Error: The quiz questions file was not found.")
        return {}

# in order to have the questions in a randomized order, randomized function 
def randomize_questions(questions):
    import random
    question_list = list(questions.items())  # convert into tulpes 
    random.shuffle(question_list)  # Shuffle the questions
    return question_list

# to display not only the questions but also the possible answers 
def ask_question(question, options):
    print("\n" + question)  # to display the question 
    for label, option in options.items():  # to display the answer options 
        print(f"{label}) {option}")

# function to have the score on a separate file 
def save_score_to_file(score, total_questions):
    try:
        with open("quiz_scores.txt", "a") as file:  # "a" means append mode
            file.write(f"Score: {score}/{total_questions}\n")  # Write the score to the file
        print("Score saved successfully.")
    except IOError:
        print("There was an error saving your score.")

# Function to make sure that the answer is correct 
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Main quiz game function
def quiz_game():
    # to load the questions from the external file
    questions = load_quiz_questions()

    if not questions:
        print("No quiz questions available!")
        return  # Exit if no questions were loaded

    # Randomize order of the questions
    question_list = randomize_questions(questions)

    # Initialize score, starting at 0 
    correct_answers = 0

    # Iterate through the randomized questions
    for question, details in question_list:
        correct = False  # Flag to track if the respondet has answered correctly

        # Use the options for the current question
        options = details["options"]

        # Loop until the user provides the correct answer
        while not correct:
            # Display the question and options
            ask_question(question, options)

            # Get the respondents answer
            user_answer = get_answer()

            # Check if user requested a hint
            if user_answer == "HINT":
                print(f"Hint: {details['hint']}")
                continue  # Show the hint and re-ask the question

            # Validate input
            if user_answer not in ['A', 'B', 'C', 'D']:
                print("Invalid input! Please choose A, B, or C.")
                continue  # Loop again to allow user to enter a valid option

            # Check if the answer is correct
            if check_answer(user_answer, details["correct"]):
                print("Correct!\n")
                correct_answers += 1  # Increment score
                correct = True  # Break the loop when the correct answer is given
            else:
                print(f"Your answer is wrong! Please try again.\n")

    # Final score summary
    print(f"Quiz finished! You got {correct_answers} out of {len(questions)} correct.")
    # Save the score to the external file
    save_score_to_file(correct_answers, len(questions))

# Run 
quiz_game()


 