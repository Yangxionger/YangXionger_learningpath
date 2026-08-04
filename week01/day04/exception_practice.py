try:
    with open('open.json','r',encoding='utf-8')as file:
        data=file.read()
        print('文件读取成功')
        print(data)
except FileNotFoundError:
    print("未找到该文件 请核对文件名")

try:
    num=int(input('请输入一个数字'))
    print(num)
except ValueError:
    print('请输入合法数字')

try:
    num1=int(input('请输入被除数'))
    num2=int(input('请输入除数'))
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('请输入合法数字')
