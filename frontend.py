import streamlit as st
import time

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Simple Chatbot")

# Function to simulate bot reply
def bot_reply(user_message):
    time.sleep(1)  # Simulate typing delay
    return f"You said: '{user_message}'. Here's my reply!"

# Chat display
for entry in st.session_state.chat_history:
    st.chat_message("user").markdown(entry["user"])
    st.chat_message("assistant").markdown(entry["bot"])

# User input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", placeholder="Ask anything", disabled=False)
    submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.chat_history.append({"user": user_input, "bot": "..."})
        st.experimental_rerun()

# Replace placeholder response with actual reply
if st.session_state.chat_history and st.session_state.chat_history[-1]["bot"] == "...":
    last_message = st.session_state.chat_history[-1]["user"]
    response = bot_reply(last_message)
    st.session_state.chat_history[-1]["bot"] = response
    st.experimental_rerun()