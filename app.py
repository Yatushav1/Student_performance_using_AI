from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# MODEL LOAD

model = joblib.load("E:\STUDENT_PERFORMANCE\model.pkl")
encoder = joblib.load("E:\STUDENT_PERFORMANCE\encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    participation = float(request.form["participation"])
    score = float(request.form["score"])

    features = np.array([[study_hours, attendance, participation, score]])

    prediction = model.predict(features)

    grade = encoder.inverse_transform(prediction)

    return render_template("index.html", result=grade[0])


if __name__ == "__main__":
    app.run(debug=True)