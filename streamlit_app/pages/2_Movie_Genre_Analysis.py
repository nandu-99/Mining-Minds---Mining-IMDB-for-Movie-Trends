import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Movie Genre Analysis", layout="wide")
st.sidebar.image("./streamlit_app/assets/logo.png", width="content")

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
    .insight-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.header("Movie Genre Analysis: Popularity & Quality Over Time")
st.markdown("---")

@st.cache_data
def load_data():
    return pd.read_csv("./streamlit_app/data/genre_movies_sampled.csv")

with st.spinner("Loading data..."):
    df = load_data()

con = duckdb.connect()
con.register("movies", df)

genre_year_stats = con.execute("""
    SELECT
        genre,
        startYear,
        ROUND(MEDIAN(averageRating), 2) AS median_rating,
        ROUND(MEDIAN(numVotes), 2) AS median_votes,
        COUNT(*) AS movie_count
    FROM movies
    GROUP BY genre, startYear
    ORDER BY genre, startYear
""").fetchdf()

top_genres = (
    genre_year_stats.groupby("genre")["movie_count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index.tolist()
)

genre_year_top = genre_year_stats[genre_year_stats["genre"].isin(top_genres)]

st.write("")
with st.expander("Insights", expanded=True):
    st.write("• Median ratings have been stable for most genres since 1995.")
    st.write("• Audience engagement (median votes) has declined compared to the early 2000s.")
    st.write("• Documentaries have the highest median quality (~7.23) but lowest popularity.")
    st.write("• Mystery, Adventure, Crime are highly popular but moderately rated (~6.0).")
    st.write("• Horror is the lowest-rated genre (~4.89) but maintains moderate interest.")
    st.write("• Drama is the most produced genre (24.8% of total).")

with st.expander("Key Statistics", expanded=True):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Median Rating (All Data)", f"{df['averageRating'].median():.2f}")

    with col2:
        st.metric("Median Votes (All Data)", f"{df['numVotes'].median():.2f}")

    with col3:
        st.metric("Total Movies (Sampled)", f"{len(df):,}")

    with col4:
        st.metric("Top Genres Analyzed", len(top_genres))

st.markdown("---")

st.subheader("Median Rating Over Time (Top Genres)")

fig1 = px.line(
    genre_year_top,
    x="startYear",
    y="median_rating",
    color="genre",
    markers=True,
    labels={"startYear": "Year", "median_rating": "Median Rating", "genre": "Genre"}
)

fig1.update_layout(
    hovermode='x unified',
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02
    ),
    margin=dict(l=50, r=150, t=30, b=50)
)

fig1.update_traces(
    hovertemplate="Year: %{x}<br>Rating: %{y:.2f}"
)

fig1.update_yaxes(tickformat=".2f")

st.plotly_chart(fig1, width="stretch")

st.markdown("---")

st.subheader("Median Votes Over Time (Top Genres)")

fig2 = px.line(
    genre_year_top,
    x="startYear",
    y="median_votes",
    color="genre",
    markers=True,
    labels={"startYear": "Year", "median_votes": "Median Votes", "genre": "Genre"}
)

fig2.update_layout(
    hovermode='x unified',
    yaxis_range=[0, None],
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02
    ),
    margin=dict(l=50, r=150, t=30, b=50)
)

fig2.update_traces(
    hovertemplate="Year: %{x}<br>Votes: %{y:.2f}"
)

fig2.update_yaxes(tickformat=".2f")

st.plotly_chart(fig2, width="stretch")

st.markdown("---")

st.subheader("Popularity vs Quality")

genre_summary = (
    genre_year_top.groupby("genre").agg(
        avg_median_rating=("median_rating", "mean"),
        avg_median_votes=("median_votes", "mean")
    )
    .reset_index()
)

genre_summary["avg_median_rating"] = genre_summary["avg_median_rating"].round(2)
genre_summary["avg_median_votes"] = genre_summary["avg_median_votes"].round(2)

fig3 = px.scatter(
    genre_summary,
    x="avg_median_votes",
    y="avg_median_rating",
    color="genre",
    size="avg_median_votes",
    text="genre",
    labels={
        "avg_median_votes": "Avg Median Votes (Popularity)",
        "avg_median_rating": "Avg Median Rating (Quality)",
        "genre": "Genre"
    }
)

fig3.update_layout(
    xaxis_type="log",
    showlegend=False
)

fig3.update_traces(
    textposition='top center',
    hovertemplate="<b>%{text}</b><br>Votes: %{x:.2f}<br>Rating: %{y:.2f}<extra></extra>",
    marker=dict(line=dict(width=1, color='white'))
)

fig3.update_xaxes(tickformat=".2f")
fig3.update_yaxes(tickformat=".2f")

st.plotly_chart(fig3, width="stretch")

st.markdown("---")

st.subheader("Average Median Rating per Genre")

genre_summary_sorted = genre_summary.sort_values(
    by="avg_median_rating", ascending=False
)

fig4 = px.bar(
    genre_summary_sorted,
    x="genre",
    y="avg_median_rating",
    labels={"avg_median_rating": "Avg Median Rating", "genre": "Genre"}, 
    color="avg_median_rating",
    color_continuous_scale="Teal"

)

fig4.update_layout(
    showlegend=False,
    xaxis=dict(tickangle=-45)
)

fig4.update_traces(
    marker=dict(line=dict(width=1, color='white')),
    hovertemplate="<b>%{x}</b><br>Rating: %{y:.2f}<extra></extra>"
)

fig4.update_yaxes(tickformat=".2f")

st.plotly_chart(fig4, width="stretch")

st.markdown("---")

st.subheader("Genre Distribution in Dataset")

genre_counts = df['genre'].value_counts().reset_index()
genre_counts.columns = ['genre', 'movie_count']

top_n = 10
top_genres = genre_counts.head(top_n)
other_count = genre_counts.iloc[top_n:]['movie_count'].sum()

if other_count > 0:
    other_row = pd.DataFrame([{'genre': 'Other', 'movie_count': other_count}])
    genre_counts = pd.concat([top_genres, other_row], ignore_index=True)
else:
    genre_counts = top_genres

genre_counts['percentage'] = (genre_counts['movie_count'] / genre_counts['movie_count'].sum()) * 100

fig5 = px.pie(
    genre_counts,
    names='genre',
    values='movie_count',
    labels={'genre': 'Genre', 'movie_count': 'Number of Movies'},
    hole=0.3, 
)

fig5.update_traces(
    textinfo='percent+label',
    hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>"
)

st.plotly_chart(fig5, width="stretch")

st.markdown("---")
