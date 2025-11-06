# **Literature Review**

This review analyzes the foundational paper "IMDb Data from Two Generations (1979 to 2019)" (Bahraminasr and Vafaei-Sadr, 2020), which serves as a primary academic justification for our project.

**Citation:** Bahraminasr, A., & Vafaei-Sadr, A. (2020). *IMDb Data from Two Generations (1979 to 2019).* arXiv:2005.14147v3 [cs.CY].

---

## 1. Overview of the Paper

This article presents the largest and most comprehensive IMDb-based dataset available to date, encompassing over 79,000 titles from 1979 to 2019. The authors compiled rich metadata and user-generated information covering movie titles, ratings, number of votes, demographic voting patterns, genres, MPAA certificates, parental guides, release years, countries, languages, and more. Using statistical and preliminary machine learning analyses, the study reveals important trends in film ratings, vote distributions, and demographic influences on the audience's reception of movies, providing a valuable resource for deeper research into movie popularity and quality factors. This paper serves as a foundational dataset introduction and preliminary analysis for subsequent detailed explorations into movie success factors.

---

## 2. Source Reliability and Authenticity

This paper is considered a reliable academic source for our project. It was published on **arXiv (arXiv:2005.14147v3)**, a standard, highly-respected open-access repository for preprints in computer science, mathematics, and related fields. Its public availability, clear methodology, and citable (scholarly) nature make it an appropriate foundation for our literature review.

Source Link: https://arxiv.org/pdf/2005.14147

---

## 3. Key Findings & Inputs from the Paper

The authors' analysis revealed several key "inputs" that directly informed our project's direction:

* **Input 1: Metadata Shows Clear Patterns with Ratings:** The study confirms that metadata has a measurable relationship with ratings. For example, the paper finds clear differences in average ratings by **MPAA certificate** ("Movies with general audience receive the highest mean IMDb rating, 6.39") and by **Genre** ("The three most highly scored genres in IMDb are Drama, Comedy, and Action").
* **Input 2: Temporal Trends are Significant:** The paper (e.g., FIG. 1, FIG. 3) proves that movie production, vote counts, and average ratings all show clear trends over time.
* **Input 3: Regional Bias is a Measurable Factor:** A core finding (e.g., FIG. 8, FIG. 9) is the demonstrable difference in rating behavior between **US and Non-US voters**.
* **Input 4: A Gap in the Research (Individuals):** The paper's analysis focuses on *demographic* groups (age, gender, region) but does not investigate the influence of *specific individuals*. While it collects "Director, Writers, Stars" data, it treats them as "some random string" and only uses "number of google results" as a proxy. This is a clear gap in their analysis.

---

## 4. Justification for Our Project's Research Questions

This paper's inputs provided the direct inspiration for our 8 research questions. We are using their findings as a starting point to ask deeper, more focused questions.

| Our Research Question | Input from the Article (The "Why") |
| :--- | :--- |
| **H1: Impact of Star Power** | **Input 4 (Research Gap):** The paper analyzed demographic groups but not the impact of *individuals*. This led us to ask if we could measure the "Star Power" of specific actors/directors. |
| **H2: Runtime Optimization** | **Input 1 (Metadata Patterns):** The paper showed that metadata like `genre` and `MPAA rating` have clear patterns with average scores. This led us to ask if we could find a deeper pattern for `runtime` within specific genres. |
| **H3: Predicting Popularity** | **Input 2 (Temporal Trends):** The paper tracks `numVotes` over time. This led us to ask if we could use this data to *predict* if a movie will become popular, treating it as a classification problem. |
| **H4: Regional Rating Bias** | **Input 3 (Regional Bias Exists):** The paper *proved* bias exists between "US vs. Non-US" voters. This led us to ask if we could find a similar bias based on the movie's *production region*. |
| **H5: Language Impact** | **Input 1 & 3 (Metadata & Bias):** Since `country` and `language` are collected and regional bias is proven, we were led to ask if `language` *by itself* is a significant factor, separate from the production region. |
| **H6: Key Drivers of Rating** | **Input 1 (Metadata Patterns):** The paper confirmed that metadata is predictive (e.g., `genre`, `MPAA rating`). This led us to ask which of our available metadata features are the *strongest* or most important drivers of a movie's rating. |
| **H7: Model Comparison** | **Input 1 (Metadata Patterns):** Since the data is predictive, we wanted to know *how* predictive. This led us to ask if a complex model (Random Forest) would be significantly better than a simple one (Ridge Regression). |
| **H8: Genre Trends Over Time** | **Input 2 (Temporal Trends):** The paper *proved* that ratings and production change over time. This led us to combine this with `genre` data to ask how *specific genres* have changed in popularity and quality. |

---

## 5. Conclusion and Project Scope

This paper is the ideal starting point for our review. It confirms our project is well-founded and that our research questions are built upon existing academic findings.

It also highlights a **critical limitation and focus** for our project. The paper's most novel insights come from a custom-scraped dataset with *age and gender demographics*, which we do not have. Because we are limited to the official IMDb datasets, our project must compensate by focusing *more deeply* on the rich *structured metadata* that *is* available: actor/director influence (H1), runtime optimization (H2), and regional/language data (H4, H5). This paper validates our approach while also clearly defining our project's unique boundaries.
