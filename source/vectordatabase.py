# adding data in our database
from langchain_pinecone import PineconeVectorStore

def add_data(texts,embeddingModel,index_name='medicalchatbot'):
    medical=PineconeVectorStore.from_documents(texts, embeddingModel ,index_name='medicalchatbot')
    return medical
# loading the dtatabase from pinecone    
def load_data( embeddingModel,index_name = "medicalchatbot" ):
    
    loadingD = PineconeVectorStore.from_existing_index(index_name = "medicalchatbot", embedding=  embeddingModel)
    return loadingD
# creating retriver
def retriver(loadingD ):
   
    retriver= loadingD.as_retriever(
        search_type="similarity",
        search_kwargs={"k":2}

    )
    return retriver 