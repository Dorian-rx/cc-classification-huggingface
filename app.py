import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/Hate-speech-CNERG/dehatebert-mono-english"
API_TOKEN = "api_wRsoGgUZnbDMqkllLUYhBXNLNitVAQtwLP"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({"inputs": "I like you. I love you"})
st.title('Classification')

form = st.form(key='my_form')
text = form.text_input(label='Enter a text to classify')
output = query({"inputs": text})

submit_button = form.form_submit_button(label='Submit')

if submit_button:
    st.header('Classification of the Text')

    st.subheader('A reminder of the Written Text')
    st.write({"Text":text})

    st.subheader('The Positive and Negative Classification of the Written Text')
    st.write([
        {
                "Label": "Positive",
                "Score": output[0][0]['score'],
            },
        
        {
                "Label": "Negative",
                "Score": output[0][1]['score'],
            }
        ])
