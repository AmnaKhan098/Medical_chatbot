import asyncio
from source.loading import dataloading
from source.chunking import splitting

BOOK = "data/A-Z Family Medical Encyclopedia.pdf"

async def main():
    data = await dataloading(BOOK)  #  Await the coroutine properly
    splitted = splitting(data)  # Assuming `splitting` is a normal function
    print(len(splitted))
    

asyncio.run(main())  #  Runs the async function



