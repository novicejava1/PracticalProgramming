from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Main Page </h1>"

@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}"