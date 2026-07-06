import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from components.footer import footer

st.set_page_config(
    page_title="NLP Analysis",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 NLP Analysis")

st.markdown("""
Analyze YouTube video titles using Natural Language Processing (NLP).
""")

st.divider()

# -----------------------------
# LOAD DATA
# -----------------------------

df = load_data()

# -----------------------------
# TITLE SEARCH
# -----------------------------

title = st.text_input(
    "Search any keyword",
    placeholder="Example: music"
)

if title:

    result = df[
        df["title"].str.contains(
            title,
            case=False,
            na=False
        )
    ]

    st.success(f"Found {len(result)} videos")

    st.dataframe(
        result[
            [
                "title",
                "Country",
                "category_name",
                "views"
            ]
        ].head(20),
        use_container_width=True
    )

st.divider()
# -----------------------------
# TOP CATEGORIES BY AVG VIEWS
# -----------------------------

st.subheader("📊 Average Views by Category")

category_views = (
    df.groupby("category_name")["views"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig = px.bar(
    category_views,
    x="category_name",
    y="views",
    color="views",
    text_auto=".2s",
    title="Top Categories by Average Views"
)

fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Average Views",
    height=500
)

st.plotly_chart(fig, use_container_width=True)
# -----------------------------
# CATEGORY DISTRIBUTION
# -----------------------------

category = (
    df["category_name"]
    .value_counts()
    .reset_index()
)

category.columns = [
    "Category",
    "Videos"
]

fig2 = px.pie(
    category,
    names="Category",
    values="Videos",
    hole=0.45,
    title="Video Category Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# -----------------------------
# NLP INSIGHTS
# -----------------------------

st.subheader("💡 NLP Insights")

st.info("""
• Entertainment and Music titles dominate trending videos.

• Short and engaging titles appear more frequently.

• Frequently occurring keywords indicate popular audience interests.

• Keyword search can be used to discover trending topics.
""")
footer()