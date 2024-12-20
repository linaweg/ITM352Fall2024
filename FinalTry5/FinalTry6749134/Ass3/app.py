from flask import Flask, render_template, request, jsonify, session
import json
import os
from flask_session import Session


app = Flask(__name__)

# Set a strong secret key for session security
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Load quiz questions from a JSON file (adjust path as needed)
def load_quiz_questions():
    with open('quiz_questions.json', 'r') as f:  # Replace 'quiz_questions.json' with your actual file name
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def start_quiz():
    questions = load_quiz_questions()
    session['questions'] = questions
    session['current_question'] = 0
    session.permanent = True  # Make session persistent (optional, for production)
    session['score'] = 0

    first_question = list(questions.keys())[0]
    return render_template('quiz.html', question=first_question, options=questions[first_question]['options'])

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    user_answer = request.json['answer']
    current_question = session['current_question']
    questions = session['questions']

    correct_answer = questions[list(questions.keys())[current_question]]['correct']
    if user_answer == correct_answer:
        session['score'] += 1

    session['current_question'] += 1

    if session['current_question'] >= len(questions):
        return jsonify({'finished': True, 'score': session['score']})

    next_question = list(questions.keys())[session['current_question']]
    return jsonify({
        'finished': False,
        'question': next_question,
        'options': questions[next_question]['options']
    })

if __name__ == '__main__':
    app.run(debug=True)
