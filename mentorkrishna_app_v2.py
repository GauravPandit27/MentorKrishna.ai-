import streamlit as st
from constants import groq_key
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from textblob import TextBlob

# -------- LLM SETUP --------
llm = ChatGroq(api_key=groq_key, model_name="llama3-8b-8192")

# -------- PAGE CONFIG --------
st.set_page_config(page_title="MentorKrishna.ai", layout="centered")

# -------- CSS & THEME --------
st.markdown("""
    <style>
        html, body {
            background-color: #1a001a;
            color: #e6e6e6;
            font-family: 'Segoe UI', sans-serif;
            background-image: url('https://i.imgur.com/zI9IVGl.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stButton button {
            background-color: #d97706;
            color: white;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
        .message-user {
            background-color: #2c0033;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 8px;
            color: #f0f0f0;
        }
        .message-krishna {
            background-color: #330033;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: #facc15;
            font-style: italic;
        }
        .small-font {
            font-size: 13px;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown("<h1 style='text-align: center;'>🧘 MentorKrishna.ai</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Spiritual Copilot Powered by Bhagavad Gita & Psychology</div>", unsafe_allow_html=True)
st.markdown("<div class='small-font' style='text-align: center;'>“When in doubt, ask Krishna.”</div><br>", unsafe_allow_html=True)

# -------- SESSION STATE --------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------- TONE TOGGLE --------
spiritual_mode = st.radio("🕉️ Krishna's Tone", ["Spiritual", "Conversational"], horizontal=True)

# -------- PROMPT TEMPLATE --------
tone_instruction = (
    "Speak in poetic, wise, divine tone like Lord Krishna from the Gita."
    if spiritual_mode == "Spiritual"
    else "Speak like a modern, emotionally intelligent friend with spiritual depth."
)

krishna_template = f"""
You are Lord Krishna, the divine strategist and philosopher from the Bhagavad Gita.

Your role is to guide the user as a compassionate mentor, blending spiritual wisdom with emotional intelligence and modern psychological understanding.

{tone_instruction}

Your answers should ALWAYS follow this structure:

📜 QUOTE:
- Include a meaningful Sanskrit shloka from the Bhagavad Gita.
- Provide its clear English translation.

🧠 MEANING:
- Explain the essence of the quote in simple conversational language.
- Talk like a friend who deeply understands human emotions.
- Add analogies if it helps.

🔍 RELEVANCE & ACTION:
- Reflect on how this quote connects with the user's problem.
- Offer practical advice the user can act on today.
- Be optimistic and empowering.

Rules:
- Respond in a calming tone, always friendly and supportive.
- You may correct user grammar silently and infer emotional intent even with typos.
- If the message is unclear, make your best guess and offer general life wisdom.
- DO NOT go off-topic or give lectures.

Chat Log:
{{history}}
User: {{user_message}}
Krishna:
"""

prompt = PromptTemplate(
    input_variables=["history", "user_message"],
    template=krishna_template
)

chain = LLMChain(llm=llm, prompt=prompt)

# -------- CHAT INPUT --------
user_message = st.chat_input("🧘 What's troubling your mind, dear friend?")

if user_message:
    corrected = str(TextBlob(user_message).correct())
    history_str = ""
    for u, k in st.session_state.chat_history:
        history_str += f"User: {u}\nKrishna: {k}\n"

    with st.spinner("🌸 Krishna is contemplating..."):
        response = chain.run({
            "history": history_str.strip(),
            "user_message": corrected
        })

    st.session_state.chat_history.append((user_message, response))

# -------- DISPLAY CHAT --------
for user, krishna in st.session_state.chat_history:
    st.markdown(f"<div class='message-user'><b>You:</b><br>{user}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='message-krishna'><b>Krishna:</b><br>{krishna}</div>", unsafe_allow_html=True)

# -------- CLEAR CHAT --------
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

