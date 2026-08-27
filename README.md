# 🫀 CardioAI — Heart Attack Risk Prediction System

## AI-Powered Cardiovascular Risk Intelligence

CardioAI is an end-to-end **Machine Learning + Data Science + Software Engineering** project that analyzes cardiovascular health indicators and provides an interactive, educational heart-attack risk prediction through a **Streamlit web application**.

[![🚀 Live Demo](https://img.shields.io/badge/🚀_Live_Demo-CardioAI-ff4b4b?style=for-the-badge)](https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.61.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=flat-square&logo=numpy&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Persistence-2C3E50?style=flat-square)

---

## 🔗 Project Links

| Resource | Link |
|---|---|
| 🚀 **Live Demo** | [Open CardioAI](https://cardioai-heart-attack-risk-prediction-system-bwlxudsu5botmwk5e.streamlit.app/) |
| 💻 **GitHub Repository** | [CardioAI Repository](https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System) |
| 👤 **GitHub Profile** | [cit-23-02-0104-creator](https://github.com/cit-23-02-0104-creator) |
| 📥 **Clone Repository** | `git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git` |

---

## 📌 Project Overview

CardioAI demonstrates a complete predictive-system workflow:

**Raw Data → Data Preparation → Machine Learning → Model Evaluation → Prediction Application → Testing → Deployment**

The system analyzes cardiovascular health-related inputs and uses a trained classification model to generate an educational heart-attack risk prediction.

### 🎯 Project Objectives

- Build a practical machine-learning classification application.
- Demonstrate a complete data-science workflow.
- Apply software-engineering principles to project organization.
- Develop an interactive web application.
- Evaluate and document machine-learning model performance.
- Deploy the completed application for public access.
- Provide a reproducible project structure.

> ⚠️ **Educational Use Only:** CardioAI is a machine-learning demonstration and is **not a medical diagnostic system**. Predictions must not be used for medical treatment or emergency decisions.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🫀 **Risk Prediction** | Interactive cardiovascular risk prediction |
| 🤖 **Machine Learning** | Trained classification model |
| 📊 **Model Evaluation** | Accuracy, Precision, Recall, F1-score and ROC-AUC |
| 📈 **Evaluation Visualizations** | Model comparison, correlation analysis and confusion matrices |
| 🎨 **Modern UI** | Interactive Streamlit web interface |
| 🧪 **Testing** | Automated project tests |
| 📁 **Modular Architecture** | Organized data, source, model, result and test directories |
| 🚀 **Public Deployment** | Deployed using Streamlit Community Cloud |
| 📚 **Documentation** | Installation, execution, testing and deployment instructions |

---

## 🧠 Machine Learning Workflow

```text
┌─────────────────────────────┐
│      Heart Attack Data      │
│          Dataset            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Data Preparation       │
│    Cleaning / Encoding      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Model Development       │
│  Train Classification Models│
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Model Evaluation      │
│ Accuracy / Recall / F1 /    │
│          ROC-AUC            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Model Selection       │
│      Logistic Regression    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Model Persistence      │
│       best_model.joblib     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Streamlit App         │
│          CardioAI           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Educational Prediction   │
└─────────────────────────────┘

📊 Model Performance

The project evaluates multiple classification algorithms using the project's validation results.

Model	Accuracy	Precision	Recall	F1 Score	ROC-AUC
🥇 Logistic Regression	84.5%	36.84%	66.67%	47.46%	86.19%
Decision Tree	81.5%	30.00%	57.14%	39.34%	69.29%
Random Forest	87.0%	33.33%	23.81%	27.78%	81.27%
XGBoost	89.5%	50.00%	19.05%	27.59%	80.13%
🏆 Selected Model

Logistic Regression is the selected model according to the project's model-selection output.

Validation Results
Accuracy: 84.5%
Precision: 36.84%
Recall: 66.67%
F1 Score: 47.46%
ROC-AUC: 86.19%

These metrics represent machine-learning validation performance and should not be interpreted as clinical performance.

📈 Evaluation Results

The results/ directory contains the project's evaluation artifacts.

Generated Results
metrics.json
model_comparison.csv
model_comparison.png
correlation_heatmap.png
Confusion-matrix visualizations

These files provide evidence of model evaluation and make the development process easier to inspect and reproduce.

🖥️ Application Workflow
1. Patient Information

The user enters the required cardiovascular health-related values through the CardioAI interface.

2. Input Processing

The application prepares the entered values in the format required by the trained machine-learning model.

3. Prediction

The persisted model generates a classification prediction based on the supplied inputs.

4. Risk Insight

The application displays the prediction together with probability-oriented information.

5. Educational Interpretation

The result is presented as an educational machine-learning output rather than a medical diagnosis.

🏗️ System Architecture
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Streamlit UI    │
                    │     app.py       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Prediction Logic │
                    │  src/predict.py  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Trained Model    │
                    │ best_model.joblib│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Risk Prediction  │
                    └──────────────────┘


      Development / Training Pipeline
      ────────────────────────────────

 Dataset
    │
    ▼
src/train.py
    │
    ├──► Model Training
    │
    ├──► Model Evaluation
    │
    ├──► metrics.json
    │
    ├──► model_comparison.csv
    │
    ├──► Evaluation Charts
    │
    └──► best_model.joblib
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
│   └── 🖼️ confusion_matrix_*.png
│
└── 📁 tests/
    └── 📄 test_project.py
🧩 Project Components
app.py

The main Streamlit application.

Responsibilities
Build the web interface
Collect user inputs
Load the trained model
Process prediction inputs
Generate predictions
Display prediction results
src/train.py

The model-training pipeline.

Responsibilities
Load the dataset
Prepare the data
Train classification models
Compare model performance
Generate evaluation outputs
Save the selected trained model
src/predict.py

Handles prediction-related functionality.

Responsibilities
Prepare application inputs
Load the trained model
Generate model predictions
Return prediction-related results
models/

Stores the trained machine-learning model used by the application.

models/
└── best_model.joblib
results/

Stores numerical and visual evaluation outputs.

tests/

Contains automated tests for important project functionality.

🛠️ Technology Stack
Category	Technology
Programming Language	Python
Web Application	Streamlit
Data Processing	Pandas, NumPy
Machine Learning	scikit-learn, XGBoost
Model Persistence	Joblib
Visualization	Matplotlib / project visualization libraries
Testing	Pytest / Python testing tools
Version Control	Git & GitHub
Deployment	Streamlit Community Cloud
⚙️ Installation
Prerequisites

Before running CardioAI, install:

Python 3.x
Git
pip
1. Clone the Repository
git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git
2. Open the Project Folder
cd CardioAI-Heart-Attack-Risk-Prediction-System
3. Create a Virtual Environment
Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
macOS / Linux
python3 -m venv .venv

Activate it:

source .venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

If models/best_model.joblib already exists:

streamlit run app.py

The application will normally be available at:

http://localhost:8501

Streamlit will also display the application URL in the terminal.

🧠 Train the Machine Learning Model

To reproduce the model-training pipeline:

python src/train.py

After training completes, start the application:

streamlit run app.py

The training workflow is implemented in:

src/train.py
🧪 Testing

Run the automated tests using:

pytest

If Pytest is not installed:

pip install pytest

Then run:

pytest
☁️ Deployment

CardioAI is deployed using Streamlit Community Cloud.

🚀 Live Demo

👉 Open CardioAI Live Application

The application can be opened directly from a web browser without installing Python locally.

🔄 Software Engineering Perspective

CardioAI combines Machine Learning, Data Science and Software Engineering into one complete application.

Requirements

The system is designed to provide an interactive cardiovascular risk-prediction application using a trained machine-learning model.

Modular Design

The project separates responsibilities into:

app.py
src/train.py
src/predict.py
tests/
data/
models/
results/

This separation improves organization and maintainability.

Testing

Automated tests are included to verify important project functionality.

Version Control

The project uses Git and GitHub for:

Source-code version control
Project history
Repository management
Documentation
Collaboration
Deployment

The application is deployed as a publicly accessible Streamlit web application.

Maintainability

The separation of application code, training code, data, models, results and tests makes the project easier to maintain and extend.

🔁 Software Development Lifecycle
Requirements
     │
     ▼
Data Collection
     │
     ▼
Data Preparation
     │
     ▼
Model Development
     │
     ▼
Model Evaluation
     │
     ▼
Model Selection
     │
     ▼
Application Development
     │
     ▼
Testing
     │
     ▼
Version Control
     │
     ▼
Deployment
     │
     ▼
Maintenance & Improvement
🔐 Reproducibility

A fresh environment can reproduce the project using:

git clone https://github.com/cit-23-02-0104-creator/CardioAI-Heart-Attack-Risk-Prediction-System.git

cd CardioAI-Heart-Attack-Risk-Prediction-System

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python src/train.py

streamlit run app.py

For macOS/Linux:

source .venv/bin/activate
🚀 Future Improvements
Machine Learning
 Hyperparameter optimization
 Cross-validation
 Advanced feature engineering
 Additional classification algorithms
 Explainable AI visualizations
 Model monitoring
Software Engineering
 Increase automated test coverage
 Add Continuous Integration
 Add Continuous Deployment
 Add model versioning
 Improve application logging
 Improve error handling
User Experience
 Improve accessibility
 Improve responsive design
 Add richer prediction analytics
 Add interactive charts
 Improve user guidance
⚠️ Medical Disclaimer

CardioAI is strictly an educational and research-oriented machine-learning demonstration.

The predictions generated by this application:

are not medical diagnoses;
are not a substitute for a qualified healthcare professional;
should not be used to make treatment decisions;
should not be used for emergency-care decisions;
may be inaccurate because of limitations in the dataset, features, model and validation process.

If you have concerns about heart-attack symptoms or cardiovascular health, seek appropriate medical care from a qualified healthcare professional.

📚 Project Information
Project Name

CardioAI — Heart Attack Risk Prediction System

Project Type

Machine Learning + Data Science + Software Engineering + Web Application

Main Technologies

Python • Streamlit • Scikit-learn • Pandas • NumPy • Joblib • Git • GitHub

Deployment Platform

Streamlit Community Cloud

🔗 Important Links
🚀 Live Application

Open CardioAI

💻 GitHub Repository

CardioAI GitHub Repository

👤 GitHub Profile

GitHub Profile

⭐ Support the Project

If you find CardioAI useful or interesting:

⭐ Star the repository
🍴 Fork the project
🐛 Report issues
💡 Suggest improvements
🫀 CardioAI
Intelligent • Interactive • Educational • Machine Learning

Built with Python and Streamlit

Machine Learning • Data Science • Software Engineering
