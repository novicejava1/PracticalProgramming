from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_login_form()

def do_the_login():
    return "Processing the Login credentials"

def show_login_form():
    return "Display Login Page"