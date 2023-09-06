from flask import Flask

app = Flask(__name__)
import ask_question_to_pdf


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


from flask import render_template


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=name)


from flask import request


@app.route("/prompt", methods=["POST"])
def prompt():
    message = {}
    message["answer"] = ask_question_to_pdf.ask_question_to_pdf(request.form["prompt"])
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
