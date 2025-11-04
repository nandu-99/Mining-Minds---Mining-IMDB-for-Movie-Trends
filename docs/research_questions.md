## **Research Questions & Objectives**

### **1. Project Overview**

The project aims to analyze IMDb’s movie datasets to uncover trends and predictive patterns related to movie ratings, popularity, and audience engagement. Using data-mining and machine-learning techniques, it explores how factors such as **genre, budget, cast, release year, and region** influence audience ratings and critical success.

---

### **Objectives**

1. **Identify Success Drivers:**
   Determine which metadata factors (e.g., genre, cast, budget, region) most strongly correlate with higher IMDb ratings or popularity.

2. **Model Cultural and Audience Influence:**
   Analyze how regional, linguistic, and temporal factors shape audience preferences.

3. **Develop Predictive Models:**
   Build interpretable machine-learning models for predicting movie ratings and popularity.

4. **Leverage Textual Features:**
   Integrate sentiment and narrative analysis from plot summaries and reviews to improve model accuracy.

5. **Ensure Transparency and Reproducibility:**
   Use IMDb’s official datasets and document the modeling pipeline clearly for reproducibility.

---

### **Research Questions**

---

#### **A. Audience Dynamics and Star Power — “What Works?” (Metadata Focus)**

1. **Star Power’s Variance Reduction:**
   To what extent does the presence of a consistently high-rated director or actor reduce the variance (uncertainty) in audience ratings across different genres and time periods?
   *Data needed:* `title.ratings`, `title.principals`, `name.basics`

2. **Genre-Specific Runtime Optimization:**
   Is there an optimal runtime range (in minutes) for maximizing the average IMDb rating within specific major genres (e.g., Horror, Comedy, Documentary), and how does the vote distribution differ for films outside this range?
   *Data needed:* `title.basics`, `title.ratings`

3. **Predicting Popularity Threshold:**
   Which combination of structured metadata features (genre, runtime, year, region) is most effective in predicting whether a movie will achieve a high popularity threshold (e.g., greater than 25,000 votes)?
   *Data needed:* `title.basics`, `title.ratings`

---

#### **B. Cultural Influence and Linguistic Bias — “Why It Works?” (Regional Focus)**

4. **Regional Rating Bias:**
   Are there statistically significant, demonstrable biases in IMDb ratings when comparing audience preferences across major film production regions/languages (e.g., US, India, South Korea, France)?
   *Data needed:* `title.akas`, `title.ratings`

5. **Language-Specific Rating Impact:**
   Does the primary original language of a film, independent of the production region, significantly correlate with the film’s average rating and total vote count when controlling for release year and genre?
   *Data needed:* `title.akas`, `title.ratings`

---

#### **C. Predictive Modeling and Interpretation — “How to Predict?” (Modeling Focus)**

6. **Feature Contribution to Rating/Popularity:**
   Which structured metadata factors (e.g., genre, runtime, production region, release year) are the strongest marginal contributors to the overall variance in movie popularity (vote count) and rating?
   *Data needed:* `title.basics`, `title.ratings`, `title.akas`, `title.principals`

7. **Model Performance & Interpretability (Metadata-Only):**
   Which machine learning model (e.g., Ridge Regression, Random Forest) achieves the best predictive performance for IMDb rating using only structured metadata, and how can interpretability techniques (e.g., SHAP) explain the relative influence of factors like genre vs. runtime?
   *Data needed:* All structured metadata files

---

#### **D. Temporal Trends — “How It Changes Over Time?”**

8. **Genre Popularity and Quality Evolution:**
   How have the popularity (median vote count) and average quality (median rating) of major genres and subgenres evolved over the last three decades, and can these temporal trends be used to forecast future audience preference shifts?
   *Data needed:* `title.basics`, `title.ratings`

---

### **Expected Outcomes**

* Identification of key quantitative and qualitative drivers behind movie success.
* A reproducible data-mining and machine-learning pipeline built on IMDb datasets.
* Insights into how sentiment, cultural, and economic factors jointly shape audience behavior.
* Visual and interpretable outputs (e.g., SHAP plots, trend visualizations) to support data-driven decision-making in entertainment analytics.

---
