import streamlit as st

from pathlib import Path
from components.hero import hero_section
from components.kpi_cards import show_kpi_cards
from components.navigation import navigation_cards


def load_css():

    css_path = Path(__file__).parent / "styles" / "style.css"

    with open(css_path) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="YouTrend AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

hero_section()

st.divider()

show_kpi_cards()

st.divider()

# ==========================================
# PROJECT STATISTICS
# ==========================================

st.subheader("📊 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📂 Dataset", "357,772")

with c2:
    st.metric("🌍 Countries", "10")

with c3:
    st.metric("🤖 ML Models", "3")

with c4:
    st.metric("📈 Features", "50+")

st.divider()

st.markdown("""
<h2 style="font-size:36px; font-weight:700;">
Project Highlights
</h2>
""", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    st.success("""
### 📊 Power BI Dashboard

Interactive dashboards with KPIs, trends and business insights.
""")

    st.success("""
### 🤖 Machine Learning

Predict trending potential using multiple ML algorithms.
""")

    st.success("""
### 🧠 NLP Analysis

Word Cloud, keyword extraction and title analysis.
""")

with right:

    st.info("""
### 🗄 SQL Analytics

Data extraction, cleaning and transformation using SQL.
""")

    st.info("""
### 🌍 Global Analysis

Analysis across 10 countries with millions of records.
""")

    st.info("""
### 🐍 Python Analytics

End-to-end data analysis using Pandas, NumPy and Plotly.
""")

st.divider()

st.subheader("⚙️ Project Workflow")

workflow = """
Dataset Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Machine Learning
        ↓
Natural Language Processing
        ↓
Business Intelligence Dashboard
        ↓
AI Prediction
"""

st.code(workflow)
st.divider()

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.success("""
### Programming

- Python
- Pandas
- NumPy
- SQL
""")

with tech2:
    st.info("""
### Machine Learning

- Random Forest
- Decision Tree
- Logistic Regression
- Scikit-Learn
""")

with tech3:
    st.warning("""
### Visualization

- Streamlit
- Plotly
- Power BI
- NLP
""")
    st.divider()

st.subheader("Key Features")

features = [
    "📊 Interactive Dashboard",
    "🤖 AI Trend Prediction",
    "🧠 NLP Analysis",
    "📈 Model Performance Evaluation",
    "🌍 Global Analytics",
    "📥 Export Ready Reports"
]

col1, col2 = st.columns(2)

for i, feature in enumerate(features):
    if i % 2 == 0:
        col1.markdown(f"{feature}")
    else:
        col2.markdown(f"{feature}")
st.divider()

st.caption(
    "YouTrend AI • Developed by Suraj Nayak • MBA • ABV-IIITM Gwalior • 2026"
)
