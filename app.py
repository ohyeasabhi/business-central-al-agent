import streamlit as st
from system_prompt import SYSTEM_PROMPT
import ollama

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Business Central AL Agent",
    layout="wide"
)

st.title("🧠 Business Central AL Agent")
st.caption("Local Claude-style AI for AL & Business Central")

# -------------------------------------------------
# System Prompt
# -------------------------------------------------


# -------------------------------------------------
# Session State
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# LIMIT history to avoid slowdown (important)
MAX_HISTORY = 6

# -------------------------------------------------
# Display Chat History
# -------------------------------------------------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# -------------------------------------------------
# User Input
# -------------------------------------------------
user_input = st.chat_input("Describe your Business Central task...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    st.chat_message("user").markdown(user_input)

    # Send only last N messages
    messages_to_send = st.session_state.messages[-MAX_HISTORY:]

    with st.spinner("Thinking like a BC Consultant..."):
        response = ollama.chat(
            model="qwen3-coder:30b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *messages_to_send
            ]
        )

    assistant_reply = response["message"]["content"]

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

    st.chat_message("assistant").markdown(assistant_reply)
