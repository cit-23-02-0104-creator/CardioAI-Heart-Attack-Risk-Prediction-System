🫀 CardioAI --- Heart Attack Risk Prediction System

<p align="center">

<strong>{=html}AI-Powered Cardiovascular Risk Prediction using Machine
Learning</strong>{=html}

</p>

<p align="center">

A complete Machine Learning, Data Science, and Software Engineering
project for educational cardiovascular risk prediction.

</p>

<p align="center">

<a href="https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/">{=html}
<img src="https://img.shields.io/badge/🚀_Live_Demo-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Live Demo">{=html}
</a>{=html}
<a href="https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System">{=html}
<img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub Repository">{=html}
</a>{=html}

</p>

🚀 Live Demo

👉 Launch CardioAI --- Live
Demo

Live URL:
https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/

📌 Project Overview

CardioAI is a machine-learning-based web application developed to
demonstrate how cardiovascular health-related indicators can be used to
build a predictive classification system.

The project combines:

Machine Learning

Data Science

Software Engineering

Software Testing

Web Application Development

Cloud Deployment

Technical Documentation

End-to-End Workflow

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
Prediction

🎯 Project Objectives

Develop a machine-learning classification system for cardiovascular
risk prediction.

Analyze health-related data using data science techniques.

Compare multiple classification algorithms.

Evaluate models using appropriate classification metrics.

Select a suitable model for the prediction application.

Build an interactive web application using Streamlit.

Separate training, prediction, application, and testing components.

Apply software engineering principles to the development lifecycle.

Implement automated testing.

Deploy the completed application as a public web application.

Provide clear technical documentation and reproducible setup
instructions.

⭐ Key Features

🫀 Cardiovascular Risk Prediction

Users can enter health-related information through an interactive web
interface and receive a machine-learning-based prediction.

🤖 Multiple Machine Learning Models

Logistic Regression

Decision Tree

Random Forest

XGBoost

📊 Model Evaluation

Accuracy

Precision

Recall

F1-Score

ROC-AUC

🌐 Interactive Web Application

The system provides a browser-based interface built with Streamlit.

🧪 Automated Testing

The project includes a test suite under the tests/ directory.

📦 Model Persistence

The trained model is stored with joblib so the deployed application
can load the model without retraining every time.

🚀 Cloud Deployment

The application is deployed through Streamlit Community Cloud.

🏗️ Software Engineering

CardioAI is designed as a combined Machine Learning + Software
Engineering project.

Requirements Engineering

The system considers required user inputs, prediction requirements,
machine-learning requirements, application requirements, testing
requirements, and deployment requirements.

System Design

                    ┌──────────────────────┐
                    │       User / UI      │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Streamlit App     │
                    │       app.py         │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Prediction Module    │
                    │    src/predict.py    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Trained ML Model   │
                    │ models/best_model    │
                    └──────────────────────┘

Software Engineering Practices

Modular design

Separation of concerns

Reusable model persistence

Automated testing

Git/GitHub version control

Technical documentation

Cloud deployment

🧠 Machine Learning Methodology

The project follows a supervised machine-learning classification
workflow.

Models Used

Model                 Description

Logistic Regression   Linear classification model
Decision Tree         Tree-based classification model
Random Forest         Ensemble tree-based model
XGBoost               Gradient boosting classification model

Workflow

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
Selected Model
   ↓
Saved Model
   ↓
Web Application

📊 Model Performance

Current training results:

Model            Accuracy    Precision       Recall     F1-Score      ROC-AUC

Logistic      84.5%   36.84%   66.67%   47.46%   86.19%
Regression
⭐

Decision            81.5%       30.00%       57.14%       39.34%       69.29%
Tree

Random              87.0%       33.33%       23.81%       27.78%       81.27%
Forest

XGBoost             89.5%       50.00%       19.05%       27.59%       80.13%

Current Application Model

The application uses Logistic Regression.

The project considers multiple metrics rather than accuracy alone. The
reported Logistic Regression result provides the strongest ROC-AUC and
higher recall than the tree-based alternatives in the current
evaluation.

Model performance depends on the dataset, preprocessing, train/test
split, and evaluation methodology. These values are not clinical
performance claims.

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

Component            Description

app.py             Main Streamlit web application
src/train.py       Model training and evaluation pipeline
src/predict.py     Prediction-related functionality
models/            Trained machine-learning model
data/              Project dataset
results/           Evaluation metrics and visualizations
tests/             Automated project tests
requirements.txt   Python dependencies
README.md          Project documentation
LICENSE            Project license
.gitignore         Files excluded from Git

🛠️ Technology Stack

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

Streamlit Community Cloud

Official Documentation

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

Automated tests are located at:

tests/test_project.py

Run:

pytest

Detailed output:

pytest -v

💻 Local Installation

1. Clone the Repository

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git

2. Navigate to the Project

cd CardioAI-Heart-Attack-Risk-Prediction-System

3. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

🧠 Train the Model

To regenerate the trained model and evaluation artifacts:

python src/train.py

If models/best_model.joblib already exists, retraining is not required
just to run the application.

▶️ Run the Application

streamlit run app.py

Open:

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

🚀 Live Application

https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/

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

Git and GitHub are used for source-code management.

git add .
git commit -m "Update project"
git push origin main

Repository

https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System

📈 Results and Visualizations

The results/ directory contains generated artifacts used for model
evaluation and analysis:

Model comparison results

Classification metrics

Correlation heatmap

Confusion matrices

Model comparison visualization

🧩 System Architecture

┌─────────────────────────────────────────────────────────┐
│                    CARDIOAI SYSTEM                      │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │     Streamlit UI    │
              │       app.py        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Input Validation  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Prediction Module   │
              │  src/predict.py     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Trained ML Model   │
              │ best_model.joblib   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Prediction Result   │
              └─────────────────────┘

🎓 Academic Project Classification

CardioAI combines:

Machine Learning
        +
Data Science
        +
Software Engineering
        +
Web Application Development
        +
Cloud Deployment

The project demonstrates how a machine-learning model can be transformed
into a complete software application using software engineering
practices.

🔮 Future Improvements

Improve model recall and F1-score.

Perform additional hyperparameter optimization.

Introduce cross-validation.

Add explainable AI techniques such as SHAP.

Improve input validation.

Add prediction history.

Add user authentication.

Add database integration.

Add CI/CD.

Increase automated test coverage.

Add application and model monitoring.

Improve accessibility and responsive UI.

Evaluate additional algorithms.

Improve model calibration and prediction thresholds.

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

⚠️ Medical Disclaimer

CardioAI is an educational machine-learning demonstration and is not a
medical diagnostic system.

Predictions generated by this application:

are not medical diagnoses;

should not be used for medical decision-making;

should not replace advice from a qualified healthcare professional;

should not be interpreted as guaranteed predictions of a heart
attack.

Always consult a qualified healthcare professional for real medical
concerns.

👩‍💻 Author

Jayani Samarakoon

GitHub:
https://github.com/cit-23-02-0104-creator

Project Repository:
https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System

Live Demo:
https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/

📄 License

This project is licensed under the MIT License.

See LICENSE for details.

<p align="center">

<strong>{=html}🫀 CardioAI</strong>{=html} <br>{=html} Machine
Learning • Data Science • Software Engineering
<br>{=html}<br>{=html} Built as an educational project demonstrating
an end-to-end machine-learning application.

</p>
