# 🎓 Student Performance Prediction — AWS CI/CD Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://www.docker.com/)
[![AWS ECR](https://img.shields.io/badge/AWS-ECR-orange?logo=amazon-aws)](https://aws.amazon.com/ecr/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions)](https://github.com/features/actions)

An end-to-end machine learning web application that predicts a student's **math score** based on demographic and academic factors. This project features a complete **CI/CD pipeline** using **GitHub Actions**, **Docker**, **AWS ECR**, and a **self-hosted EC2 runner**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [CI/CD Pipeline Architecture](#cicd-pipeline-architecture)
- [Getting Started (Local)](#getting-started-local)
- [EC2 Self-Hosted Runner Setup](#ec2-self-hosted-runner-setup)
- [GitHub Secrets Configuration](#github-secrets-configuration)
- [Input Features](#input-features)
- [Models Trained](#models-trained)
- [Author](#author)

---

## Overview

This project predicts a student's math exam score using features like gender, ethnicity, parental education level, lunch type, test preparation course completion, reading score, and writing score.

The application is containerized with **Docker**, pushed to **AWS ECR**, and deployed on an **EC2 instance** via a **self-hosted GitHub Actions runner** — achieving full automation from code push to deployment.

---

## Project Structure

```
AWS-CI-CD-Project/
│
├── .github/
│   └── workflows/          # GitHub Actions CI/CD workflow files
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
├── Dockerfile              # Docker image definition
├── .dockerignore           # Files excluded from Docker build
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Web Framework | Flask |
| ML Libraries | scikit-learn, XGBoost, CatBoost |
| Data Processing | pandas, NumPy |
| Containerization | Docker |
| Container Registry | AWS ECR |
| CI/CD | GitHub Actions |
| Compute | AWS EC2 (Self-Hosted Runner) |

---

## CI/CD Pipeline Architecture

```
Code Push (GitHub)
       │
       ▼
GitHub Actions Triggered
       │
       ├── 1. Continuous Integration
       │       ├── Lint & Test Code
       │       ├── Build Docker Image
       │       └── Push Image to AWS ECR
       │
       └── 2. Continuous Deployment
               ├── SSH into EC2 (Self-Hosted Runner)
               ├── Pull Latest Image from ECR
               └── Run Docker Container on EC2
```

---

## Getting Started (Local)

### Prerequisites

- Python 3.8 or higher
- pip
- Docker (optional, for containerized run)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/navneetsxngh/AWS-CI-CD-Project.git
   cd AWS-CI-CD-Project
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

## EC2 Self-Hosted Runner Setup

These commands configure an Ubuntu EC2 instance as a GitHub Actions self-hosted runner with Docker installed.

### 1. Update & Upgrade the System

```bash
sudo apt-get update -y
sudo apt-get upgrade
```

### 2. Install Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 3. Add User to Docker Group

```bash
sudo usermod -aG docker ubuntu
newgrp docker
```

> After running `newgrp docker`, the `ubuntu` user can run Docker commands without `sudo`.

### 4. Register EC2 as a Self-Hosted GitHub Actions Runner

Go to your GitHub repository → **Settings** → **Actions** → **Runners** → **New self-hosted runner**, then follow the commands provided by GitHub to download and configure the runner on your EC2 instance.

---

## GitHub Secrets Configuration

The CI/CD pipeline requires the following secrets to be configured in your GitHub repository.

**Go to:** `Repository → Settings → Secrets and variables → Actions → New repository secret`

| Secret Name | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | Your AWS IAM user's Access Key ID |
| `AWS_SECRET_ACCESS_KEY` | Your AWS IAM user's Secret Access Key |
| `AWS_REGION` | AWS region where your ECR is hosted (e.g., `ap-south-1`) |
| `AWS_ECR_LOGIN_URI` | Your ECR registry URI (e.g., `123456789.dkr.ecr.ap-south-1.amazonaws.com`) |
| `ECR_REPOSITORY_NAME` | The name of your ECR repository (e.g., `student-performance`) |

### How to Get These Values

- **`AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`** → AWS Console → IAM → Users → Your User → Security Credentials → Create Access Key
- **`AWS_REGION`** → The region where you created your ECR (e.g., `us-east-1`, `ap-south-1`)
- **`AWS_ECR_LOGIN_URI`** → AWS Console → ECR → Your Repository → Copy the URI up to `.amazonaws.com`
- **`ECR_REPOSITORY_NAME`** → The short name of your ECR repository (last part of the URI)

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

The training pipeline evaluates multiple regression models and selects the best one based on R² score:

- Linear Regression
- Ridge & Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The best-performing model is serialized and saved to the `artifacts/` directory for inference.

---

## Author

**Navneet Singh**
[GitHub](https://github.com/navneetsxngh)