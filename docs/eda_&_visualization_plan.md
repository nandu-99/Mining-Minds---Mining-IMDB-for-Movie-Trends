# **EDA & Visualization Plan**

This document outlines the complete plan for Exploratory Data Analysis (EDA) and Visualization for the "Mining IMDb for Movie Trends" project.

The goal is to validate our cleaned data, test our hypotheses using core data science methods, and create the deliverables for the Phase 2 and 3 evaluations.

---

## 1. **Objectives**

1.  **Validate Data:** To programmatically and visually confirm that our preprocessed datasets are clean (e.g., using Histograms to check distributions and Box Plots for outliers).
2.  **Generate Descriptive Insights:** To understand the underlying distributions and relationships using **Summary Statistics** (mean, median, percentiles) and **Core Visualizations** (Scatter Plots, Box Plots).
3.  **Hypothesis-Driven Visualization:** To create specific, targeted visualizations for *each* of the 8 hypotheses using our approved toolset.
4.  **Plan for Deliverables:** To design the key "data story" visualizations for the final presentation, including the required interactive dashboard.

---

## 2. **Core EDA Steps (General Analysis)**

This phase will be conducted first on the main `clean_master.csv` file to understand the "big picture."

1.  **Univariate Analysis (Distributions & Summary Statistics):**
    * **Objective:** Understand the shape of our key numeric features.
    * **Actions:**
        * Calculate **Summary Statistics** (mean, median, mode, percentiles, range, variance) for `averageRating`, `numVotes`, `startYear`, and `runtimeMinutes`.
        * Plot **Histograms** for these same features to visualize their distributions.
        * Plot **Box Plots** to visually identify outliers and quartiles.

2.  **Bivariate Analysis (Correlations):**
    * **Objective:** Find initial relationships between numeric variables.
    * **Action:** Create **Scatter Plots** for key pairs (e.g., `runtimeMinutes` vs. `averageRating`, `numVotes` vs. `averageRating`).
    * **Action:** Create a **Correlation Heatmap** to display summary statistics (correlations).

3.  **Categorical Analysis (Counts):**
    * **Objective:** Understand the composition of our dataset.
    * **Action:** Plot **Bar Charts** to show the **Frequencies** (counts) of the top 15 `genre_primary`, `region`, and `language` categories.

---

## 3. **Hypothesis-Driven Visualization Mapping**

This is the core of our analysis. Each hypothesis will be mapped to a specific visualization.

| Hypothesis | Data Source | Visualization Type | Justification (How it tests the hypothesis) |
| :--- | :--- | :--- | :--- |
| **H1: Star Power Variance** | `df_star_power.csv` | **Box Plots** | We will plot `averageRating` (y-axis) against `director_tier` (x-axis). This will directly let us compare the median, quartiles, and outlier range (variance) for each tier. |
| **H2: Runtime Optimization** | `df_runtime_genre.csv` | **Scatter Plot (with Regression Fit)** | We'll use `seaborn.lmplot` to plot `runtimeMinutes` vs. `averageRating`, faceted by `genre_primary`. This will visually test the non-linear trend. |
| **H3: Predicting Popularity** | Model Output | **Bar Chart** | After the model runs, we will plot its `feature_importances_` as a simple **Bar Chart** to show which features were most predictive. |
| **H4: Regional Rating Bias** | `df_region_language.csv` | **Bar Plot (with Error Bars)** | A `seaborn.barplot` shows the **Mean** (a summary statistic) for each region. The error bars (also a summary statistic) show the confidence interval for easy comparison. |
| **H5: Language Impact** | `df_region_language.csv` | **Faceted Box Plots** | We will use **Box Plots** to show the distribution of `averageRating` (y-axis) for each `language` (x-axis). Faceting by `region` will help us control for that variable visually. |
| **H6: Feature Contribution** | `df_popularity_model.csv` | **Correlation Heatmap** | A heatmap is a valid way to show the **Summary Statistics** (correlations) between all our features and the target variables (`averageRating`, `numVotes`). This acts as a "Filter approach" to feature selection. |
| **H7: Model Performance** | Model Results | **Grouped Bar Chart** | A standard **Bar Chart** is the clearest way to compare the performance metrics (RMSE, R²) of the two models. |
| **H8: Temporal Trends** | `df_temporal_trends.csv` | **Line Charts** | A **Line Chart** is the standard plot for time-series data. We will plot `startYear` vs. `medianRating` (a summary statistic) for each genre. |

---

## 4. **Deliverables**

This plan will produce the following key artifacts for Phase 2 and 3.

### 4.1. `EDA.ipynb` (Phase 2 Deliverable)
* A single, clean Jupyter Notebook containing the full execution of this plan.
* It will include all code, the plots from Section 2 and 3, and markdown cells with clear interpretations ("deep, actionable insights") of what each plot means.
* This notebook will be the primary evidence for the Phase 2 EDA grade.

### 4.2. `Key_Findings.md` (Phase 3 Presentation Aid)
* A summary document listing the 3-5 most "surprising" or "insightful" findings from the EDA (e.g., "Our box plots show that Top-Tier directors have a 50% smaller rating variance...").
* This will form the basis of our "data story" for the final presentation.

### 4.3. Plan for Phase 3 Interactive Visualization
This section outlines the plan for the **"sophisticated and well-integrated interactive visualisation"** required by the Phase 3 evaluation.

* **Tool:** The team will use **Plotly (Dash)** or **Streamlit**.
* **Core Functionality:** To fulfill the project brief's requirement, the dashboard will include:
    1.  A **dropdown menu** for users to select a `director_name`.
    2.  On selection, the dashboard will dynamically update to show a table/chart of that director's **top 3 movies by `averageRating`** (also showing `runtimeMinutes`).
* **"Sophisticated" Extension:** To achieve an "exemplary" score, we will add a secondary plot that also updates dynamically, such as:
    * A **Scatter Plot** showing the director's entire filmography (`startYear` vs. `averageRating`) to let users "explore the data dynamically."
