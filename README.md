# Iris Classification using Kedro

An end-to-end Machine Learning pipeline project built using Kedro orchestration framework and Scikit-learn for Iris flower classification.

---

# 🚀 Project Overview

This project demonstrates how to build a modular and production-style ML pipeline using Kedro.

The pipeline performs:

- Data Loading
- Train/Test Splitting
- Model Training
- Model Evaluation
- Pipeline Visualization using Kedro Viz

---

# 🛠️ Tech Stack

- Python
- Kedro
- Scikit-learn
- Pandas
- Jupyter Notebook
- Kedro Viz

---

# 📂 Project Structure

```bash
iris-classification-kedro/
│
├── conf/                       # Configuration files
├── data/                       # Data storage
│   ├── 01_raw/
│   ├── 02_intermediate/
│   ├── 06_models/
│   └── 08_reporting/
│
├── notebooks/                  # Jupyter notebooks
│
├── src/iris_classification/
│   ├── pipelines/
│   │   └── data_processing/
│   │       ├── nodes.py
│   │       └── pipeline.py
│   │
│   ├── pipeline_registry.py
│   └── settings.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

# ⚙️ Pipeline Flow

```text
Load Iris Dataset
        ↓
Split Train/Test Data
        ↓
Train Logistic Regression Model
        ↓
Evaluate Model Accuracy
        ↓
Save Model & Metrics
```

---

# 🔥 Kedro Pipeline Architecture

```text
Notebook
   ↓
nodes.py
   ↓
pipeline.py
   ↓
pipeline_registry.py
   ↓
catalog.yml
   ↓
kedro run
```

---

# 📊 Model Used

- Logistic Regression

---

# 📈 Evaluation Metric

- Accuracy Score

---

# 🚀 How to Run Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/iris-classification-kedro.git
```

---

## 2️⃣ Navigate to Project

```bash
cd iris-classification-kedro
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Run Kedro Pipeline

```bash
kedro run
```

---

## 7️⃣ Run Kedro Viz

```bash
kedro viz
```

Open browser:

```text
http://127.0.0.1:4141
```

---

# 📂 Output Artifacts

## Processed Data

```text
data/02_intermediate/
```

- X_train.csv
- X_test.csv
- y_train.csv
- y_test.csv

---

## Trained Model

```text
data/06_models/trained_model.pkl
```

---

## Evaluation Metrics

```text
data/08_reporting/model_metrics.json
```

---

# 🧠 Key Learnings

This project helped in understanding:

- Kedro orchestration
- Modular ML pipelines
- Dataset catalog management
- Node-based workflow design
- Model persistence
- Pipeline visualization
- Production-style ML engineering

---

# 🎯 Future Improvements

- Add Hyperparameter Tuning
- Add MLflow Integration
- Add Docker Support
- Add FastAPI Deployment
- Add CI/CD Pipeline
- Add Airflow Scheduling

---

# 👨‍💻 Author

Pramod Gaikwad

---

# ⭐ If you like this project

Give this repository a star ⭐
