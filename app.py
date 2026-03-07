from flask import Flask, render_template, request, redirect, url_for, session
from database.db import db
from auth.auth import auth
from predict import predict_grade

app = Flask(__name__)

app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db.init_app(app)

app.register_blueprint(auth)


@app.route("/")
def home():
    return redirect(url_for("auth.login"))


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    participation = float(request.form["participation"])
    score = float(request.form["score"])

    features = [study_hours, attendance, participation, score]

    grade = predict_grade(features)

    return render_template("index.html", result=grade)


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("auth.login"))


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)