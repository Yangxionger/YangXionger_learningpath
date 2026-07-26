# Day 03 学习记录｜2026-07-26

## 今日完成

- 完成 7.25 遗留任务
- 创建并完善 Log Analyzer Issue
- 编写 Python 日志分析程序
- 将程序拆分为 `analyzer.py` 和 `main.py`
- 完成 GitHub PR、合并到 `main` 并删除功能分支
- 完成 LeetCode 242、209、438

## Python

### Log Analyzer

实现功能：

- 读取 `app.log`
- 统计 `INFO`、`WARNING`、`ERROR` 数量
- 跳过空行
- 忽略其他日志类型

学习内容：

- `with open()` 文件读取
- `strip()` 和 `split()`
- 字典计数
- 函数参数与返回值
- Python 模块导入
- 功能代码与程序入口分离

遇到的问题：

- `FileNotFoundError` 与终端当前目录有关
- 相对路径从当前工作目录开始查找
- 当前项目没有第三方库，因此暂时不需要 `requirements.txt`

## Git 与 GitHub

完成流程：

```text
Issue
→ feature/log-analyzer
→ add
→ commit
→ push
→ Pull Request
→ merge main
→ 删除分支