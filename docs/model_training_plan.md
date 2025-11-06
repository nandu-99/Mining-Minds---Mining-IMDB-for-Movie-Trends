# **Model Training Plan**

This document outlines the initial methodology for developing the predictive models required by our project objectives and hypotheses (specifically H3, H6, and H7).

---

## 1. **Objectives**

The primary goal is to train, evaluate, and interpret three distinct predictive models as defined in our hypotheses:

1.  **A Regression Model:** To predict a movie's continuous `averageRating` (Hypothesis H7).
2.  **A Classification Model:** To predict a movie's binary popularity status `is_popular` (Hypothesis H3).
3.  **A Second Regression Model:** To predict a movie's continuous `normalized_votes` (Hypothesis H6).

This plan covers the target variables, feature selection, baseline models, and evaluation metrics for each task.

## 2. **Model 1: Predicting Movie Rating (Regression)**

* **Hypothesis:** H7 (Model Comparison), H6 (Feature Contribution)
* **Dataset:** `df_popularity_model.csv`
* **Objective:** Predict the `averageRating` (a continuous float from 1.0-10.0).

### **Target Variable**
* `averageRating`

### **Feature Selection (Initial Set)**
Based on `data_preprocessing_plan.md` (Section 7), our features will be:
* `startYear` (Numeric)
* `runtimeMinutes` (Numeric)
* `genres` (Categorical, will be one-hot encoded)
* `region` (Categorical, will be one-hot encoded)
* `language` (Categorical, will be one-hot encoded)

### **Models & Evaluation Metrics**
As per Hypothesis H7, we will compare two models:

**1. Baseline Model: `Ridge Regression`**
* **Why:** A simple, interpretable linear model that provides a strong baseline. It fulfills the H7 requirement.
* **Feature Scaling:** `StandardScaler` will be applied to all numeric features.
* **Evaluation Metrics:**
    * **R² (R-squared):** Primary metric. To measure the proportion of variance explained.
    * **RMSE (Root Mean Squared Error):** Secondary metric. To measure the average prediction error in "rating points."

**2. Advanced Model: `Random Forest Regressor`**
* **Why:** A tree-based ensemble model that can capture non-linear relationships (fulfilling H7) and will be used for feature contribution analysis (fulfilling H6).
* **Feature Scaling:** Not required.
* **Evaluation Metrics:** R² and RMSE (for direct comparison with the baseline).

---

## 3. **Model 2: Predicting Popularity (Classification)**

* **Hypothesis:** H3
* **Dataset:** `df_popularity_model.csv`
* **Objective:** Predict if a movie will achieve a high popularity threshold.

### **Target Variable**
* `is_popular` (Binary: 1 if `numVotes > 25,000`, 0 otherwise).

### **Feature Selection (Initial Set)**
* `startYear` (Numeric)
* `runtimeMinutes` (Numeric)
* `genres` (Categorical, will be one-hot encoded)
* `region` (Categorical, will be one-hot encoded)
* `language` (Categorical, will be one-hot encoded)

### **Models & Evaluation Metrics**
As per Hypothesis H3, we will use the following:

**1. Baseline Model: `Logistic Regression`**
* **Why:** The standard, highly interpretable baseline for binary classification (fulfills H3).
* **Feature Scaling:** `StandardScaler` will be applied.
* **Evaluation Metrics:**
    * **AUC-ROC (Area Under the Curve):** Primary metric, as specified in H3.
    * **F1-Score:** Secondary metric, also specified in H3 for handling potential class imbalance.

**2. Advanced Model: `Random Forest Classifier`**
* **Why:** A powerful ensemble model specified in H3, also good for deriving feature importance.
* **Feature Scaling:** Not required.
* **Evaluation Metrics:** AUC-ROC and F1-Score (for direct comparison).

---

## 4. **Model 3: Predicting Popularity (Regression)**

* **Hypothesis:** H6
* **Dataset:** `df_popularity_model.csv`
* **Objective:** Predict a movie's popularity as a continuous value.

### **Target Variable**
* `normalized_votes` (This is the log-transformed `numVotes` as defined in `data_preprocessing_plan.md`, Section 5, which is better for regression stability).

### **Feature Selection (Initial Set)**
* `startYear` (Numeric)
* `runtimeMinutes` (Numeric)
* `genres` (Categorical, will be one-hot encoded)
* `region` (Categorical, will be one-hot encoded)
* `language` (Categorical, will be one-hot encoded)

### **Models & Evaluation Metrics**
As per Hypothesis H6, we will use the following:

**1. Model: `Random Forest Regressor`**
* **Why:** Hypothesis H6 explicitly specifies using a Random Forest to identify the strongest contributors to popularity.
* **Feature Scaling:** Not required.
* **Evaluation Metrics:**
    * **R² (R-squared):** To measure the proportion of variance in `normalized_votes` that the model can explain.
    * **RMSE (Root Mean Squared Error):** To measure the average prediction error.
    * **SHAP Summary Plot:** The primary deliverable, as specified in H6, to interpret feature contribution.

---

## 5. **Training & Validation Methodology (For All Models)**

1.  **Data Splitting:** The `df_popularity_model.csv` dataset will be split into a **Training Set (80%)** and a **Test Set (20%)** using `scikit-learn`'s `train_test_split`.
2.  **Cross-Validation:** As per H7, we will use **5-fold Cross-Validation** on the *training set* to tune hyperparameters and get a robust, reliable estimate of each model's performance.
3.  **Final Evaluation:** The *test set* will be held out until the very end and used only once to evaluate the final, tuned models. This prevents data leakage and gives an honest assessment of model generalization.
