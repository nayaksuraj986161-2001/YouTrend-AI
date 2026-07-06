import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

from components.footer import footer

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Prediction",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# LOAD MODELS
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "models"

classifier = joblib.load(MODEL_DIR / "trending_classifier.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
encoders = joblib.load(MODEL_DIR / "label_encoders.pkl")

# =====================================================
# PAGE TITLE
# =====================================================

st.title("🤖 AI Prediction")

st.markdown("""
Predict whether a YouTube video has **High Trending Potential**
using the trained **Machine Learning Model**.
""")

st.divider()

# =====================================================
# USER INPUT
# =====================================================

left, right = st.columns(2)

with left:

    likes = st.number_input(
        "👍 Likes",
        min_value=0,
        value=10000
    )

    dislikes = st.number_input(
        "👎 Dislikes",
        min_value=0,
        value=200
    )

    comments = st.number_input(
        "💬 Comments",
        min_value=0,
        value=500
    )

    trending_duration = st.slider(
        "📈 Trending Duration (Days)",
        1,
        30,
        7
    )

    publish_hour = st.slider(
        "🕒 Publish Hour",
        0,
        23,
        18
    )

with right:

    country = st.selectbox(
        "🌍 Country",
        list(encoders["Country"].classes_)
    )

    category = st.selectbox(
        "📂 Category",
        list(encoders["category_name"].classes_)
    )

    upload_period = st.selectbox(
        "⏰ Upload Period",
        list(encoders["Upload_Period"].classes_)
    )

    publish_month = st.selectbox(
        "📅 Publish Month",
        list(encoders["publish_month"].classes_)
    )

    publish_day = st.selectbox(
        "📆 Publish Day",
        list(encoders["publish_day"].classes_)
    )

st.divider()

# =====================================================
# PREDICT BUTTON
# =====================================================

if st.button("Predict Trending Potential", use_container_width=True):
        # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    engagement_rate = (
        (likes + comments)
        / max((likes + dislikes + comments), 1)
    ) * 100

    like_ratio = (
        likes /
        max((likes + dislikes), 1)
    )

    comment_ratio = (
        comments /
        max(likes, 1)
    )

    like_comment_ratio = (
        likes /
        max(comments, 1)
    )

    # =====================================================
    # ENCODE CATEGORICAL FEATURES
    # =====================================================

    country_encoded = encoders["Country"].transform([country])[0]

    category_encoded = encoders["category_name"].transform([category])[0]

    upload_period_encoded = encoders["Upload_Period"].transform([upload_period])[0]

    publish_month_encoded = encoders["publish_month"].transform([publish_month])[0]

    publish_day_encoded = encoders["publish_day"].transform([publish_day])[0]

    # =====================================================
    # CREATE INPUT DATAFRAME
    # =====================================================

    input_df = pd.DataFrame([{

        "likes": likes,

        "dislikes": dislikes,

        "comment_count": comments,

        "Engagement_Rate": engagement_rate,

        "Like_Ratio": like_ratio,

        "Comment_Ratio": comment_ratio,

        "Like_to_Comment_Ratio": like_comment_ratio,

        "Trending_Duration": trending_duration,

        "publish_hour": publish_hour,

        "Country": country_encoded,

        "category_name": category_encoded,

        "Upload_Period": upload_period_encoded,

        "publish_month": publish_month_encoded,

        "publish_day": publish_day_encoded

    }])

    # =====================================================
    # SCALE NUMERICAL FEATURES
    # =====================================================

    numeric_features = [

        "likes",

        "dislikes",

        "comment_count",

        "Engagement_Rate",

        "Like_Ratio",

        "Comment_Ratio",

        "Like_to_Comment_Ratio",

        "Trending_Duration",

        "publish_hour"

    ]

    input_df[numeric_features] = scaler.transform(
        input_df[numeric_features]
    )

    # =====================================================
    # MODEL PREDICTION
    # =====================================================

    prediction = classifier.predict(input_df)[0]

    probability = classifier.predict_proba(input_df)[0]

    confidence = probability.max() * 100
    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    st.divider()

    if prediction == 1:
        st.success("🔥 High Trending Potential")
    else:
        st.error("📉 Low Trending Potential")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with col2:
        st.progress(confidence / 100)

    # =====================================================
    # AI PREDICTION SCORE
    # =====================================================

    st.info(f"""
### 🤖 AI Prediction Score

The model estimates a **{confidence:.2f}%** confidence that this video will be classified as **{"High Trending" if prediction == 1 else "Low Trending"}**.

This prediction is based on historical YouTube trending patterns learned during model training.
""")

    # =====================================================
    # PREDICTION SUMMARY
    # =====================================================

    st.divider()

    st.subheader("📋 Prediction Summary")

    predicted_class = (
        "🔥 High Trending"
        if prediction == 1
        else "📉 Low Trending"
    )

    summary = pd.DataFrame({
        "Feature": [
            "Country",
            "Category",
            "Upload Period",
            "Publish Month",
            "Publish Day",
            "Publish Hour",
            "Prediction",
            "Confidence"
        ],
        "Value": [
            country,
            category,
            upload_period,
            publish_month,
            publish_day,
            f"{publish_hour}:00",
            predicted_class,
            f"{confidence:.2f}%"
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # KEY FACTORS
    # =====================================================

    st.divider()

    st.subheader("🎯 Key Factors Influencing Prediction")

    st.markdown("""
- 👍 Likes
- 💬 Comments
- ❤️ Engagement Rate
- 📂 Video Category
- 🌍 Country
- 🕒 Upload Timing
- 📈 Trending Duration
""")
    # =====================================================
    # BUSINESS RECOMMENDATION
    # =====================================================

    st.divider()

    st.subheader("💼 Business Recommendation")

    if prediction == 1:

        st.success("""
### ✅ Content Strategy

Your video shows **strong trending potential**.

Recommended Actions:

• Publish immediately.

• Keep similar upload timing.

• Promote using YouTube Shorts.

• Share through Community Posts.

• Respond to comments quickly.

• Continue the same content strategy.
""")

    else:

        st.warning("""
### ⚠ Improvement Suggestions

Your video currently has **lower trending potential**.

Recommended Improvements:

• Improve the thumbnail.

• Write a more attractive title.

• Increase audience engagement.

• Publish during peak hours.

• Encourage viewers to like and comment.

• Promote the video on social media.
""")

    # =====================================================
    # AI INSIGHT
    # =====================================================

    st.divider()

    st.subheader("AI Insight")

    if prediction == 1:

        st.info(f"""
Based on the supplied information, the model predicts that this video has a
**{confidence:.2f}% confidence** of achieving a **High Trending** outcome.

The strongest contributing factors include:

• High engagement

• Suitable upload timing

• Strong interaction levels

• Favorable historical patterns
""")

    else:

        st.info(f"""
Based on the supplied information, the model predicts that this video has a
**{confidence:.2f}% confidence** of remaining **Low Trending**.

The prediction indicates opportunities to improve:

• Viewer engagement

• Publishing strategy

• Thumbnail and title quality

• Audience interaction
""")

    # =====================================================
    # FINAL RECOMMENDATION
    # =====================================================

    st.divider()

    st.subheader(" Next Suggested Action")

    if prediction == 1:

        st.success("""
### Recommended Next Steps

✅ Publish the video.

✅ Promote within the first 24 hours.

✅ Share on social media.

✅ Monitor engagement closely.

✅ Continue using similar publishing strategies.
""")

    else:

        st.warning("""
### Recommended Next Steps

⚠ Improve the content before publishing.

⚠ Increase expected engagement.

⚠ Upload during a better time window.

⚠ Optimize the title and thumbnail.

⚠ Build early audience interaction.
""")
# =====================================================
# FOOTER
# =====================================================

footer()
