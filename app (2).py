import streamlit as st
import torch
import torch.nn.functional as F
import time
import random
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from inference import predict_intent  # Import function from inference.py

# Load the fine-tuned model
model_path = "fine_tuned_chatbot"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = DistilBertForSequenceClassification.from_pretrained(model_path).to(device)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

# Function to add typing effect
def chatbot_typing_effect(response):
    with st.spinner("🤖 Chatbot is thinking..."):
        time.sleep(1.5)
    st.write(response)

# Apply a calming background color & UI styling
st.markdown(
    """
    <style>
    body {
        background-color: #E8F5E9;
    }
    .stButton>button {
        background-color: #81C784;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 12px;
        border-radius: 10px;
        border: 2px solid #AED581;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Chatbot UI
st.image("https://cdn-icons-png.flaticon.com/512/4727/4727429.png", width=120)
st.title("💙 Your Mental Health Companion")
st.write("Hello there! I'm here to listen. You can share how you're feeling, and I'll do my best to support you. 💬")

# Soothing Background Music
st.markdown(
    """
    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-relaxing.mp3" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
)

# Meditation Feature
st.write("💆 Need a quick relaxation break? Try a 2-minute guided meditation.")
if st.button("🎧 Start Meditation"):
    st.audio("https://www.bensound.com/bensound-music/bensound-meditation.mp3")

# User input
user_input = st.text_input("How are you feeling today?")

fallback_responses = [
    "I'm here for you. Could you tell me a bit more about how you're feeling? 💙",
    "I want to help. Can you describe what’s bothering you?",
    "It sounds like you’re going through something. Would you like some relaxation techniques?",
    "I'm listening. You can share as much or as little as you’d like. 💬"
]

if st.button("Submit"):
    if user_input.strip():
        predicted_intent, confidence, response = predict_intent(user_input, model, tokenizer, device)

        if confidence < 0.3:
            chatbot_typing_effect(random.choice(fallback_responses))
        else:
            st.write(f"**🧠 Predicted Intent:** {predicted_intent} (Confidence: {confidence:.2f})")

            if predicted_intent == "stress":
                chatbot_typing_effect("🌿 Take a deep breath. You’re not alone. Would you like some stress management tips?")
            elif predicted_intent == "anxiety":
                chatbot_typing_effect("💜 It’s okay to feel anxious sometimes. Would you like to try a grounding technique?")
            elif predicted_intent == "depression":
                chatbot_typing_effect("❤️ I'm really sorry you’re feeling this way. You're not alone, and I'm here to help.")
            else:
                chatbot_typing_effect(response)
    else:
        st.write("⚠️ Please enter a valid message.")



