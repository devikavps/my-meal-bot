import os
import google.generativeai as genai

# Google Gemini API Key-ah inga paste pannu
GOOGLE_API_KEY = "AIzaSyDS0pHfF3_1-DK5CmqB68Fy2nVpuNiFHiw"

genai.configure(api_key=GOOGLE_API_KEY)
# Inga model name gemini-2.5-flash nu update aagi iruku
model = genai.GenerativeModel("gemini-2.5-flash")

# Strictly short-ah pesa instruction kuduthurukom
system_instruction = (
    "You are Kishore's personal South Indian Dietitian. "
    "CRITICAL RULE: Give extremely short, bulleted, and crisp responses. No long paragraphs. "
    "Strictly limit each reply to maximum 3-4 bullet points or lines. "
    "Respond friendly in Tanglish. Suggest practical South Indian meals."
)

print("--- AI Meal Planner Bot Start Aagiduchi! (Exit panna 'quit' type pannu) ---\n")
chat = model.start_chat(history=[])
chat.send_message(system_instruction)
print("Bot: Vanakkam Kishore! Naan un personal meal planner. Iniku enna saptinga? Enna fitness goal?")

while True:
    user_input = input("\nKishore: ")
    if user_input.lower() == 'quit':
        print("Bot: Romba nandri Kishore! Bye, take care!")
        break
    if not user_input.strip():
        continue
    response = chat.send_message(user_input)
    print(f"Bot: {response.text}")