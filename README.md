<div align="center">

🫀 CardioAI — Heart Attack Risk Prediction System

AI-Powered Cardiovascular Risk Prediction using Machine Learning

A modern, end-to-end Machine Learning + Data Science + Software Engineering project that analyzes cardiovascular health indicators and provides an educational risk prediction through an interactive Streamlit web application.

<br>






</div>

🔗 Project Links

Resource

Link

🌐 Live Demo

Open CardioAI Application

📦 GitHub Repository

CardioAI-Heart-Attack-Risk-Prediction-System

📥 Clone Repository

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git
cd CardioAI-Heart-Attack-Risk-Prediction-System

🫀 About CardioAI

CardioAI is an educational machine-learning application developed to demonstrate an end-to-end predictive analytics workflow.

The system takes selected cardiovascular health indicators as input and uses a trained classification model to generate a risk prediction.

✨ What makes this project complete?

🧠 Machine Learning model development

📊 Data analysis and visualization

🤖 Model comparison and evaluation

💻 Modular Python application structure

🌐 Interactive Streamlit web interface

🧪 Automated testing with Pytest

📦 Saved trained model using Joblib

🔐 Input validation and application logic

🔄 Git/GitHub version control

🚀 Public cloud deployment

📚 Professional project documentation

🎯 Project Objectives

The main objectives of CardioAI are to:

Build a supervised machine-learning classification system.

Analyze cardiovascular health-related data.

Train and compare multiple classification algorithms.

Evaluate models using several performance metrics.

Select a suitable model for application integration.

Build a user-friendly web application.

Separate training, prediction, application, and testing components.

Apply software-engineering practices to an ML project.

Test the application using automated tests.

Deploy the final application online.

⚡ Key Features

<div align="center">

🧠 Machine Learning

📊 Analytics

🌐 Application

Multiple classifiers

Performance metrics

Streamlit UI

Model comparison

Correlation analysis

Interactive inputs

Model persistence

Confusion matrices

Instant prediction

</div>

🔥 Main Features

Risk Prediction — Generates a machine-learning-based cardiovascular risk result.

Multiple Algorithms — Logistic Regression, Decision Tree, Random Forest and XGBoost.

Model Evaluation — Accuracy, Precision, Recall, F1-Score and ROC-AUC.

Interactive UI — Clean browser-based interface using Streamlit.

Reusable Model — Trained model stored with Joblib.

Testing — Automated tests included in the tests/ directory.

Deployment Ready — Configured for Streamlit Community Cloud.

🏗️ System Architecture

                    ┌───────────────────────┐
                    │        USER           │
                    │  Health Information   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     STREAMLIT UI      │
                    │        app.py         │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   INPUT VALIDATION    │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   PREDICTION MODULE  │
                    │    src/predict.py    │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │    TRAINED MODEL      │
                    │ best_model.joblib     │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   RISK PREDICTION     │
                    │  + Probability Info  │
                    └───────────────────────┘

🤖 Machine Learning Workflow

                    DATASET
                       │
                       ▼
              ┌─────────────────┐
              │ Data Preparation│
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Exploratory     │
              │ Data Analysis   │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Model Training  │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Model Evaluation│
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Model Comparison│
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Best Model      │
              │ Selection       │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Joblib Model    │
              │ Persistence     │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Streamlit App   │
              └─────────────────┘

🧠 Models Evaluated

Model

Type

Logistic Regression

Linear Classification

Decision Tree

Tree-Based Classification

Random Forest

Ensemble Learning

XGBoost

Gradient Boosting

📊 Model Performance

Current evaluation results from the project:

Model

Accuracy

Precision

Recall

F1-Score

ROC-AUC

⭐ Logistic Regression

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

🏆 Selected Application Model

Logistic Regression is used by the current application.

The project evaluates several metrics instead of relying on accuracy alone. In the current evaluation, Logistic Regression provides the strongest ROC-AUC and higher recall among the compared models.

Note: These metrics are based on the project's evaluation setup and dataset. They are not clinical validation results.

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
│   └── 🖼️ confusion_matrices...
│
└── 📁 tests/
    └── 📄 test_project.py

🧩 Project Components

File / Folder

Responsibility

app.py

