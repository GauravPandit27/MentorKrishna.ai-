
```markdown
# 🧘‍♂️ MentorKrishna.ai  
*A Spiritual Copilot Powered by Bhagavad Gita & Generative AI*

> “When in doubt, ask Krishna.”

---

## 🌟 Overview

**MentorKrishna.ai** is a conversational AI built with **LangChain + LLaMA3 (Groq)** that embodies the wisdom of **Lord Krishna**. It blends **ancient Gita shlokas**, **modern psychology**, and **emotional intelligence** to guide users through their emotional challenges — in a kind, contextual, and deeply human way.

Whether you're stuck in self-doubt, recovering from rejection, or just seeking calm clarity, MentorKrishna responds like a divine life coach — with wisdom, empathy, and actionable insight.

---

## 🔮 Features

- 📜 **Bhagavad Gita-Based Advice**  
  Every response includes a relevant shloka, translation, meaning, and practical takeaway.

- 🤖 **Conversational Memory**  
  Maintains context from previous messages to offer evolving and personalized guidance.

- 🧠 **Emotion-Aware Response Generation**  
  Soft correction of typos and tone interpretation using `TextBlob`.

- 🧘 **Spiritual & Conversational Mode**  
  Choose between **Gita-style poetic tone** or **modern friendly talk**.

- 🎨 **Beautiful Krishna-Themed UI**  
  Dark purple spiritual aesthetic, glowing orange ‘Om’, and soothing font for a divine feel.

- 💬 **Chat History Tracking**  
  Previous conversations are stored in-session to give the feel of an evolving dialogue.

- 🔊 (Optional) **Voice Output using gTTS** *(can be toggled on/off)*

---

## 📸 Screenshot

![MentorKrishna.ai Screenshot](https://i.imgur.com/zI9IVGl.png)

---

## 🚀 Tech Stack

| Tool          | Purpose                               |
|---------------|----------------------------------------|
| `Streamlit`   | Frontend UI (fast, beautiful)          |
| `LangChain`   | Prompt templating and memory chain     |
| `Groq + LLaMA3` | Fast, contextual LLM engine           |
| `TextBlob`    | Typo correction + tone smoothing       |
| `gTTS` (opt.) | Text-to-speech voice playback          |

---

## 🧠 Prompt Philosophy

The AI is primed to act as **Krishna** — not just a chatbot.  
Each reply includes:

1. 📜 **Shloka** (Sanskrit + English Translation)  
2. 🧠 **Meaning** (in simple, relatable words)  
3. 🔍 **Relevance** (contextual insight + practical advice)

> It is built to **comfort, not just respond**.

---

## 📂 Project Structure

```

MentorKrishna/
│
├── mentorkrishna\_app.py        # Main Streamlit app
├── constants.py                # Stores Groq API key
├── README.md                   # You're reading it
├── requirements.txt            # Required Python libs

````

---

## 🛠️ Installation & Usage

```bash
# Clone the repo
git clone https://github.com/yourusername/MentorKrishna.git
cd MentorKrishna

# Create virtual environment
python3 -m venv Genai
source Genai/bin/activate

# Install requirements
pip install -r requirements.txt

# Add your Groq API key in constants.py
groq_key = 'your_groq_api_key'

# Run the app
streamlit run mentorkrishna_app.py
````

---

## 🙏 Why This Matters

This is more than an AI project.
It’s a **fusion of timeless Indian wisdom and cutting-edge technology**, designed to comfort the mind, encourage reflection, and guide you forward — just like Krishna did for Arjuna.

---

## 📌 Built By

👤 **Gaurav Pandit** – Visionary AI Strategist & Founder, [PAIRS](https://www.linkedin.com/in/gauravpandit-ai/)
🏷️ Final-Year Data Science | AI Ecosystem Builder | LinkedIn: [@gauravpandit-ai](https://www.linkedin.com/in/gauravpandit-ai/)

---

## 📃 License

MIT License. Use freely, but always give credit where it’s due 🙏

---

## 🌱 Future Enhancements

* 🌐 Multilingual support (Hindi, Marathi, Tamil)
* 📱 Mobile-responsive version
* 🧠 Emotion detection via facial/voice cues
* 🔊 Custom TTS with soothing Krishna voice
* 🧘‍♀️ Daily Krishna Quote Mode

---

## 🚀 Join the Movement

Contribute, fork, or spread the word. Let’s **make wisdom mainstream** again.

> *“In the age of anxiety, truth must wear new clothes. This project is Krishna in a hoodie.”*

---

Jai Shri Krishna 🙏

```

---

Would you like me to:
- Generate the `requirements.txt` too?
- Help write your `about` section on GitHub profile based on this?
- Add a small Krishna-themed logo?

Let’s polish it like a temple bell, Boss.
```
