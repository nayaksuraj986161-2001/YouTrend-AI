import pandas as pd
from pathlib import Path
import streamlit as st

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Dataset Path
DATA_PATH = PROJECT_ROOT / "Data" / "processed" / "youtube_feature_engineered_sample.csv"


@st.cache_data
def load_data():
    """
    Load the processed dataset.
    """

    df = pd.read_csv(DATA_PATH)

    return df