import os
from dotenv import load_dotenv,find_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from openai import OpenAI

app=FastAPI()

load_dotenv(find_dotenv())

client=OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

class ChatRequest(BaseModel):
    question:str
    level: Literal["beginner", "intermediate"] = "beginner"

def get_prompt(level):
    if level=='beginner':
        return """
        你是一名计算机学习助手。
        用户目前是初学者。

        回答要求：
        1. 先用简单语言解释概念
        2. 尽量使用生活中的类比
        3. 再给出技术上的准确解释
        4. 不要一次使用太多专业术语
        5. 回答控制在 500 字以内
        6. 专业术语第一次出现时必须解释
        7. 不要延伸太多用户没有询问的知识
        """
    elif level=='intermediate':
        return """
        你是一名计算机学习助手
        用户目前是中等水平的学习者

        回答要求：
        1.用相对专业的语言解释概念
        2.尽量练习计算机学习的知识去解释概念
        3.再引导用户去对于当前知识串联起相关知识
        4.可以适当用专业术语
        5. 回答控制在 800 字以内
        6. 重点解释底层机制和知识之间的联系
        7. 最后给出 2 个建议继续学习的相关知识点
        """
    
@app.post("/chat")
def chat(request:ChatRequest):
    system_prompt=get_prompt(request.level)
    response=client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":request.question
            }
        ],
        stream=False
    )
    return {
        "level":request.level,
        "answer":response.choices[0].message.content
    }


