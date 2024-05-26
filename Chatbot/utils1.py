# chatbot.py
from langchain.llms import OpenAI
from prompt import get_prompt

# Assuming you have already scraped and cleaned the data
from web_crawler import get_data_from_website, get_doc_chunks

# Scrape and clean the data
url = "https://www.udemy.com/"  
text_content, metadata = get_data_from_website(url)
doc_chunks = get_doc_chunks(text_content, metadata)

# Combine text chunks into a single context string
context = "\n".join([chunk.page_content for chunk in doc_chunks])

# Chatbot function
def chatbot_response(question, chat_history, organization_name, organization_info, contact_info):
    prompt_template = get_prompt()
    prompt = prompt_template.format(
        context=context,
        question=question,
        chat_history=chat_history,
        organization_name=organization_name,
        organization_info=organization_info,
        contact_info=contact_info
    )
    # Initialize your model here
    llm = OpenAI(api_key="YOUR_OPENAI_API_KEY", model="accounts/fireworks/models/mixtral-8x7b-instruct")
    response = llm(prompt)
    return response

# Example usage
question = "What courses are available on Udemy?"
chat_history = ""
organization_name = "Udemy"
organization_info = "Udemy is an online learning platform with a wide range of courses."
contact_info = "You can contact Udemy support at support@udemy.com."

response = chatbot_response(question, chat_history, organization_name, organization_info, contact_info)
print(response)
