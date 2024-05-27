from langchain.llms import fireworks
from prompt import get_prompt
from langchain_fireworks import ChatFireworks
from langchain_core.messages import HumanMessage, SystemMessage
from web_crawler import get_data_from_website
from text_to_doc import get_doc_chunks
from dotenv import load_dotenv
import os 
load_dotenv()

url = "https://www.udemy.com/"  
text_content, metadata = get_data_from_website(url)
doc_chunks = get_doc_chunks(text_content, metadata)

context = "\n".join([chunk.page_content for chunk in doc_chunks])

def generate_response(system_prompt, user_question):
    api_key = os.getenv("FIREWORKS_API_KEY")
    chat = llm = ChatFireworks(api_key=api_key, 
                    model="accounts/fireworks/models/mixtral-8x7b-instruct",
                    max_tokens=256)

    system_message = SystemMessage(content=system_prompt)
    human_message = HumanMessage(content=user_question)
    response = chat.invoke([system_message, human_message])
    generated_response = response.content
    return generated_response

# Define the function to get the response
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

# Example usage
question = "What courses are available on Udemy?"
chat_history = ""
organization_name = "Udemy"
organization_info = "Udemy is an online learning platform with a wide range of courses."
contact_info = "You can contact Udemy support at support@udemy.com."

response = get_response(question, organization_name, organization_info, contact_info)
print(response)
