import json
with open("study_traker.json","r",encoding="utf-8")as file:
    data=json.load(file)
print(data)