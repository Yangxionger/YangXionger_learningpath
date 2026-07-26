def analyze_log(filename):
    dic=dict()
    with open(filename,'r',encoding='utf-8')as file:
        for line in file:
            clean_line=line.strip()
            if not clean_line:
                continue
            parts=clean_line.split()
            dic[parts[0]]=dic.get(parts[0],0)+1
    return dic

result=analyze_log('app.log')
print('日志统计结果：')
print("INFO:", result["INFO"])
print("WARNING:", result["WARNING"])
print("ERROR:", result["ERROR"])
