from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from web_crawler import get_data_from_website
from text_to_doc import get_doc_chunks
from prompt import get_prompt
from langchain_community.vectorstores import Chroma
from langchain_fireworks import FireworksEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_fireworks import ChatFireworks

app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    organization_name: str
    organization_info: str
    contact_info: str

@app.on_event("startup")
def startup_event():
    global vector_store
    vector_store = get_chroma_client()

def get_chroma_client():
    embedding_function = FireworksEmbeddings(model="nomic-ai/nomic-embed-text-v1.5")
    return Chroma(
        collection_name="website_data",
        embedding_function=embedding_function,
        persist_directory="data/chroma"
    )

@app.post("/store_docs/")
def store_docs(url: str):
    try:
        text, metadata = get_data_from_website(url)
        if text is None:
            raise HTTPException(status_code=500, detail="Failed to retrieve data from the website.")
        
        docs = get_doc_chunks(text, metadata)
        vector_store.add_documents(docs)
        vector_store.persist()
        return {"message": "Documents stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_response/")
def get_response(query: QueryRequest):
    try:
        prompt = get_prompt()
        model = ChatFireworks(model_name="accounts/fireworks/models/mixtral-8x7b-instruct",
                              temperature=0.0,
                              verbose=True)

        human_message = HumanMessage(content=query.question)
        system_message = SystemMessage(content=prompt.format(
            context="",
            chat_history="",
            organization_name=query.organization_name,
            organization_info=query.organization_info,
            contact_info=query.contact_info
        ))
        response = model([system_message, human_message])

        return {"answer": response['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
