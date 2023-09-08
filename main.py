import ask_question_to_pdf
from flask import Flask
from flask import request
from flask import render_template
from flask import send_file

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
    a = request.form["prompt"]
    message["answer"] = ask_question_to_pdf.ask_question_to_pdf(a)
    return message


@app.route("/question", methods=["GET"])
def quest():
    message = {}
    message["answer"] = ask_question_to_pdf.chat_ask_question()
    return message


@app.route("/simplequestion", methods=["GET"])
def questsimple():
    message = {}
    message["answer"] = ask_question_to_pdf.chat_ask_question_simple()
    return message


@app.route("/answer", methods=["POST"])
def ans():
    message = {}
    message["answer"] = ask_question_to_pdf.verif_reponse(
        request.form["prompt"], request.form["question"]
    )
    return message


@app.route("/pdf")
def pdf():
    path = "C:/Users/maxim/Desktop/hackaton_6D/filename.pdf"
    return send_file(path, as_attachment=True)


# @app.route("/txt")
# def txt():
#     path = "C:/Users/maxim/Desktop/hackaton_6D/livre.txt"
#     return send_file(path, as_attachment=True)


if __name__ == "_main_":
    app.run()
