import streamlit as st
from utils.data_loader import load_data
from utils.helper import calculate_kpis
from utils.helper import format_number


def show_kpi_cards():

    df = load_data()

    kpi = calculate_kpis(df)

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            label="🎬 Videos",
            value=format_number(kpi["videos"])
        )

    with c2:
        st.metric(
            label="👁 Views",
            value=format_number(kpi["views"])
        )

    with c3:
        st.metric(
            label="👍 Likes",
            value=format_number(kpi["likes"])
        )

    with c4:
        st.metric(
            label="💬 Comments",
            value=format_number(kpi["comments"])
        )

    with c5:
        st.metric(
            label="🌍 Countries",
            value=str(kpi["countries"])
        )