from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

history=[]

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "AI Study Assistant is running"
    }

class QuestionRequest(BaseModel):
    question:str

@app.post("/ask")
def ask_quetion(item:QuestionRequest):
    question=item.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="问题不能为空"
        )
    answer=f"这是对问题'{item.question}'的回答"
    record={
        "id":len(history)+1,
        "question":item.question,
        "answer":answer
    }
    history.append(record)
    return record

@app.get("/history")
def get_history():
    return{
        "count":len(history),
        "data":history
    }