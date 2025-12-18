
# End-to-End Chest Cancer Deep Learning Image Classification

## Project Overview
This project is an end-to-end deep learning image classification system for chest cancer detection. The goal is to build a complete, production-ready pipeline starting from project setup to deployment using MLOps best practices.

---

## Step 1: Project overview

```bash
Project Introduction
GitHub Repository Setup
Project Template Creation
Project Setup & Environment Installation
Logging Utilities & Custom Exception Module
Project Flow & Workflow Design
Component-wise Notebook Experiments
Component-wise Modular Code Implementation
Training Pipeline Development
MLflow (MLOps-1): Experiment Tracking & Model Registration
DVC (MLOps-2): Pipeline Tracking & Versioning
Prediction Pipeline Development
User Application Creation
Dockerization
```

## Step 2: Github Repositary
``` bash 
GitHub Repository Setup
Initialized Git repository
Added .gitignore
Created .github/workflows/ for future CI/CD
Structured code under src/ for scalability
```


## Step 3: Project Structure 
``` bash 
src/ProjectName/ → Core source code
components/ → Data ingestion, preprocessing, training, evaluation
pipelines/ → Training and prediction pipelines
utils/ → Common utilities, logging, helpers
entitys/ → Artifact and configuration entities
constants/ → Constant values
config/ → Configuration management
config/config.yaml → Project paths and settings
params.yaml → Model parameters
dvc.yaml → DVC pipeline stages
research/trials.ipynb used for notebook-based experiments before modular coding
main.py → Main training execution file
templates/index.html → Frontend template for prediction app
```
``` bash
Tools & Technologies (Planned)
Python
Deep Learning (CNN)
MLflow (Experiment Tracking & Model Registry)
DVC (Pipeline & Data Versioning)
Docker
CI/CD (AWS & Azure)
```


