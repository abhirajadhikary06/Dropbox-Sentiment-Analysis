# src/app.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from textblob import TextBlob
import pandas as pd

from utils.database import get_reviews_for_sentiment

st.set_page_config(
    page_title="Dropbox Analysis - Airbyte Hackathon",
    page_icon="🗳️",
    layout="wide",
)

# Title and description
st.markdown(
    """
    <h1>🗳️<span style='color:#0061FE'>Dropbox</span> Reviews Sentiment Analysis</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    This dashboard provides deep insights into the sentiment of Dropbox app reviews.
    """
)

# Sidebar filters
st.sidebar.header("Filters")
sentiment_type = st.sidebar.selectbox(
    "Sentiment Analysis Type",
    options=["Polarity", "Subjectivity"],
    index=0  # This sets "Polarity" as the default selection
)

# Fetch reviews
reviews_df = get_reviews_for_sentiment()

# Perform sentiment analysis
def get_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity if sentiment_type == "Polarity" else blob.sentiment.subjectivity

reviews_df['sentiment'] = reviews_df['content'].apply(get_sentiment)

# Top metrics
col1, col2, col3 = st.columns(3)

with col1:
    avg_sentiment = reviews_df['sentiment'].mean()
    st.metric(f"Average {sentiment_type}", f"{avg_sentiment:.2f}")

with col2:
    positive_reviews = (reviews_df['sentiment'] > 0).sum()
    st.metric("Positive Reviews", f"{positive_reviews} ({positive_reviews/len(reviews_df)*100:.1f}%)")

with col3:
    negative_reviews = (reviews_df['sentiment'] < 0).sum()
    st.metric("Negative Reviews", f"{negative_reviews} ({negative_reviews/len(reviews_df)*100:.1f}%)")

# Sentiment Distribution Chart
st.header("📊 Sentiment Distribution")
fig_sentiment_dist = px.histogram(
    reviews_df, 
    x='sentiment', 
    title=f'{sentiment_type} Distribution',
    labels={'sentiment': f'{sentiment_type} Score'},
    color_discrete_sequence=['#0061FE']
)
st.plotly_chart(fig_sentiment_dist, use_container_width=True)

# Sentiment by Rating
st.header("⭐ Sentiment by Rating")
sentiment_by_rating = reviews_df.groupby('score')['sentiment'].mean().reset_index()

# Custom colors for scores 1-5
bar_colors = ['#D3DDEF', '#748CB2', '#3B6FC3', '#0061FF', '#003A98']

# Create figure with custom colored bars
fig_sentiment_rating = go.Figure(
    go.Bar(
        x=sentiment_by_rating['score'],
        y=sentiment_by_rating['sentiment'],
        marker_color=bar_colors,
        hovertemplate='Score: %{x}<br>Average Sentiment: %{y:.2f}<extra></extra>'
    )
)

# Update layout
fig_sentiment_rating.update_layout(
    title=f'{sentiment_type} by Review Score',
    xaxis_title='Review Score',
    yaxis_title=f'Average {sentiment_type}',
    showlegend=False,
    hoverlabel=dict(
        bgcolor="#0E1117",
        font=dict(color="#FAFAFA")
    )
)

st.plotly_chart(fig_sentiment_rating, use_container_width=True)

# Sample Reviews
st.header("📝 Sample Reviews")
sentiment_categories = pd.cut(
    reviews_df['sentiment'], 
    bins=[-1, -0.5, 0.5, 1], 
    labels=['Negative', 'Neutral', 'Positive']
)
reviews_df['sentiment_category'] = sentiment_categories

for category in ['Negative', 'Neutral', 'Positive']:
    category_reviews = reviews_df[reviews_df['sentiment_category'] == category]
    if not category_reviews.empty:
        with st.expander(f"{category} Reviews"):
            sample_review = category_reviews.sample(min(5, len(category_reviews)))
            for _, review in sample_review.iterrows():
                st.write(f"Score: {review['score']} | Sentiment: {review['sentiment']:.2f}")
                st.write(review['content'])
                st.markdown("---")

# Footer
st.markdown("---")
st.markdown("""
    <center>
    <p>Sentiment Analysis of 📥 by <a href="https://github.com/abhirajadhikary06" style='color:#0061FF' target="_blank">abhirajadhikary06</a></p>
    </center>
""", unsafe_allow_html=True)