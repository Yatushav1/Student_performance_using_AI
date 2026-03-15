from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

# simple user storage
users = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():

    # generate captcha numbers
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    session["captcha"] = num1 + num2

    return render_template("login.html", num1=num1, num2=num2)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/do_register", methods=["POST"])
def do_register():

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    if email in users:
        return render_template("register.html", error="User already exists")

    users[email] = password

    return redirect(url_for("login"))


@app.route("/do_login", methods=["POST"])
def do_login():

    email = request.form["email"]
    password = request.form["password"]
    captcha = request.form["captcha"]

    if email not in users:
        return render_template("login.html", error="User not registered", num1=0, num2=0)

    if users[email] != password:
        return render_template("login.html", error="Incorrect password", num1=0, num2=0)

    # captcha validation
    if int(captcha) != session.get("captcha"):
        return render_template("login.html", error="Captcha incorrect", num1=0, num2=0)

    session["user"] = email

    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)