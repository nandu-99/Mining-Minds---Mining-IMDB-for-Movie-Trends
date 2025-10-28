# 🎬 IMDb Dataset — Data Dictionary

This document explains all IMDb data files and their corresponding columns, including data types, descriptions, and sample values.

---

## 📄 **1. title.akas.tsv.gz**

Alternate/localized titles for each film or show.

| **Column Name**     | **Data Type** | **Description**                                                                                                         | **Sample Values**                    |
| ------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **titleId**         | string        | Unique IMDb identifier (`tconst`) for the title                                                                         | `tt1375666`                          |
| **ordering**        | integer       | Unique row number for the given titleId                                                                                 | `1`, `2`                             |
| **title**           | string        | Localized title for the region                                                                                          | `Inception`, `Origen`                |
| **region**          | string        | Region code for this title version                                                                                      | `US`, `ES`, `IN`                     |
| **language**        | string        | Language of the title                                                                                                   | `en`, `es`, `hi`                     |
| **types**           | array         | Type of alternative title (e.g., `alternative`, `dvd`, `festival`, `tv`, `video`, `working`, `original`, `imdbDisplay`) | `["imdbDisplay"]`, `["alternative"]` |
| **attributes**      | array         | Additional terms describing this alternative title                                                                      | `["3D version"]`, `\N`               |
| **isOriginalTitle** | boolean       | `1` if original title, `0` otherwise                                                                                    | `1`, `0`                             |

---

## 🎥 **2. title.basics.tsv.gz**

Main metadata about each title.

| **Column Name**    | **Data Type** | **Description**                                                  | **Sample Values**              |
| ------------------ | ------------- | ---------------------------------------------------------------- | ------------------------------ |
| **tconst**         | string        | Unique IMDb identifier for the title                             | `tt0111161`                    |
| **titleType**      | string        | Type of content (e.g. `movie`, `short`, `tvSeries`, `tvEpisode`) | `movie`, `tvSeries`            |
| **primaryTitle**   | string        | Popular or promotional title                                     | `The Shawshank Redemption`     |
| **originalTitle**  | string        | Original title in its native language                            | `The Shawshank Redemption`     |
| **isAdult**        | boolean       | 1 = Adult title, 0 = Non-adult title                             | `0`, `1`                       |
| **startYear**      | integer       | Release year (or series start year)                              | `1994`, `2010`                 |
| **endYear**        | integer       | Series end year (else `\N`)                                      | `\N`, `2015`                   |
| **runtimeMinutes** | integer       | Runtime in minutes                                               | `142`, `89`                    |
| **genres**         | string array  | Up to three genres                                               | `Drama,Crime`, `Action,Sci-Fi` |

---

## 🎬 **3. title.crew.tsv.gz**

Information about directors and writers of each title.

| **Column Name** | **Data Type** | **Description**                      | **Sample Values**     |
| --------------- | ------------- | ------------------------------------ | --------------------- |
| **tconst**      | string        | Unique IMDb identifier for the title | `tt1375666`           |
| **directors**   | array         | Director(s) IMDb IDs (`nconst`)      | `nm0634240,nm0913389` |
| **writers**     | array         | Writer(s) IMDb IDs (`nconst`)        | `nm0634240`           |

---

## 📺 **4. title.episode.tsv.gz**

Episode-level details for TV series.

| **Column Name**   | **Data Type** | **Description**                    | **Sample Values** |
| ----------------- | ------------- | ---------------------------------- | ----------------- |
| **tconst**        | string        | Unique identifier of the episode   | `tt0959621`       |
| **parentTconst**  | string        | Identifier of the parent TV series | `tt0903747`       |
| **seasonNumber**  | integer       | Season number of the episode       | `2`               |
| **episodeNumber** | integer       | Episode number within the season   | `5`               |

---

## 🎭 **5. title.principals.tsv.gz**

Cast and crew roles in each title.

| **Column Name** | **Data Type** | **Description**                              | **Sample Values**              |
| --------------- | ------------- | -------------------------------------------- | ------------------------------ |
| **tconst**      | string        | Unique IMDb identifier of the title          | `tt1375666`                    |
| **ordering**    | integer       | Row identifier within the title              | `1`, `2`                       |
| **nconst**      | string        | Unique person identifier                     | `nm0000138`                    |
| **category**    | string        | Job category                                 | `actor`, `actress`, `director` |
| **job**         | string        | Specific job title (if available)            | `producer`, `\N`               |
| **characters**  | string        | Name of the character played (if applicable) | `["Dom Cobb"]`, `\N`           |

---

## ⭐ **6. title.ratings.tsv.gz**

Aggregated ratings and votes.

| **Column Name**   | **Data Type** | **Description**                     | **Sample Values**   |
| ----------------- | ------------- | ----------------------------------- | ------------------- |
| **tconst**        | string        | Unique IMDb identifier of the title | `tt0111161`         |
| **averageRating** | float         | Weighted average user rating (1–10) | `9.3`, `8.2`        |
| **numVotes**      | integer       | Total number of votes               | `2567389`, `879231` |

---

## 👤 **7. name.basics.tsv.gz**

Information about individuals in IMDb.

| **Column Name**       | **Data Type** | **Description**                                 | **Sample Values**               |
| --------------------- | ------------- | ----------------------------------------------- | ------------------------------- |
| **nconst**            | string        | Unique identifier of the person                 | `nm0000138`                     |
| **primaryName**       | string        | Name by which the person is most often credited | `Leonardo DiCaprio`             |
| **birthYear**         | integer       | Year of birth                                   | `1974`                          |
| **deathYear**         | integer       | Year of death, if applicable (`\N` otherwise)   | `\N`                            |
| **primaryProfession** | array         | Top 3 professions, comma-separated              | `actor,producer`                |
| **knownForTitles**    | array         | IMDb IDs of notable titles                      | `tt1375666,tt0993846,tt0407887` |

---

✅ **Purpose of Data Dictionary:**
This serves as a unified reference for all contributors to understand the IMDb dataset schema before performing cleaning, EDA, or modeling.

---
