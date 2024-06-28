import json

with open("data.txt") as file:
    content=file.read()
    dt =json.loads(content)

dt['weight']=55
with open("data.txt","w") as file:
    content=json.dumps(dt)
    file.write(content)