import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from components.footer import footer

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

df = load_data()

# ==================================================
# PAGE TITLE
# ==================================================

st.title("📊 Dashboard")
st.markdown("Interactive dashboard for global YouTube trending videos.")

st.divider()

# ==================================================
# FILTERS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    country = st.selectbox(
        "Country",
        ["All"] + sorted(df["Country"].dropna().unique())
    )

with col2:
    category = st.selectbox(
        "Category",
        ["All"] + sorted(df["category_name"].dropna().unique())
    )

with col3:
    year = st.selectbox(
        "Publish Year",
        ["All"] + sorted(df["publish_year"].dropna().unique())
    )

# ==================================================
# FILTER DATA
# ==================================================

filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[
        filtered_df["Country"] == country
    ]

if category != "All":
    filtered_df = filtered_df[
        filtered_df["category_name"] == category
    ]

if year != "All":
    filtered_df = filtered_df[
        filtered_df["publish_year"] == year
    ]

st.success(f"Filtered Records : {len(filtered_df):,}")

st.divider()

# ==================================================
# KPI CARDS
# ==================================================

st.subheader("📊 Key Performance Indicators")

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        "🎬 Trending Videos",
        f"{len(filtered_df):,}"
    )

with k2:
    st.metric(
        "🌍 Countries",
        filtered_df["Country"].nunique()
    )

with k3:
    st.metric(
        "📂 Categories",
        filtered_df["category_name"].nunique()
    )

k4, k5, k6 = st.columns(3)

with k4:
    st.metric(
        "👁 Total Views",
        f"{filtered_df['views'].sum()/1e9:.2f} B"
    )

with k5:
    st.metric(
        "👍 Total Likes",
        f"{filtered_df['likes'].sum()/1e9:.2f} B"
    )

with k6:
    st.metric(
        "❤️ Avg Engagement",
        f"{filtered_df['Engagement_Rate'].mean():.2f}%"
    )

st.divider()
# ==================================================
# ROW 1
# ==================================================

left_chart, right_chart = st.columns(2)

# --------------------------------------------------
# Top Categories by Views
# --------------------------------------------------

with left_chart:

    st.subheader("📊 Top Categories by Views")

    category_views = (
        filtered_df.groupby("category_name")["views"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig1 = px.bar(
        category_views,
        x="category_name",
        y="views",
        color="views",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )

    fig1.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="Views",
        xaxis_tickangle=-30
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# --------------------------------------------------
# Top Countries by Views
# --------------------------------------------------

with right_chart:

    st.subheader("🌍 Top Countries by Views")

    country_views = (
        filtered_df.groupby("Country")["views"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        country_views,
        x="views",
        y="Country",
        orientation="h",
        color="views",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )

    fig2.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Views",
        yaxis_title=""
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()
# ==================================================
# ROW 2
# ==================================================

left_chart, right_chart = st.columns(2)

# --------------------------------------------------
# Upload Period Distribution
# --------------------------------------------------

with left_chart:

    st.subheader("🕒 Upload Period Distribution")

    upload = (
        filtered_df["Upload_Period"]
        .value_counts()
        .reset_index()
    )

    upload.columns = ["Upload Period", "Videos"]

    fig3 = px.pie(
        upload,
        names="Upload Period",
        values="Videos",
        hole=0.45
    )

    fig3.update_layout(height=450)

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
# --------------------------------------------------
# VIEWS vs LIKES (Bubble Chart)
# --------------------------------------------------

with right_chart:

    st.subheader("🎈 Video Performance Bubble Chart")

    bubble_df = filtered_df.sample(
        min(2500, len(filtered_df)),
        random_state=42
    )

    fig6 = px.scatter(
        bubble_df,
        x="views",
        y="likes",
        size="Engagement_Rate",
        color="category_name",
        hover_name="title",
        size_max=40,
        opacity=0.75,
        title="Views vs Likes (Bubble Size = Engagement)"
    )

    fig6.update_layout(
        height=520,
        xaxis_title="Views",
        yaxis_title="Likes",
        legend_title="Category"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )
# ==================================================
# ROW 3
# ==================================================

left_chart, right_chart = st.columns(2)

# --------------------------------------------------
# TOP 10 CHANNELS
# --------------------------------------------------

with left_chart:

    st.subheader("📺 Top 10 Channels by Views")

    top_channels = (
        filtered_df.groupby("channel_title")["views"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig5 = px.bar(
        top_channels,
        x="views",
        y="channel_title",
        orientation="h",
        color="views",
        text_auto=".2s",
        color_continuous_scale="Purples"
    )

    fig5.update_layout(
        height=500,
        showlegend=False,
        xaxis_title="Views",
        yaxis_title="Channel",
        yaxis={"categoryorder":"total ascending"}
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# --------------------------------------------------
# VIEWS VS ENGAGEMENT
# --------------------------------------------------

with right_chart:

    st.subheader("📈 Views vs Engagement")

    scatter_df = filtered_df.sample(
        min(3000, len(filtered_df)),
        random_state=42
    )

    fig6 = px.scatter(
        scatter_df,
        x="views",
        y="Engagement_Rate",
        color="category_name",
        opacity=0.6
    )

    fig6.update_layout(
        height=500,
        xaxis_title="Views",
        yaxis_title="Engagement Rate (%)"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

st.divider()
# ==================================================
# ROW 4
# GLOBAL VIEWS MAP
# ==================================================

st.divider()

st.subheader("🌍 Global YouTube Trending Views")

country_map = (
    filtered_df.groupby("Country")["views"]
    .sum()
    .reset_index()
)

country_name_mapping = {
    "US": "United States",
    "USA": "United States",
    "CA": "Canada",
    "GB": "United Kingdom",
    "FR": "France",
    "DE": "Germany",
    "RU": "Russia",
    "IN": "India",
    "JP": "Japan",
    "KR": "South Korea",
    "MX": "Mexico"
}

country_map["Country"] = (
    country_map["Country"]
    .replace(country_name_mapping)
)

fig7 = px.choropleth(
    country_map,
    locations="Country",
    locationmode="country names",
    color="views",
    hover_name="Country",
    color_continuous_scale="Blues",
    title="Global Trending Views"
)

fig7.update_layout(
    height=600,
    margin=dict(l=0, r=0, t=40, b=0)
)

st.plotly_chart(
    fig7,
    use_container_width=True
)
# ==================================================
# ROW 5# ==================================================
# TREEMAP
# ==================================================

st.divider()

st.subheader("🌳 YouTube Category Distribution by Country")

treemap_df = (
    filtered_df
    .groupby(["category_name", "Country"])["views"]
    .sum()
    .reset_index()
)

fig8 = px.treemap(
    treemap_df,
    path=["category_name", "Country"],
    values="views",
    color="views",
    color_continuous_scale="RdBu",
    hover_data={
        "views":":,.0f"
    }
)

fig8.update_traces(

    marker=dict(
        line=dict(
            color="white",
            width=2
        )
    ),

    textfont=dict(
        size=14
    ),

    root_color="#f4f6f9"
)

fig8.update_layout(

    height=700,

    margin=dict(
        t=50,
        l=20,
        r=20,
        b=20
    ),

    coloraxis_colorbar=dict(
        title="Views"
    )
)

st.plotly_chart(
    fig8,
    use_container_width=True
)
# ==================================================
# DOWNLOAD FILTERED DATA
# ==================================================

st.divider()

st.subheader("📥 Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Filtered Dataset (CSV)",
    data=csv,
    file_name="youtube_filtered_data.csv",
    mime="text/csv",
    use_container_width=True,
)
footer()