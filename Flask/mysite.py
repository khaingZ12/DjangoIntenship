from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/hello/<username>/")
def hello_world(username):
    return f"<p>Hello, World!</p>{username}"


@app.route("/home/")
def homepage():
    return render_template('blog.html', name="This is Student")

@app.route("/user/")
def userpage():
        return redirect("/home/")

@app.route("/blog/")
def blogpage():
        return f"This is blog page"

@app.route("/product/")
def productpage():
        return f"This is product page"


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


@app.route("/login/")
def login():
    return render_template('exampleform.html')

@app.route("/submit/", methods=["GET"])
def form_submit():
    usr = request.args.get('username')
    pas = request.args.get('password')
    print(usr)
    print(pas)
    return f"hello {usr} and password : {pas}"


if __name__ == '__main__':
    app.run()