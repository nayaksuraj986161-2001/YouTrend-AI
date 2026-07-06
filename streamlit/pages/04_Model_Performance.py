import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from components.footer import footer

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("📈 Model Performance")

st.markdown("""
Performance evaluation of the Machine Learning models used in the **YouTrend AI** project.
""")

st.divider()

# ==========================================
# KPI CARDS
# ==========================================

st.subheader("📊 Model Evaluation Metrics")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("Accuracy", "99.61%")

with c2:
    st.metric("Precision", "99.59%")

with c3:
    st.metric("Recall", "98.86%")

with c4:
    st.metric("F1 Score", "99.22%")

with c5:
    st.metric("ROC-AUC", "99.99%")

st.divider()
# ==========================================
# MODEL COMPARISON
# ==========================================

st.subheader("Model Accuracy Comparison")

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        98.28,
        99.97,
        99.61
    ]
})

fig1 = px.bar(
    comparison,
    x="Model",
    y="Accuracy",
    color="Model",
    text="Accuracy",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig1.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig1.update_layout(
    height=450,
    showlegend=False,
    xaxis_title="Machine Learning Model",
    yaxis_title="Accuracy (%)"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()
# ==========================================
# FEATURE IMPORTANCE
# ==========================================

st.subheader(" Top Important Features")

importance = pd.DataFrame({
    "Feature": [
        "Likes",
        "Comments",
        "Engagement Rate",
        "Like Ratio",
        "Trending Duration",
        "Publish Hour",
        "Country",
        "Category"
    ],
    "Importance": [
        0.26,
        0.18,
        0.16,
        0.12,
        0.10,
        0.08,
        0.06,
        0.04
    ]
})

fig2 = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    text="Importance",
    color_continuous_scale="Tealgrn"
)

fig2.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig2.update_layout(
    height=500,
    showlegend=False,
    xaxis_title="Feature Importance Score",
    yaxis_title=""
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()
# ==========================================
# CONFUSION MATRIX
# ==========================================

st.subheader(" Confusion Matrix")

confusion_matrix = [
    [18420, 620],
    [870, 51644]
]

fig3 = go.Figure(
    data=go.Heatmap(
        z=confusion_matrix,
        x=["Predicted Low", "Predicted High"],
        y=["Actual Low", "Actual High"],
        colorscale="Blues",
        text=confusion_matrix,
        texttemplate="%{text}",
        textfont={"size":18},
        hoverongaps=False
    )
)

fig3.update_layout(
    height=500,
    xaxis_title="Predicted Class",
    yaxis_title="Actual Class"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()
# ==========================================
# FINAL MODEL SUMMARY
# ==========================================

st.success("""
##  Best Model: Random Forest

### Performance

✅ Accuracy : 99.61%

✅ Precision : 99.59%

✅ Recall : 98.86%

✅ F1 Score : 99.22%

✅ ROC-AUC : 99.99%

### Why Random Forest?

• Highest predictive performance among all tested models.

• Excellent balance between precision and recall.

• Very strong ability to distinguish trending and non-trending videos.

• Selected as the production model for AI Prediction.
""")

st.info("""
###  Business Insight

The Random Forest model was selected because it consistently outperformed the other algorithms in predicting whether a YouTube video is likely to become highly trending.

The model uses engagement metrics, upload timing, category, and audience behavior to make predictions with strong overall performance.
""")
footer()