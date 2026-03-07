# IMPORT LIBRARIES

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report


# LOAD DATASET
data = pd.read_csv("E:\STUDENT_PERFORMANCE\student_performance.csv")

print("Dataset shape:", data.shape)
print(data.head())

# DEFINE TARGET VARIABLE
data = data.drop("student_id", axis=1)
X = data.drop("grade", axis=1)
y = data["grade"]


# ENCODING
encoder = LabelEncoder()
y = encoder.fit_transform(y)


# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42
)


# ML MODEL
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# MODEL TRANING

model.fit(X_train, y_train)


# PREDICTION
pred = model.predict(X_test)


# EVALUATION MATRIX
acc = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average="weighted")

print("\nModel Performance")
print("-----------------")
print("Accuracy :", acc)
print("F1 Score :", f1)

print("\nClassification Report")
print(classification_report(y_test, pred))


# SAVE MODEL
joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("\nModel and encoder saved successfully!")