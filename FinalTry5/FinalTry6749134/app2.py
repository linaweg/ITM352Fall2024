from flask import Flask, render_template, request, redirect, url_for, session
import json
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_questions():
    try:
        with open(os.path.join(os.getcwd(), 'questions.json'), 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        return []

questions = load_questions()

static_dir = os.path.join(app.root_path, "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

@app.route('/')
def home():
    session['current_question'] = 0
    session['scores'] = {"Personal": 0, "Professional": 0, "Relational": 0, "Societal": 0}
    return render_template('home.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'current_question' not in session:
        session['current_question'] = 0

    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice is not None:
            try:
                choice = int(choice)
                current_question_index = session['current_question']
                question = questions[current_question_index]
                area = question.get('area', "")
                scores = question.get('scores', [])

                # Update scores if applicable
                if scores and area in session['scores'] and 0 <= choice < len(scores):
                    session['scores'][area] += scores[choice]
            except (ValueError, IndexError):
                print("Invalid choice or question data.")

        session['current_question'] += 1

        
        if session['current_question'] >= len(questions):
            return redirect(url_for('results'))

    
    question = questions[session['current_question']]
    return render_template('quiz.html', question=question, question_number=session['current_question'] + 1)


@app.route('/results', methods=['GET'])
def results():
    scores = session.get('scores', {})
    if not scores:
        return redirect(url_for('home'))

    
    top_area = max(scores, key=scores.get, default="")

    
    chart_path = os.path.join(static_dir, "focus_area_chart.png")
    try:
        plt.figure(figsize=(6, 4))
        plt.bar(scores.keys(), scores.values(), color=['#FF5733', '#33C1FF', '#75FF33', '#FF33A6'])
        plt.title("Your Focus Areas")
        plt.xlabel("Areas")
        plt.ylabel("Points")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()
    except Exception as e:
        print(f"Error generating chart: {e}")
        return "Error while generating chart.", 500

    
    recommendations = {
        "Personal": "We recommend 'The Inner Compass' podcast for personal growth.",
        "Professional": "Check out 'Level Up: Career Conversations' podcast for career advancement.",
        "Relational": "Listen to 'The Relationship Blueprint' for improving relationships.",
        "Societal": "Try 'Reclaiming the Future' for societal empowerment resources."
    }
    recommendation = recommendations.get(top_area, "Explore resources that suit your needs.")

    return render_template(
        'results.html',
        scores=scores,
        top_area=top_area,
        chart=url_for('static', filename='focus_area_chart.png'),
        recommendation=recommendation
    )

if __name__ == '__main__':
    app.run(debug=True)



