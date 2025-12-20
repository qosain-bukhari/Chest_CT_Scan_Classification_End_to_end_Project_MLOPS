# End-to-End Chest Cancer Deep Learning Image Classification

## Project Overview

This project implements a comprehensive, end-to-end deep learning pipeline for chest cancer detection using CT scan images. It is designed with production-ready practices and integrates MLOps workflows to ensure reproducibility, scalability, and maintainability.

---

## Step 1: Project Workflow

The project follows a structured workflow to cover all stages from initialization to deployment:

```bash
1. Project Introduction & Objective
2. GitHub Repository Setup
3. Project Template Creation
4. Project Environment Setup & Dependency Installation
5. Logging & Custom Exception Module Implementation
6. Project Flow & Workflow Design
7. Component-wise Notebook Experiments
8. Component-wise Modular Code Implementation
9. Training Pipeline Development
10. MLflow Integration for Experiment Tracking & Model Registration
11. DVC Integration for Pipeline Tracking & Versioning
12. Prediction Pipeline Development
13. User Application Development
14. Dockerization & Container Deployment
```

---

## Step 2: Environment Setup

```bash
# Create and activate Conda environment
conda create -n chest_cancer_dl python=3.13.11 -y
conda activate chest_cancer_dl

# Install project dependencies
pip install -r requirements.txt
pip install -e .
```

---

## Step 3: GitHub Repository

```bash
# Repository Initialization
git init
# Add .gitignore
# Setup CI/CD workflows in .github/workflows/
# Organize code under src/ directory for modularity and scalability
```

---

## Step 4: Project Structure

```bash
src/ProjectName/ → Core project code
components/ → Data ingestion, preprocessing, model training & evaluation modules
pipelines/ → Training and prediction pipeline scripts
utils/ → Common utility functions, logging, helper methods
entitys/ → Data and configuration entities for modular pipelines
constants/ → Project-wide constants
config/ → Configuration files management
config/config.yaml → Configuration for paths and settings
params.yaml → Model hyperparameters
dvc.yaml → DVC pipeline stages for reproducibility
research/trials.ipynb → Notebook experiments for initial model development
main.py → Entry point for pipeline execution
templates/index.html → Frontend template for prediction application
```

---

## Step 5: Tools & Technologies

```bash
Python 3.13.11
Deep Learning (TensorFlow, Keras)
MLflow for experiment tracking and model registry
DVC for data and pipeline versioning
Streamlit/Flask for user application
Docker for containerization
CI/CD deployment on AWS & Azure
```

---

## Step 6: setup file ,logging and Utiles 
```bash
✔ Requirements and setup.py configured
✔ Centralized logging implemented
✔ Common utility helper functions added
```

## Step 6: project workflow
```bash
update config.yml
update params.yml
update the entity
update the configuration manager in src config
update the components
update pipeline
update main.py
update the dvc.yml

```



## Step 7: DVC tracking 
```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/yourlink
set MLFLOW_TRACKING_USERNAME=youname
set MLFLOW_TRACKING_PASSWORD=Password
```
# End-to-End Chest Cancer Deep Learning Image Classification

## Project Overview

This project implements a comprehensive, end-to-end deep learning pipeline for chest cancer detection using CT scan images. It is designed with production-ready practices and integrates MLOps workflows to ensure reproducibility, scalability, and maintainability.

---

## Step 1: Project Workflow

The project follows a structured workflow to cover all stages from initialization to deployment:

```bash
1. Project Introduction & Objective
2. GitHub Repository Setup
3. Project Template Creation
4. Project Environment Setup & Dependency Installation
5. Logging & Custom Exception Module Implementation
6. Project Flow & Workflow Design
7. Component-wise Notebook Experiments
8. Component-wise Modular Code Implementation
9. Training Pipeline Development
10. MLflow Integration for Experiment Tracking & Model Registration
11. DVC Integration for Pipeline Tracking & Versioning
12. Prediction Pipeline Development
13. User Application Development
14. Dockerization & Container Deployment
```

---

## Step 2: Environment Setup

```bash
# Create and activate Conda environment
conda create -n chest_cancer_dl python=3.13.11 -y
conda activate chest_cancer_dl

# Install project dependencies
pip install -r requirements.txt
pip install -e .
```

---

## Step 3: GitHub Repository

```bash
# Repository Initialization
git init
# Add .gitignore
# Setup CI/CD workflows in .github/workflows/
# Organize code under src/ directory for modularity and scalability
```

---

## Step 4: Project Structure

