import streamlit as st
from backend.api_client import get_gemini_response
from backend.memory import format_history, update_history
from backend.prompts import build_prompt

st.set_page_config(page_title="Career Advisor Chatbot")

st.title("💼 Career Advisor Chatbot")

# Initialize session memory
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.chat_input("Ask your career question...")

if user_input:
    with st.spinner("Thinking..."):
        history_text = format_history(st.session_state.history)
        prompt = build_prompt(user_input, history_text)
        response = get_gemini_response(prompt)

        st.session_state.history = update_history(
            st.session_state.history,
            user_input,
            response
        )

# Display chat history
for chat in st.session_state.history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])