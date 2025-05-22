import re

def parse_chat(text):
    user_msgs, ai_msgs = [], []
    all_msgs = []
    for line in text.strip().split('\n'):
        if line.startswith("User:"):
            msg = line[5:].strip()
            user_msgs.append(msg)
            all_msgs.append(msg)
        elif line.startswith("AI:"):
            msg = line[3:].strip()
            ai_msgs.append(msg)
            all_msgs.append(msg)
    return {
        "user": user_msgs,
        "ai": ai_msgs,
        "all_messages": all_msgs
    }