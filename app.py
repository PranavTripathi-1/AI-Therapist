import streamlit as st
from chatbot import get_bot_response
from sentiment_analysis import analyze_sentiment
from logger import log_conversation

st.set_page_config(page_title="AI Therapist", layout="centered")

st.title("🧠 AI Therapist")
st.markdown("Talk to your virtual mental health assistant. Type how you feel, and I’ll listen and support you.")

# Use text input instead of microphone for Streamlit Cloud
user_input = st.text_area("How are you feeling today?", height=150)

if st.button("Analyze & Respond") and user_input:
    # Analyze sentiment and stress
    sentiment, stress_level = analyze_sentiment(user_input)

    # Get chatbot response
    response = get_bot_response(user_input)

    # Show results
    st.markdown("### 🧾 Chatbot Response")
    st.write(response)

    st.markdown("### 📊 Sentiment Analysis")
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Stress Level:** {stress_level}")

    # Log the conversation
    log_conversation(user_input, response, sentiment, stress_level)

