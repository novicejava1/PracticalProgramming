from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    user_input = '<script>alert("Hello, world!");</script>'
    escaped_input = escape(user_input)
    return "<h1>Hello, %s</h1>" % escaped_input    