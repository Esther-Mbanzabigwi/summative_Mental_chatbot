
 Mental Healthcare Chatbot - README

📌 Overview

The Mental Healthcare Chatbot is an AI-powered assistant designed to provide empathetic conversations, mental health support, stress management tips, and guided relaxation exercises. While it does not replace professional therapy, it offers accessible, AI-powered support for individuals experiencing stress, anxiety, or depression.

This chatbot uses Natural Language Processing (NLP) and is built using Hugging Face Transformers (DistilBERT), Streamlit for UI, and PyTorch for deep learning.

🚀 Features

- AI-Powered Mental Health Support – Understands and responds empathetically.- Relaxing UI & Calming Theme – Uses soft colors and a welcoming design.- Background Music for Relaxation  – Helps create a soothing environment.- Guided Meditation Feature  – Plays calming audio for mindfulness exercises.- Breathing Exercises  – Provides simple relaxation techniques.- AI Affirmations 💙 – Encouraging messages for users feeling down.

📌 Technologies Used

Python (3.8+)

Hugging Face Transformers (DistilBERT)

PyTorch / TensorFlow

Streamlit (UI Framework)

NLTK (Text Processing)

Ngrok (For Public Deployment)

Docker (For Containerized Deployment)

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-repo/mental-health-chatbot.git
cd mental-health-chatbot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Chatbot

streamlit run app.py

 Your chatbot will be available at: http://localhost:8501

 Model & Dataset

Model: Fine-tuned DistilBERT for mental health intent classification.

Dataset: Based on mental health queries (stress, anxiety, depression).

Training: Preprocessed with NLTK, Tokenization, and Fine-Tuning.

 User Interface (UI) Enhancements

Soft soothing colors for mental relaxation 

Welcoming chatbot avatar & friendly messages 

Breathing GIF for stress relief 

Real-time chatbot typing effect 

🚀 Deployment Options

1️⃣ Deploy Locally

streamlit run app.py

2️⃣ Deploy via Ngrok

!streamlit run app.py &>/dev/null &
from pyngrok import ngrok
public_url = ngrok.connect("8501")
print(f"Chatbot is live at: {public_url}")

3️⃣ Deploy on Hugging Face Spaces

Upload the app.py, model, and requirements.txt to a Hugging Face Space.

Set app.py as the main execution file.

📜 License

This project is open-source under the MIT License.

📌 YouTube Demo Video

 Watch the Demo






