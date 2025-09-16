# logger.py

import json
import os
from datetime import datetime

LOG_FILE = "conversation_log.json"

def log_conversation(user_input, bot_response, sentiment, stress_level):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_input": user_input,
        "bot_response": bot_response,
        "sentiment": sentiment,
        "stress_level": stress_level
    }

    # Load existing log or start a new list
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new entry and save
    data.append(log_entry)
    with open(LOG_FILE, "w") as file:
        json.dump(data, file, indent=2)

