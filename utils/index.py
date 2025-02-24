# PineCone vector database
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
load_dotenv()
import os

api_key1 = os.getenv("PINECONE_API_KEY")


pc = Pinecone(api_key= api_key1 )
def creatingindex():
    index_name = "medicalchatbot"

    pc.create_index(
        name=index_name,
        dimension=768, # Replace with your model dimensions
        metric="cosine", # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )