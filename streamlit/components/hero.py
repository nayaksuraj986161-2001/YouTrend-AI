import streamlit as st
from PIL import Image
from pathlib import Path


def hero_section():

    assets_path = Path(__file__).parent.parent / "assets"

    logo_path = assets_path / "logo.png"

    col1, col2 = st.columns([1, 3])

    with col1:
        if logo_path.exists():
            logo = Image.open(logo_path)
            st.image(logo, width=180)
        else:
            st.warning("Logo not found")

    with col2:

        st.markdown("""
        <h1 style='
        font-size:58px;
        font-weight:800;
        margin-bottom:0px;
        color:#111827;'>
        YouTrend AI
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 style='
        color:#6366F1;
        margin-top:0px;'>
        AI-Powered YouTube Trending Analytics Platform
        </h3>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="
        font-size:18px;
        color:#6B7280;
        line-height:1.7;">
        Analyze millions of YouTube trending videos using
        Machine Learning, Natural Language Processing,
        Business Intelligence and Interactive Dashboards.
        </p>
        """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.info("📊 Data Analytics")

    with c2:
        st.info("🤖 Machine Learning")

    with c3:
        st.info("🧠 NLP")

    with c4:
        st.info("📈 Power BI")

    with c5:
        st.info("🐍 Python")