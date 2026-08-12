# 2026-08-11 学习记录

## 今日目标

继续完善 AI 学习助手，将昨天已经跑通的 FastAPI + DeepSeek 后端进一步扩展为一个可以从网页直接使用的 AI 应用。

---

## 一、AI 学习助手

### 1. 后端代码拆分

将原本全部写在 `main.py` 中的大模型调用逻辑进行了简单拆分：

* `main.py`

  * 创建 FastAPI 应用
  * 定义 `/chat`、`/health` 路由
  * 使用 Pydantic 校验请求数据
  * 根据 `level` 生成不同的 system prompt
  * 返回 HTTP 响应

* `ai_service.py`

  * 初始化 DeepSeek API Client
  * 调用 DeepSeek 模型
  * 获取并返回模型回答

理解了：

> 业务流程可以互相依赖，但不同职责的代码仍然可以分开管理。

---

### 2. 增加 `/health` 接口

增加：

```python
GET /health
```

用于快速判断 FastAPI 后端是否正常运行。

正常返回：

```json
{
  "status": "ok"
}
```

理解：

* `/health`：检查后端服务是否正常
* `/chat`：检查 AI 聊天业务是否正常

---

### 3. 后端异常处理

为 DeepSeek 调用增加：

```python
try / except
```

模型调用失败时：

```python
raise HTTPException(status_code=500, ...)
```

并通过：

```python
except Exception as e
```

获取真正的异常对象，在后端终端打印具体错误原因。

理解：

* `500`：服务器内部处理发生错误
* `422`：客户端发送的数据不符合后端要求
* `e`：保存实际发生的异常对象，方便开发者排查问题

实际测试：

* 故意使用不存在的模型名
* DeepSeek API 调用失败
* 后端成功返回 `500`
* 终端能够看到真实的模型错误信息

---

## 二、前后端通信

### 1. 使用 `fetch()` 调用 FastAPI

使用原生 HTML + JavaScript 编写简单前端。

实现完整链路：

```text
用户输入问题
→ JavaScript 获取输入
→ JSON.stringify()
→ fetch()
→ POST /chat
→ FastAPI
→ DeepSeek
→ FastAPI 返回 JSON
→ response.json()
→ data.answer
→ HTML 显示回答
```

---

### 2. JSON 数据转换

发送请求时：

```javascript
JSON.stringify(requestData)
```

作用：

```text
JavaScript 对象
→ JSON 字符串
→ 通过 HTTP 发送
```

接收响应时：

```javascript
response.json()
```

作用：

```text
HTTP Response 中的 JSON
→ JavaScript 数据对象
```

---

### 3. `.then()` 的理解

当前请求流程：

```javascript
fetch(...)
.then(response => {
    return response.json()
})
.then(data => {
    // 使用解析后的数据
})
```

理解：

* 第一个 `.then()`：获得 HTTP Response
* `response.json()`：读取并解析响应体
* 第二个 `.then()`：获得解析后的 JavaScript 数据
* 第二个 `.then()` 中参数名可以自己定义，它接收上一步返回的结果

---

## 三、解决 CORS 问题

前端第一次请求 FastAPI 时出现：

```text
OPTIONS /chat 405 Method Not Allowed
```

原因：

浏览器在发送跨域 POST 请求前，会先发送 `OPTIONS` 预检请求。

通过 FastAPI：

```python
CORSMiddleware
```

允许前端跨域访问后端。

理解：

```text
浏览器
→ OPTIONS 预检
→ FastAPI 允许
→ POST /chat
```

并理解：

> CORS 是浏览器的跨域访问规则，不等于 API 身份认证或真正的安全保护。

---

## 四、前端交互完善

实现：

* 点击提交后显示：

  * `AI正在疯狂思考中`
* 请求成功：

  * 显示 `data.answer`
* 请求失败：

  * 检查 `response.ok`
  * 主动 `throw new Error(...)`
  * 使用 `.catch()` 显示错误信息

完成前后端异常链路：

```text
DeepSeek 调用失败
→ FastAPI 返回 500
→ response.ok == false
→ throw Error
→ catch
→ 页面显示错误信息
```

---

## 五、学习难度选择

前端增加：

```html
<select>
```

支持：

* `beginner`
* `intermediate`

JavaScript 获取：

```javascript
select.value
```

并发送：

```json
{
  "question": "...",
  "level": "beginner"
}
```

后端根据 `level` 选择不同 system prompt。

完整链路：

```text
HTML select
→ JavaScript value
→ requestData.level
→ FastAPI
→ get_prompt(level)
→ 不同 system prompt
→ DeepSeek
```

---

## 六、Network 调试

第一次使用浏览器开发者工具：

```text
F12 → Network → Fetch/XHR
```

观察 `/chat` 请求。

能够大致理解：

* Request URL
* Request Method
* Status Code
* Request Payload
* Response

将之前学习的 HTTP、POST、JSON、状态码与真实请求联系起来。

---

## 七、Codex Code Review

让 Codex 对当前 FastAPI + HTML/JavaScript 项目进行代码审查。

主要发现：

1. `/chat` 暂时没有认证、限流和输入长度限制
2. 前端将 `127.0.0.1:8000` 写死，目前只适合本地开发
3. 后端异常全部转换成 500 后不利于定位真实问题

今天主要改进第 3 点：

```python
except Exception as e:
```

保留用户友好的错误响应，同时让开发者能够在后端终端看到真实异常。

---

## 八、算法

### LeetCode 128：最长连续序列

主要使用：

```cpp
unordered_set
```

练习：

* 哈希集合
* O(1) 平均查找
* 利用哈希优化算法复杂度

完成题目。

### LeetCode 347：前 K 个高频元素

主要使用：

```cpp
unordered_map
priority_queue
```

思路：

```text
unordered_map 统计元素频率
→ priority_queue 存储 {频率, 元素}
→ 取出频率最高的 K 个元素
```

一次通过。

---

## 九、Git

今天完成：

* AI 学习助手代码 commit
* push 功能分支到 GitHub
* 将 `feature/0804-fastapi` 合并到 `main`
* 成功 push `main`
* 本地 `main` 与 `origin/main` 保持一致

今天进一步理解：

```text
git add
→ 决定这次 commit 包含哪些修改

git commit
→ 在本地保存一次代码版本

git push
→ 将本地已经存在的 commit 上传到 GitHub
```

以后提交时应尽量只 `add` 当前功能相关文件，避免直接使用 `git add .` 将无关修改混入同一个 commit。

---

## 今日遇到的问题

* 虚拟环境中的 Python 与系统 `py` 命令不是同一个解释器
* `OPTIONS /chat 405`，最终定位为 CORS 问题
* 一开始把 HTTP `Response` 对象误认为后端返回的具体数据
* `beginner` 拼写错误导致请求数据不符合 Pydantic 的 `Literal`
* DeepSeek 模型名错误时学会通过异常对象 `e` 查看真实错误
* Git 中曾将多个无关文件一起加入同一个 commit，对 `add / commit / push` 的区别理解更加清晰

---

## 今日总结

今天完成了 AI 学习助手第一个可以实际使用的版本。

从昨天只能通过 Swagger 调用 DeepSeek，推进到了：

```text
网页
→ JavaScript
→ HTTP
→ FastAPI
→ DeepSeek
→ JSON
→ JavaScript
→ 网页显示 AI 回答
```

同时加入了：

* beginner / intermediate 学习难度
* loading
* 前端错误提示
* 后端异常处理
* health check
* CORS
* Code Review

今天最大的收获是开始真正理解一个简单 AI Web 应用从前端到大模型再返回前端的完整数据流。
