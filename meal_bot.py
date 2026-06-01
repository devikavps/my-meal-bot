import streamlit as st
import google.generativeai as genai

# Direct API Key
GOOGLE_API_KEY = "AIzaSyCZT9WYwhIeeJqlsGqClYTV5W3FF81AoWc"

genai.configure(api_key=GOOGLE_API_KEY)

# Simple system instruction setup
system_instruction = (
    "You are Kishore's personal South Indian Dietitian. "
    "Give extremely short, bulleted, and crisp responses. No long paragraphs. "
    "Strictly limit each reply to maximum 3-4 bullet points or lines. "
    "Respond friendly in Tanglish."
)

st.set_page_config(page_title="Kishore's Meal Planner", page_icon="🥗")
st.title("🥗 Kishore's Personal Meal Planner")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Vanakkam Kishore! Naan un personal meal planner. Iniku enna fitness goal?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # 100% Fixed Content Generation Logic for Older Libraries
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    # Prompt கூடவே system instruction-ஐயும் சேர்த்து அனுப்புறோம்
    full_prompt = f"{system_instruction}\n\nUser Question: {user_input}"
    response = model.generate_content(full_prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)
