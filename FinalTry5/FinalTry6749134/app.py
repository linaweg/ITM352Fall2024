from flask import Flask, render_template, request, redirect, url_for, session
import json
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_questions():
    try:
        with open('/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/questions.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        return []

questions = load_questions()


if not os.path.exists("/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/static"):
    os.makedirs("/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/static")


@app.route('/')
def home():
    session['current_question'] = 0
    session['scores'] = {"Personal": 0, "Professional": 0, "Relational": 0, "Societal": 0}
    
    return render_template('/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/templates/home.html')


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
                session['scores'][area] += scores[int(choice)]  # Map choice index to score

        session['current_question'] += 1  # Move to the next question

    
    if session['current_question'] >= len(questions):
        # Full path for results.html redirection
        return redirect('/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/templates/results.html')

    
    question = questions[session['current_question']]
    # Full path for quiz.html
    return render_template('/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/templates/quiz.html', question=question, question_number=session['current_question'] + 1)

@app.route('/results')
def results():
    scores = session.get('scores', {})
    if not scores:
        print("No scores found, redirecting to home.")
        return redirect(url_for('home'))  # Redirect to home if no scores are found.

    print("Debug: Scores -", scores)  # Ensure scores are printed for debugging

    # Check if session data exists
    top_area = max(scores, key=scores.get) if scores else "None"

    try:
        
        chart_path = os.path.join(app.root_path, "static", "focus_area_chart.png")
        print("Debug: Saving chart to ->", chart_path)

        plt.figure(figsize=(6, 4))
        plt.bar(scores.keys(), scores.values(), color=['#FF5733', '#33C1FF', '#75FF33', '#FF33A6'])
        plt.title("Your Focus Areas")
        plt.xlabel("Areas")
        plt.ylabel("Points")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

        if not os.path.exists(chart_path):
            print("Error: Chart file not created.")
            return "Error: Chart could not be generated.", 500
    except Exception as e:
        print("Error while generating chart:", e)
        return "Error while generating chart.", 500


    recommendations = {
        "Personal": "We recommend 'The Inner Compass' podcast for personal growth.",
        "Professional": "Check out 'Level Up: Career Conversations' podcast for career advancement.",
        "Relational": "Listen to 'The Relationship Blueprint' for improving relationships.",
        "Societal": "Try 'Reclaiming the Future' for societal empowerment resources."
    }
    recommendation = recommendations.get(top_area, "Explore resources that suit your needs.")

    print("Debug: Top Area -", top_area)
    print("Debug: Recommendation -", recommendation)

    
    return render_template(
        '/Users/linawegert/Documents/GitHub/Lab5.Dic/.venv/FinalTry4/templates/results.html',
        scores=scores,
        top_area=top_area,
        chart=url_for('static', filename='focus_area_chart.png'),
        recommendation=recommendation
    )

if __name__ == '__main__':
    app.run(debug=True)


