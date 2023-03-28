from flask import Flask, url_for, render_template, abort, redirect
from markupsafe import escape


app = Flask(__name__)


# route binds function to URL's
# render_template look for html files inside templates directory
@app.route("/<name>")
def welcome(name):
    # return "<h2>Welcome to the Script!!</h2>"
    return render_template("hello.html", name=name)


"""Variable will be placed between <> and need to be escaped before returning.
/ after the user_name will be redirected to the below url even if called with 
without slash at the end."""


# @app.route("/<user_name>/")
# def welcome_user(user_name):
#     return f"<h1>Welcome to your first Flask API {escape(user_name)}</h1>"


# Variable can be used with converter to mention its type
@app.route("/<int:post_id>")
def return_int_variable(post_id):
    return f"<h3>Interger Id = {escape(post_id)}</h3>"


# post decorator can be used to specify HTTP Methods
# use abort with status codes to abort the process
@app.route("/loginPost")
def login():
    # return f"<h1>Login Successful - POST</h1>"
    # abort(403)
    # redirect redirects the request to mentioned method name
    return redirect(url_for('login_get'))


@app.route("/loginGet", methods=['GET', 'POST'])
def login_get():
    return "<h1>Login HTTP GET Method</h1>"


# CSS and JS files will be placed under static files

# use url_for to bind functions to urls's as its easy to maintain than hard coding teh URL's
with app.test_request_context():
    print(url_for("welcome", name='h'))
    # print(url_for("welcome_user", user_name='Shashikiran N'))
    print(url_for("return_int_variable", post_id=99))
