def build_prompt(user_input, history_text):
    system_prompt = """
You are a professional career advisor chatbot.

Rules:
- Give clear, structured, practical advice
- Be concise but helpful
- Suggest actionable steps
- Stay within career guidance domain
"""

    return f"""
{system_prompt}

Conversation so far:
{history_text}

User: {user_input}
Bot:
"""