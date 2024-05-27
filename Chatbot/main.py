from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from web_crawler import get_data_from_website
from text_to_doc import get_doc_chunks
from prompt import get_prompt
from langchain_fireworks import ChatFireworks
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Scrape and clean the data
url = "https://www.udemy.com/"
text_content, metadata = get_data_from_website(url)
doc_chunks = get_doc_chunks(text_content, metadata)
context = "\n".join([chunk.page_content for chunk in doc_chunks])

class ChatRequest(BaseModel):
    question: str
    organization_name: str
    organization_info: str
    contact_info: str

def generate_response(system_prompt, user_question):
    api_key = os.getenv("FIREWORKS_API_KEY")
    chat = ChatFireworks(api_key=api_key, 
                         model="accounts/fireworks/models/mixtral-8x7b-instruct",
                         max_tokens=256)

    system_message = SystemMessage(content=system_prompt)
    human_message = HumanMessage(content=user_question)
    response = chat.invoke([system_message, human_message])
    generated_response = response.content
    return generated_response

def get_response(question, organization_name, organization_info, contact_info):
    prompt = get_prompt()
    formatted_prompt = prompt.format_prompt(
        context=context,
        question=question,
        chat_history="",
        organization_name=organization_name,
        organization_info=organization_info,
        contact_info=contact_info
    )
    formatted_prompt_str = str(formatted_prompt)  # Ensure it's a string
    response = generate_response(formatted_prompt_str, question)
    return response

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        response = get_response(request.question, request.organization_name, request.organization_info, request.contact_info)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example endpoint to check the service status
@app.get("/")
def read_root():
    return {"message": "Welcome to the chatbot API. Use /chat to interact with the bot."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
