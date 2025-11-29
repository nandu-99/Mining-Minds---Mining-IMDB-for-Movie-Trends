import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import zipfile
import os

st.set_page_config(page_title="IMDb Dashboard", layout="wide")

# styles - css
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    h1 {
        color: #1f77b4;
        padding-bottom: 20px;
        border-bottom: 3px solid #1f77b4;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("IMDb Dashboard Overview")

st.sidebar.image("./streamlit_app/assets/logo.png", width="content")

# unzip file
ZIP_PATH = "./streamlit_app/data/homepage_master.zip"
CSV_PATH = "./streamlit_app/data/homepage_master.csv"

if not os.path.exists(CSV_PATH):
    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall("./streamlit_app/data")

# cache data
@st.cache_data
def load_homepage_data():
    return duckdb.read_csv(CSV_PATH).df()

@st.cache_data
def get_genre_df(df):
    return df["genres"].str.split(",").explode().reset_index(name="genre")

@st.cache_data
def get_yearly_counts(df):
    return (
        df.groupby(["startYear", "titleType"])
        .size()
        .reset_index(name="count")
    )

@st.cache_data
def get_rating_trend(df):
    return (
        df.groupby("startYear")["averageRating"]
        .mean()
        .reset_index()
    )

# loader
with st.spinner("Loading data..."):
    df = load_homepage_data()

# sidebar - global filters
with st.sidebar:
    st.header("Filters")
    year_min = int(df["startYear"].min())
    year_max = int(df["startYear"].max())

    selected_years = st.slider(
        "Year Range",
        year_min, year_max,
        (year_min, year_max)
    )

    title_options = ["All"] + sorted(df["titleType"].unique())
    selected_title_type = st.selectbox("Title Type", title_options)

    all_genres = sorted(df["genres"].str.split(",").explode().unique())
    selected_genres = st.multiselect("Genres", all_genres)

filtered_df = df[
    (df["startYear"] >= selected_years[0]) &
    (df["startYear"] <= selected_years[1])
]

if selected_title_type != "All":
    filtered_df = filtered_df[filtered_df["titleType"] == selected_title_type]

if selected_genres:
    filtered_df = filtered_df[
        filtered_df["genres"].apply(
            lambda x: any(g in x.split(",") for g in selected_genres)
        )
    ]

# helper function
def format_number(num):
    if num >= 1_000_000_000:
        return f"{num/1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"{num/1_000_000:.2f}M"
    elif num >= 1_000:
        return f"{num/1_000:.2f}K"
    else:
        return str(num)

# key statistics
st.write("")
with st.expander("Key Statistics", expanded=True):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        movies_count = filtered_df[filtered_df["titleType"] == "movie"].shape[0]
        st.metric("Movies", f"{movies_count:,}", delta="Total Films")

    with col2:
        tv_count = filtered_df[
            filtered_df["titleType"].isin(["tvSeries", "tvMiniSeries"])
        ].shape[0]
        st.metric("TV Shows", f"{tv_count:,}", delta="Series & Mini-Series")

    with col3:
        title_types = filtered_df["titleType"].nunique()
        st.metric("Title Types", title_types, delta="Unique Categories")

    with col4:
        genres_count = (
            filtered_df["genres"].str.split(",").explode().nunique()
        )
        st.metric("Genres", genres_count, delta="Unique Genres")

# performance metrics
with st.expander("Performance Metrics", expanded=True):

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        avg_rating = round(filtered_df["averageRating"].mean(), 2)
        st.metric("Average Rating", f"{avg_rating} / 10", delta="Overall Score")

    with col6:
        total_votes = int(filtered_df["numVotes"].sum())
        st.metric("Total Votes", format_number(total_votes), delta="Community Engagement")

    with col7:
        directors_count = (
            filtered_df["directors"].str.split(",").explode().nunique()
        )
        st.metric("Directors", f"{directors_count:,}", delta="Unique Directors")

    with col8:
        actors_count = (
            filtered_df["actors"].str.split(",").explode().nunique()
        )
        st.metric("Actors", f"{actors_count:,}", delta="Unique Actors")

st.markdown("---")

# trends over time
st.subheader("Trends Over Time")

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    yearly_counts = get_yearly_counts(filtered_df)

    fig_count = px.line(
        yearly_counts,
        x="startYear",
        y="count",
        color="titleType",
        markers=True,
        labels={"startYear": "Year", "count": "Number of Titles"},
        title="Title Types Released Over Time"
    )

    st.plotly_chart(fig_count, width = 'content')

with row1_col2:
    rating_trend = get_rating_trend(filtered_df)

    fig_rating = px.line(
        rating_trend,
        x="startYear",
        y="averageRating",
        markers=True,
        labels={"startYear": "Year", "averageRating": "Average Rating"},
        title="Average IMDb Rating Over Time"
    )

    st.plotly_chart(fig_rating, width = 'content')

st.markdown("---")

# distributions
st.subheader("Distributions")

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    genre_df = get_genre_df(filtered_df)
    genre_counts = (
        genre_df.groupby("genre").size().reset_index(name="count")
    )

    fig_genre = px.treemap(
        genre_counts,
        path=["genre"],
        values="count",
        title="Genre Distribution"
    )
    
    fig_genre.update_layout(
        title_font_size=18,
        title_font_color="#2c3e50",
        font=dict(size=13, color="#2c3e50", family="Arial"),
        margin=dict(t=50, l=10, r=10, b=10)
    )
    
    fig_genre.update_traces(
        textposition="middle center",
        textfont=dict(size=12),
        hovertemplate="<b>%{label}</b><br>Count: %{value}<extra></extra>",
        marker=dict(line=dict(width=1))
    )

    st.plotly_chart(fig_genre, width = 'content')

with row2_col2:
    fig_hist = px.histogram(
        filtered_df,
        x="averageRating",
        nbins=20,
        labels={"averageRating": "IMDb Rating"},
        title="Rating Distribution"
    )
    
    fig_hist.update_layout(
        title_font_size=18,
        title_font_color="#2c3e50",
        font=dict(size=12, color="#34495e"),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            title_font=dict(size=14, color="#2c3e50")
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            title_text="Count",
            title_font=dict(size=14, color="#2c3e50")
        ),
        plot_bgcolor="rgba(0,0,0,0)",
        bargap=0.1
    )
    
    fig_hist.update_traces(
        marker=dict(
            line=dict(width=1.5, color="white"),
            opacity=0.85
        ),
        hovertemplate="<b>Rating:</b> %{x}<br><b>Count:</b> %{y}<extra></extra>"
    )

    st.plotly_chart(fig_hist, width = 'content')

st.markdown("---")
