# 🎓 Student Performance Prediction — End-to-End ML Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask)
![AWS](https://img.shields.io/badge/Deployed%20on-AWS%20Elastic%20Beanstalk-orange?logo=amazon-aws)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellow?logo=scikit-learn)

An end-to-end machine learning web application that predicts a student's **math score** based on various demographic and academic factors. The project covers the full ML lifecycle — from data ingestion and model training to deployment on **AWS Elastic Beanstalk**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started (Local)](#getting-started-local)
- [Deployment on AWS Elastic Beanstalk](#deployment-on-aws-elastic-beanstalk)
- [Input Features](#input-features)
- [Models Trained](#models-trained)

---

## Overview

This project predicts a student's math exam score using features like gender, ethnicity, parental education level, lunch type, test preparation course completion, reading score, and writing score.

The web interface accepts these inputs through a form and returns the predicted math score using a trained and serialized ML model.

---

## Project Structure

```
Ml-Project-Learning/
│
├── .ebextensions/          # AWS Elastic Beanstalk configuration
├── artifacts/              # Saved model files and preprocessors
├── catboost_info/          # CatBoost training logs
├── notebooks/              # EDA and model experimentation notebooks
├── src/
│   ├── components/         # Data ingestion, transformation, model training
│   ├── pipeline/           # Prediction & training pipelines
│   ├── exception.py        # Custom exception handling
│   ├── logger.py           # Logging setup
│   └── utils.py            # Utility functions
├── templates/
│   ├── index.html          # Landing page
│   └── home.html           # Prediction form & result page
├── application.py          # Flask app entry point
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
└── README.md
```

---

## Features

- Clean modular codebase with separate components for ingestion, transformation, and training
- Multiple regression models evaluated and best one selected automatically
- Custom exception handling and logging throughout the pipeline
- Flask web interface for real-time predictions
- Deployed on AWS Elastic Beanstalk for public access

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Web Framework | Flask |
| ML Libraries | scikit-learn, XGBoost, CatBoost |
| Data Processing | pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Serialization | dill |
| Deployment | AWS Elastic Beanstalk |

---

## Getting Started (Local)

### Prerequisites

- Python 3.8 or higher
- pip

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/navneetsxngh/Ml-Project-Learning.git
   cd Ml-Project-Learning
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**

   ```bash
   python application.py
   ```

5. **Open your browser** and visit `http://localhost:5000`

---

## Deployment on AWS Elastic Beanstalk

> **Note:** The entry point file is named `application.py` (not `app.py`) because AWS Elastic Beanstalk looks for a callable named `application` inside `application.py` by default.

### Prerequisites

- An [AWS account](https://aws.amazon.com/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) installed

### Step-by-Step Deployment

1. **Configure AWS credentials**

   ```bash
   aws configure
   # Enter your AWS Access Key ID, Secret Access Key, region (e.g. ap-south-1), and output format
   ```

2. **Initialize Elastic Beanstalk in your project directory**

   ```bash
   eb init -p python-3.8 ml-student-performance --region ap-south-1
   ```

   - Select your preferred region
   - Choose `Python` as the platform
   - Say **No** to CodeCommit if prompted

3. **Create the Elastic Beanstalk environment**

   ```bash
   eb create ml-student-env
   ```

   This provisions an EC2 instance, load balancer, and other AWS resources automatically.

4. **Deploy the application**

   ```bash
   eb deploy
   ```

5. **Open the deployed app in your browser**

   ```bash
   eb open
   ```

### Important Notes

- The `.ebextensions/` folder in this repo contains configuration files that Elastic Beanstalk uses during setup (e.g., setting the WSGI path).
- Make sure `requirements.txt` is up to date before deploying — Elastic Beanstalk installs dependencies from it automatically.
- To check logs if something goes wrong:

  ```bash
  eb logs
  ```

- To terminate the environment and avoid AWS charges:

  ```bash
  eb terminate ml-student-env
  ```

---

## Input Features

| Feature | Description | Example Values |
|---|---|---|
| Gender | Student's gender | `male`, `female` |
| Race/Ethnicity | Ethnic group | `group A` through `group E` |
| Parental Education | Highest level of parent's education | `bachelor's degree`, `some college`, etc. |
| Lunch | Type of lunch | `standard`, `free/reduced` |
| Test Preparation | Whether course was completed | `completed`, `none` |
| Reading Score | Score in reading exam | 0–100 |
| Writing Score | Score in writing exam | 0–100 |

**Output:** Predicted **Math Score** (0–100)

---

## Models Trained

The training pipeline evaluates multiple regression models and picks the best one based on R² score:

- Linear Regression
- Ridge & Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The best-performing model is serialized and saved to the `artifacts/` directory for use during inference.

---

## Author

**Navneet Singh**  
[GitHub](https://github.com/navneetsxngh)