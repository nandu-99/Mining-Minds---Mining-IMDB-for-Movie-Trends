import streamlit as st
import pandas as pd

st.set_page_config(page_title="Research Overview", layout="wide")
st.sidebar.image("./streamlit_app/assets/logo.png", width="content")

st.title("Movie & TV Show Analysis: Research Overview")
st.markdown("Comprehensive analysis of film industry trends, patterns, and insights")

st.markdown("---")

st.subheader("Research Objectives")

col1, col2 = st.columns(2)

with col1:
    # Objective 1
    with st.expander("Objective 1: Genre Evolution Over Time", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** How have genres and subgenres changed in popularity over time?")
        st.markdown("**Analysis Page:** Genre Popularity Tracker")
        
        obj1_insights = pd.DataFrame({
            "Insight": [
                "Ratings have stayed mostly stable for all genres since 1995",
                "Documentaries show highest quality but lowest popularity",
                "Mystery, Adventure, and Crime are popular but only moderately rated",
                "Horror has the lowest ratings yet keeps steady audience interest"
            ]
        })
        st.dataframe(obj1_insights, width="stretch", hide_index=True)

    # Objective 3
    with st.expander("Objective 3: Budget vs Performance Relationship", expanded=False):
        st.error("NOT COMPLETED")
        st.markdown("**Question:** Is there a relationship between budget and audience ratings (or gross earnings)?")
        st.markdown("**Analysis Page:** Budget vs Performance")
        
        obj3_insights = pd.DataFrame({
            "Insight": [
                "No budget or revenue fields were available in datasets",
                "Financial comparisons could not be performed"
            ]
        })
        st.dataframe(obj3_insights, width="stretch", hide_index=True)
        st.error("**Limitations:** Budget and earnings data were missing.")

    # Objective 5
    with st.expander("Objective 5: Critics vs Audience Ratings", expanded=False):
        st.error("NOT COMPLETED")
        st.markdown("**Question:** How do critic ratings compare with audience ratings?")
        st.markdown("**Analysis Page:** Critics vs Audience")
        
        obj4_insights = pd.DataFrame({
            "Insight": [
                "Only audience ratings were available in data",
                "No critic scores were included",
                "Direct comparison could not be performed"
            ]
        })
        st.dataframe(obj4_insights, width="stretch", hide_index=True)
        st.error("**Limitations:** Critic Ratings data were missing.")

with col2:
    # Objective 2
    with st.expander("Objective 2: Regional Rating Patterns", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** Do movies from certain regions get higher ratings, and what drives global reach?")
        st.markdown("**Analysis Page:** Regional Analysis")
        
        obj5_insights = pd.DataFrame({
            "Insight": [
                "Global movies release across many countries and languages",
                "Hybrid-genre films perform better internationally",
                "Action, Comedy, Crime, and Thriller dominate global hits",
                "Regional films rate higher but draw fewer viewers"
            ]
        })
        st.dataframe(obj5_insights, width="stretch", hide_index=True)

    # Objective 4
    with st.expander("Objective 4: Interactive Director Visualization", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** Build an interactive visualization to explore top movies by director.")
        st.markdown("**Analysis Page:** Director Showcase")
        
        obj7_insights = pd.DataFrame({
            "Insight": [
                "Users can select a director interactively",
                "Top 3 movies displayed by rating and runtime",
                "Easy visual comparison of filmographies"
            ]
        })
        st.dataframe(obj7_insights, width="stretch", hide_index=True)

    # Objective 6
    with st.expander("Objective 6: Predictive & Descriptive Analysis", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** Perform predictive and descriptive analysis on movie success.")
        st.markdown("**Analysis Page:** Predictive Models")
        
        obj8_insights = pd.DataFrame({
            "Insight": [
                "Director and Cast Career Scores added as key features",
                "Leakage controls removed one-hit career bias",
                "Advanced evaluation added ROC-AUC and Macro F1 metrics",
                "Final model reached 80.65% accuracy with 0.89 ROC-AUC"
            ]
        })
        st.dataframe(obj8_insights, width="stretch", hide_index=True)

st.markdown("---")

st.subheader("Core Research Questions")

col3, col4 = st.columns(2)

with col3:
    # RQ1
    with st.expander("Research Question 1: Tracking Movie Genre Popularity and Quality", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** How have popularity (median votes) and quality (median ratings) evolved by genre?")
        st.markdown("**Analysis Page:** Genre Evolution Timeline")
        
        rq1_insights = pd.DataFrame({
            "Insight": [
                "Ratings stayed highly stable across all genres",
                "Audience votes became more volatile after early-2000 peaks",
                "Documentaries lead quality but trail popularity",
                "Popular genres retain only mid-level ratings"
            ]
        })
        st.dataframe(rq1_insights, width="stretch", hide_index=True)

    # RQ2
    with st.expander("Research Question 2: TV Show Rating Decay", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** Do TV series lose rating quality across seasons?")
        st.markdown("**Analysis Page:** TV Series Rating Decay")
        
        rq2_insights = pd.DataFrame({
            "Insight": [
                "Average ratings remain stable from seasons 1 to 10",
                "About half of shows show small rating declines",
                "Many series improve or remain steady",
                "Strong rating decay is uncommon"
            ]
        })
        st.dataframe(rq2_insights, width="stretch", hide_index=True)

    with st.expander("Research Question 5: Predicting Expectation Mismatch", expanded=False):
        st.error("NOT COMPLETED")
        st.markdown("**Question:** Can we predict a 'High-Profile Flop' — movies with top-tier directors and casts that still end up with low audience ratings (averageRating < 6.0)?")
        st.markdown("**Analysis Page:** Expectation Mismatch Analysis")
        
        rq5_insights = pd.DataFrame({
            "Insight": [
                "High-profile flops require budget or scale indicators to validate expectations",
                "Talent scores alone are insufficient without production investment data",
                "No budget dataset was available to define true expectation mismatch"
            ]
        })
        st.dataframe(rq5_insights, width="stretch", hide_index=True)
        st.error("**Limitations:** Budget data was missing.")


with col4:
    # RQ3
    with st.expander("Research Question 3: The Genre Hybridity Paradox", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** Do multi-genre movies perform better than single-genre titles?")
        st.markdown("**Analysis Page:** Genre Hybridity Explorer")
        
        rq3_insights = pd.DataFrame({
            "Insight": [
                "Hybrid movies outperform pure-genre films on popularity",
                "Comedy, Action, and Drama benefit most from mixing genres",
                "Multi-genre titles reach wider global audiences",
                "Genre blending supports engagement growth"
            ]
        })
        st.dataframe(rq3_insights, width="stretch", hide_index=True)

    # RQ4
    with st.expander("Research Question 4: The Cross-Cultural Breakout Formula", expanded=False):
        st.success("COMPLETE")
        st.markdown("**Question:** What makes some movies succeed worldwide while others remain regional?")
        st.markdown("**Analysis Page:** Cross-Cultural Success Patterns")
        
        rq4_insights = pd.DataFrame({
            "Insight": [
                "Worldwide release increases global visibility",
                "Hybrid genres attract broader international audiences",
                "Action, Crime, Comedy, and Adventure dominate global hits",
                "Local films rate higher but remain niche"
            ]
        })
        st.dataframe(rq4_insights, width="stretch", hide_index=True)

st.markdown("---")

st.subheader("Analysis Design & Methodology")

with st.expander("Methodology Overview", expanded=False):
    st.markdown("**Purpose:** Describe how data was collected, cleaned, and analyzed to produce insights.")
    
    methodology_insights = pd.DataFrame({
        "Insight": [
            "Used IMDb dataset with 12M+ titles and key metadata fields",
            "Cleaned year outliers and handled missing runtime values",
            "Created stratified 200K title sample for balanced analysis",
            "Combined descriptive trends with Phase-3 predictive modeling"
        ]
    })
    st.dataframe(methodology_insights, width="stretch", hide_index=True)

st.markdown("---")
