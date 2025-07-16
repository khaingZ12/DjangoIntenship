from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/hello/<username>/")
def hello_world(username):
    return f"<p>Hello, World!</p>{username}"


@app.route("/home/")
def homepage():
    return f"This is home page context"

@app.route("/user/")
def userpage():
        return redirect("/home/")
    

@app.route('/welcome/<user>/')
def welcome(user):
     if user == 'admin':
          return redirect(url_for('hello_admin'))
     else:
          return redirect(url_for('hello_guest'))

@app.route("/hello_admin/")
def hello_admin():
    return "Welcome Admin"

@app.route("/hello_guest/")
def hello_guest():
    return "Welcome hello_guest"


if __name__ == '__main__':
    app.run()