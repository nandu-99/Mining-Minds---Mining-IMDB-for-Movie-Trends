import streamlit as st
import duckdb
import plotly.express as px

st.set_page_config(page_title="Director Movie Explorer", layout="wide")

@st.cache_data
def load_data():
    return duckdb.read_csv("data/raw/processed/director_movies_filter.csv").df()

df = load_data()

st.title("Director Movie Explorer")
st.write("Select a director to view their top 3 movies based on IMDb rating.")

# Sidebar
st.sidebar.header("Filters")


directors = sorted(df["director"].unique())
selected_director = st.sidebar.selectbox("Select Director", directors)

# Top 3 movies
top3 = (
    df[df["director"] == selected_director]
    .sort_values("averageRating", ascending=False)
    .head(3)
)

if top3.empty:
    st.warning("No movies found for this director.")
else:
    fig = px.bar(
        top3,
        x="primaryTitle",
        y="averageRating",
        text="averageRating",
        labels={
            "primaryTitle": "Movie Title",
            "averageRating": "Rating"
        },
        title=f"Top 3 IMDb Rated Movies by {selected_director}"
    )
    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, width="stretch")

    st.subheader("Movie Details")
    st.dataframe(top3, width="stretch")
