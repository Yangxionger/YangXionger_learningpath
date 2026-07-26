from analyzer import analyze_log


result = analyze_log("app.log")

print("日志统计结果：")
print("INFO:", result["INFO"])
print("WARNING:", result["WARNING"])
print("ERROR:", result["ERROR"])