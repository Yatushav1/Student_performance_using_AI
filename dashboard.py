from flask import Blueprint, render_template, request, session, redirect, url_for

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@dashboard_bp.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect(url_for("login"))

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_score = float(request.form["previous_score"])

    prediction = (study_hours * 5 + attendance * 0.3 + previous_score * 0.5)
    prediction = round(prediction, 2)

    return render_template("dashboard.html", prediction=prediction)