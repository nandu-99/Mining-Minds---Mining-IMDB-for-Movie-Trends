# **Data Preprocessing Plan**

This document details the complete **data preprocessing pipeline** for the *"Mining IMDb for Movie Trends"* project.
The goal is to transform the raw IMDb `.tsv` relational datasets into a single, clean, and analysis-ready master dataset that can directly support the hypotheses defined in [`Hypotheses.md`](docs/hypothesis.md).

---

## 1. **Objectives**

1. **Integrate** multiple IMDb datasets (`title.basics`, `title.ratings`, `title.principals`, `name.basics`, `title.akas`) into a unified schema.
2. **Clean, normalize, and enrich** data for analytical and predictive modeling tasks.
3. **Engineer derived features** (e.g., career averages, popularity thresholds, genre aggregations).
4. **Prepare modular, reusable datasets** aligned with each hypothesis domain:

    * Audience Dynamics & Star Power
    * Cultural Influence & Linguistic Bias
    * Predictive Modeling
    * Temporal Trends

---

## 2. **Source Datasets**

| Dataset | Description | Key Fields Used |
| :--- | :--- | :--- |
| `title.basics.tsv` | Core metadata about titles | `tconst`, `primaryTitle`, `titleType`, `startYear`, `runtimeMinutes`, `genres` |
| `title.ratings.tsv` | IMDb user ratings | `tconst`, `averageRating`, `numVotes` |
| `title.principals.tsv` | Links between titles and people (actors, directors, etc.) | `tconst`, `nconst`, `category` |
| `name.basics.tsv` | Personal info (names, careers) | `nconst`, `primaryName`, `birthYear`, `primaryProfession` |
| `title.akas.tsv` | Alternate titles with regional/language info | `tconst`, `region`, `language`, `title` |

---

## 3. **Data Cleaning & Standardization**

### 3.1 Missing Values

| Field | Handling Strategy |
| :--- | :--- |
| `runtimeMinutes` | Replace `\N` with median runtime per genre |
| `genres` | Drop if missing; not useful for modeling |
| `startYear` | Drop if missing or invalid (non-numeric) |
| `averageRating` / `numVotes` | Drop rows with missing ratings |
| `region`, `language` | Keep `Unknown` placeholder if missing |

### 3.2 Type Conversion

* Convert numeric columns (`startYear`, `runtimeMinutes`, `averageRating`, `numVotes`) to appropriate numeric types.
* Split `genres` into multiple rows (1 genre per row) using **explode** technique for genre-level analysis.

### 3.3 Filtering for Relevant Titles

Keep only:

* `titleType` ∈ { "movie" }
* `startYear` ≥ 1950 (to avoid incomplete early data)
* `numVotes` ≥ 100 (to exclude irrelevant, low-visibility titles)

### 3.4 Deduplication

* Remove duplicate `tconst` entries across joins.
* Retain only the **primary title** per `tconst` from `title.akas` (`isOriginalTitle = 1` preferred).

---

## 4. **Data Integration Steps**

1.  **Join** `title.basics` (filtered) $\leftrightarrow$ `title.ratings` on `tconst` to create a base `movies_df`.
2.  **Pre-process `title.akas`** to get one primary `region`/`language` per `tconst`, then left join to `movies_df`.
3.  **Process `title.principals` and `name.basics` separately** to create aggregated features (e.g., `career_avg_rating`).
4.  **Join** the final aggregated features from step 3 back to the main `movies_df` (maintaining one row per movie).

Final integrated table schema (simplified):

| tconst | title | startYear | runtimeMinutes | genres | averageRating | numVotes | region | language | director_nconst | actor_nconst | director_name | actor_name |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

---

## 5. **Feature Engineering**

