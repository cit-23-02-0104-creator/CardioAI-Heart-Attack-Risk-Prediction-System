# ❤️ Heart Attack Risk Prediction using Machine Learning

A complete end-to-end **Data Science / Machine Learning** project that predicts the likelihood of a heart attack from demographic, cholesterol, blood-pressure, smoking, and diabetes features.

> **Important:** This is an educational machine-learning project. It is **not a medical diagnostic tool** and must not be used to make healthcare decisions.

## 🎯 Project Goals

- Load and validate a structured healthcare dataset.
- Explore distributions, class balance, and feature correlations.
- Handle missing values safely.
- Split data into stratified training and testing sets.
- Train and compare four classification algorithms.
- Evaluate models using accuracy, precision, recall, F1-score, and ROC-AUC.
- Save trained models and evaluation artifacts.
- Provide both a command-line prediction utility and a Streamlit web app.

## 🧠 Models

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost

Because the positive class is relatively small, the project uses class balancing where supported and reports **recall and ROC-AUC** in addition to accuracy.

## 📊 Dataset

The included CSV contains **1,000 records** and these columns:

| Feature | Meaning |
|---|---|
| `age` | Age |
| `sex` | Binary encoded sex |
| `total_cholesterol` | Total cholesterol |
| `ldl` | LDL cholesterol |
| `hdl` | HDL cholesterol |
| `systolic_bp` | Systolic blood pressure |
| `diastolic_bp` | Diastolic blood pressure |
| `smoking` | Smoking indicator |
| `diabetes` | Diabetes indicator |
| `heart_attack` | Target: 0 = no, 1 = yes |

The dataset contains 896 class-0 records and 104 class-1 records, so the target is imbalanced. For that reason, accuracy alone should not be treated as the main success criterion.

## 📁 Project Structure

```text
heart-attack-risk-prediction/
├── app.py
├── data/
│   └── heart_attack_risk.csv
├── models/
│   └── best_model.joblib          # generated after training
├── results/
│   ├── metrics.json               # generated after training
│   ├── model_comparison.csv       # generated after training
│   ├── model_comparison.png       # generated after training
│   ├── class_distribution.png     # generated after training
│   ├── correlation_heatmap.png    # generated after training
│   └── *_confusion_matrix.png     # generated after training
├── src/
│   ├── __init__.py
│   ├── train.py
│   └── predict.py
├── tests/
│   └── test_project.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/heart-attack-risk-prediction.git
cd heart-attack-risk-prediction
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Train the models

Run:

```bash
python src/train.py
```

This will:

- validate the dataset
- create exploratory plots
- train all four models
- calculate evaluation metrics
- save confusion matrices
- save trained `.joblib` models
- select the best model using ROC-AUC with F1 as the tie-breaker
- save `results/metrics.json`

## 🌐 Run the Web App

After training:

```bash
streamlit run app.py
```

A browser window will open with an interactive prediction form.

## 🖥️ Command-Line Prediction

After training:

```bash
python src/predict.py
```

Enter values in this order:

```text
age, sex, total_cholesterol, ldl, hdl, systolic_bp, diastolic_bp, smoking, diabetes
```

Example:

```text
55, 1, 220, 140, 45, 135, 85, 0, 0
```

## 📈 Evaluation

The project reports:

- **Accuracy** — overall correct predictions.
- **Precision** — how many predicted positive cases were actually positive.
- **Recall** — how many actual positive cases were detected.
- **F1-score** — balance between precision and recall.
- **ROC-AUC** — ranking/discrimination performance across thresholds.

For a medical-risk classification demonstration, recall and ROC-AUC are especially important because a high accuracy can be misleading when the positive class is uncommon.

## 🧪 Testing

Run:

```bash
python -m unittest discover -s tests
```

or, if pytest is installed:

```bash
pytest
```

## 🔐 Reproducibility

The train/test split uses:

- Test size: 20%
- Random state: 42
- Stratified target split

## 📌 Limitations

- The dataset is small and imbalanced.
- Model performance depends entirely on the supplied dataset.
- The features are limited and do not represent a complete clinical assessment.
- Probability outputs are model estimates, not medically calibrated risk scores.
- No external clinical validation is performed.

## 👩‍💻 Author

**Jayani Samarakoon**

Built as an academic Data Science / Machine Learning project.

## 📄 License

MIT License.
