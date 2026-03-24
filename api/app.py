from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Dual-chatbot Langchain Server",
    version="1.0",
    description="Base Api Server"

)

llm1=Ollama(model="mistral",num_ctx=1024)
llm2=Ollama(model="gemma",num_ctx=1024)

prompt1=ChatPromptTemplate.from_template("write a proverb about {topic} with 25 words")
prompt2=ChatPromptTemplate.from_template("write an essay about {topic} with 150 words")

add_routes(
    app,
    prompt1|llm1,
    path="/proverb"

)

add_routes(
    app,
    prompt2|llm2,
    path="/essay"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8888)