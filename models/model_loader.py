import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "models"

def load_models():
    classifier = joblib.load(MODEL_DIR / "trending_classifier.pkl")
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")
    tfidf = joblib.load(MODEL_DIR / "tfidf_vectorizer.pkl")
    encoders = joblib.load(MODEL_DIR / "label_encoders.pkl")

    return classifier, scaler, tfidf, encoders