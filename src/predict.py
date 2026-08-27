"""Simple command-line prediction utility."""
from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "best_model.joblib"

FEATURES = [
    "age", "sex", "total_cholesterol", "ldl", "hdl",
    "systolic_bp", "diastolic_bp", "smoking", "diabetes"
]


def predict(values):
    model = joblib.load(MODEL_PATH)
    row = pd.DataFrame([values], columns=FEATURES)
    probability = float(model.predict_proba(row)[0, 1])
    prediction = int(probability >= 0.5)
    return prediction, probability


if __name__ == "__main__":
    print("Enter patient values in this order:")
    print(", ".join(FEATURES))
    raw = input("> ")
    values = [float(x.strip()) for x in raw.split(",")]
    if len(values) != len(FEATURES):
        raise ValueError(f"Expected {len(FEATURES)} values.")
    prediction, probability = predict(values)
    print(f"Predicted class: {prediction}")
    print(f"Estimated probability: {probability:.2%}")
    print("Note: This is an educational ML project, not a medical diagnosis.")
