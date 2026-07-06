import streamlit as st

def navigation_cards():

    st.markdown("##  Quick Navigation")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link(
            "pages/01_Dashboard.py",
            label="📊 Dashboard",
            icon="📊"
        )

    with col2:
        st.page_link(
            "pages/02_AI_Prediction.py",
            label="🤖 AI Prediction",
            icon="🤖"
        )

    with col3:
        st.page_link(
            "pages/03_NLP_Analysis.py",
            label="🧠 NLP Analysis",
            icon="🧠"
        )

    st.write("")

    col4, col5 = st.columns(2)

    with col4:
        st.page_link(
            "pages/04_Model_Performance.py",
            label="📈 Model Performance",
            icon="📈"
        )

    with col5:
        st.page_link(
            "pages/05_About.py",
            label="ℹ️ About",
            icon="ℹ️"
        )