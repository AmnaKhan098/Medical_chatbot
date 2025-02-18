# splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter
def splitting(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    return texts