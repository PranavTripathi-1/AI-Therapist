# sentiment_analysis.py

from transformers import pipeline

# Load a pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']

    # Classify stress level based on label and confidence
    if label == "NEGATIVE" and score > 0.9:
        stress_level = "High"
    elif label == "NEGATIVE":
        stress_level = "Moderate"
    elif label == "POSITIVE" and score > 0.9:
        stress_level = "Low"
    else:
        stress_level = "Normal"

    return label.capitalize(), stress_level

