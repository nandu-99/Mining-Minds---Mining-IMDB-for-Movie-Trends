import streamlit as st
import duckdb
import pandas as pd
import kagglehub
import os

@st.cache_resource
def download_kaggle_data():
    return kagglehub.dataset_download("vivekananda99/imdb-universal-search")

DATA_PATH = download_kaggle_data()

st.set_page_config(page_title="Universal Movie Search", layout="wide")
st.sidebar.image("./streamlit_app/assets/logo.png", width="content")

st.markdown("""
<style>
.main {
    padding: 0rem 1rem;
}
h1 {
    color: #1f77b4;
    padding-bottom: 15px;
    border-bottom: 2px solid #1f77b4;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("Universal Movie Search")

@st.cache_resource
def load_db():
    con = duckdb.connect()
    con.execute(f"""
        CREATE TABLE movies AS
        SELECT * FROM read_parquet('{DATA_PATH}/movies_master_clean.parquet');
    """)

    con.execute(f"""
        CREATE TABLE actors AS
        SELECT * FROM read_parquet('{DATA_PATH}/movie_actors.parquet');
    """)

    con.execute(f"""
        CREATE TABLE directors AS
        SELECT * FROM read_parquet('{DATA_PATH}/movie_directors.parquet');
    """)

    return con

con = load_db()

st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

search_query = st.text_input("Search by Movie, Actor, or Director")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    year_min, year_max = st.slider("Year", 1900, 2025, (1990, 2025))
with col2:
    min_rating = st.slider("Rating", 0.0, 10.0, 5.0)
with col3:
    min_votes = st.number_input("Min Votes", 0, 1000000, 1000, step=1000)
with col4:
    type_filter = st.selectbox("Type", ["All", "movie", "tvSeries"])
with col5:
    genre_filter = st.text_input("Genre contains")

page_size = 25

if "page" not in st.session_state:
    st.session_state.page = 1

where_clauses = []

if search_query:
    where_clauses.append(f"""
        (
            m.displayTitle ILIKE '%{search_query}%'
            OR m.tconst IN (SELECT tconst FROM actors WHERE actorName ILIKE '%{search_query}%')
            OR m.tconst IN (SELECT tconst FROM directors WHERE directorName ILIKE '%{search_query}%')
        )
    """)

where_clauses.append(f"m.startYear BETWEEN {year_min} AND {year_max}")
where_clauses.append(f"m.averageRating >= {min_rating}")
where_clauses.append(f"m.numVotes >= {min_votes}")

if type_filter != "All":
    where_clauses.append(f"m.titleType = '{type_filter}'")

if genre_filter:
    where_clauses.append(f"m.genres ILIKE '%{genre_filter}%'")

where_sql = " AND ".join(where_clauses)

offset = (st.session_state.page - 1) * page_size

query = f"""
WITH base AS (
    SELECT
        m.tconst,
        m.displayTitle,
        m.titleType,
        m.startYear,
        m.runtimeMinutes,
        m.genres,
        m.averageRating,
        m.numVotes
    FROM movies m
    WHERE {where_sql}
    ORDER BY m.averageRating DESC, m.numVotes DESC
    LIMIT {page_size}
    OFFSET {offset}
),
actors_ranked AS (
    SELECT
        a.tconst,
        a.actorName,
        ROW_NUMBER() OVER (
            PARTITION BY a.tconst
            ORDER BY a.actorName
        ) AS rn
    FROM actors a
    JOIN base b ON a.tconst = b.tconst
),
actors_agg AS (
    SELECT
        tconst,
        STRING_AGG(actorName, ', ') AS actors
    FROM actors_ranked
    WHERE rn <= 4
    GROUP BY tconst
),
directors_agg AS (
    SELECT
        d.tconst,
        STRING_AGG(d.directorName, ', ') AS directors
    FROM directors d
    JOIN base b ON d.tconst = b.tconst
    GROUP BY d.tconst
)
SELECT
    b.displayTitle,
    b.titleType,
    b.startYear,
    b.runtimeMinutes,
    b.genres,
    b.averageRating,
    b.numVotes,
    COALESCE(a.actors, '') AS Actors,
    COALESCE(d.directors, '') AS Directors
FROM base b
LEFT JOIN actors_agg a ON b.tconst = a.tconst
LEFT JOIN directors_agg d ON b.tconst = d.tconst;
"""

results = con.execute(query).df()

count_query = f"""
SELECT COUNT(*)
FROM movies m
WHERE {where_sql}
"""

total_results = con.execute(count_query).fetchone()[0]
total_pages = max((total_results - 1) // page_size + 1, 1)

st.markdown(f"### Results ({total_results:,} matches)")

if results.empty:
    st.warning("No results found.")
else:
    st.dataframe(results, width="stretch", hide_index=True)

st.markdown("---")

# Improved pagination
pagination_col1, pagination_col2, pagination_col3 = st.columns([1, 2, 1])

with pagination_col1:
    if st.button("<- Previous", disabled=st.session_state.page == 1, width="stretch"):
        st.session_state.page -= 1
        st.rerun()

with pagination_col2:
    st.markdown(
        f"<div style='text-align:center; font-size:16px; font-weight:600; padding-top:8px;'>Page {st.session_state.page} of {total_pages}</div>",
        unsafe_allow_html=True
    )

with pagination_col3:
    if st.button("Next ->", disabled=st.session_state.page >= total_pages, width="stretch"):
        st.session_state.page += 1
        st.rerun()
