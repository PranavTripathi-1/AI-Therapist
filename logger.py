import json
from datetime import datetime

def log_conversation(user_text, bot_response, sentiment, score):
    entry = {
        "timestamp": str(datetime.now()),
        "user_text": user_text,
        "bot_response": bot_response,
        "sentiment": sentiment,
        "score": score
    }
    with open("conversation_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
