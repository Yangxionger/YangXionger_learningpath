import os
from openai import OpenAI

client=OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def ask_llm(question):
    response=client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role":"user",
                "content":question
            }
        ],
        stream=False
    )
    return response.choices[0].message.content

answer=ask_llm("请用简单的话解释什么是二分查找")

print(answer)