from main import main
import asyncio
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

chain=asyncio.run(main())
app= FastAPI()
class QuestionAPI(BaseModel):
    q:str


@app.get("/")
def home():
   return {"message":"welcome"}
@app.post("/question/")
def askquestion(question:QuestionAPI):
    question1=question.q
    answer=chain.invoke({"input": question1})
    return answer["answer"]
    

# 
# while True:
#     # asking questions
#     question=input("enter your question")
#     answer=chain.invoke({"input": question})
#     print(answer["answer"])

if __name__ =="__main__":
    uvicorn.run(app)