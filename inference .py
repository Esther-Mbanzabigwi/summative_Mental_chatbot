import torch
import torch.nn.functional as F
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Load the fine-tuned model and tokenizer
model_path = "fine_tuned_chatbot"

# Define response dictionary
intent_responses = {
    "greeting": "Hello! How can I help you today?",
    "stress": "I'm sorry you're feeling stressed. Would you like some tips on relaxation?",
    "anxiety": "It sounds like you're experiencing anxiety. I can suggest breathing exercises.",
    "depression": "I'm really sorry you're feeling depressed. Talking to someone may help.",
    "relaxation": "Try deep breathing, meditation, or a short walk to relax.",
    "other": "Could you provide more details? I'm here to help."
}

# Function for intent prediction
def predict_intent(text, model, tokenizer, device, temperature=0.7):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs = {key: val.to(device) for key, val in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits / temperature
    probabilities = F.softmax(logits, dim=1)
    predicted_idx = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0][predicted_idx].item()

    # Get labels dynamically
    num_labels = model.config.num_labels
    labels = [f"intent_{i}" for i in range(num_labels)]  # Placeholder labels

    # Ensure valid labels
    predicted_intent = labels[predicted_idx] if predicted_idx < len(labels) else "other"
    response = intent_responses.get(predicted_intent, "take a deep breath first.")

    return predicted_intent, confidence, response


