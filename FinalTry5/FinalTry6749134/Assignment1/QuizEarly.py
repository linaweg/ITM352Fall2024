###quiz version before inserting my requirements 

def get_answer():
    return input("Enter the letter of the right answer: ").strip().upper()
# Function for quiz questions and the different quiz questions 
def quiz_questions():
    return {
        "How was Columbus' ship called in 1492?": {
            "options": {"A": "Santa Maria", "B": "Santa Nina", "C": "Santa Pinta"},
            "correct": "A"
        },
        "What is 2 + 2?": {
            "options": {"A": "3", "B": "4", "C": "5"},
            "correct": "B"
        },
        "What is the capital of Florida?": {
            "options": {"A": "Miami", "B": "Tallahassee", "C": "Orlando"},
            "correct": "B"
        },
        "Who wrote 'Romeo and Juliet'?": {
            "options": {"A": "Shakespeare", "B": "Hemingway", "C": "Goethe"},
            "correct": "A"
        },
        "What is the primary language spoken in Brazil?": {
            "options": {"A": "Spanish", "B": "Barzilian", "C": "Portuguese"},
            "correct": "C"
        },
        "You’re in a race and you pass the third place runner, what place are you in now?": {
            "options": {"A": "Second", "B": "First", "C": "Third"},
            "correct": "C"
        }

    }



# function to shuffle a list
def list_shuffle(lst):
    for i in range(len(lst)-1, 0, -1):
        # Generate a "random" index based on the sum of ASCII values in the list's string representations
        swap_index = sum([ord(char) for char in str(lst[i])]) % (i + 1)
        lst[i], lst[swap_index] = lst[swap_index], lst[i]
    return lst

# Function to randomize order of questions
def randomize_questions(questions):
    question_list = list(questions.items())
    return list_shuffle(question_list)

# Function to randomize the answer options for each question
#def randomize_options(options):
    #options_list = list(options.items())
    #return list_shuffle(options_list)



# Function to display the question and its options
def ask_question(question, options):
    print("\n" + question)  # Display the question
    for label, option in options.items():  # Display the answer options (use .items())
        print(f"{label}) {option}")

# quiz game function
def quiz_game():
    # Get the questions
    questions = quiz_questions()

    # Randomize order of the questions
    question_list = randomize_questions(questions)

    # Initialize score
    correct_answers = 0

    # Iterate through the randomized questions
    for question, details in question_list:
        correct = False  # Flag to track if the user has answered correctly

        # Use the options for the current question
        options = details["options"]

        # Loop until the user provides the correct answer
        while not correct:
            # Display the question and options
            ask_question(question, options)

        # Get the user's answer
            user_answer = get_answer()

            # Check if the answer is correct
            if check_answer(user_answer, details["correct"]):
                print("Correct!\n")
                correct_answers += 1  # Increment score
                correct = True  # Break the loop once the correct answer is given
            else:
                print(f"Your answer is wrong! Please try again.\n")



    # Final score summary
    print(f"Quiz finished! You got {correct_answers} out of {len(questions)} correct.")

# Function that checks if the answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Run the quiz game
quiz_game()

