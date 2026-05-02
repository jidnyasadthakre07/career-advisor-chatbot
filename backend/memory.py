def format_history(history):
    formatted = ""
    for chat in history:
        formatted += f"User: {chat['user']}\nBot: {chat['bot']}\n"
    return formatted


def update_history(history, user_input, bot_response):
    history.append({
        "user": user_input,
        "bot": bot_response
    })
    return history