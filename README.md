# 🩺 Diabetes Prediction using Machine Learning

A Machine Learning web application built with **Python**, **Scikit-learn**, and **Streamlit** that predicts whether a patient is likely to have diabetes based on various medical parameters.

The application provides real-time predictions through an interactive and user-friendly web interface.

---

##  Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help healthcare professionals and patients take preventive measures.

This project uses the **Pima Indians Diabetes Dataset** to train a Machine Learning model capable of predicting the likelihood of diabetes based on patient health information.

---

## Live Demo

🔗 **Streamlit App:** *(https://diabetes-prediction-awhrqvqzrdyf7mgar3uwu8.streamlit.app/)*


---

## 📂 Dataset

Dataset Source:

https://www.kaggle.com/code/sandragracenelson/diabetes-prediction

Dataset Features:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

Target Variable:

- Outcome
  - 0 → Non-Diabetic
  - 1 → Diabetic

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## 📊 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Robust Scaling
- Quantile Transformation
- Model Training
- Model Evaluation
- Model Serialization (.pkl)
- Streamlit Deployment

---

## 🤖 Machine Learning Model

Model Used:

- K-Nearest Neighbors (KNN) Classifier

Preprocessing Techniques:

- RobustScaler
- QuantileTransformer

Model was saved using:

```python
joblib.dump(model, "diabetes_knn_model.pkl")
```

---

## 📁 Project Structure

```
Diabetes-Prediction/
│
├── app.py
├── diabetes_knn_model.pkl
├── requirements.txt
├── README.md
├── diabetes.csv
└── images/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction.git
```

Move into the project folder

```bash
cd Diabetes-Prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

```

---

## 📸 Application Preview

Add screenshots here after deployment.

Example:

```
images/home.png
images/result.png
```

---

## 🎯 Features

- Interactive User Interface
- Instant Diabetes Prediction
- Machine Learning Based Prediction
- Clean and Responsive Streamlit Dashboard
- Real-Time Prediction
- Easy to Deploy
- User-Friendly Input Forms

---

---

## 📋 Requirements

```
streamlit
numpy
pandas
scikit-learn
joblib
matplotlib
seaborn
```

---
