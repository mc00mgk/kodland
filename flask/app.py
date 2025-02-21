from flask import Flask, render_template, request

app = Flask(__name__)

# Soruların doğru cevapları ve her birinin puanı
correct_answers = {
    "q1": 5,  # Soru 1: Doğru cevap: "Diş sağlığı uzmanı"
    "q2": 5,  # Soru 2: Doğru cevap: "Sond"
    "q3": 5,  # Soru 3: Doğru cevap: "Dolgu"
    "q4": 5,  # Soru 4: Doğru cevap: "Dişler düzenli olarak fırçalanmalıdır."
}
max_score = sum(correct_answers.values())  # Maksimum toplam puan (örnek: 20)

@app.route('/')
def home():
    return render_template("quiz.html")

@app.route('/result', methods=['POST'])
def result():
    user_answers = request.form
    user_score = 0

    # Kullanıcının puanını hesapla
    for question, correct_value in correct_answers.items():
        if question in user_answers and int(user_answers[question]) == correct_value:
            user_score += correct_value

    # 100 üzerinden puan hesapla
    percentage_score = (user_score / max_score) * 100

    return render_template("result.html", score=percentage_score)

if __name__ == "__main__":
    app.run(debug=True)
