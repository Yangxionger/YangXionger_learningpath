from analyzer import analyze_log

result = analyze_log("app.log")

if result is not None:
    print("日志统计结果：")
    print("INFO:", result["INFO"])
    print("WARNING:", result["WARNING"])
    print("ERROR:", result["ERROR"])
