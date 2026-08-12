from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from llm import chat_with_llm

KNOWLEDGE_FILE = Path(__file__).resolve().parent / "knowledge.txt"


def load_knowledge():
    try:
        with open(KNOWLEDGE_FILE, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('请检查文件路径正确性')
        return []


def retrieve(question):
    vectorizer=TfidfVectorizer()
    texts=load_knowledge()
    vectors=vectorizer.fit_transform(texts)
    question_vector=vectorizer.transform([question])

    similarities=cosine_similarity(question_vector,vectors)

    best_index=similarities.argmax()
    return(texts[best_index])

def ask_with_rag(question,system_prompt):
    context=retrieve(question)
    rag_prompt = f"""
    {system_prompt}

    下面是从知识库中检索到的相关资料：
    {context}
    请结合知识库资料和你已有的知识回答用户的问题。
    知识库资料应优先作为参考，但可以使用你已有的知识进行补充解释。
    回答要求：
    1. 优先保证知识库中的内容得到正确使用。
    2. 可以使用你已有的知识进行补充解释。
    3. 如果补充内容不是来自知识库，请不要与知识库内容冲突。
    4. 回答尽量清晰、适合初学者理解。
    """
    answer=chat_with_llm(question,rag_prompt)
    return answer