```bash
src/ProjectName/ → Core project code
components/ → Data ingestion, preprocessing, model training & evaluation modules
pipelines/ → Training and prediction pipeline scripts
utils/ → Common utility functions, logging, helper methods
entitys/ → Data and configuration entities for modular pipelines
constants/ → Project-wide constants
config/ → Configuration files management
config/config.yaml → Configuration for paths and settings
params.yaml → Model hyperparameters
dvc.yaml → DVC pipeline stages for reproducibility
research/trials.ipynb → Notebook experiments for initial model development
main.py → Entry point for pipeline execution
templates/index.html → Frontend template for prediction application
```

---

## Step 5: Tools & Technologies

```bash
Python 3.13.11
Deep Learning (TensorFlow, Keras)
MLflow for experiment tracking and model registry
DVC for data and pipeline versioning
Streamlit/Flask for user application
Docker for containerization
CI/CD deployment on AWS & Azure
```

---

## Step 6: setup file ,logging and Utiles 
```bash
✔ Requirements and setup.py configured
✔ Centralized logging implemented
✔ Common utility helper functions added
```

## Step 6: project workflow
```bash
update config.yml
update params.yml
update the entity
update the configuration manager in src config
update the components
update pipeline
update main.py
update the dvc.yml

```



## Step 6: DVC tracking 
```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/yourlink
set MLFLOW_TRACKING_USERNAME=youname
set MLFLOW_TRACKING_PASSWORD=Password
```
# End-to-End Chest Cancer Deep Learning Image Classification

## Project Overview

This project implements a comprehensive, end-to-end deep learning pipeline for chest cancer detection using CT scan images. It is designed with production-ready practices and integrates MLOps workflows to ensure reproducibility, scalability, and maintainability.

---

## Step 1: Project Workflow

The project follows a structured workflow to cover all stages from initialization to deployment:

```bash
1. Project Introduction & Objective
2. GitHub Repository Setup
3. Project Template Creation
4. Project Environment Setup & Dependency Installation
5. Logging & Custom Exception Module Implementation
6. Project Flow & Workflow Design
7. Component-wise Notebook Experiments
8. Component-wise Modular Code Implementation
9. Training Pipeline Development
10. MLflow Integration for Experiment Tracking & Model Registration
11. DVC Integration for Pipeline Tracking & Versioning
12. Prediction Pipeline Development
13. User Application Development
14. Dockerization & Container Deployment
```

---

## Step 2: Environment Setup

```bash
# Create and activate Conda environment
conda create -n chest_cancer_dl python=3.13.11 -y
conda activate chest_cancer_dl

# Install project dependencies
pip install -r requirements.txt
pip install -e .
```

---

## Step 3: GitHub Repository

```bash
# Repository Initialization
git init
# Add .gitignore
# Setup CI/CD workflows in .github/workflows/
# Organize code under src/ directory for modularity and scalability
```

---

## Step 4: Project Structure

```bash
src/ProjectName/ → Core project code
components/ → Data ingestion, preprocessing, model training & evaluation modules
pipelines/ → Training and prediction pipeline scripts
utils/ → Common utility functions, logging, helper methods
entitys/ → Data and configuration entities for modular pipelines
constants/ → Project-wide constants
config/ → Configuration files management
config/config.yaml → Configuration for paths and settings
params.yaml → Model hyperparameters
dvc.yaml → DVC pipeline stages for reproducibility
research/trials.ipynb → Notebook experiments for initial model development
main.py → Entry point for pipeline execution
templates/index.html → Frontend template for prediction application
```

---

## Step 5: Tools & Technologies

```bash
Python 3.13.11
Deep Learning (TensorFlow, Keras)
MLflow for experiment tracking and model registry
DVC for data and pipeline versioning
Streamlit/Flask for user application
Docker for containerization
CI/CD deployment on AWS & Azure
```

---

## Step 6: setup file ,logging and Utiles 
```bash
✔ Requirements and setup.py configured
✔ Centralized logging implemented
✔ Common utility helper functions added
```

## Step 6: project workflow
```bash
update config.yml
update params.yml
update the entity
update the configuration manager in src config
update the components
update pipeline
update main.py
update the dvc.yml

```

## Step 6: DVC tracking 
```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/yourlink
set MLFLOW_TRACKING_USERNAME=youname
set MLFLOW_TRACKING_PASSWORD=Password

dvc init
dvc repro
dvc dag
```

## Step 8: prediction and user app
 ```bash
 user application using flask
 app.py
 
 ```