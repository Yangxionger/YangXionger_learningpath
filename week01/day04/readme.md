# Day 04 学习记录｜2026-07-26

## 今日完成

- 学习 Python 异常处理
- 使用 pathlib 优化 Log Analyzer 文件路径处理
- 学习 HTTP 请求与响应基础
- 使用 requests 获取并解析 JSON 数据
- 完成 LeetCode 704 二分查找
- 完成 LeetCode 20 有效的括号
- 完成当天学习记录整理并提交 Git


## Python

### 异常处理

学习内容：

- try / except 基本结构
- FileNotFoundError
- ValueError
- ZeroDivisionError

能够处理：

- 文件不存在
- 用户输入非法数字
- 除数为0


### Log Analyzer 优化

原程序通过：

```python
Path(__file__).parent