| Feature | Description | Relevant Hypotheses |
| :--- | :--- | :--- |
| `career_avg_rating` | Mean rating across all films by a person (`nconst`) | H1 (Star Power) |
| `career_film_count` | Number of films linked to that person | H1 |
| `director_tier` / `actor_tier` | Categorical: Top-Tier / Mid-Tier / Novice (based on thresholds) | H1 |
| `is_popular` | Binary: 1 if `numVotes > 25,000`, else 0 | H3 |
| `genre_primary` | First listed genre (after exploding) | H2, H8 |
| `runtime_bin` | Categorized runtime (<80, 80–100, 100–120, 120–150, >150) | H2 |
| `decade` | Group `startYear` into decades | H8 |
| `normalized_votes` | log-transform of `numVotes` for regression stability | H3, H6 |
| `rating_zscore` | Standardized rating across all films | H4–H6 |
| `region_code` | Encoded numerical region (via label encoding) | H4–H5 |
| `language_code` | Encoded numerical language | H5–H6 |

---

## 6. **Outlier Handling**

| Field | Detection Method | Handling |
| :--- | :--- | :--- |
| `runtimeMinutes` | IQR method | Clip to [5th, 95th] percentile |
| `numVotes` | Log-transform | Maintain distributional balance |
| `averageRating` | Winsorize (1st–99th percentile) | Reduce extreme influence |

---

## 7. **Dataset Splitting for Hypothesis Testing**

To support modular analysis, generate separate filtered datasets:

| Dataset | Target Hypotheses | Key Columns |
| :--- | :--- | :--- |
| `df_star_power` | H1 | `nconst`, `director_tier`, `actor_tier`, `averageRating`, `genres`, `startYear` |
| `df_runtime_genre` | H2 | `runtimeMinutes`, `averageRating`, `genre_primary` |
| `df_popularity_model` | H3, H6, H7 | `is_popular`, `numVotes`, `startYear`, `genres`, `region`, `runtimeMinutes` |
| `df_region_language` | H4, H5 | `region`, `language`, `averageRating`, `genre_primary` |
| `df_temporal_trends` | H8 | `startYear`, `genre_primary`, `averageRating`, `numVotes` |

---

## 8. **Normalization & Feature Scaling**

Before modeling, the following preprocessing step from the syllabus will be applied where necessary:

1.  **Feature Scaling:** Apply `StandardScaler` to numerical features (e.g., `runtimeMinutes`, `numVotes`) for regression-based hypotheses to ensure all features contribute equally.

---

## 9. **Output Artifacts**

| Artifact | Description | Format |
| :--- | :--- | :--- |
| `clean_master.csv` | Final cleaned integrated dataset | CSV |
| `df_star_power.csv` | Dataset for Star Power & Audience analysis | CSV |
| `df_runtime_genre.csv` | Dataset for runtime–rating analysis | CSV |
| `df_popularity_model.csv` | Dataset for predictive modeling | CSV |
| `df_region_language.csv` | Dataset for regional & linguistic analysis | CSV |
| `df_temporal_trends.csv` | Dataset for trend visualization | CSV |

All outputs will be stored in the `/processed_data/` directory.

---

## 1. **Reproducibility & Automation**

* All preprocessing steps will be scripted in **Python (Pandas)**, wrapped into modular functions.
* A top-level orchestrator script (`preprocess.py`) will:

    1. Load raw `.tsv` files.
    2. Apply cleaning, integration, and feature engineering.
    3. Generate hypothesis-specific datasets.
    4. Log dataset statistics (rows, nulls, distributions) for reproducibility.

---

## 11. **Next Steps**

1. Finalize schema validation on a sample of 100K records.
2. Implement the preprocessing pipeline using Jupyter Notebook or a modular Python script.
3. Conduct exploratory data analysis (EDA) using the cleaned datasets.
4. Proceed to statistical tests and modeling as per [`hypotheses.md`](docs/hypothesis.md).

---

### Deliverable Summary

| Stage | Deliverable | Output |
| :--- | :--- | :--- |
| Data Ingestion | Raw IMDb `.tsv` load | Pandas DataFrames |
| Data Cleaning | Standardized dataset | `clean_master.csv` |
| Feature Engineering | Derived variables | Updated DataFrames |
| Hypothesis Prep | Modular datasets | Per-hypothesis CSVs |
| Quality Assurance | EDA summary logs | `.ipynb` or `.md` reports |

---
