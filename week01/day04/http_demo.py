import requests

url='https://jsonplaceholder.typicode.com/todos/1'



try:
    response=requests.get(url,timeout=5)
    response.raise_for_status()
    data=response.json()
    print(data)

except requests.exceptions.RequestException as e:
    print('请求失败')