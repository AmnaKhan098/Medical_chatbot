import asyncio
from source.loading import dataloading
from source.chunking import splitting
from source.embedding import embeddings
from source.vectordatabase import load_data , retriver
from source.model import model

BOOK = "data/A-Z Family Medical Encyclopedia.pdf"

async def main():
    # data = await dataloading(BOOK)  #  Await the coroutine properly
    # splitted = splitting(data)
    print("embedding_model")
    embedding_model= embeddings()
    print("loaded_data")
    loaded_data= load_data(embedding_model,index_name = "medicalchatbot" )
    print("retrived")
    retrived=retriver(loaded_data)
    print("chain")
    chain=model(retrived)
    # asking questions
    answer=chain.invoke({"input": "what are the symptoms of fever?"})
    return answer

asyncio.run(main())  #  Runs the async function  



    
    





