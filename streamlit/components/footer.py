import streamlit as st

def footer():

    st.divider()

    st.markdown(
        """
        <div style='text-align:center;
                    color:gray;
                    padding:15px;
                    font-size:14px;'>

        <b>YouTrend AI</b><br>

        Developed by <b>Suraj Nayak</b><br>

        MBA | ABV-IIITM Gwalior | 2026

        </div>
        """,
        unsafe_allow_html=True,
    )