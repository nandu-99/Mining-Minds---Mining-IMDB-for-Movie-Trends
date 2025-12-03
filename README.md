# Mining IMDb for Movie Trends (Data Mining Project)

## Problem Statement

The movie industry is influenced by several factors such as genres, budgets, directors, actors, and audience preferences.
This project aims to analyze IMDb datasets to uncover **patterns and trends** that drive a movie’s success — identifying what truly impacts ratings, popularity, and long-term audience interest.

---

## Objectives

1. Analyze how **genres** and **themes** have evolved over time.
2. Identify directors and actors who consistently achieve higher ratings.
3. Examine the relationship between **budget, runtime, and audience rating**.
4. Compare **critic vs. audience preferences**.
5. Explore **regional differences** in movie ratings and production.
6. Investigate how **runtime** or **release year** correlates with popularity.
7. Create an **interactive visualization** to explore top-rated movies by director or genre.

---

## Dataset

**Source:** [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/)

We are using the following files from the official IMDb dataset:

| File Name                 | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| `title.akas.tsv.gz`       | Contains alternative titles and regional information      |
| `title.basics.tsv.gz`     | Core details like title, year, runtime, and genres        |
| `title.crew.tsv.gz`       | Lists directors and writers for each title                |
| `title.episode.tsv.gz`    | Links episodes to their respective series                 |
| `title.principals.tsv.gz` | Key cast and crew for each title                          |
| `title.ratings.tsv.gz`    | IMDb user ratings and number of votes                     |
| `name.basics.tsv.gz`      | Contains information about actors, directors, and writers |

---

## Repository Structure (Detailed)

```
imdb-movie-trends
 ┣ 📂 data
 ┃ ┣ 📂 raw
 ┃ ┣ 📂 processed
 ┣ 📂 notebooks
 ┣ 📂 docs
 ┃ ┣ team_roles_and_rotation.md       # Roles, leadership, responsibilities
 ┃ ┣ literature_review.md             # Related research summary
 ┃ ┣ research_questions.md            # Core exploratory questions and rationale
 ┃ ┣ hypotheses.md                    # Hypotheses to be tested from the data
 ┃ ┣ eda_&_visualization_plan.md      # Planned methodology and analysis approach
 ┃ ┣ data_dictionary.md               # Field descriptions from all IMDb files
 ┃ ┣ data_preprocessing_plan.md     
 ┃ ┣ progress_log.md                  # Progress log of complete project
 ┣ 📂 reports
 ┣ 📂 streamlit_app
 ┣ README.md                       # Project overview (this file)
 ┣ requirements.txt                # Python dependencies and environment setup
 ┗ .gitignore                      # Files and folders to ignore in Git
```

## Quick Access to Key Documentation

- [Progress Log](./docs/progress_log.md)  
- [Literature Review](./docs/literature_review.md)  
- [Research Questions](./docs/research_questions.md)  
- [Hypotheses](./docs/hypotheses.md) 
- [Data Dictionary](./docs/data_dictionary.md)


---

## Streamlit Dashboard

**Live App:**
[https://mining-minds-imdb.streamlit.app/](https://mining-minds-imdb.streamlit.app/)

**Dashboard Screenshot:**
<img width="1440" height="813" alt="Screenshot 2025-12-03 at 8 06 04 PM" src="https://github.com/user-attachments/assets/65cbd845-e2b5-4ea8-a489-3f555f215cf5" />

---

## Team Members & Phase Contributions

| Name                   | Phase 1                                                                                  | Phase 2                                                                      | Phase 3                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Vivekananda (Lead)** | Repo setup, folder structure, dataset preparation, contributed across all planning tasks | Complete EDA, descriptive analysis, insight generation                       | EDA refinements, Streamlit dashboard development, key research questions |
| **Prashant**           | Literature review, research questions, hypothesis design                                 | Workflow planning, task coordination, predictive analysis                    | Predictive modeling, report preparation, documentation                   |
| **Prerak**             | Data preprocessing, model training plan                                                  | Refining research questions, research methodology, Streamlit app development | Workflow planning, coordination, key question contributions              |

---

**Leadership Rotation Plan:**

* **Phase 1 Lead:** Vivekananda
* **Phase 2 Lead:** Prashant
* **Phase 3 Lead:** Prerak

---

## Workflow & GitHub Usage

* **Branch Naming Convention:**
  `name/issue-number-description` → e.g., `vivek/issue-02-readme`
* **Commit Format:**
  `Added README.md with problem statement and objectives (#2)`
* **Issue Tracking:**
  Each major task is tracked as a GitHub Issue linked to a PR.
* **Kanban Workflow:**
  To Do → In Progress → In Review → Done

**Kanban Board:** [View Project Board](https://github.com/users/nandu-99/projects/2)
![Kanban Board](https://cdn.shopify.com/s/files/1/0868/4250/7448/files/kanban-board.png?v=1761656895)

---

## Phase Overview

| Phase       | Focus Area               | Key Deliverables                                         |
| ----------- | ------------------------ | -------------------------------------------------------- |
| **Phase 1** | Project Setup & Planning | Repo setup, dataset download, research plan, hypotheses  |
| **Phase 2** | Analysis & Exploration   | Data cleaning, EDA, visualization, trend discovery       |
| **Phase 3** | Modeling & Insights      | Predictive model, dashboard, final report & presentation |

---

