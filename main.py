from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_fireworks import ChatFireworks
from fireworks.client.api import ChatCompletionStreamResponse, ChatCompletionResponseStreamChoice, DeltaMessage
import asyncio
from dotenv import load_dotenv
import os 


load_dotenv()

app = FastAPI()

# Allowing CORS for all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World, Universe"}

@app.post("/get_fireworks_completion")
async def get_fireworks_completion(
    fireworks_api_key: str = Form(...),
    prompt: str = Form(...),
):
    try:
        os.environ['FIREWORKS_API_KEY']=os.getenv("FIREWORKS_API_KEY")
        model = ChatFireworks( model_name="accounts/fireworks/models/mixtral-8x7b-instruct",
                                    temperature=0.0,
                                    verbose=True)
        response = model.generate_content(prompt)
        print(response)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
