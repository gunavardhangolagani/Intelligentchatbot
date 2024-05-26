from langchain_community.vectorstores import Chroma
from langchain_fireworks import FireworksEmbeddings, ChatFireworks
from langchain_core.messages import HumanMessage, SystemMessage
from text_to_doc import get_doc_chunks
from web_crawler import get_data_from_website
from prompt import get_prompt

def get_chroma_client():
    embedding_function = FireworksEmbeddings(model="nomic-ai/nomic-embed-text-v1.5")
    return Chroma(
        collection_name="website_data",
        embedding_function=embedding_function,
        persist_directory="data/chroma"
    )

def store_docs(url):
    text, metadata = get_data_from_website(url)
    docs = get_doc_chunks(text, metadata)
    vector_store = get_chroma_client()
    vector_store.add_documents(docs)
    vector_store.persist()

def generate_response(system_prompt, user_question):
    chat = ChatFireworks(model="accounts/fireworks/models/mixtral-8x7b-instruct")
    system_message = SystemMessage(content=system_prompt)
    human_message = HumanMessage(content=user_question)
    response = chat.invoke([system_message, human_message])
    generated_response = response.content
    
    return generated_response

def get_response(question, organization_name, organization_info, contact_info):
    vector_store = get_chroma_client()  
    retriever = vector_store.as_retriever(search_type="mmr", verbose=True)
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = get_prompt()
    formatted_prompt = prompt.format(
        context=context,
        question=question,
        chat_history="",
        organization_name=organization_name,
        organization_info=organization_info,
        contact_info=contact_info
    )
    response = generate_response(formatted_prompt, question)  
    return response
