import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def ask_deepseek(question: str, system_prompt: str):

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        stream=False
    )

    return response.choices[0].message.content