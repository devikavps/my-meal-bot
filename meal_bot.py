import streamlit as st
import google.generativeai as genai

# Direct API Key configuration
GOOGLE_API_KEY = "AQ.Ab8RN6JCQbO31meG-Xtl11FcKSyl4m5UPq8dZKlDL073L385qQ"
genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="Kishore's Meal Planner", page_icon="🥗")
st.title("🥗 Kishore's Personal Meal Planner")

# Welcome message initial setup
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Vanakkam Kishore! Naan un personal meal planner. Iniku enna fitness goal?"}]

# Display past chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User inputs text
if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    try:
        # 2026 Fixed API syntax for Gemini 2.5
        model = genai.GenerativeModel(model_name="gemini-2.5-flash")
        
        # System instruction and user prompt combined together to avoid library conflicts
        combined_prompt = (
            "Instruction: You are Kishore's personal South Indian Dietitian. "
            "Give extremely short, bulleted, and crisp responses in friendly Tanglish. "
            "Strictly limit the reply to maximum 3-4 lines.\n\n"
            f"User input: {user_input}"
        )
        
        # Generate content safely
        response = model.generate_content(combined_prompt)
        bot_reply = response.text
        
    except Exception as e:
        bot_reply = "An error occurred, but we are fixing it! Please try again."

    # Display assistant response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
