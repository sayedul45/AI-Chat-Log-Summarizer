def generate_summary(parsed_data, keywords):
    user_count = len(parsed_data["user"])
    ai_count = len(parsed_data["ai"])
    total = user_count + ai_count
    summary = {
        "total_exchanges": total,
        "user_messages": user_count,
        "ai_messages": ai_count,
        "common_keywords": keywords,
        "topic_hint": f"Conversation is mainly about {', '.join(keywords[:2])}."
    }
    return summary