# this is a todo list taker application using session
from flask import Flask, request, render_template, session, redirect
from flask_session import Session

# configure the application..
app = Flask(__name__)

# configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():

    if session.get("todo") is None:
        session["todo"] = []

    if request.method == "POST":

        todo = request.form.get("todo")
        session["todo"].append(todo)

    return render_template("index.html", todo_list = session["todo"])
