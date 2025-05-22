import streamlit as st
import requests
import os

# Title and instructions
st.set_page_config(page_title="AI Chat Log Summarizer")
st.title("🤖 AI Chat Log Summarizer")
st.write("""
Upload a .txt file of your chat log between a user and an AI.
The app will analyze it and summarize the conversation with statistics and keywords.
""")

# File uploader
uploaded_file = st.file_uploader("Choose a .txt chat log file", type=["txt"])

if uploaded_file is not None:
    # Display filename
    st.success(f"Uploaded: {uploaded_file.name}")

    # Send file to backend API
    with st.spinner("Analyzing chat log..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/plain")}
        try:
            response = requests.post("http://localhost:8000/summarize/", files=files)
            if response.status_code == 200:
                data = response.json()
                st.subheader("📊 Summary Report")
                st.markdown(f"**Total Messages**: {data['total_exchanges']}")
                st.markdown(f"**User Messages**: {data['user_messages']}")
                st.markdown(f"**AI Messages**: {data['ai_messages']}")
                st.markdown(f"**Most Common Keywords**: {', '.join(data['common_keywords'])}")
                st.markdown(f"**Topic Hint**: {data['topic_hint']}")
            else:
                st.error("❌ Failed to summarize the chat log.")
        except Exception as e:
            st.error(f"An error occurred: {e}")