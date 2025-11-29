import streamlit as st
import duckdb
import plotly.express as px

st.set_page_config(page_title="Director Movie Explorer", layout="wide")
st.sidebar.image("./streamlit_app/assets/logo.png", width="content")

# Custom CSS for better styling
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
    h3 {
        color: #2c3e50;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .stSelectbox {
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Director Movie Explorer")

@st.cache_data
def load_director_data():
    return duckdb.read_csv("./streamlit_app/data/director_movies_filter.csv").df()

with st.spinner("Loading data..."):
    df = load_director_data()

# Director Selection Section
st.markdown("### Select a Director")

col1, col2 = st.columns([2, 3])

with col1:
    directors = sorted(df["director"].unique())
    selected_director = st.selectbox("Choose from the list", directors, label_visibility="collapsed")

with col2:
    # Show director stats
    director_df = df[df["director"] == selected_director]
    if not director_df.empty:
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        with col_stat1:
            st.metric("Total Movies", len(director_df))
        with col_stat2:
            st.metric("Avg Rating", f"{director_df['averageRating'].mean():.2f}")
        with col_stat3:
            st.metric("Total Votes", f"{director_df['numVotes'].sum():,}")

st.markdown("---")

# Top Movies Section
top3 = (
    df[df["director"] == selected_director]
    .sort_values("averageRating", ascending=False)
    .head(3)
)

if top3.empty:
    st.warning("No movies found for this director.")
else:
    st.markdown("### Top Rated Movies")
    
    fig = px.bar(
        top3,
        x="primaryTitle",
        y="averageRating",
        text="averageRating",
        labels=dict(primaryTitle="Movie Title", averageRating="Rating"),
        title=f"Top Three IMDb Rated Movies by {selected_director}",
        color="averageRating",
        color_continuous_scale="Purp"
    )

    fig.update_traces(textposition="outside", texttemplate='%{text:.1f}')
    fig.update_layout(
        showlegend=False,
        xaxis_title="Movie Title",
        yaxis_title="IMDb Rating",
        title_font_size=16
    )
    st.plotly_chart(fig, width="stretch")

    st.markdown("---")
    
    st.markdown("### Movie Details")
    st.dataframe(top3, width="stretch", hide_index=True)

st.markdown("---")
