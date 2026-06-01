import streamlit as st
import google.generativeai as genai

# Direct API Key
GOOGLE_API_KEY = "AIzaSyDSOpHfF3_1-DK5CmqB68Fy2nVpuNiFHiw"

genai.configure(api_key=GOOGLE_API_KEY)

system_instruction = (
    "You are Kishore's personal South Indian Dietitian. "
    "Give extremely short, bulleted, and crisp responses. No long paragraphs. "
    "Strictly limit each reply to maximum 3-4 bullet points or lines. "
    "Respond friendly in Tanglish."
)

st.set_page_config(page_title="Kishore's Meal Planner", page_icon="🥗")
st.title("🥗 Kishore's Personal Meal Planner")

# Simplest way to use Gemini without chat history session clash
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Vanakkam Kishore! Naan un personal meal planner. Iniku enna fitness goal?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Direct content generation with system instruction
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_instruction
    )
    
    # Safe text response call
    response = model.generate_content(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)
