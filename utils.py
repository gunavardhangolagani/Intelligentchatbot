from text_data import get_doc_chunks
from data import get_data_from_website
from prompt import get_prompt
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# load environment variables from env files
from dotenv import load_dotenv
# load all the environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#initialize gemini-pro model
model=genai.GenerativeModel("gemini-pro")

# chathistory
chat=model.start_chat(history=[])

# function of chatcompletion 
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

#initialize our streamlit app
st.set_page_config(page_title="Question Bank")
st.header("Gemini Chatbot")

#initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input =st.text_input("Input:",key="input")
submit=st.button("Ask the question ")

if submit and input :
    response=get_gemini_response(input)

    # Remember user and response queries to session chat history

    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response :")
    
    # advantage of stream=true
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini",chunk.text))
    st.subheader("The Chat history :")

    for role,text in st.session_state['chat_history']:
        st.write(f"{role}:{text}")
    