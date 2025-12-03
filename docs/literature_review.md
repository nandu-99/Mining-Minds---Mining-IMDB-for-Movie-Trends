# **Literature Review**

This review analyzes two foundational papers that form the academic basis for our project: **Bahraminasr & Vafaei-Sadr (2020)**, which provides the contextual framework for our trend analysis, and **Asad et al. (2012)**, which provides the methodological validation for our predictive modeling.

---

## **Part 1: Contextual Foundation**

**Citation:** Bahraminasr, A., & Vafaei-Sadr, A. (2020). *IMDb Data from Two Generations (1979 to 2019).* arXiv:2005.14147v3 [cs.CY].

### **1. Overview of the Paper**
This article presents a comprehensive, custom-scraped IMDb-based dataset of over 79,000 titles from 1979 to 2019. The authors compiled rich metadata (genres, MPAA certificates, release years, countries, languages, etc.) and user-generated information (ratings, number of votes, demographic voting patterns). Using statistical analysis, the study reveals important trends in film ratings, vote distributions, and demographic influences on audience reception. This paper provides a foundational analysis for subsequent explorations into movie success factors.

### **2. Source Reliability and Authenticity**
This paper is considered a reliable academic source for our project. It was published on **arXiv (arXiv:2005.14147v3)**, a standard, highly-respected open-access repository for preprints in computer science, mathematics, and related fields. Its public availability, clear methodology, and citable (scholarly) nature make it an appropriate foundation for our literature review.

**Source Link:** https://arxiv.org/pdf/2005.14147

### **3. Key Findings from the Paper**
The authors' analysis of the 12-page paper revealed several key findings that validate our project's core assumptions.

* **Finding 1: Metadata Patterns are Measurable:** The study confirms that metadata has a measurable relationship with ratings. For example, the paper finds clear differences in average ratings by **MPAA certificate** and by **Genre**.
* **Finding 2: Temporal Trends are Significant:** The paper proves that movie production (FIG. 1), vote counts (FIG. 2), and average ratings (FIG. 4) all show clear trends over time.
* **Finding 3: Demographic & Regional Bias is Proven:** A core finding is the demonstrable difference in rating behavior between **US and Non-US voters** (FIG. 8, FIG. 9).
* **Finding 4: Not All Metadata is Equally Predictive:** The paper's correlation analysis on "Parental Guide" items found an "almost-zero correlation" with ratings (FIG. 7), suggesting that simple linear correlations are not enough to find value.
* **Finding 5: Temporal Genre Trends are Explicitly Confirmed:** The paper's analysis explicitly confirms that genre popularity and ratings are not static, noting a "descending trend of fantasy genre since 1994" and an "increasing percentage of documentary."

### **4. Identified Research Gaps**
While the paper provides a solid foundation, its primary value is in the **research gaps** it leaves open. Our project is designed to fill these gaps.

* **Gap 1: Simplistic Genre Analysis:** The paper's analysis of genre is limited to basic statistics. It **does not** analyze the effect of **genre combinations** (e.g., Horror-SciFi-Comedy).
* **Gap 2: The "Individual" Analysis Failure:** This is the paper's most significant gap. The authors *failed* to meaningfully analyze the impact of "Director, Writers, Stars," stating they "do not have a lot of data to assign them a value."
* **Gap 3: Identified Bias, But No Solution:** The paper *proves* a measurable rating bias exists between "US and Non-US voters" but does not explore the *solution* (i.e., what makes a non-US film successful *despite* the bias).
* **Gap 4: Exclusive Focus on Movies:** The paper provides no insights into the trends or quality patterns of **TV Series**, which is a major part of the IMDb dataset.

---

## **Part 2: Methodological Validation**

**Citation:** Asad, K. I., Ahmed, T., & Rahman, M. S. (2012). *Movie Popularity Classification based on Inherent Movie Attributes using C4.5, PART and Correlation Coefficient.* IEEE/OSA/IAPR International Conference on Informatics, Electronics & Vision.

### **1. Overview of the Paper**
Unlike the first paper which focused on broad trends, Asad et al. (2012) explicitly executed a predictive model to classify movies into success tiers. They utilized the **C4.5 Decision Tree** algorithm (J4.8) on a dataset of ~1,000 movies to predict whether a movie would be "Excellent," "Average," "Poor," or "Terrible."

**Source Link:** https://ieeexplore.ieee.org/document/6317401

### **2. Key Findings & Inputs for Our Project**
This paper provides the **technical blueprint** for our predictive modeling phase (Phase 2 & 3).

* **Input 1: Validation of Classification Strategy:** The paper successfully converted continuous ratings into discrete classes (e.g., Excellent ≥ 7.5) and achieved **~77% accuracy**. This validates our project's decision to use **Multi-Class Classification** (Low/Medium/High) rather than regression for rating prediction.
* **Input 2: Validation of Decision Trees:** The authors chose Decision Trees for their interpretability. This supports our use of **Decision Tree** and **Random Forest** classifiers to extract rules and feature importance.
* **Input 3: The "Director Rank" Discovery:** The most critical finding was that **Director Rank** was the single most important attribute for classification (Information Gain: 92.36%). This insight directly influenced our strategy to **improve model accuracy in Phase 3** by engineering the high-value **"Star Power" features** (`director_score` and `cast_score`), moving beyond simple metadata.

---

## **6. Synthesis: Justification for Our Project's Research Questions**

We combine the *contextual gaps* from Bahraminasr (2020) with the *methodological proofs* from Asad et al. (2012) to fully justify our six research questions.

| Our Research Question | Justification based on Literature Review |
| :--- | :--- |
| **Q1: Tracking Movie Genre Popularity** | **Builds on Bahraminasr Finding 5:** The paper *confirms* that temporal genre trends exist. Our question formalizes this by creating a comprehensive, side-by-side visualization of *both* popularity and quality over time. |
| **Q2: TV Show "Rating Decay"** | **Fills Bahraminasr Gap 4:** This is a *new area of inquiry* not covered by the paper. Our question extends the paper's temporal analysis methods to the unanalyzed TV Series dataset. |
| **Q3: The "Genre Hybridity" Paradox** | **Builds on Bahraminasr Gap 1:** The paper's analysis stops at single-genre statistics. Our question explores the *interaction effects* and *combinations* of genres. |
| **Q4: The "Cross-Cultural Breakout"** | **Solves Bahraminasr Gap 3:** The paper *identified* the problem (US vs. Non-US bias). Our question builds the *solution*: a predictive model to find the "fingerprints" of non-US films that *overcome* this bias. |
| **Q5: The "High-Profile Flop"** | **Builds on Asad et al. (Input 3):** Since Asad et al. proved that High Director Rank *should* predict success, a movie with a Top-Tier Director that *fails* is a significant anomaly. This justifies our risk assessment model. |

---

## **7. Conclusion and Project Scope**

By synthesizing these two papers, our project stands on a robust academic foundation. **Bahraminasr (2020)** provides the broad dataset and identifies the key gaps (lack of individual analysis, regional bias). **Asad et al. (2012)** provides the solution: it proves that **Classification Models** and **Director Ranking** are effective tools. We leverage the official IMDb datasets to apply Asad's proven methodology (Decision Trees/Feature Importance) to fill Bahraminasr's identified gaps, creating a scalable framework for analyzing genre evolution, talent impact, and risk.
