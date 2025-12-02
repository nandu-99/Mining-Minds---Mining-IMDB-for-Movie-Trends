import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Genre Hybridity Explorer", layout="wide")

st.markdown("""
<style>
.main {
    padding: 0rem 1rem;
}
.stMetric {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.header("Genre Hybridity Paradox Explorer")
st.markdown("Explore whether genre blending improves popularity and quality.")

@st.cache_data
def load_data():
    return pd.read_csv("./streamlit_app/data/genre_hybridity_master.csv")

df = load_data()

con = duckdb.connect()
con.register("movies", df)

genres = sorted(
    set(
        g.strip()
        for row in df['genres']
        for g in row.split(",")
    )
)

st.markdown("---")

st.subheader("Select Genre for Analysis")

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    base_genre = st.selectbox(
        "Primary Genre",
        genres,
        index=genres.index("Drama") if "Drama" in genres else 0
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    compare_mode = st.checkbox("Enable Comparison", value=False)
    
with col3:
    if compare_mode:
        compare_genre = st.selectbox(
            "Secondary Genre",
            [g for g in genres if g != base_genre],
            index=0
        )
    else:
        compare_genre = None

def get_genre_combinations(genre, hybridity_level):
    if hybridity_level == "Pure":
        query = f"""
            SELECT genres, COUNT(*) as count,
                   ROUND(AVG(averageRating), 2) as avg_rating,
                   ROUND(AVG(votes_per_year), 2) as avg_votes
            FROM movies
            WHERE genres = '{genre}' AND hybridity_bucket = 'Pure'
            GROUP BY genres
            ORDER BY count DESC
        """
    elif hybridity_level == "Hybrid-2":
        query = f"""
            SELECT genres, COUNT(*) as count,
                   ROUND(AVG(averageRating), 2) as avg_rating,
                   ROUND(AVG(votes_per_year), 2) as avg_votes
            FROM movies
            WHERE genres LIKE '%{genre}%' AND hybridity_bucket = 'Hybrid-2'
            GROUP BY genres
            ORDER BY count DESC
            LIMIT 3
        """
    else:
        query = f"""
            SELECT genres, COUNT(*) as count,
                   ROUND(AVG(averageRating), 2) as avg_rating,
                   ROUND(AVG(votes_per_year), 2) as avg_votes
            FROM movies
            WHERE genres LIKE '%{genre}%' AND hybridity_bucket = 'Hybrid-3+'
            GROUP BY genres
            ORDER BY count DESC
            LIMIT 3
        """
    return con.execute(query).fetchdf()

def compute_hybridity_stats(genre):
    query = f"""
        SELECT
            hybridity_bucket,
            COUNT(*) AS movie_count,
            ROUND(MEDIAN(averageRating), 3) AS median_rating,
            ROUND(MEDIAN(votes_per_year), 2) AS median_votes_year,
            ROUND(STDDEV(averageRating), 3) AS rating_std
        FROM movies
        WHERE genres LIKE '%{genre}%'
        GROUP BY hybridity_bucket
        ORDER BY hybridity_bucket
    """
    return con.execute(query).fetchdf()

def find_best_category(stats):
    best_rating_idx = stats['median_rating'].idxmax()
    best_votes_idx = stats['median_votes_year'].idxmax()
    
    best_rating_cat = stats.loc[best_rating_idx, 'hybridity_bucket']
    best_votes_cat = stats.loc[best_votes_idx, 'hybridity_bucket']
    
    if best_rating_cat == best_votes_cat:
        return best_rating_cat, "both"
    else:
        return best_rating_cat, best_votes_cat

def display_genre_analysis(genre, show_title=True):
    if show_title:
        st.markdown("---")
        st.subheader(f"📊 {genre} Analysis")
    
    stats = compute_hybridity_stats(genre)
    
    best_cat, performance = find_best_category(stats)
    
    if performance == "both":
        st.success(f"**{genre}** performs best in **{best_cat}** for both Quality and Popularity")
    else:
        st.info(f"**{genre}** has best Quality in **{best_cat}** and best Popularity in **{performance}**")
    
    st.markdown("### Performance Summary")
    
    summary_data = []
    for _, row in stats.iterrows():
        bucket = row['hybridity_bucket']
        summary_data.append({
            "Category": bucket,
            "Movies": int(row['movie_count']),
            "Median Rating": row['median_rating'],
            "Votes/Year": row['median_votes_year'],
            "Rating STD": row['rating_std']
        })
    
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, width="stretch", hide_index=True)

    with st.expander("Top Genre Combinations", expanded=False):
        
        all_combos = []
        
        pure_combos = get_genre_combinations(genre, "Pure")
        if len(pure_combos) > 0:
            pure_combos['Category'] = 'Pure'
            all_combos.append(pure_combos)
        
        hybrid2_combos = get_genre_combinations(genre, "Hybrid-2")
        if len(hybrid2_combos) > 0:
            hybrid2_combos['Category'] = 'Hybrid-2'
            all_combos.append(hybrid2_combos)
        
        hybrid3_combos = get_genre_combinations(genre, "Hybrid-3+")
        if len(hybrid3_combos) > 0:
            hybrid3_combos['Category'] = 'Hybrid-3+'
            all_combos.append(hybrid3_combos)
        
        if all_combos:
            combined_df = pd.concat(all_combos, ignore_index=True)
            display_df = combined_df[['Category', 'genres', 'count', 'avg_rating', 'avg_votes']].rename(columns={
                'genres': 'Genre Combination',
                'count': 'Movies',
                'avg_rating': 'Rating',
                'avg_votes': 'Votes/Year'
            })
            display_df['Movies'] = display_df['Movies'].astype(int)
            display_df['Votes/Year'] = display_df['Votes/Year'].round(1)
            st.dataframe(display_df, width="stretch", hide_index=True)
        else:
            st.write("No genre combinations found")

    st.markdown("---")
    
    st.markdown("### Visual Performance Analysis")
    
    colA, colB = st.columns(2)
    
    fig_combo = go.Figure()
    fig_combo.add_trace(go.Bar(
        x=stats['hybridity_bucket'],
        y=stats['median_rating'],
        name='Quality (Rating)',
        yaxis='y',
        marker_color="#DDF2EE",
    ))
    fig_combo.add_trace(go.Bar(
        x=stats['hybridity_bucket'],
        y=stats['median_votes_year'],
        name='Popularity (Votes/Year)',
        yaxis='y2',
        marker_color="#9FCED1",
    ))

    
    fig_combo.update_layout(
        title=f"{genre}: Quality vs Popularity",
        xaxis=dict(title='Category'),
        yaxis=dict(title='Median Rating', side='left'),
        yaxis2=dict(title='Median Votes/Year', overlaying='y', side='right'),
        barmode='group',
        hovermode='x unified'
    )
    
    colA.plotly_chart(fig_combo, width="stretch")
    
    fig_bubble = px.scatter(
        stats,
        x="median_votes_year",
        y="median_rating",
        size="movie_count",
        text="hybridity_bucket",
        title=f"{genre}: Quality vs Popularity Map",
        labels={
            "median_votes_year": "Popularity (Votes/Year)",
            "median_rating": "Quality (Rating)"
        },
        color_continuous_scale="Teal",
        color="median_rating"
    )
    fig_bubble.update_traces(textposition="top center")
    colB.plotly_chart(fig_bubble, width="stretch")

    st.markdown("---")
    
    colC, colD = st.columns(2)

    
    
    fig_polar = px.bar(
        stats,
        x="hybridity_bucket",
        y="rating_std",
        title=f"{genre}: Audience Polarization",
        labels={"rating_std": "Rating STD"},
        color_continuous_scale="Teal",
        color="rating_std"
    )
    colC.plotly_chart(fig_polar, width="stretch")
    
    fig_count = px.bar(
        stats,
        x="hybridity_bucket",
        y="movie_count",
        title=f"{genre}: Movie Distribution",
        labels={"movie_count": "Number of Movies"}, 
        color_continuous_scale="Teal",
        color="movie_count"
    )
    colD.plotly_chart(fig_count, width="stretch")

    st.markdown("---")

if not compare_mode:
    display_genre_analysis(base_genre, show_title=False)
else:
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown(f"## {base_genre}")
        stats1 = compute_hybridity_stats(base_genre)
        best_cat1, perf1 = find_best_category(stats1)
        
        if perf1 == "both":
            st.success(f"Best in **{best_cat1}** for both")
        else:
            st.info(f"Quality: **{best_cat1}** | Popularity: **{perf1}**")
        
        summary_data1 = []
        for _, row in stats1.iterrows():
            summary_data1.append({
                "Category": row['hybridity_bucket'],
                "Movies": int(row['movie_count']),
                "Rating": row['median_rating'],
                "Votes/Yr": row['median_votes_year']
            })
        st.dataframe(pd.DataFrame(summary_data1), width="stretch", hide_index=True)
        
        
        st.markdown("#### Top Combinations")
        
        all_combos = []
        for level in ["Pure", "Hybrid-2", "Hybrid-3+"]:
            combos = get_genre_combinations(base_genre, level)
            if len(combos) > 0:
                combos['Category'] = level
                all_combos.append(combos.head(2))
        
        if all_combos:
            combined_combos = pd.concat(all_combos, ignore_index=True)
            display_df = combined_combos[['Category', 'genres', 'count', 'avg_rating', 'avg_votes']].rename(columns={
                'genres': 'Genre Combination',
                'count': 'Movies',
                'avg_rating': 'Rating',
                'avg_votes': 'Votes/Yr'
            })
            display_df['Movies'] = display_df['Movies'].astype(int)
            display_df['Votes/Yr'] = display_df['Votes/Yr'].round(1)
            st.dataframe(display_df, width="stretch", hide_index=True)
        else:
            st.write("No combinations found")
        
        fig1 = px.bar(
            stats1,
            x="hybridity_bucket",
            y=["median_rating", "median_votes_year"],
            title=f"{base_genre} Performance",
            barmode="group", 
            color_discrete_map={
                "median_rating": "#334F6A",
                "median_votes_year": "#9FCED1"
            }
        )
        st.plotly_chart(fig1, width="stretch")
    
    with col_right:
        st.markdown(f"## {compare_genre}")
        stats2 = compute_hybridity_stats(compare_genre)
        best_cat2, perf2 = find_best_category(stats2)
        
        if perf2 == "both":
            st.success(f"Best in **{best_cat2}** for both")
        else:
            st.info(f"Quality: **{best_cat2}** | Popularity: **{perf2}**")
        
        summary_data2 = []
        for _, row in stats2.iterrows():
            summary_data2.append({
                "Category": row['hybridity_bucket'],
                "Movies": int(row['movie_count']),
                "Rating": row['median_rating'],
                "Votes/Yr": row['median_votes_year']
            })
        st.dataframe(pd.DataFrame(summary_data2), width="stretch", hide_index=True)
        
        st.markdown("#### Top Combinations")
        
        all_combos = []
        for level in ["Pure", "Hybrid-2", "Hybrid-3+"]:
            combos = get_genre_combinations(compare_genre, level)
            if len(combos) > 0:
                combos['Category'] = level
                all_combos.append(combos.head(2))
        
        if all_combos:
            combined_combos = pd.concat(all_combos, ignore_index=True)
            display_df = combined_combos[['Category', 'genres', 'count', 'avg_rating', 'avg_votes']].rename(columns={
                'genres': 'Genre Combination',
                'count': 'Movies',
                'avg_rating': 'Rating',
                'avg_votes': 'Votes/Yr'
            })
            display_df['Movies'] = display_df['Movies'].astype(int)
            display_df['Votes/Yr'] = display_df['Votes/Yr'].round(1)
            st.dataframe(display_df, width="stretch", hide_index=True)
        else:
            st.write("No combinations found")
        
        fig2 = px.bar(
            stats2,
            x="hybridity_bucket",
            y=["median_rating", "median_votes_year"],
            title=f"{compare_genre} Performance",
            barmode="group", 
            color_discrete_map={
                "median_rating": "#334F6A",
                "median_votes_year": "#9FCED1"
            }
        )
        st.plotly_chart(fig2, width="stretch")
    
    st.markdown("---")
    st.markdown("### Direct Comparison")
    
    comparison_data = []
    for bucket in stats1['hybridity_bucket'].unique():
        row1 = stats1[stats1['hybridity_bucket'] == bucket].iloc[0] if bucket in stats1['hybridity_bucket'].values else None
        row2 = stats2[stats2['hybridity_bucket'] == bucket].iloc[0] if bucket in stats2['hybridity_bucket'].values else None
        
        comparison_data.append({
            "Category": bucket,
            f"{base_genre} Rating": row1['median_rating'] if row1 is not None else "-",
            f"{compare_genre} Rating": row2['median_rating'] if row2 is not None else "-",
            f"{base_genre} Votes": row1['median_votes_year'] if row1 is not None else "-",
            f"{compare_genre} Votes": row2['median_votes_year'] if row2 is not None else "-"
        })
    
    st.dataframe(pd.DataFrame(comparison_data), width="stretch", hide_index=True)
    
    combined_stats = pd.concat([
        stats1.assign(Genre=base_genre),
        stats2.assign(Genre=compare_genre)
    ])
    
    fig_compare = px.line(
        combined_stats,
        x="hybridity_bucket",
        y="median_rating",
        color="Genre",
        markers=True,
        title="Quality Comparison Across Categories", 
        color_discrete_sequence=["#334F6A", "#9FCED1"]
    )
    st.plotly_chart(fig_compare, width="stretch")

    st.markdown("---")
