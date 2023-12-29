from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route("/flaskapp/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

@app.route("/about")
def about():
    return "About MT"