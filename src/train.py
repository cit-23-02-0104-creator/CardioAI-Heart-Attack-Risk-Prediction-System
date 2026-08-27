"""Train and evaluate heart-attack risk classification models."""
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report,
)
from xgboost import XGBClassifier

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "heart_attack_risk.csv"
MODEL_DIR = ROOT / "models"
RESULTS_DIR = ROOT / "results"
RANDOM_STATE = 42
TARGET = "heart_attack"

FEATURES = [
    "age", "sex", "total_cholesterol", "ldl", "hdl",
    "systolic_bp", "diastolic_bp", "smoking", "diabetes"
]


def load_data():
    df = pd.read_csv(DATA_PATH)
    required = FEATURES + [TARGET]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    if df[required].isnull().any().any():
        df[required] = df[required].fillna(df[required].median(numeric_only=True))
    return df


def build_models():
    return {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(
                max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE
            )),
        ]),
        "Decision Tree": DecisionTreeClassifier(
            max_depth=5, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, max_depth=8, class_weight="balanced",
            random_state=RANDOM_STATE, n_jobs=-1
        ),
        "XGBoost": XGBClassifier(
            n_estimators=300, max_depth=4, learning_rate=0.05,
            subsample=0.9, colsample_bytree=0.9, eval_metric="logloss",
            random_state=RANDOM_STATE, n_jobs=2
        ),
    }


def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)
    probability = model.predict_proba(X_test)[:, 1]
    return {
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probability),
        "pred": pred,
    }


def plot_class_distribution(df):
    plt.figure(figsize=(7, 5))
    df[TARGET].value_counts().sort_index().plot(kind="bar")
    plt.title("Heart Attack Class Distribution")
    plt.xlabel("Heart Attack (0 = No, 1 = Yes)")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "class_distribution.png", dpi=160)
    plt.close()


def plot_correlation(df):
    plt.figure(figsize=(10, 7))
    sns.heatmap(df[FEATURES + [TARGET]].corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "correlation_heatmap.png", dpi=160)
    plt.close()


def plot_model_comparison(results):
    metric_df = pd.DataFrame(results).T[["accuracy", "precision", "recall", "f1", "roc_auc"]]
    metric_df.to_csv(RESULTS_DIR / "model_comparison.csv")
    ax = metric_df.plot(kind="bar", figsize=(11, 6))
    ax.set_ylim(0, 1)
    ax.set_ylabel("Score")
    ax.set_title("Model Performance Comparison")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "model_comparison.png", dpi=160)
    plt.close()


def main():
    MODEL_DIR.mkdir(exist_ok=True)
    RESULTS_DIR.mkdir(exist_ok=True)

    df = load_data()
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=RANDOM_STATE, stratify=y
    )

    plot_class_distribution(df)
    plot_correlation(df)

    results = {}
    trained = {}
    for name, model in build_models().items():
        model.fit(X_train, y_train)
        evaluation = evaluate_model(model, X_test, y_test)
        results[name] = {k: float(v) for k, v in evaluation.items() if k != "pred"}
        trained[name] = model

        safe_name = name.lower().replace(" ", "_")
        joblib.dump(model, MODEL_DIR / f"{safe_name}.joblib")

        report = classification_report(
            y_test, evaluation["pred"], target_names=["No Risk", "Risk"], zero_division=0
        )
        (RESULTS_DIR / f"{safe_name}_classification_report.txt").write_text(report)

        cm = confusion_matrix(y_test, evaluation["pred"])
        plt.figure(figsize=(5, 4))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                    xticklabels=["No Risk", "Risk"],
                    yticklabels=["No Risk", "Risk"])
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title(f"{name} - Confusion Matrix")
        plt.tight_layout()
        plt.savefig(RESULTS_DIR / f"{safe_name}_confusion_matrix.png", dpi=160)
        plt.close()

    plot_model_comparison(results)

    # Select the model using ROC-AUC, with F1 as a secondary criterion.
    best_name = max(results, key=lambda n: (results[n]["roc_auc"], results[n]["f1"]))
    joblib.dump(trained[best_name], MODEL_DIR / "best_model.joblib")

    metadata = {
        "best_model": best_name,
        "features": FEATURES,
        "target": TARGET,
        "random_state": RANDOM_STATE,
        "test_size": 0.20,
        "dataset_rows": int(len(df)),
        "class_distribution": {str(k): int(v) for k, v in y.value_counts().sort_index().items()},
        "metrics": results,
    }
    (RESULTS_DIR / "metrics.json").write_text(json.dumps(metadata, indent=2))

    print(f"Dataset: {len(df)} rows, {len(FEATURES)} features")
    print(f"Best model: {best_name}")
    print(pd.DataFrame(results).T.round(4))


if __name__ == "__main__":
    main()
