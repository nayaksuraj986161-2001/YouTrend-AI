import streamlit as st
from components.footer import footer

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About YouTrend AI")

st.markdown("""
## Global YouTube Trending Analytics Platform
""")

st.write("""
YouTrend AI is an end-to-end data analytics and machine learning platform
developed to analyze global YouTube trending videos.

The project combines data engineering, visualization, machine learning,
natural language processing, and business intelligence into one interactive
dashboard.
""")

st.divider()

# -------------------------------------------------

c1, c2 = st.columns(2)

with c1:

    st.subheader("🎯 Objectives")

    st.markdown("""
- Analyze global YouTube trending videos

- Predict trending potential

- Discover audience behavior

- Perform NLP on video titles

- Generate business insights

- Build interactive dashboards
""")

with c2:

    st.subheader("🛠 Technologies Used")

    st.markdown("""
- Python

- Pandas

- NumPy

- Scikit-Learn

- Plotly

- Streamlit

- SQL

- Power BI

- NLP (TF-IDF)

- Random Forest
""")

st.divider()

st.subheader("📂 Dataset")

st.info("""
Global YouTube Trending Dataset

• 357,772+ Records

• 10 Countries

• 50+ Features

• Millions of YouTube videos analyzed
""")

st.divider()

st.subheader("🤖 Machine Learning Models")

st.markdown("""
✔ Logistic Regression

✔ Decision Tree

✔ Random Forest Classifier

✔ TF-IDF Vectorizer

✔ Upload Time Prediction Model
""")

st.divider()

st.markdown("""
<h2 style="font-size:34px;font-weight:700;">
💼 Business Applications
</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.success("""
### Marketing

• Content Strategy

• Audience Analysis

• Campaign Planning

• Trend Discovery
""")

with col2:
    st.info("""
### Business Intelligence

• KPI Monitoring

• Country-wise Insights

• Category Performance

• AI-based Prediction
""")
st.divider()

st.markdown("""
<h2 style="font-size:34px;font-weight:700;">
Future Enhancements
</h2>
""", unsafe_allow_html=True)

st.write("""
- Live YouTube Data Integration

- Real-time Trend Prediction

- Deep Learning Models

- Sentiment Analysis of Comments

- Recommendation System

- Cloud Deployment

- Mobile Dashboard
""")

st.divider()

st.success("""
Project Developed as an End-to-End Data Analytics & Machine Learning Project
using Python, SQL, Power BI, NLP and Streamlit.
""")
footer()