<div align="center">

🫀 CardioAI — Heart Attack Risk Prediction System

AI-Powered Cardiovascular Risk Intelligence

<p>
  <strong>A modern Machine Learning + Data Science + Software Engineering project</strong><br>
  that analyzes cardiovascular health indicators and provides an interactive,
  educational heart-attack risk prediction through a Streamlit web application.
</p>

<p>
  <a href="https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-CardioAI-ff4b4b?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-1.61.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=flat-square&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Joblib-Model%20Persistence-2C3E50?style=flat-square">
</p>

</div>

🔗 Project Links

Resource

Link

🚀 Live Demo

Open CardioAI Application

💻 GitHub Repository

CardioAI-Heart-Attack-Risk-Prediction-System

📥 Clone Repository

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git

📌 Overview

CardioAI is an end-to-end machine-learning application developed to demonstrate how data science, predictive modelling, and software engineering can be combined into a practical web-based system.

The application accepts selected cardiovascular health indicators, processes the input through a trained classification model, and presents a risk prediction together with probability-oriented insights.

⚠️ Important: CardioAI is an educational machine-learning demonstration. It is not a medical diagnostic tool and must not be used to make medical decisions.

✨ Key Features

🫀 Interactive heart-attack risk prediction interface

🤖 Trained machine-learning classification model

📊 Model evaluation and comparison

📈 Accuracy, precision, recall, F1-score and ROC-AUC evaluation

🔍 Probability-based prediction insight

🎨 Modern responsive Streamlit interface

🧪 Automated project tests

📁 Organized data, model, source-code and results structure

🚀 Public Streamlit deployment

📚 Clear documentation for reproducibility

🧠 Machine Learning Pipeline

                    ┌──────────────────────┐
                    │   Heart Attack Data  │
                    │       Dataset        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Preparation   │
                    │  Cleaning / Encoding │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Train & Evaluate     │
                    │ Multiple ML Models   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Model Comparison   │
                    │ Accuracy / ROC-AUC   │
                    │ Recall / F1 / etc.   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Best Model        │
                    │  Logistic Regression │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Saved .joblib      │
                    │       Model          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Web App    │
                    │     CardioAI         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Educational Risk     │
                    │     Prediction       │
                    └──────────────────────┘

📊 Model Performance

The project evaluates multiple classification algorithms and selects the model based on the project's validation results.

Model

Accuracy

Precision

Recall

F1 Score

ROC-AUC

🥇 Logistic Regression

84.5%

36.84%

66.67%

47.46%

86.19%

Decision Tree

81.5%

30.00%

57.14%

39.34%

69.29%

Random Forest

87.0%

33.33%

23.81%

27.78%

81.27%

XGBoost

89.5%

50.00%

19.05%

27.59%

80.13%

🏆 Selected Model

Logistic Regression

The project identifies Logistic Regression as the selected prediction model according to the project's model-selection output. Its validation ROC-AUC is 86.19%, with an accuracy of 84.5%.

Note: Accuracy alone should not be interpreted as clinical performance. The model metrics are presented for educational machine-learning evaluation.

📈 Evaluation Results

The repository contains visual and numerical evaluation outputs, including:

Model comparison results

Confusion matrices

Correlation heatmap

Class distribution visualization

Evaluation metrics in JSON format

These artifacts make the project easier to inspect, evaluate, and reproduce.

🖥️ Application

The CardioAI web interface provides a structured workflow:

1. Patient Information

Users enter the required health-related indicators.

2. Prediction

The trained model processes the supplied values.

3. Risk Insight

The application displays the model's prediction and supporting probability information.

4. Educational Interpretation

The result is presented as a machine-learning demonstration rather than a clinical diagnosis.

🏗️ Project Architecture

CardioAI-Heart-Attack-Risk-Prediction-System/
│
├── 📄 app.py
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 LICENSE
├── 📄 .gitignore
│
├── 📁 data/
│   └── 📄 heart_attack_dataset.csv
│
├── 📁 models/
│   └── 📦 best_model.joblib
│
├── 📁 src/
│   ├── 📄 __init__.py
│   ├── 📄 train.py
│   └── 📄 predict.py
│
├── 📁 results/
│   ├── 📄 metrics.json
│   ├── 📄 model_comparison.csv
│   ├── 🖼️ model_comparison.png
│   ├── 🖼️ correlation_heatmap.png
│   └── 🖼️ confusion_matrix_*.png
│
└── 📁 tests/
    └── 📄 test_project.py

