from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    label = result['label']
    score = result['score']
    
    if label == 'NEGATIVE':
        stress_level = 'High Stress'
    elif label == 'POSITIVE':
        stress_level = 'Low Stress'
    else:
        stress_level = 'Moderate Stress'
    
    return label, score, stress_level
