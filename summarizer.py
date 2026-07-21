import json
from openai import OpenAI
from fastapi import FastAPI, Request, UploadFile

from pydantic import BaseModel


OLLAMA_HOST = "http://127.0.0.1:11434"
MODEL_NAME = "qwen2.5-coder:7b"

client = OpenAI(base_url="http://localhost:11434/v1", api_key="EMPTY") #I had to correct the port

def chat(message:list, temperature:float=0.7, max_tokens:int=400, top_p:float=1.0)->str:
    resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=message, #open code gave me a message that had a set value for the system content, but to make the function more reusable the message will be passed as a whole and constructed outside
            temperature= temperature,
            top_p=top_p,
            max_tokens= max_tokens)
    return resp.choices[0].message.content

def build_prompt(text: str, type: str) -> list: #pre built prompts to make it more streamlined
    if type == "bullets":
        instruction = (
            "Summarize the given text as bullet points, only include information from the given text."
        )
    elif type=="paragraph":
        instruction = (
            "Summarize the given text as a paragraph (3-5 sentences). Only include information present in the text. "
        )
    else:
        instruction = (
            "Summarize the given text by giving a list of key words, only include information from the given text."
        )

    return [
        {"role": "system", "content": "You are a summarization assistant."},
        {"role": "user", "content": f"{instruction}\n\nTEXT:\n{text}"},
    ]

#print(chat(message=[{"role": "user", "content": "Hello!"}]))

app = FastAPI()

@app.post("/build_prompt/")
async def build_prompt_endpoint(text:str, type:str):
    text_data = text
    type_data = type
    prompt = build_prompt(text_data, type_data)
    response=chat(message=prompt)
    return {"summary": response}

@app.post("/build_prompt_file/")
async def build_prompt_file_endpoint(file: UploadFile, type: str):
    content = await file.read()
    text_data = content.decode("utf-8")
    
    prompt = build_prompt(text_data, type)
    response = chat(message=prompt)
    return {"summary": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)