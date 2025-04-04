import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Downloading necessary NLTK data
nltk.download('punkt_tab')
nltk.download('stopwords')

#loading a pre-trained Hugging Face model
chatbot = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

#pre-processing user output
def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Defining Health-care specific response logic
def healthcare_chatbot(user_input):
    user_input = preprocess_input(user_input).lower()
   if "sneeze" in user_input or "sneezing" in user_input:
        return "I understand that you've been sneezing since morning. This could be due to allergies, a common cold, or environmental factors like dust or pollen. You may find relief by staying hydrated, avoiding triggers, and using over-the-counter antihistamines if needed. If the sneezing is persistent, accompanied by fever or other symptoms, consider consulting a doctor for further evaluation."
    
    elif "fever" in user_input:
        return "A fever could indicate an infection or illness. If it's mild, rest, stay hydrated, and take fever-reducing medication if needed. If your fever is high or persists for more than 3 days, consult a doctor."

    elif "headache" in user_input:
        return "Headaches can be caused by stress, dehydration, lack of sleep, or underlying medical conditions. Drinking water, getting enough rest, and managing stress can help. If your headache is severe or persistent, consult a doctor."

    elif "cough" in user_input:
        return "A cough can be due to a cold, flu, allergies, or even respiratory infections. Try drinking warm fluids, using cough drops, or taking over-the-counter cough medicine. If your cough lasts more than two weeks or is severe, seek medical attention."

    elif "stomach pain" in user_input or "stomachache" in user_input:
        return "Stomach pain can have various causes, including indigestion, infections, or food intolerance. Try drinking water, eating light meals, and avoiding spicy foods. If the pain is severe or persistent, consult a doctor."

    elif "blood pressure" in user_input or "hypertension" in user_input:
        return "High blood pressure can be managed with a healthy diet, regular exercise, and proper medication. Monitoring your blood pressure regularly and consulting a doctor for medication adjustments is crucial."

    elif "diabetes" in user_input or "sugar level" in user_input:
        return "Managing diabetes involves maintaining a balanced diet, regular exercise, and monitoring blood sugar levels. If you notice abnormal sugar levels or symptoms like excessive thirst, fatigue, or blurred vision, consult a doctor."

    elif "symptom" in user_input:
        return "If you experience persistent or severe symptoms, it's best to consult a doctor for proper evaluation and treatment."

    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"

    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."

    elif "mental health" in user_input or "stress" in user_input or "anxiety" in user_input:
        return "Mental health is important. If you're feeling stressed or anxious, try relaxation techniques like meditation or breathing exercises. If your feelings persist, consider talking to a therapist or counselor."

    elif "skin rash" in user_input or "itching" in user_input:
        return "Skin rashes and itching can be due to allergies, infections, or irritants. Keep the area clean, avoid scratching, and try anti-itch creams. If the rash worsens, consult a dermatologist."

    else:
        context = """
        Common Health-Care related scenarios include symptoms of colds, flu, and allergies,
        along with medication guidance and appointment scheduling.
        """
        response = chatbot(question=user_input,context=context)
        return response['answer']
    
#Streamlit web app interface
def main():
    st.title("HealthCare Assistant Chatbot")
    user_input = st.text_input("How can I assist you Today? :) ", "")
    if st.button("Submit"):
        if user_input:
            st.write("User: ",user_input)
            response = healthcare_chatbot(user_input)
            st.write("HealthCare Assistant: ",response)
        else:
            st.write("Please enter a query.")

if __name__=="__main__":
    main()
