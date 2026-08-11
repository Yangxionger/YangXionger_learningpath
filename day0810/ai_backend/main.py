from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Literal

from ai_service import ask_deepseek

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str
    level: Literal["beginner", "intermediate"] = "beginner"


def get_prompt(level):
    if level == "beginner":
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

    elif level == "intermediate":
        return """
        你是一名计算机学习助手。
        用户目前是中等水平的学习者。

        回答要求：
        1. 用相对专业的语言解释概念
        2. 尽量联系计算机学习的知识去解释概念
        3. 引导用户把当前知识和相关知识串联起来
        4. 可以适当使用专业术语
        5. 回答控制在 800 字以内
        6. 重点解释底层机制和知识之间的联系
        7. 最后给出 2 个建议继续学习的相关知识点
        """


@app.post("/chat")
def chat(request: ChatRequest):
    system_prompt = get_prompt(request.level)

    try:
        answer = ask_deepseek(
            question=request.question,
            system_prompt=system_prompt
        )
    except Exception as e:
        print("大模型调用失败:",e)
        raise HTTPException(
            status_code=500,
            detail="大模型调用失败"
        )
    
    return {
        "level": request.level,
        "answer": answer
    }

@app.get("/health")
def examine_health():
    return {
        "status": "ok"
    }