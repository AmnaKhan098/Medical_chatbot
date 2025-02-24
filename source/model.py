# calling llm model from grok using Langchain
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
load_dotenv()
import os
api_key2 = os.getenv("GROK_API_KEY")



def model(retriver):
    chat = ChatGroq(temperature=0.5,
        api_key= api_key2,
        model_name="mixtral-8x7b-32768"
        )
   
# creating a system prompt
    prompt = ChatPromptTemplate([
        ("system", "You are a very helpful medical AI assistant.You need to provide answers based on the provided context \n\n {context}."),
        ("human", "{input}"),

    ])
    # creating stuff document
    stuff_document1 = create_stuff_documents_chain(chat, prompt)   
    # create retriveral chain

    retrieval_chain = create_retrieval_chain(retriver,stuff_document1 ) 
    return  retrieval_chain 