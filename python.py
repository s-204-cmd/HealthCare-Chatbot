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
        return "If you experience persistent or severe sneezing along with other symptoms, it's best to consult a doctor for proper evaluation and treatment."
    elif "symptom" in user_input:
        return "If you experience persistent or severe symptoms, it's best to consult a doctor for proper evaluation and treatment."
    elif "appointment" in user_input:
        return "Would you like me too schedule an appointment with a Doctor ?"
    elif "medication" in user_input:
        return "It's important to your prescribed medications regularly. If you have a concerns, consult your doctor."
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
