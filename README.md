# ❤️ Heart Disease Prediction using Logistic Regression

This project predicts whether a person is a **heart patient or not** based on medical attributes using **Logistic Regression** — a simple yet effective machine learning algorithm for binary classification.

---

## 🧠 Project Overview

Heart disease is one of the leading causes of death worldwide, and early prediction can save lives.  
This project uses machine learning techniques to analyze medical data and determine whether a person is likely to have heart disease.

**Prediction Goal:**
- `1` → Heart patient  
- `0` → Not a heart patient

---

## ⚙️ Workflow

### 1️⃣ Data Collection & Loading
- Imported the dataset using **pandas** (`.csv` format).  
- Performed initial inspection using `df.head()`, `df.info()`, and `df.describe()`.

### 2️⃣ Exploratory Data Analysis (EDA)
- Visualized feature distributions and relationships using:
  - **matplotlib**
  - **seaborn**
- Checked for correlation between numerical features using a **heatmap**.

### 3️⃣ Data Preprocessing
- Encoded categorical features into numeric format.  
- Split dataset into **training** and **testing** sets using `train_test_split`.  
- Standardized feature values using `StandardScaler` (if necessary).

### 4️⃣ Model Training
- Applied **Logistic Regression** from `sklearn.linear_model`.  
- Trained model using the processed data.  

### 5️⃣ Model Evaluation
Evaluated performance with the following metrics:
- ✅ **Accuracy Score**: `~0.8446`
- 📊 **Precision**, **Recall**, and **F1-score**
- 🧩 **Confusion Matrix**

### 6️⃣ Prediction
- Model predicts whether a person is likely to have heart disease based on new input medical data.
---
## 🧰 Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python |
| **Data Handling** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Model Building** | scikit-learn |
| **Environment** | Jupyter Notebook |

---

## 📈 Results

- **Model:** Logistic Regression  
- **Accuracy:** `~84.46%`  
- The model shows a **strong ability** to distinguish between heart patients and healthy individuals.

---


## 🚀 deployment

- Use **cross-validation** for better generalization.  
- Deploy model via **Streamlit** or **Flask web app** for user-friendly predictions.  

---


