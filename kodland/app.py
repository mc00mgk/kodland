from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, username, score):
        self.username = username
        self.score = score

@app.route("/")
def quiz():
    return render_template("quiz.html")

@app.route("/result", methods=["POST"])
def result():
    
    username = request.form.get("username")
    user_answers = {
        "q1": request.form.get("q1"),
        "q2": request.form.get("q2"),
        "q3": request.form.get("q3"),
        "q4": request.form.get("q4"),
    }

    correct_answers = {"q1": "1", "q2": "2", "q3": "3", "q4": "1"}
    score = sum(
        1 for q, ans in user_answers.items() if ans == correct_answers[q]
    ) * 5

    new_score = UserScore(username=username, score=score)
    db.session.add(new_score)
    db.session.commit()

    
    all_scores = UserScore.query.filter_by(username=username).all()
    return render_template("result.html", username=username, score=score, all_scores=all_scores)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