Main Streamlit web application

src/train.py

Data processing, training and model evaluation

src/predict.py

Prediction functionality

models/

Stores the trained machine-learning model

data/

Contains the project dataset

results/

Stores evaluation metrics and visualizations

tests/

Automated project tests

requirements.txt

Required Python packages

.gitignore

Files excluded from Git

LICENSE

Project license

README.md

Project documentation

🛠️ Technology Stack

<div align="center">

Technology

Purpose

🐍 Python

Core programming language

🐼 Pandas

Data manipulation

🔢 NumPy

Numerical computing

🤖 Scikit-learn

Machine learning

🚀 XGBoost

Gradient boosting

📦 Joblib

Model persistence

📈 Matplotlib

Visualization

📊 Seaborn

Statistical visualization

🌐 Streamlit

Web application

🧪 Pytest

Automated testing

🔧 Git

Version control

🐙 GitHub

Repository hosting

☁️ Streamlit Cloud

Deployment

</div>

💻 Installation & Setup

1️⃣ Clone the Project

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git
cd CardioAI-Heart-Attack-Risk-Prediction-System

2️⃣ Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

🧠 Train the Model

To train the models and regenerate the evaluation artifacts:

python src/train.py

The training pipeline compares the available models and saves the selected trained model to:

models/best_model.joblib

▶️ Run the Application Locally

Start Streamlit with:

streamlit run app.py

Then open:

http://localhost:8501

🧪 Run Tests

Run all automated tests:

pytest

For detailed test output:

pytest -v

🚀 Live Deployment

The application is publicly deployed using Streamlit Community Cloud.

<div align="center">

🌐 Try CardioAI Now



Live URL:
https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/

</div>

🔄 Software Development Lifecycle

┌──────────────────────┐
│  Requirements        │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Data Preparation    │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Model Development   │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Evaluation          │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Application Design  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Implementation      │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Testing             │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Deployment          │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Documentation       │
└──────────────────────┘

💻 Software Engineering Practices

CardioAI demonstrates software-engineering concepts around an ML system:

✅ Modular Design — training and prediction logic are separated.

✅ Separation of Concerns — UI, prediction and training responsibilities are organized separately.

✅ Reusable Components — prediction functionality can be reused by the application.

✅ Version Control — Git and GitHub are used to manage the source code.

✅ Testing — automated tests are included.

✅ Dependency Management — project dependencies are defined in requirements.txt.

✅ Documentation — project setup, architecture and usage are documented.

✅ Deployment — the application is deployed as a public web application.

📈 Results & Analysis

The project stores generated model-analysis artifacts inside the results/ directory.

These include:

📊 Model comparison data

📋 Evaluation metrics

🔥 Correlation heatmap

🎯 Confusion matrices

📈 Model comparison visualization

These artifacts help demonstrate the model-development and evaluation process.

🔮 Future Improvements

Possible future enhancements include:

🔬 Hyperparameter optimization

🔁 Cross-validation

📊 Improved class-imbalance handling

🧠 Explainable AI using SHAP

📈 Better probability calibration

🗃️ Prediction history and database integration

🔐 User authentication

🧪 Increased automated test coverage

⚙️ CI/CD automation with GitHub Actions

📡 Application and model monitoring

♿ Improved accessibility

📱 Further responsive UI improvements

⚠️ Medical Disclaimer

<div align="center">

🚨 IMPORTANT

CardioAI is an educational Machine Learning demonstration.
It is NOT a medical diagnostic system.

</div>

Predictions produced by this application:

❌ Are not medical diagnoses.

❌ Should not be used for medical decision-making.

❌ Should not replace advice from a qualified healthcare professional.

❌ Should not be interpreted as a guaranteed prediction of a heart attack.

For real health concerns, consult a qualified healthcare professional.

👩‍💻 Author

<div align="center">

Jayani Samarakoon

Student / Developer



</div>

📚 Official Technologies

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

<div align="center">

🫀 CardioAI

Heart Risk Intelligence

Machine Learning • Data Science • Software Engineering • Web Development

<br>

⭐ If you like this project, consider giving the repository a star!

<br>

🚀 LIVE DEMO
  •  
📦 GITHUB REPOSITORY

</div>
