import json
import os

def add_task(tasks):
    title=input('请输入要添加的任务标题 ')
    tasks.append({"title":title,"completed":False})
    save_tasks(tasks)

def show_tasks(tasks):
    if not tasks:
        print('当前还没有任何任务噢 ')
    else:
        for index,task in enumerate(tasks,start=1):
            print(index,task)

def save_tasks(tasks):
    with open('task_manager.json','w',encoding='utf-8')as file:
        json.dump(tasks,file,ensure_ascii=False,indent=4)

def load_tasks():
    if not os.path.exists("task_manager.json"):
        return []
    try:
        with open("task_manager.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("任务文件内容损坏，将使用空任务列表")
        return []

def complete_task(tasks):
    if not tasks:
        print("当前没有可以完成的任务")
        return
    show_tasks(tasks)
    while True:
        title=input('请输入你已完成的任务标题 ')
        for task in tasks:
            if task['title']==title:
                task['completed']=True
                print('任务已完成')
                save_tasks(tasks)
                return   
        print('未找到该任务，请重新输入')


def delete_task(tasks):
    if not tasks:
        print("当前没有可以删除的任务")
        return
    show_tasks(tasks)
    while True:
        title=input('请输入你要删除的任务标题 ')
        for task in tasks:
            if task['title']==title:
                tasks.remove(task)
                save_tasks(tasks)
                print('删除成功')
                return
        print("未找到该任务，请重新输入")
    

def main():
    tasks=load_tasks()
    while True:
        print('1.查看任务\n2.添加任务\n3.完成任务\n4.删除任务\n5.退出程序')
        instru=input('请输入你想要选择的序列数字 ')
        if not instru.isdigit():
            print("请输入正确的序列数字 ")
            continue
        else:
            instru = int(instru)
        if(instru==5):
            return
        elif instru==1:
            show_tasks(tasks)
        elif instru==2:
            add_task(tasks)
        elif instru==3:
            complete_task(tasks)
        elif instru==4:
            delete_task(tasks)
        else:
            print('没有这个选择，请重新输入')

if __name__ == "__main__":
    main()

    
