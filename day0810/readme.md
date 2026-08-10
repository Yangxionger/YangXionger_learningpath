# 2026-08-10 学习记录

## 今日完成

### FastAPI
- 完成 Task API 小练习
- 理解 `@app.get("/tasks")`、`@app.post("/tasks")` 中 API 路径的作用
- 理解前端 JSON → Pydantic 对象 → Python 后端处理的过程
- 使用 Swagger `/docs` 测试接口

### LLM API
- 使用 DeepSeek API 完成第一次真实大模型调用
- 理解 `client.chat.completions.create()`
- 理解 `messages`、`role`、`content`
- 理解 `stream=False`
- 理解 `response.choices[0].message.content`
- 使用 `.env` 保存 API Key

### AI 学习助手 v0.1
- 使用 FastAPI + DeepSeek 完成 `POST /chat`
- 前端传入问题，后端调用 LLM 并返回回答
- 增加 `beginner` / `intermediate` 两种学习水平
- 使用 system prompt 控制不同回答风格
- 使用 `Literal` 限制 level 合法取值
- 测试非法参数并理解 HTTP 422
- 理解 Pydantic 的默认值与参数校验区别

### LeetCode
- 49. 字母异位词分组
- 使用排序结果作为哈希表 key
- 使用 `unordered_map<string, vector<string>>` 完成分组
- 理解时间复杂度 O(n * k log k)

## 今日遇到的问题
- Uvicorn 启动目录错误导致找不到 main.py
- API Key 使用临时环境变量时，新终端无法读取
- `os.getenv()` 使用方式不熟悉
- Pydantic 对象、dict、JSON 一开始容易混淆
- `intermediate` 拼写错误导致业务逻辑没有按预期执行

## 今日收获
- 第一次真正把 FastAPI 和大模型 API 串联起来
- 理解了一个 AI 后端从请求到模型回答再到返回 JSON 的完整流程
- 开始理解 Prompt 不只是“问模型一句话”，而是后端业务逻辑的一部分
- 对 Pydantic 输入校验有了实际认识
- 更熟悉 unordered_map 的分组思路