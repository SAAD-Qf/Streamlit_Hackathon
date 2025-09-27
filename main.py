# streamlit_app.py
import streamlit as st
import asyncio
from agents import Runner
from doctor_agent import dr_agent

st.set_page_config(page_title="Dr On Call AI", layout="centered")
st.title("🩺 Dr On Call – AI Doctor Agent")
st.write("Ask your questions and get instant responses from the AI doctor.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Type your question here:")

if st.button("Send") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    st.write(f"**You:** {user_input}")
    st.write("⏳ Dr Agent is thinking...")

    async def run_agent():
        try:
            result = await Runner.run(
                starting_agent=dr_agent,
                input=st.session_state.history
            )
            st.session_state.history.append({"role": "assistant", "content": result.final_output})
            st.write(f"**Dr Agent:** {result.final_output}")
        except Exception as e:
            st.write("**Dr Agent:** Error processing your request.")
            print("Error:", e)

    asyncio.run(run_agent())

# Display chat history
st.subheader("Chat History")
for msg in st.session_state.history:
    role = "You" if msg["role"] == "user" else "Dr Agent"
    st.write(f"**{role}:** {msg['content']}")













