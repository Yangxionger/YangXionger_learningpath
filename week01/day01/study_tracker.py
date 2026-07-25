import json

try:
    with open("study_record.json","r",encoding="utf-8") as file:
        dic=json.load(file)

except:
    dic={}

today_time=0
while True:
    message=input("请输入科目名称和学习分钟数(用空格隔开)," \
    "如果结束请输入q")

    if message.lower()=='q':
        break
    parts=message.split()
    if len(parts) != 2:
        print("输入格式有误，请确保输入了两个变量！\n")
        continue  
    subject=parts[0]
    try:
        time_len=float(parts[1])
    except:
        print("请输入数字")
        continue
    if time_len < 0:
        print("学习时间不能为负数")
        continue
    today_time+=time_len
    dic[subject]=dic.get(subject,0)+time_len

if today_time == 0:
    print("今天没有记录任何学习时间。")
else:
    print(f'\n今天总学习时长是{today_time}时')
    max_time=0
    max_subject=""
    for subject in dic:
        if dic[subject] >max_time:
           max_subject=subject
    print(f'学习时间最长的科目是：{max_subject}')
    print('下面输出每个科目的学习时间占比：')
    for subject in dic:
        # 修复4：使用 :.2% 自动将小数转为百分数
        print(f'科目：{subject}, 占比时间：{ (dic[subject] / today_time) :.2%}')
    with open("study_tracker.json","w",encoding="utf-8")as file:
        json.dump(dic,file,ensure_ascii=False,indent=4)


