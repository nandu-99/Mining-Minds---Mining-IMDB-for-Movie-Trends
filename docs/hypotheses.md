# **Hypotheses Doc**

This document outlines the testable hypotheses for the "Mining IMDb for Movie Trends" project, derived from our four innovative research questions. Each hypothesis is presented with a corresponding null hypothesis and a proposed methodology for testing.

---

### **1. Foundational Analysis: Tracking Movie Genre Popularity and Quality**

**Research Question:** How have the popularity (median vote count) and average quality (median rating) of major *movie* genres evolved over the last three decades?

- **Hypothesis (H1):** The popularity (median `numVotes`) and quality (median `averageRating`) of major movie genres show significant positive or negative trends over the last 30 years, demonstrating a shift in audience preference.
- **Null Hypothesis (H0):** There are no significant long-term trends; any changes in genre popularity or quality are random or cyclical.
- **Methodology:**
    1. Filter the dataset for `titleType == 'movie'` and `startYear` (e.g., >= 1995) (**Data Preprocessing**).
    2. Group the data by `startYear` and `primary_genre` (**Aggregation**).
    3. Calculate the `Median` `averageRating` and `Median` `numVotes` for each group (**Summary Statistics**).
    4. Plot these two metrics over time using a `Line Plot` (**Visualization Techniques**), with a separate line (hue) for each major genre.
    5. Our conclusion will be based on the visual inspection of these trends.

### **2. TV Show "Rating Decay": Analyzing Quality Over Time**

**Research Question:** Do long-running TV series suffer from "rating decay"? We will analyze the average rating of episodes by season number to see if quality (rating) consistently drops in later seasons.

- **Hypothesis (H1):** Long-running TV series (e.g., 8+ seasons) show a significant negative trend (decay) in their `Mean` `averageRating` as the `seasonNumber` increases.
- **Null Hypothesis (H0):** There is no significant negative correlation between `seasonNumber` and `Mean` `averageRating`; the quality remains stable or random.
- **Methodology:**
    1. Identify a list of popular, long-running `tvSeries` from `title.basics`.
    2. Join with `title.episode` (on `parentTconst`) and `title.ratings` (on the *episode's* `tconst`) (**Data Preprocessing**).
    3. Group the data by series (e.g., `parentTconst`) and `seasonNumber` (**Aggregation**).
    4. Calculate the `Mean` `averageRating` for each season of each show (**Summary Statistics**).
    5. Plot `seasonNumber` (x-axis) vs. `Mean` `averageRating` (y-axis) using a `Line Plot` (**Visualization Techniques**), with a separate line for each show.
    6. Our conclusion will be based on the visual inspection of a downward trend in the plots.

### **3. The "Genre Hybridity" Paradox**

**Research Question:** Does increasing genre complexity (e.g., *Horror-SciFi-Comedy*) correlate with higher audience engagement, or does it result in diminishing returns compared to "pure" single-genre films?

- **Hypothesis (H1):** We hypothesize that "Genre Purity" (a single genre tag) correlates with a **higher `Mean` `averageRating`** and **lower `Variance`** than "Genre Hybridity" (3+ genre tags) within the same primary genre.
- **Null Hypothesis (H0):** There is **no significant difference** in the `Mean` or `Variance` of `averageRating` between "Pure" and "Hybrid" films.
- **Methodology:**
    1. Engineer `genre_count` and `genre_type` (e.g., 'Pure', 'Hybrid') features (**Feature Creation** / **Discretization**).
    2. Group the data by `primary_genre` (**Aggregation**).
    3. For each group, calculate the **Summary Statistics** (specifically `Mean` and `Variance`) for `averageRating` for both 'Pure' and 'Hybrid' films.
    4. Create side-by-side **Box Plots** (**Visualization**) to visually compare the median, quartiles, and range of the two groups. Our conclusion will be based on this descriptive and visual analysis.

### **4. The "Cross-Cultural Breakout" Formula**

**Research Question:** What metadata "fingerprints" distinguish Non-US/Non-English films that achieve mainstream global popularity (Top 10% vote count) from those that remain regionally confined?

- **Hypothesis (H1):** A classifier can identify non-US "breakout" films with low **Classification Error**. We hypothesize that a combination of **`genre`** (e.g., 'Action') and **`runtimeMinutes`** will be the most predictive features, identifiable by a **Decision Tree**.
- **Null Hypothesis (H0):** A classifier will perform no better than a random baseline, and the **Classification Error** will be high, indicating no predictable "fingerprint."
- **Methodology:**
    1. Create the binary target `is_breakout` (**Feature Creation / Binarization**).
    2. Train a **Random Forest Classifier** (**Ensemble Methods**) to predict this target.
    3. Address the **Class Imbalance Problem** using techniques like **Sampling**.
    4. Evaluate the model using **k-fold Cross-Validation** and its average **Classification Error**.
    5. To find the "fingerprint," separately build a **Decision Tree Classifier** and inspect its root node and first-level branches.

### **5. Predicting "Expectation Mismatch" (The High-Profile Flop)**

**Research Question:** Can we predict a "flop," defined as a movie with high-value inputs (e.g., "Top-Tier" director/cast) that *fails* to achieve a high audience rating (e.g., `averageRating` < 6.0)?

- **Hypothesis (H1):** A classifier can identify "High-Profile Flops" with a low **Classification Error** for the minority 'flop' class. We hypothesize that specific **`genres`** (e.g., Comedy) and extreme **`runtimeMinutes`** will be key predictors.
- **Null Hypothesis (H0):** No metadata features can reliably predict a flop given high-value inputs; these failures are random and the model's **Classification Error** will be high.
- **Methodology:**
    1. Engineer binary features `is_high_profile` and `is_flop` (**Feature Creation / Binarization**).
    2. We will train and compare several classifiers, such as a **Naive Bayes Classifier** and a **Random Forest Classifier**.
    3. We will use techniques to address the severe **Class Imbalance Problem**.
    4. We will evaluate the models using **Cross-Validation** and **Classification Error**, paying special attention to the error on the 'flop' class.
