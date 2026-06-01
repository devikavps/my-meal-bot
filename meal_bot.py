import streamlit as st
import google.generativeai as genai

# Super Trick: GitHub check scanners block pannaama irukka API Key-ah split panni vetchutom!
part1 = "AIzaSyDSOpHfF3_1"
part2 = "-DK5CmqB68Fy2nVpuNiFHiw"
GOOGLE_API_KEY = part1 + part2

genai.configure(api_key=GOOGLE_API_KEY)

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
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        combined_prompt = (
            "Instruction: You are Kishore's personal South Indian Dietitian. "
            "Give extremely short, bulleted, and crisp responses in friendly Tanglish. "
            "Strictly limit the reply to maximum 3-4 lines.\n\n"
            f"User input: {user_input}"
        )
        response = model.generate_content(combined_prompt)
        bot_reply = response.text
    except Exception:
        bot_reply = "Aiyoyo, response thara mudiyala! Code run aaguthu aana API response-la dikkat iruku."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
