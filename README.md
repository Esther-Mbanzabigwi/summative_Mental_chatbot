
# 🧠 Mental Healthcare Chatbot

A **supportive  chatbot** designed to provide mental health assistance, offering **calm conversations, guided meditation, and stress relief techniques**. This chatbot is built using **Hugging Face Transformers & Streamlit**, with a soothing UI for a better user experience.



---

## 🌟 Features

✅ **Mental Health Support** - Understands and responds empathetically to stress, anxiety, and depression.  
✅ **Relaxing UI & Calming Theme** - Uses soft colors and a welcoming design.  
✅ **Background Music for Relaxation** 🎶 - Helps create a soothing environment.  
✅ **Guided Meditation Feature** 🧘 - Plays calming audio for mindfulness exercises.  
✅ **Breathing Exercises** 🌬️ - Provides simple relaxation techniques.  
✅ **Affirmations** 💙 - Encouraging messages for users feeling down.  

---

## 📌 Technologies Used

- **Python** (3.8+)
- **Hugging Face Transformers** (DistilBERT)
- **TensorFlow / PyTorch**
- **Streamlit** (Frontend UI)
- **Ngrok / LocalTunnel** (For Deployment)
- **Google Colab** (For Training)

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Esther-Mbanzabigwi/summative_Mental_chatbott.git
cd mental-health-chatbot


### **2️⃣ Deploy via Ngrok**

!streamlit run app.py &>/dev/null &
from pyngrok import ngrok
public_url = ngrok.connect("8501", "http")
print(f"Chatbot is live at: {public_url}")

****your chatbot is live on****
NgrokTunnel:[ "Mentalhealth chatbot"]("https://170c-34-132-69-254.ngrok-free.app") -> "http://localhost:8501"
