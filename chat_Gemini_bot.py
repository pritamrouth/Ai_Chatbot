import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key="AIzaSyCPHAdaF1oDGq8AFb4NccNePz873SvUkH8")

## Function to load gemini pro model for response

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(query):
    response = chat.send_message(query, stream=True)
    return response

# Initializing streamlit app

st.set_page_config(page_title="Chat Bot")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it's does not exist
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("ask the question")

if submit and input:
    response= get_gemini_response(input)
    ## Add user query and response to chat history
    st.session_state['chat_history'].append(("you: ", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
    