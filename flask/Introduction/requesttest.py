from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    print(name)
    if name == "Sudhir":
        return "Hello %s" % name
    else:
        return "Pass in the name"

