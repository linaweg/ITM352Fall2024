import json

# Open the JSON file and read the content 
with open("./quiz_questions.json", "r") as quiz_data_file:
    quiz_data = json.load(quiz_data_file)  # Load the JSON data directly

# Print the entire quiz data
print(quiz_data)

# Print a specific question and its answer if it exists
question = "What is the airspeed of an unladen swallow in miles/hr"
if question in quiz_data:
    print(f"Question: {question}")
    print(f"Answer: {quiz_data[question]}")
else:
    print(f"The question '{question}' does not exist in the quiz data.")
