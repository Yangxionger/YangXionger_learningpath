from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

tasks=[]

class Task(BaseModel):
    title:str
    done:bool=False

@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def add_task(task:Task):
    new_task=task.model_dump()
    tasks.append(new_task)
    return 