<div align="center">

🫀 CardioAI

Heart Attack Risk Prediction System

AI-Powered Cardiovascular Risk Prediction using Machine Learning




An end-to-end educational Machine Learning + Data Science + Software Engineering project.

</div>

🚀 Live Demo

👉 Open CardioAI — Live Application

Try the deployed application directly in your browser.

GitHub Repository:
CardioAI-Heart-Attack-Risk-Prediction-System

📌 Project Overview

CardioAI is a machine-learning-based web application that demonstrates how cardiovascular health indicators can be used to build a predictive classification system.

The project combines

🧠 Machine Learning

📊 Data Science

💻 Software Engineering

🧪 Software Testing

🌐 Web Application Development

🚀 Cloud Deployment

📚 Technical Documentation

🔄 End-to-End Workflow

Raw Dataset
     ↓
Data Preparation
     ↓
Exploratory Data Analysis
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Comparison
     ↓
Best Model Selection
     ↓
Model Persistence
     ↓
Streamlit Web Application
     ↓
Risk Prediction

🎯 Project Objectives

Develop a machine-learning classification system for cardiovascular risk prediction.

Analyze health-related data using data-science techniques.

Compare multiple classification algorithms.

Evaluate models using appropriate classification metrics.

Select a suitable model for the prediction application.

Build an interactive web application using Streamlit.

Separate training, prediction, application, and testing components.

Apply software-engineering principles throughout development.

Implement automated testing.

Deploy the application as a public web application.

Provide clear and reproducible technical documentation.

⭐ Key Features

Feature

Description

🫀 Risk Prediction

Accepts health-related inputs and generates an ML prediction

🤖 Multiple Models

Logistic Regression, Decision Tree, Random Forest and XGBoost

📊 Model Evaluation

Accuracy, Precision, Recall, F1-Score and ROC-AUC

🌐 Web Interface

Interactive browser-based UI built with Streamlit

🧪 Automated Testing

Project tests included under tests/

📦 Model Persistence

Trained model saved with Joblib

🚀 Cloud Deployment

Public deployment through Streamlit Community Cloud

📚 Documentation

Complete setup, architecture and usage documentation

🏗️ Software Engineering

CardioAI is not only an ML experiment. It demonstrates the development of a complete software system around a trained model.

Requirements Engineering

The project considers:

User input requirements

Prediction requirements

Machine-learning requirements

Application requirements

Testing requirements

Deployment requirements

Documentation requirements

🧩 System Architecture

┌──────────────────────────────┐
│          User / UI           │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       Streamlit App          │
│           app.py             │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      Input Validation        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      Prediction Module       │
│       src/predict.py         │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       Trained ML Model       │
│     best_model.joblib        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       Prediction Result      │
└──────────────────────────────┘

🛠️ Software Engineering Practices

Modular architecture

Separation of concerns

Reusable components

Model persistence

Input validation

Automated testing

Git/GitHub version control

Technical documentation

Cloud deployment

🧠 Machine Learning

CardioAI follows a supervised classification workflow.

🤖 Models Compared

Model

Description

Logistic Regression

Linear classification model

Decision Tree

Tree-based classification model

Random Forest

Ensemble tree-based model

XGBoost

Gradient-boosting classification model

🔬 Machine Learning Pipeline

Dataset
   ↓
Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Model Selection
   ↓
Model Persistence
   ↓
Web Application

📊 Model Performance

Current evaluation results:

Model

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Logistic Regression ⭐

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

Current Application Model

Logistic Regression is used by the deployed application.

The project considers multiple evaluation metrics rather than accuracy alone. The current Logistic Regression evaluation provides the strongest ROC-AUC and higher recall among the evaluated alternatives.

Important: These results depend on the dataset, preprocessing, train/test split and evaluation methodology. They are not clinical performance claims.

📁 Project Structure

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
│   └── 🖼️ confusion matrices
│
└── 📁 tests/
    └── 📄 test_project.py

📂 Component Description

Component

Purpose

app.py

Main Streamlit web application

src/train.py

Model training and evaluation pipeline

src/predict.py

Prediction-related functionality

models/

Stored trained ML model

data/

Project dataset

