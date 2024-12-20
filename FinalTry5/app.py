from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

###getting flask started 
app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'

#getting the questions 
def load_questions():
    try:
        with open('questions.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        return []

questions = load_questions()

###posdcast and book recommendations 
podcasts = {
    "Societal": "Reclaiming the Future",
    "Relational": "The Relationship Blueprint",
    "Professional": "Level Up: Career Conversations",
    "Personal": "The Inner Compass"
}

books = {
    "Societal": '"The Art of Gathering: How We Meet and Why It Matters" by Priya Parker',
    "Relational": '"Attached: The New Science of Adult Attachment and How It Can Help You Find—and Keep—Love" by Amir Levine and Rachel Heller',
    "Professional": '"So Good They Can\'t Ignore You: Why Skills Trump Passion in the Quest for Work You Love" by Cal Newport',
    "Personal": '"Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones" by James Clear'
}

static_dir = os.path.join('static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

@app.route('/')
def home():
    session['current_question'] = 0
    session['scores'] = {"Personal": 0, "Professional": 0, "Relational": 0, "Societal": 0}
    return render_template('home.html')  # Adjust based on your home.html

##starting the quiz with 0 and adding scores depending on which area 
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'current_question' not in session:
        session['current_question'] = 0

    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice is not None:
            current_question_index = session['current_question']
            question = questions[current_question_index]
            area = question.get('area')
            scores = question.get('scores')

            
            if scores and area in session['scores']:
                session['scores'][area] += scores[int(choice)]

        session['current_question'] += 1

    if session['current_question'] >= len(questions):
        return redirect(url_for('recommendation'))

    question = questions[session['current_question']]
    return render_template('quiz.html', question=question, question_number=session['current_question'] + 1)

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    scores = session.get('scores', {})

    if not scores:
        return redirect(url_for('home'))

    ###finding outt the top area 
    top_area = max(scores, key=scores.get) if scores else "None"
    
    
    recommendation_choice = request.args.get('choice', '')

    ###recommendation variable 
    recommendation = "Please select a valid option."

    if recommendation_choice == 'podcast':
        recommendation = podcasts.get(top_area, "Explore podcasts that suit your needs.")
    elif recommendation_choice == 'book':
        recommendation = books.get(top_area, "Explore books that suit your needs.")
    elif recommendation_choice == 'talking':
        if top_area == "Societal":
            recommendation = "It might help you to talk about your ideas and perspectives of society with someone."
        elif top_area == "Relational":
            recommendation = "It might help you to talk about your relations with someone."
        elif top_area == "Professional":
            recommendation = "It might help you to talk about your ideas, goals, and perspectives about your career with someone."
        elif top_area == "Personal":
            recommendation = "It might help you to talk about your ideas, problems, and perspectives of your personal life with someone."

    return render_template('results.html', top_area=top_area, recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