🧩 Project Components

app.py

Main Streamlit application responsible for:

User interface

Input collection

Model loading

Prediction execution

Result presentation

src/train.py

Training pipeline responsible for:

Loading the dataset

Preparing data

Training classification models

Comparing model performance

Saving evaluation results

Saving the selected trained model

src/predict.py

Prediction-related functionality used to process inputs and generate model predictions.

models/

Contains the persisted trained model used by the application.

results/

Contains machine-learning evaluation artifacts and visualizations.

tests/

Contains automated tests for checking important project functionality.

🛠️ Technology Stack

Category

Technology

Programming Language

Python

Web Framework

Streamlit

Data Processing

Pandas, NumPy

Machine Learning

scikit-learn, XGBoost

Model Persistence

Joblib

Testing

Python testing tools

Visualization

Matplotlib / project visualization libraries

Version Control

Git & GitHub

Deployment

Streamlit Community Cloud

⚙️ Installation

1. Clone the repository

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git

2. Open the project

cd CardioAI-Heart-Attack-Risk-Prediction-System

3. Create a virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

▶️ Run the Application

If the trained model already exists:

streamlit run app.py

Then open the local URL shown in the terminal, normally:

http://localhost:8501

🧠 Train the Model

To reproduce the training pipeline:

python src/train.py

This generates/updates the project's model evaluation artifacts and trained model according to the implementation in src/train.py.

After training, run:

streamlit run app.py

🧪 Run Tests

Run the project's tests with:

pytest

If pytest is not installed:

pip install pytest

☁️ Deployment

CardioAI is deployed using Streamlit Community Cloud.

🌐 Live Application

🚀 Launch CardioAI Live Demo

The deployed application allows users to access the prediction interface directly through a web browser without running the project locally.

🔄 Software Engineering Workflow

This project follows a practical development workflow:

Requirement
    ↓
Data Collection
    ↓
Data Preparation
    ↓
Model Development
    ↓
Model Evaluation
    ↓
Model Selection
    ↓
Application Development
    ↓
Testing
    ↓
Version Control
    ↓
Deployment
    ↓
Maintenance / Improvement

The repository separates application code, source modules, data, trained models, evaluation results, and tests to keep the project maintainable and easier to understand.

📁 Repository Organization

The project uses a modular structure instead of placing everything inside a single Python file.

Folder / File

Purpose

app.py

Main user-facing application

data/

Dataset

models/

Trained model artifacts

src/

Training and prediction modules

results/

Evaluation outputs

tests/

Automated tests

requirements.txt

Python dependencies

README.md

Project documentation

LICENSE

Project license

.gitignore

Git exclusions

🔐 Reproducibility

To reproduce the project locally:

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git
cd CardioAI-Heart-Attack-Risk-Prediction-System
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/train.py
streamlit run app.py

🚀 Future Improvements

Potential future enhancements include:

🔹 Improved feature engineering

🔹 Hyperparameter optimization

🔹 Cross-validation and stronger model validation

🔹 Explainable AI / feature-importance visualizations

🔹 More detailed prediction analytics

🔹 Improved accessibility and responsive UI

🔹 Automated CI/CD testing

🔹 Model monitoring and versioning

🔹 More comprehensive test coverage

⚠️ Medical Disclaimer

CardioAI is strictly an educational and research-oriented machine-learning demonstration.

The predictions generated by this application:

are not medical diagnoses;

are not a substitute for a qualified healthcare professional;

should not be used to make treatment or emergency-care decisions;

may be inaccurate or affected by limitations in the dataset and model.

If you have concerns about heart-attack symptoms or cardiovascular health, seek appropriate medical care.

👩‍💻 Author

CardioAI — Heart Attack Risk Prediction System

Developed as a practical project combining:

Machine Learning • Data Science • Software Engineering • Web Application Development

<p align="center">
  <a href="https://github.com/cit-23-02-0104-creator">
    <img src="https://img.shields.io/badge/GitHub-cit--23--02--0104--creator-181717?style=for-the-badge&logo=github" alt="GitHub Profile">
  </a>
</p>

<div align="center">

🫀 CardioAI

Turning cardiovascular data into an educational machine-learning insight.

<br>

<a href="https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/">
  <strong>🚀 Open Live Demo</strong>
</a>
&nbsp;&nbsp;•&nbsp;&nbsp;
<a href="https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System">
  <strong>⭐ View on GitHub</strong>
</a>

<br><br>

⭐ If you find this project useful, consider giving the repository a star!

</div>
