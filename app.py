import streamlit as st
from speech_to_text import voice_to_text
from sentiment_analysis import analyze_sentiment
from chatbot import chatbot_response
from logger import log_conversation

st.title("🧠 AI Therapist for Mental Health")

if st.button("Start Talking"):
    user_input = voice_to_text()
    st.text_area("You said:", user_input)

    sentiment, score, stress = analyze_sentiment(user_input)
    st.markdown(f"**Sentiment**: {sentiment} | **Stress**: {stress} ({score:.2f})")

    bot_reply, _ = chatbot_response(user_input)
    st.text_area("Therapist:", bot_reply)

    log_conversation(user_input, bot_reply, sentiment, score)