results/

Metrics and evaluation visualizations

tests/

Automated project tests

requirements.txt

Python dependencies

README.md

Project documentation

LICENSE

Project license

.gitignore

Git-excluded files

🛠️ Technology Stack

Technology

Purpose

Python

Core programming language

Pandas

Data manipulation

NumPy

Numerical computing

Scikit-learn

Machine-learning algorithms

XGBoost

Gradient boosting

Joblib

Model persistence

Matplotlib

Data visualization

Seaborn

Statistical visualization

Streamlit

Web application

Pytest

Automated testing

Git

Version control

GitHub

Source-code hosting

Streamlit Community Cloud

Deployment

📚 Official Documentation

Python

Pandas

NumPy

Scikit-learn

XGBoost

Joblib

Matplotlib

Seaborn

Streamlit

Pytest

Git

GitHub

🧪 Testing

Automated tests are located in:

tests/test_project.py

Run the test suite:

pytest

For detailed output:

pytest -v

💻 Local Installation

1️⃣ Clone the Repository

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git
cd CardioAI-Heart-Attack-Risk-Prediction-System

2️⃣ Create a Virtual Environment

Windows

python -m venv venv
venv\Scriptsctivate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

🧠 Train the Model

To regenerate the trained model and evaluation artifacts:

python src/train.py

If models/best_model.joblib already exists, retraining is not required simply to run the application.

▶️ Run the Application

streamlit run app.py

Then open:

http://localhost:8501

🌐 Deployment

The application is deployed using Streamlit Community Cloud.

GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Install requirements.txt
       ↓
Run app.py
       ↓
Public Web Application

🚀 Production Demo

Open the Live CardioAI Application →

📈 Results & Visualizations

The results/ directory contains artifacts generated during model evaluation and analysis:

📊 Model comparison results

📋 Classification metrics

🔥 Correlation heatmap

🎯 Confusion matrices

📈 Model comparison visualization

🔄 Development Lifecycle

Requirements
     ↓
Data Preparation
     ↓
Exploratory Data Analysis
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
Deployment
     ↓
Documentation

🔐 Version Control

Git and GitHub are used for source-code management and project version control.

git add .
git commit -m "Update project"
git push origin main

Repository:
View the GitHub Repository →

🎓 Academic Project Classification

CardioAI combines:

🧠 Machine Learning
        +
📊 Data Science
        +
💻 Software Engineering
        +
🌐 Web Application Development
        +
🚀 Cloud Deployment

The project demonstrates how a machine-learning model can be developed, evaluated, integrated into a software application, tested, version-controlled and deployed using software-engineering practices.

📚 Learning Outcomes

This project demonstrates practical experience in:

Machine-learning model development

Classification algorithms

Data preprocessing

Exploratory data analysis

Model evaluation

Feature analysis

Python programming

Streamlit application development

Modular software architecture

Separation of concerns

Automated testing

Git and GitHub

Cloud deployment

Technical documentation

🔮 Future Improvements

Improve model recall and F1-score

Perform additional hyperparameter optimization

Introduce cross-validation

Add explainable AI techniques such as SHAP

Improve input validation

Add prediction history

Add user authentication

Add database integration

Implement CI/CD

Increase automated test coverage

Add application and model monitoring

Improve accessibility and responsive UI

Evaluate additional algorithms

Improve model calibration and prediction thresholds

⚠️ Medical Disclaimer

CardioAI is an educational machine-learning demonstration and is NOT a medical diagnostic system.

Predictions generated by this application:

❌ Are not medical diagnoses

❌ Should not be used for medical decision-making

❌ Should not replace advice from a qualified healthcare professional

❌ Should not be interpreted as guaranteed predictions of a heart attack

For real medical concerns, always consult a qualified healthcare professional.

👩‍💻 Author

Jayani Samarakoon

GitHub Profile:
https://github.com/cit-23-02-0104-creator

Project Repository:
https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System

Live Demo:
https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/

📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.

<div align="center">

🫀 CardioAI

Machine Learning • Data Science • Software Engineering

Built as an educational end-to-end machine-learning application.

⭐ If you find this project useful, consider giving the repository a star!

</div>
