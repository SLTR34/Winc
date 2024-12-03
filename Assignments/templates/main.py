from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)

@app.route("/")
def index():
    return "This is an empty Flask project that you need to work on."

@app.route("/home")
def home():
    return render_template("index.html",title="index")

@app.route("/about")
def about():
    return render_template("about.html",title="About me")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="My Projects")