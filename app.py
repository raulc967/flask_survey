from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey

app = Flask(__name__)
app.secret_key = 'applepiewithicecream'

responses = []

@app.route("/")
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("home.html", title=title, instructions=instructions)

@app.route("/question/<num>")
def questions(num):
    if int(num) > len(satisfaction_survey.questions) - 1:
        return redirect("/thank_you")
    if int(num) != len(responses):
        return redirect(f"/question/{len(responses)}")
    question = satisfaction_survey.questions[int(num)].question
    return render_template("question.html", question=question)

@app.route("/answer", methods=['POST'])
def answer():
    if request.form['answer'] == 'true':
        answer = True
    else:
        answer = False
    responses.append(answer)
    return redirect(f"/question/{len(responses)}")

@app.route("/thank_you")
def thank_you():
    flash("You have already completed the survey")
    return render_template("thank_you.html", title=satisfaction_survey.title)