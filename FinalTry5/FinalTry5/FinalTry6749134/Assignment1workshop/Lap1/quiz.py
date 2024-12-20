#score = 0

#questions = ("What is the airspeed of an unladen swallow in miles/hr?", "What is the capital of Texas ?")
#answer = input(questions[0] + "?")
#answer = ("12", "Austin")
    #score = score +1

#for question_num in range (1, len(questions)):
    #answer = input (f{question_num})

#answer = input(questions[0] + "?")
#if answer == answer[0]:
    #score = score +1

#print(f"your score is {score})
      
#answer = input("What is the capital of Texas ?")
#if answer == "Austin":
    #score = score +1

# Initialize questions and answers
questions = ["What is 5 + 7", "What is the capital of Texas"]
answers = ["12", "Austin"]

# Initialize score
score = 0

# Ask the first question
answer = input(questions[0] + "? ")

# Check if the answer is correct
if answer == answers[0]:
    score += 1

# Ask the second question
answer = input(questions[1] + "? ")

# Check if the answer is correct
if answer == answers[1]:
    score += 1

# Print the final score
print(f"Your score is {score}")
