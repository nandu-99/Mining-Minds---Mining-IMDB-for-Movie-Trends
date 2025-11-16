This review analyzes the foundational paper "IMDb Data from Two Generations (1979 to 2019)" (Bahraminasr and Vafaei-Sadr, 2020), which serves as a primary academic justification for our project.

**Citation:** Bahraminasr, A., & Vafaei-Sadr, A. (2020). *IMDb Data from Two Generations (1979 to 2019).* arXiv:2005.14147v3 [[cs.CY](http://cs.cy/)].

---

## 1. Overview of the Paper

This article presents a comprehensive, custom-scraped IMDb-based dataset of over 79,000 titles from 1979 to 2019. The authors compiled rich metadata (genres, MPAA certificates, release years, countries, languages, etc.) and user-generated information (ratings, number of votes, demographic voting patterns). Using statistical analysis, the study reveals important trends in film ratings, vote distributions, and demographic influences on audience reception. This paper provides a foundational analysis for subsequent explorations into movie success factors.

---

## 2. Source Reliability and Authenticity

This paper is considered a reliable academic source for our project. It was published on **arXiv (arXiv:2005.14147v3)**, a standard, highly-respected open-access repository for preprints in computer science, mathematics, and related fields. Its public availability, clear methodology, and citable (scholarly) nature make it an appropriate foundation for our literature review.

Source Link: https://arxiv.org/pdf/2005.14147

---

## 3. Key Findings from the Paper

The authors' analysis of the 12-page paper revealed several key findings that validate our project's core assumptions.

- **Finding 1: Metadata Patterns are Measurable:** The study confirms that metadata has a measurable relationship with ratings. For example, the paper finds clear differences in average ratings by **MPAA certificate** ("Movies with general audience receive the highest mean IMDb rating, 6.39") and by **Genre** ("The three most highly scored genres in IMDb are Drama, Comedy, and Action").
- **Finding 2: Temporal Trends are Significant:** The paper proves that movie production (FIG. 1), vote counts (FIG. 2), and average ratings (FIG. 4) all show clear trends over time. For instance, the number of titles produced annually grew steadily until a peak in 2017.
- **Finding 3: Demographic & Regional Bias is Proven:** A core finding is the demonstrable difference in rating behavior between demographic groups.
    - **Gender:** Females tend to give slightly higher scores than males (FIG. 4, FIG. 5), while males constitute the largest portion of voters (FIG. 2).
    - **Region:** A clear rating bias exists between **US and Non-US voters** (FIG. 8, FIG. 9).
    - **Algorithm Bias:** The paper notes that the final "IMDb rating" is more correlated with Non-US voters and male voters than other groups.
- **Finding 4: Not All Metadata is Equally Predictive:** The paper's correlation analysis on "Parental Guide" items (like "Sex & Nudity," "Violence & Gore") found an "almost-zero correlation" with ratings (FIG. 7). This suggests that simple linear correlations are not enough to find value, and more complex modeling is needed.
- **Finding 5: Temporal Genre Trends are Explicitly Confirmed:** The paper's analysis explicitly confirms that genre popularity and ratings are not static. It notes a "descending trend of fantasy genre since 1994" and an "increasing the percentage of documentary... overtime". It also provides a baseline for genre quality, noting that "Drama, Comedy, and Action" are among the most highly scored.

---

## 4. Identified Research Gaps

While the paper provides a solid foundation, its primary value is in the **research gaps** it leaves open. Our project is designed to fill these gaps.

- **Gap 1: Simplistic Genre Analysis:** The paper's analysis of genre is limited to basic statistics. It identifies the most frequent or "most highly scored genres" but treats them in isolation. It **does not** analyze the effect of **genre combinations** (e.g., Horror-SciFi-Comedy).
- **Gap 2: The "Individual" Analysis Failure:** This is the paper's most significant gap. The authors *failed* to meaningfully analyze the impact of "Director, Writers, Stars". They explicitly state the data is "some random string" and they "do not have a lot of data to assign them a value or a vector". Their only solution was a weak proxy: "the number of google results".
- **Gap 3: Identified Bias, But No Solution:** The paper *proves* a measurable rating bias exists between "US and Non-US voters" (Finding 3). It identifies the *problem* (the bias) but does not explore the *solution* (i.e., what makes a non-US film successful *despite* the bias).
- **Gap 4: Exclusive Focus on Movies, Ignoring TV Series:** The paper's analysis is entirely focused on *movies*. It provides no insights into the trends or quality patterns of *TV Series* or *episodes* (e.g., season-by-season quality), which is a major, unanalyzed part of the IMDb dataset.

---

---

## 5. Justification for Our Project's Research Questions

This paper's findings and gaps provide the direct inspiration for our 6 research questions. We are using their work as a foundation to either formalize their basic findings or fill the innovative gaps they left open.

| Our Research Question | Justification based on the Literature Review |
| --- | --- |
| **Q1: Tracking Movie Genre Popularity** | **Builds on Finding 5:** The paper *confirms* that temporal genre trends exist. Our question formalizes this by creating a comprehensive, side-by-side visualization of *both* popularity (votes) and quality (rating) over time. |
| **Q2: TV Show "Rating Decay"** | **Fills Gap 4:** This is a *new area of inquiry* not covered by the paper. Our question extends the paper's temporal analysis methods (used for movies) to this entirely different and unanalyzed dataset (TV Series). |
| **Q3: The "Genre Hybridity" Paradox** | **Builds on Gap 1:** The paper's analysis stops at single-genre statistics. Our question explores the *interaction effects* and *combinations* of genres, a more complex analysis the paper did not attempt. |
| **Q4: The "Creative Hierarchy"** | **Fills Gap 2:** The paper *gave up* on analyzing creative roles, calling them a "random string". Our question uses a superior methodology (ML) to *solve* this problem and rank the "Creative Hierarchy." |
| **Q5: The "Cross-Cultural Breakout"** | **Solves Gap 3:** The paper *identified* the problem (US vs. Non-US bias). Our question builds the *solution*: a predictive model to find the "fingerprints" of non-US films that *overcome* this bias. |
| **Q6: The "High-Profile Flop"** | **Fills Gap 2:** The paper's inability to quantify "high-value inputs" (like a top-tier director) made this risk model impossible. By solving the "Star Power" problem, we can now build this high-value model. |

## 6. Conclusion and Project Scope

The Bahraminasr (2020) paper is the ideal academic foundation for our project. It validates our basic premises (e.g., metadata is predictive, regional bias exists) while leaving clear, high-value research gaps that our project is designed to fill.

The paper's focus on a *demographic* dataset (age/gender) which we lack, combined with its *failure* to analyze *individuals* (actors/directors), gives our project a clear and innovative focus. We will leverage the official IMDb datasets to conduct the sophisticated, role-based metadata analysis that this paper proved was a missing piece of the puzzle.