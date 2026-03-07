import joblib
import numpy as np

model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")


def predict_grade(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    grade = encoder.inverse_transform(prediction)
    return grade[0]