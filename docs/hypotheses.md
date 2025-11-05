# Hypotheses

This document outlines the testable hypotheses for the "Mining IMDb for Movie Trends" project, derived from the team's core research questions. Each hypothesis is presented with a corresponding null hypothesis and a proposed methodology for testing.

---

## A. Audience Dynamics and Star Power — “What Works?”

### Research Question 1: Star Power’s Variance Reduction
**Description:** To what extent does the presence of a consistently high-rated director or actor reduce the variance (uncertainty) in audience ratings across different genres and time periods?

* **Hypothesis (H1):** The variance (statistical spread) of `averageRating` for movies associated with a "Top-Tier" director/actor (defined by a high career-average rating) will be **significantly lower** than the variance for movies from "Mid-Tier" or "Novice" directors/actors.
* **Null Hypothesis (H0):** A director's or actor's "Top-Tier" status has **no statistically significant effect** on the rating variance of their new movies; the variance will be similar across all tiers.
* **Methodology:**
    1.  Join `title.basics` (movie info) with `title.ratings` (rating), `title.principals` (link movies to people), and `name.basics` (people info).
    2.  Filter `title.principals` for 'director' and 'actor'/'actress' roles.
    3.  Engineer a new feature for each `nconst` (person ID): `career_avg_rating`.
    4.  Segment directors/actors into tiers (e.g., 'Top-Tier': career avg > 8.0 with >10 films; 'Mid-Tier'; 'Novice').
    5.  Use a statistical test (like **Levene's test**) to compare the variance of `averageRating` between these groups.

### Research Question 2: Genre-Specific Runtime Optimization
**Description:** Is there an optimal runtime range (in minutes) for maximizing the average IMDb rating within specific major genres, and how does the vote distribution differ for films outside this range?

* **Hypothesis (H1):** A **non-linear relationship** (likely an inverted U-shape) exists between `runtimeMinutes` and `averageRating`. We hypothesize this "peak" or optimal runtime will be shorter for 'Comedy' and 'Horror' films than for 'Drama' or 'Sci-Fi' films.
* **Null Hypothesis (H0):** The relationship between `runtimeMinutes` and `averageRating` is **linear** (e.g., longer is always better/worse) or **non-existent**.
* **Methodology:**
    1.  Join `title.basics` (for `runtimeMinutes`, `genres`) with `title.ratings`.
    2.  Filter for major genres and handle `runtimeMinutes` outliers.
    3.  Create scatter plots of `runtimeMinutes` vs. `averageRating` per genre, fitting a polynomial or LOESS curve to visualize the trend.
    4.  Bin runtimes (e.g., <80, 80-100, 100-120, 120-150, 150+) and use an **ANOVA** to test for significant differences in mean ratings between these bins.

### Research Question 3: Predicting Popularity Threshold
**Description:** Which combination of structured metadata features (genre, runtime, year, region) is most effective in predicting whether a movie will achieve a high popularity threshold (e.g., greater than 25,000 votes)?

* **Hypothesis (H1):** A classification model (e.g., Random Forest) can predict whether a movie's `numVotes` will exceed 25,000 with high accuracy (e.g., AUC > 0.80). We hypothesize that `startYear` (recency) and `genre` will be the most important predictive features.
* **Null Hypothesis (H0):** The model will perform **no better than a random baseline** (AUC $\approx$ 0.50), and no single feature will show significant predictive power.
* **Methodology:**
    1.  Join `title.basics`, `title.ratings`, and `title.akas` (for `region`).
    2.  Create a binary target variable: `is_popular` (1 if `numVotes > 25000`, 0 otherwise).
    3.  Train a **Random Forest or Logistic Regression classifier**.
    4.  Evaluate using the **AUC-ROC curve** and **F1-score** due to likely class imbalance.
    5.  Extract and plot feature importances.

---

## B. Cultural Influence and Linguistic Bias — “Why It Works?”

### Research Question 4: Regional Rating Bias
**Description:** Are there statistically significant, demonstrable biases in IMDb ratings when comparing audience preferences across major film production regions/languages?

* **Hypothesis (H1):** There is a **statistically significant difference** in the mean `averageRating` of films produced in different major regions (e.g., US, India, South Korea, France), even after controlling for genre.
* **Null Hypothesis (H0):** The film's production `region` has **no effect** on its mean `averageRating`; any observed differences are due to chance.
* **Methodology:**
    1.  Join `title.ratings` with `title.akas` (which contains `region` information).
    2.  Filter for a list of major film-producing regions to compare (e.g., 'US', 'IN', 'KR', 'FR', 'GB').
    3.  Perform an **ANOVA** (or its non-parametric equivalent, Kruskal-Wallis) to compare the mean `averageRating` across these groups.

### Research Question 5: Language-Specific Rating Impact
**Description:** Does the primary original language of a film, independent of the production region, significantly correlate with the film’s average rating and total vote count when controlling for release year and genre?

* **Hypothesis (H1):** In a multiple regression model, `originalLanguage` will be a **statistically significant predictor** (p < 0.05) of `averageRating`, even when `region`, `startYear`, and `genre` are included as control variables.
* **Null Hypothesis (H0):** The coefficient for `originalLanguage` in the regression model will **not be statistically significant** (p > 0.05) once other factors are controlled for.
* **Methodology:**
    1.  Join `title.basics`, `title.ratings`, and `title.akas` (for `language` and `region`).
    2.  Build a **multiple linear regression model**: `averageRating ~ C(originalLanguage) + C(region) + startYear + C(genre)`.
    3.  Examine the p-value of the `originalLanguage` coefficient.

---

## C. Predictive Modeling and Interpretation — “How to Predict?”

### Research Question 6: Feature Contribution to Rating/Popularity
**Description:** Which structured metadata factors are the strongest marginal contributors to the overall variance in movie popularity (vote count) and rating?

* **Hypothesis (H1):** For predicting `averageRating`, `runtimeMinutes` and `genre` will be the strongest contributors. For predicting `numVotes` (popularity), `startYear` (recency) and `genre` will be the strongest.
* **Null Hypothesis (H0):** All features will have roughly equal, or negligible, contribution to the model's predictive power.
* **Methodology:**
    1.  Build two separate predictive models: one for `averageRating` (regression) and one for `numVotes` (regression).
    2.  Use a **Random Forest Regressor** for both.
    3.  Extract and plot the **feature importances** (e.g., Gini importance) or a **SHAP summary plot** to identify the top contributors for each model.

### Research Question 7: Model Performance & Interpretability (Metadata-Only)
**Description:** Which machine learning model (e.g., Ridge Regression, Random Forest) achieves the best predictive performance for IMDb rating using only structured metadata?

* **Hypothesis (H1):** A **tree-based ensemble model (Random Forest)** will significantly outperform a **linear model (Ridge Regression)** in predicting `averageRating`, as measured by a lower Root Mean Squared Error (RMSE) and higher $R^2$, due to its ability to capture complex, non-linear feature interactions.
* **Null Hypothesis (H0):** Both models will have **statistically similar performance** (RMSE and $R^2$ values will not be significantly different).
* **Methodology:**
    1.  Train, test, and tune both a `RidgeRegression` and a `RandomForestRegressor` model on the same dataset using k-fold cross-validation.
    2.  Compare their mean **RMSE** and **$R^2$** scores.
    3.  Use **SHAP plots** (e.g., summary plot, dependence plots) to interpret the "black box" Random Forest model.

---

## D. Temporal Trends — “How It Changes Over Time?”

### Research Question 8: Genre Popularity and Quality Evolution
**Description:** How have the popularity (median vote count) and average quality (median rating) of major genres and subgenres evolved over the last three decades?

* **Hypothesis (H1):** Over the past 30 years (1995-2025), 'Documentary' and 'Sci-Fi' will show a **statistically significant positive trend** in median `averageRating`. 'Action' will show a positive trend in median `numVotes` but a flat or declining trend in median `averageRating`.
* **Null Hypothesis (H0):** No statistically significant long-term trends exist; median ratings and votes per genre are stable or random (cyclical) over time.
* **Methodology:**
    1.  Join `title.basics` and `title.ratings`.
    2.  Filter for `startYear` >= 1995.
    3.  Aggregate data by `startYear` and `genre`. Calculate `MEDIAN(averageRating)` and `MEDIAN(numVotes)` for each group. (Median is used to be robust to outliers).
    4.  Plot these as **time-series charts**.
    5.  Run a simple linear regression on each time-series (e.g., `median_rating ~ year` for 'Documentary') to find the significance and slope of the trend.
