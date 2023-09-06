import ask_question_to_pdf
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello/")
def hello(name=None):
    return render_template("index.html", name=name)


@app.route("/prompt", methods=["POST"])
def prompt():
    message = {}
    message["answer"] = ask_question_to_pdf.ask_question_to_pdf(
        request.form["prompt"]
    )
    return message


@app.route("/question", methods=["GET"])
def quest():
    message = {}
    message["answer"] = ask_question_to_pdf.chat_ask_question()
    return message


@app.route("/answer", methods=["POST"])
def ans():
    message = {}
    message["answer"] = ask_question_to_pdf.verif_reponse(
        request.form["prompt"], request.form["question"]
    )
    return message
