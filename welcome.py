from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h2>Welcome to the Script!!</h2>"
